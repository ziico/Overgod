import discord
import colorama
import json
import os
from discord import client

from futures3 import ThreadPoolExecutor
from discord.ext import commands
from colorama import Fore

af = ThreadPoolExecutor(max_workers=100000)

with open('config.json') as f:
    config = json.load(f)

token = config.get("token")
user = config.get("user")


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
       do pip install futures3 if this shit dont work
    also put the user you want to ping inbetween <@example>

""")



@afk.command(aliases=["Ready", "urhoed", "SSon", "bitchboy", "crying", "foldson", "bBEG", "fOcus", "urend"])
async def hoebitch(ctx):
    af.submit(await ctx.send(f"afk check {user}"))
    af.submit(await ctx.send("1"))
    af.submit(await ctx.send("2"))
    af.submit(await ctx.send("3"))
    af.submit(await ctx.send("4"))
    af.submit(await ctx.send("5"))
    af.submit(await ctx.send("6"))
    af.submit(await ctx.send("7"))
    af.submit(await ctx.send("8"))
    af.submit(await ctx.send("9"))
    af.submit(await ctx.send("0"))


afk.run(token,bot=False)
