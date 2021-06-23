import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def help(self,ctx):
        embed=discord.Embed(title="**Commands**",description="- **changeprefix** <prefix> : changes the prefix\n- **add** <number1> <number2> : _adds up the numbers_\n- **sub** <number1> <number2> : _subtracts the numbers_\n- **mul** <number1> <number2> : _multiplies the numbers_\n- **div** <number1> <number2> : _divides the numbers_\n- **credits** : _shows the credits_\n- **help** : _shows the help message_\n- **ping** : _shows the bot latency_",colour=discord.Color.green())
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Help(Bot))
