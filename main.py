import asyncio
import discord
from discord.ext import commands
import os
import json
import asyncio

def getprefixes(Bot,message):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

intents = discord.Intents().all()
Bot = commands.Bot(command_prefix=getprefixes,intents=intents,help_command=None,case_insensitive=True)
TOKEN = open('token.txt','r').read()

async def status_change():
    while True:
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"-help ⚒️"))
        await asyncio.sleep(25)
        await Bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="📝 Math Operations"))
        await asyncio.sleep(25)

@Bot.event
async def on_ready():
    Bot.loop.create_task(status_change())
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
@commands.has_permissions(administrator=True)
async def setprefix(ctx,prefix):
    with open("prefixes.json","r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json","w") as f:
        json.dump(prefixes,f,indent=4)

    changedEmbed=discord.Embed(title=f"**Prefix successfully set to `{prefix}`**",colour=discord.Color.green())
    await ctx.send(embed=changedEmbed)
    
for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"Cogs.{filename[:-3]}")

Bot.run(TOKEN)
