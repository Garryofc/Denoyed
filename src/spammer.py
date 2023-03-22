import asyncio
import discord
import time
from discord.ext import commands
import colorama
from colorama import Fore
from colorama import Style
import Start
colorama.init()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))
    spammessage = input("What message do you want to spam? ")
    repeats = int(input("How many times? "))
    channelid = int(input("Channel id? ")) 
    for i in range (0,repeats):
        channel = client.get_channel(channelid)
        try:
            await channel.send(f'@everyone {spammessage}, StarX on top https://dsc.gg/𝘚𝘵𝘢𝘳𝘟')  
        except:
            print(Fore.GREEN + f"Message was NOT sended." + Fore.RESET)
    print("")
    return Start.welcome()

f = open("token.txt", "r")
token = f.read()
client.run(token)