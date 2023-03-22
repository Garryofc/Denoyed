import asyncio
from ast import Load
from colorama import Fore
import colorama
import sys
import discord
import discord.ext
import time
import os
from http import client
colorama.init()


bot = discord.Client()

def welcome():
    key = open("Key.txt", "r")
    Key = key.read()
    if Key == "093728719385.823717848939?29378":
        Loading = [ Fore.WHITE + "[■□□□□□□□□□ 10%]","[■■□□□□□□□□ 20%]", "[■■■□□□□□□□ 30%]", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
        for i in range(10):
            time.sleep(0.15)
            sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
            sys.stdout.flush()
        print('')
        print('')
        print(f'{Fore.RED}[{Fore.WHITE}1{Fore.RED}]{Fore.WHITE}Spammer {Fore.GREEN}')
        print(f'{Fore.RED}[{Fore.WHITE}2{Fore.RED}]{Fore.WHITE}Channel maker (!CMaker command){Fore.GREEN}')
        print(f'{Fore.RED}[{Fore.WHITE}3{Fore.RED}]{Fore.WHITE}Nuker (!nuke command){Fore.GREEN}')
        print(f'{Fore.RED}[{Fore.WHITE}4{Fore.RED}]{Fore.WHITE}Roles delete (!droles command){Fore.GREEN}')
        print(f'{Fore.RED}[{Fore.WHITE}5{Fore.RED}]{Fore.WHITE}Roles creator (!croles command){Fore.GREEN}')
        print(f'{Fore.RED}[{Fore.WHITE}6{Fore.RED}]{Fore.WHITE}DM spammer {Fore.GREEN}')
        print(f'{Fore.GREEN}[{Fore.WHITE}7{Fore.GREEN}]{Fore.LIGHTRED_EX}EXIT {Fore.GREEN}')
        print('')
        choice = input('[?] > ')
        print(f'{Fore.WHITE}')
        if choice == '1':
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            os.system('spammer.py')
        if choice == "2":
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            os.system('CM.py')
        if choice == "3":
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            print('Write !nuke now')
            os.system('Nuke.py')
        if choice == "4":
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            print('Write !droles now')
            os.system('droles.py')
        if choice == "5":
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            print('Write !croles now')
            os.system('croles.py')
        if choice == "6":
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            print('')
            os.system('dmspammer.py')
        if choice == "7":
            print('Turning off')
            print('')
            for i in range(10):
                time.sleep(0.15)
                sys.stdout.write("\rWait Few seconds..." + Loading[i % len(Loading)])
                sys.stdout.flush()
            exit()
        else:
            print(Fore.WHITE + "There isn't that module")
            print('')
            return welcome()
    else:
        print(Fore.WHITE + 'You stoled this item')
        time.sleep(5)


if __name__ == '__main__':
    welcome()
