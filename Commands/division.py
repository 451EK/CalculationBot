import discord
from discord.ext import commands

class Division(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def div(self,ctx,number1 : int = None,number2 : int = None):
        if number1 is None:
            await ctx.send(f"{ctx.message.author.mention},make sure you typed the command correctly!",delete_after=3)
            await ctx.message.delete()
            return
        if number2 is None:
            await ctx.send(f"{ctx.message.author.mention},make sure you typed the command correctly!",delete_after=3)
            await ctx.message.delete()
            return
        else:
            result = number1 // number2
            embed = discord.Embed(title="**Result**",description=f"{number1} ÷ {number2} = {result}")
            await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Division(Bot))