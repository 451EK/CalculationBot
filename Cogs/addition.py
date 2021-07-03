import discord
from discord.ext import commands

class Addition(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def add(self,ctx,number1 : float = None,number2 : float = None):
        if number1 is None:
            WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-add <number1> <number2>`",colour=discord.Color.red())
            await ctx.send(embed=WARNembed,delete_after=10)
            await ctx.message.delete()
            return
        if number2 is None:
            WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-add <number1> <number2>`",colour=discord.Color.red())
            await ctx.send(embed=WARNembed,delete_after=10)
            await ctx.message.delete()
            return
        else:
            result = number1 + number2
            embed = discord.Embed(title="**Result**",description=f"{number1} + {number2} = {result}")
            await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Addition(Bot))
