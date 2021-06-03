import discord
import colorama
import json
import os
from discord import client

from discord.ext import commands
from colorama import Fore


with open('config.json') as f:
    config = json.load(f)

token = config.get("token")


prefix=""

afk = discord.Client()
afk = commands.Bot(command_prefix=prefix, self_bot=True)
afk.remove_command('help') 

os.system("title OVERGOD MADE BY TOUSKI")

print(f"""{Fore.YELLOW}

 ▒█████   ██▒   █▓▓█████ ██▀███     ▄████  ▒█████   ▓█████▄ 
▒██▒  ██▒▓██░   █▒▓█   ▀▓██ ▒ ██▒▒ ██▒ ▀█▒▒██▒  ██▒ ▒██▀ ██▌
▒██░  ██▒ ▓██  █▒░▒███  ▓██ ░▄█ ▒░▒██░▄▄▄░▒██░  ██▒ ░██   █▌
▒██   ██░  ▒██ █░░▒▓█  ▄▒██▀▀█▄  ░░▓█  ██▓▒██   ██░▒░▓█▄   ▌
░ ████▓▒░   ▒▀█░  ░▒████░██▓ ▒██▒░▒▓███▀▒░░ ████▓▒░░░▒████▓ 
░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░ ░▒   ▒  ░ ▒░▒░▒░ ░ ▒▒▓  ▒ 
  ░ ▒ ▒░    ░ ░░   ░ ░    ░▒ ░ ▒░  ░   ░    ░ ▒ ▒░   ░ ▒  ▒ 
░ ░ ░ ▒       ░░     ░     ░   ░ ░ ░   ░ ░░ ░ ░ ▒    ░ ░  ░ 
    ░ ░        ░     ░     ░           ░      ░ ░      ░    
                    made by touski
                github : TheyLoveTouski

""")

afk.event()
async def on_message(message):
        if "afk check 10" in message.content.lower():
            await message.channel.send("9")
            await message.channel.send("8")
            await message.channel.send("7")
            await message.channel.send("6")
            await message.channel.send("5")
            await message.channel.send("4")
            await message.channel.send("3")
            await message.channel.send("2")
            await message.channel.send("1")
                                

afk.run(token,bot=False)
