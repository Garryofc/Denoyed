from fileinput import close
import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore
from colorama import Style
import Start
colorama.init()

client = discord.Client() 
client = discord.Client()
client = commands.Bot(command_prefix="!")

class person:
    name = ''
    def setName(self, name):
        self.name = name

person_obj = person()
person_obj.name = ""



channelname = input("Name of channel? ")
repeats = int(input("How many times? "))
channelmessage = input("Message to channel? ")
person_obj.setName(channelmessage)
print('Write !CMaker now')
@client.command()
async def CMaker(ctx):
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))
    await ctx.message.delete()
    guild = ctx.guild
    for i in range (0, repeats):
        try:
            await guild.create_text_channel(channelname)
        except:
            print(Fore.GREEN + f"{channelname} was NOT created." + Fore.RESET)
    print('')
    return Start.welcome()

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(f"@everyone StarX nuker: https://discord.gg/DWbcez9T6F (Owner: Annonymous) {person_obj.name}")
f = open("token.txt", "r")
token = f.read()
client.run(token)