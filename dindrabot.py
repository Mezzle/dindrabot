import os
from ircbot import SingleServerIRCBot
from response import SimpleResponse
from irclib import nm_to_n, nm_to_h, irc_lower, ip_numstr_to_quad, ip_quad_to_numstr

class DindraBot(SingleServerIRCBot):

    def __init__(self, channel, nickname, server, port=6667):

        pth = os.path.join(os.path.split(__file__)[0], "password.txt")
        if not os.path.exists(pth):
            self.password = None
        else:
            fp = open(pth)
            self.password = fp.read().strip()
            fp.close()
        print "Connecting to", channel
        self.channel = channel
        self.nickname = nickname

        self.response = SimpleResponse()

        SingleServerIRCBot.__init__(self, [(server, port, self.password)], nickname, nickname)

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        print "Connected"
        c.join(self.channel)
        print

    def on_join(self, c, e):
        ch = e.target()

    def on_pubmsg(self, c, e):
        speaker = nm_to_n(e.source())
        channel = e.target()
        spoken = e.arguments()[0]
        if channel != self.channel: return
        melower = c.get_nickname().lower()
        if not spoken.startswith("!"):
            return

        spoken = spoken[1:].strip()

        if self.response.has_response(spoken):
            c.privmsg(channel, self.response.get_response(spoken, speaker, self.channels[channel].is_oper(speaker)))

