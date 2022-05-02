import socket

import discord
import wakeonlan
import yaml

class MyClient(discord.Client):

    def __init__(self,TCPServer):
        super(MyClient, self).__init__()
        self.tcpServer = TCPServer
        with open("./config.yml", "r") as config:
            try:
                self.config_general = yaml.safe_load(config)
                self.config = self.config_general["Discord"]
            except yaml.YAMLError as exc:
                print("ERROR: Load Config File")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self,message):
        if message.content.startswith(self.config["commande"]["start"]):
            content = message.content.replace(self.config["commande"]["start"],"")
            if content in self.config["commande"]["cmd"]:
                try:
                    await getattr(self,"cmd_"+content)(message)
                except AttributeError:
                    await message.channel.send("Unimplemented method")
                    print("Unimplemented method")


    def run(self):
        super(MyClient, self).run(self.config["token"])


    async def cmd_help(self,message):
        text =""
        for line in self.config["response"]["help"]:
            text+=line +"\n"
        await message.channel.send(text)

    async def cmd_start(self,message):
        await message.channel.send(self.config["response"]["startup"])
        mac = self.config_general["Startup"]["wol"]["mac"]
        wakeonlan.send_magic_packet(mac)

    async def cmd_pong(self,message):
        await message.channel.send(self.config["response"]["pong"])

    async def cmd_ask(self,message):
        client_list = self.tcpServer.get_client()
        if len(client_list) == 0:
            await message.channel.send(self.config["response"]["ask"]["switched_off"])
        else:
            for client in client_list:
                try :
                    response = client.ask(self.config["response"]["ask"]["commande"])
                    if( int(response) < self.config["response"]["ask"]["timeMin"]):
                        await message.channel.send(self.config["response"]["ask"]["unvailable"])
                    else:
                        await message.channel.send(self.config["response"]["ask"]["available"]+response+" minutes!")
                except Exception:
                    print("Removing Connexion de %s %s" % (client.ip, client.port, ))
                    self.tcpServer.client.remove(client)
                    await message.channel.send(self.config["response"]["ask"]["switched_off"])
