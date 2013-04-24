import os
from ircbot import SingleServerIRCBot
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
        spoken = e.arguments()[0].lower()
        if channel != self.channel: return
        melower = c.get_nickname().lower()
        if not spoken.startswith("%s " % melower) and \
           not spoken.startswith("%s," % melower) and \
           not spoken.startswith("!") and \
           not spoken.startswith("%s:" % melower):
            return

        if spoken.startswith("!"):
            spoken = spoken[1:].strip()
        else:
            spoken = spoken[len(melower)+1:].strip()
        if spoken in ["hello", "o hai", 'hi']:
            c.privmsg(channel, "o hai %s" % speaker)

        if spoken == "facebook":
            c.privmsg(channel, "Go check out Dindra on Facebook: http://www.facebook.com/DindraHeartLoL")
        elif spoken == "youtube":
            c.privmsg(channel, "Go check out Dindra on Youtube: http://www.youtube.com/DindraHeartLoL")
        elif spoken == "age":
            c.privmsg(channel, "Dindra is currently 17 years old, but she'll be 18 soon!")
        elif spoken == "from":
            c.privmsg(channel, "Dindra is originally from Russia, but currently living in the Netherlands")
        elif spoken == "cam" :
            c.privmsg(channel, "The cam is currently off so that Dindra can eat (or just hide from the perverts!)")
        elif spoken == "region":
            c.privmsg(channel, "Dindra plays on EU West")
        elif spoken == "whoisdindrasman":
            if speaker == 'qazrzark':
                c.privmsg(channel, "Not you, you're french")
            else:
                c.privmsg(channel, "Not you, %s!" % (speaker))
        elif spoken == "zark":
            c.privmsg(channel, "He's basically french")
        elif spoken == "pimp":
            c.privmsg(channel, "Don't forget to hit the follow button!  And you can also check out Dindra on Facebook at http://www.facebook.com/DindraHeartLoL and on Youtube at http://www.youtube.com/DindraHeartLoL")
        elif spoken == "friends":
            c.privmsg(channel, "Dindra doesn't accept random friend requests - too many people!!!")
        elif spoken == "english":
            c.privmsg(channel, "Please keep the chat english!")
