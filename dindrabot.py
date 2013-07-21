from twisted.words.protocols import irc

class DindraBot(irc.IRCClient):

    response = None
    mods = []

    def signedOn(self):
        self.join(self.factory.channel)

    def privmsg(self, speaker, channel, msg):

        if channel != self.factory.channel: return

        if not msg.startswith("!"):
            return

        msg = msg[1:]

        speaker = speaker.split('!')[0]

        is_mod = speaker in self.mods

        if self.response.has_response(msg):
            self.msg(channel, self.response.get_response(msg, speaker, is_mod))


    def modeChanged(self, user, channel, set, modes, args):
        if channel != self.factory.channel:
            return

        if set:
            for nick in args:
                print '%s given op' % nick
                if nick not in self.mods:
                    self.mods.append(nick)
