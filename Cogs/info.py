import discord
from discord.ext import commands
from datetime import *

class Info(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.Bot.launch_time = datetime.utcnow()

    @commands.command()
    async def info(self,ctx):
        total_members = sum([len(guild.members) for guild in self.Bot.guilds])
        delta_uptime = datetime.utcnow() - self.Bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        embed=discord.Embed(title="**Info**",description="Calculator is a discord bot developed to help you for your basic math operations.",colour=discord.Color.from_rgb(0,255,148))
        embed.set_footer(text=f"Requested By {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=self.Bot.user.avatar_url)
        embed.add_field(name="**Author**",value="451#2950")
        embed.add_field(name="Communication",value="[Support Server](https://discord.gg/tXd9gPtKCj) & [Developer](https://discordapp.com/users/453613270725558292)")
        embed.add_field(name="Uptime",value=f"{days}d, {hours}h, {minutes}m")
        embed.add_field(name="Servers",value=len(self.Bot.guilds))
        embed.add_field(name="Users",value=total_members)
        embed.add_field(name="Ping",value=f"{round(self.Bot.latency * 1000)}ms")
        embed.add_field(name="Links",value="[Github](https://github.com/451EK/Calculator) | [Invite](https://discord.com/oauth2/authorize?client_id=869500014899122246&scope=bot&permissions=201706561) | [Vote](https://top.gg/bot/869500014899122246/vote)",inline=False)
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Info(Bot))
