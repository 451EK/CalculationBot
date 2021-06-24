import discord
from discord.ext import commands
import datetime

class Ping(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot
    
    @commands.command()
    async def ping(self,ctx):
        if round(self.Bot.latency * 1000) > 100:
            REDembed=discord.Embed(title="**Pong! 🏓**",description=f"**Ping {round(self.Bot.latency * 1000)} ms**",colour=discord.Color.red(),timestamp=datetime.datetime.utcnow())
            REDembed.set_footer(text="Calculation#1494",icon_url=self.Bot.user.avatar_url)
            await ctx.send(embed=REDembed)
        elif round(self.Bot.latency * 1000) < 100:
            ORANGEembed=discord.Embed(title="**Pong! 🏓**",description=f"**Ping {round(self.Bot.latency * 1000)} ms**",colour=discord.Color.orange(),timestamp=datetime.datetime.utcnow())
            ORANGEembed.set_footer(text="Calculation#1494",icon_url=self.Bot.user.avatar_url)
            await ctx.send(embed=ORANGEembed)
        elif round(self.Bot.latency * 1000) < 50:
            GREENembed=discord.Embed(title="**Pong! 🏓**",description=f"**Ping {round(self.Bot.latency * 1000)} ms**",colour=discord.Color.green(),timestamp=datetime.datetime.utcnow())
            GREENembed.set_footer(text="Calculation#1494",icon_url=self.Bot.user.avatar_url)
            await ctx.send(embed=GREENembed
    
def setup(Bot):
    Bot.add_cog(Ping(Bot))
