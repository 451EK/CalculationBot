import discord
from discord.ext import commands

class Length(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def length(self,ctx,*,message = None):
        if message == None:
            WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-length <message>`",colour=discord.Color.red())
            await ctx.send(embed=WARNembed,delete_after=10)
            await ctx.message.delete()
            return
        else:
            length = len(message) - message.count(' ')
            embed = discord.Embed(title="**Length**",description = f"Message length is `{length}`.")
            await ctx.send(embed = embed)

def setup(Bot):
    Bot.add_cog(Length(Bot))