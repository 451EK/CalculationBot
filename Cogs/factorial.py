import discord
from discord.ext import commands
import math

class Factorial(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def factorial(self,ctx,number = None):
        try:
            number = int(number)
            if number is None:
                WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-factorial <number>`",colour=discord.Color.red())
                await ctx.send(embed=WARNembed,delete_after=10)
                await ctx.message.delete()
                return
            else:
                if len(str(number)) > 3:
                    WARN = discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},length of entered number must be less than four!**",colour=discord.Color.red())
                    await ctx.send(embed=WARN,delete_after=8)
                    await ctx.message.delete()
                else:
                    result = math.factorial(number)
                    RESULTembed = discord.Embed(title="**Result**",description=f"{number}! = {result}")
                    await ctx.send(embed=RESULTembed)
        except ValueError:
            ERRORembed = discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},you can't use decimals with factorial command.**",colour=discord.Color.red())
            await ctx.send(embed=ERRORembed,delete_after=10)
            await ctx.message.delete()

def setup(Bot):
    Bot.add_cog(Factorial(Bot))
