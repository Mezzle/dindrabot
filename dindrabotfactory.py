from twisted.internet import protocol
from response import SimpleResponse
from dindrabot import DindraBot
import os

class DindraBotFactory(protocol.ClientFactory):

    def __init__(self, channel, nickname):

        self.channel = channel
        self.nickname = nickname

    def buildProtocol(self, addr):
        bot = DindraBot()
        bot.factory = self

        pth = os.path.join(os.path.split(__file__)[0], "password.txt")

        if os.path.exists(pth):
            fp = open(pth)
            bot.password = fp.read().strip()
            fp.close()

        bot.nickname = self.nickname
        bot.factory = self

        response = SimpleResponse()
        bot.response = response

        return bot
