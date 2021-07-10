import discord
from discord.ext import commands
import datetime

class Time(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def time(self,ctx):
        now = datetime.datetime.now()
        timestamp=datetime.datetime.now()
        time = timestamp.strftime(r"%I:%M %p")
        timeInfo = now.strftime("%A, %B %d,%Y")
        TIMEembed=discord.Embed(title="**Time**",description=f"{timeInfo}\n{time}",colour=discord.Color.dark_green())
        TIMEembed.set_footer(text="Make sure your time zone settings are correct!")
        await ctx.send(embed=TIMEembed)

def setup(Bot):
    Bot.add_cog(Time(Bot))