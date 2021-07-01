import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="**Commands (8)**",description="➜ **Moderation**\n`setprefix`\n➜ **Info**\n`help`,`credits`,`ping`\n ➜**Calculation**\n `add`,`sub`,`mul`,`div`",colour=discord.Color.blue())
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Help(Bot))
