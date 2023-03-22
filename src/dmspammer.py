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
    channelid = int(input("User id? ")) 
    for i in range (0,repeats):
        try:
            user = await client.fetch_user(channelid)
            await user.send(spammessage)
            print(Fore.MAGENTA + f"Message was sended." + Fore.RESET)
        except:
            print(Fore.GREEN + f"Message was NOT deleted." + Fore.RESET)
    return Start.welcome()

f = open("token.txt", "r")
token = f.read()
client.run(token)