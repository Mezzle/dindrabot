from dindrabotfactory import DindraBotFactory
from twisted.internet import reactor
import sys

if __name__ == "__main__":

    channel = "#dindraheart"
    nickname = "DindraBot"

    server = "irc.twitch.tv"
    port = 6667
    if len(sys.argv) > 1: channel = sys.argv[1]
    if len(sys.argv) > 2: nickname = sys.argv[2]
    if len(sys.argv) > 3: server = sys.argv[3]
    if len(sys.argv) > 4: port = sys.argv[4]

    f = DindraBotFactory(channel, nickname)

    reactor.connectTCP(server, port, f)

    reactor.run()
