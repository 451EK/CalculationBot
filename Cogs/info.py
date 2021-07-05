import discord
from discord.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def info(self,ctx):
        embed=discord.Embed(title="**Info**",description="Calculation is a discord bot developed to help you for your basic math operations.",colour=discord.Color.blue())
        embed.set_footer(text=f"Requested By {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=self.Bot.user.avatar_url)
        embed.add_field(name="**Author**",value="451#2950")
        embed.add_field(name="Communication",value="[Support Server & Community](https://discord.gg/3BB8XS27Pw)")
        embed.add_field(name="Current Bot Version",value="0.2",inline=False)
        embed.add_field(name="Servers",value=len(self.Bot.guilds))
        embed.add_field(name="Users",value=ctx.guild.member_count)
        embed.add_field(name="Ping",value=f"{round(self.Bot.latency * 1000)}ms")
        embed.add_field(name="Links",value="[Website](http://calculationbot.cf) | [Github Repository](https://github.com/451EK/CalculationBot) | [Vote](https://top.gg/bot/849705216244449300/vote)",inline=False)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Info(Bot))
