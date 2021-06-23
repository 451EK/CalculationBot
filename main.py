import discord
from discord.ext import commands
import os

intents = discord.Intents().all()
Bot = commands.Bot(command_prefix="-",intents=intents,help_command=None)
TOKEN = open('token.txt','r').read()

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help | Version 0.1"))
    print("Bot is online!")

for filename in os.listdir("./Commands"):
    if filename.endswith(".py"):
        Bot.load_extension(f"Commands.{filename[:-3]}")

Bot.run(TOKEN)
