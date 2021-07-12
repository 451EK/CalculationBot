import discord
from discord.ext import commands
import datetime

class Time(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def time(self,ctx):
        now = datetime.datetime.now()
        timeInfo = now.strftime("%A, %B %d,%Y")
        time = now.strftime("%I:%M %p")
        TIMEembed=discord.Embed(title="**Time**",description=f"{timeInfo}\n{time}",colour=discord.Color.dark_green())
        await ctx.send(embed=TIMEembed)

def setup(Bot):
    Bot.add_cog(Time(Bot))