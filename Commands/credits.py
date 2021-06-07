import discord
from discord.ext import commands
import datetime

class Credits(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def credits(self,ctx):
        embed=discord.Embed(title="**Credits**",description="This Bot made by 451#2950,\nMade in Visual Studio Code with using discord.py,\nGithub Repository : https://github.com/451EK/CalculationBot ",colour=discord.Color.blue())
        embed.set_footer(text=f"Requested By {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url=self.Bot.user.avatar_url)
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Credits(Bot))