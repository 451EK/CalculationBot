import discord
from discord.ext import commands
import os
import json

def getprefixes(Bot,message):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents().all()
Bot = commands.Bot(command_prefix=getprefixes,intents=intents,help_command=None)
TOKEN = open('token.txt','r').read()

@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help | Version 0.1"))
    print("Bot is online!")

@Bot.event
async def on_guild_join(guild):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "-"

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

@Bot.event
async def on_guild_remove(guild):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

@Bot.command()
async def changeprefix(ctx,prefix):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

    changedEmbed=discord.Embed(title=f"**Prefix succesfully changed to `{prefix}`**",colour=discord.Color.green())
    await ctx.send(embed=changedEmbed)
    
for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"Cogs.{filename[:-3]}")

Bot.run(TOKEN)
