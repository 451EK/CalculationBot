import discord
from discord.ext import commands
import math

class SquareRoot(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def sqrt(self,ctx,number : float = None):
        if number is None:
            WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-sqrt <number>`",colour=discord.Color.red())
            await ctx.send(embed=WARNembed,delete_after=10)
            await ctx.message.delete()
            return
        else:
            result = math.sqrt(number)
            RESULTembed = discord.Embed(title="**Result**",description=f"√{number} = {result}")
            await ctx.send(embed=RESULTembed)

def setup(Bot):
    Bot.add_cog(SquareRoot(Bot))