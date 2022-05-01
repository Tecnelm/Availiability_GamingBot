from Discord.Bot import MyClient
from Server.Server import TCPServer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server = TCPServer()
    server.start()
    bot = MyClient(server)
    bot.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
