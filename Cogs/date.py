import discord
from discord.ext import commands
import datetime

class Date(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def date(self,ctx):
        now = datetime.datetime.now()
        timeInfo = now.strftime("%A, %B %d,%Y")
        TIMEembed=discord.Embed(title="**Date**",description=f"{timeInfo}",colour=discord.Color.dark_green(),timestamp = datetime.datetime.utcnow())
        await ctx.send(embed=TIMEembed)

def setup(Bot):
    Bot.add_cog(Date(Bot))