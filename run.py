from dindrabot import DindraBot
import sys


def main(channel, name, server, port):
    bot = DindraBot(channel, name, server, int(port))

    bot.start()

if __name__ == "__main__":
    channel = "#dindraheart"
    name = "DindraBot"
    server = "dindraheart.jtvirc.com"
    port = "6667"
    if len(sys.argv) > 1: channel = sys.argv[1]
    if len(sys.argv) > 2: name = sys.argv[2]
    if len(sys.argv) > 3: server = sys.argv[3]
    if len(sys.argv) > 4: port = sys.argv[4]
    main(channel, name, server, port)

