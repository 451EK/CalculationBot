import discord
from discord.ext import commands
import random

class Random(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def random(self,ctx,number1 = None,number2 = None):
        try:
            number1 = float(number1)
            number2 = float(number2)
            if number1 == None:
                ERROR = discord.Embed(title="**Error**",description="• **You must enter the first number!**\n• **Usage :** `-random <number1> <number2>`")
                await ctx.send(embed=ERROR,delete_after=9)
                await ctx.message.delete()
            elif number2 == None:
                ERROR = discord.Embed(title="**Error**",description="• **You must enter the second number!**\n• **Usage :** `-random <number1> <number2>`")
                await ctx.send(embed=ERROR,delete_after=9)
                await ctx.message.delete()
            else:
                randomNum = random.uniform(number1,number2)
                embed = discord.Embed(title="**Random Number Generated**")
                embed.add_field(name="**Number 1**",value=number1)
                embed.add_field(name="**Number 2**",value=number2)
                embed.add_field(name="**Random Number**",value=f"`{randomNum}`",inline=False)
                await ctx.send(embed=embed)
        except ValueError:
            ERROR = discord.Embed(title="**Error**",description="• **Make sure you typed the command correctly!**\n• **Usage :** `-random <number1> <number2>`")
            await ctx.send(embed=ERROR,delete_after=9)
            await ctx.message.delete()

def setup(Bot):
    Bot.add_cog(Random(Bot))