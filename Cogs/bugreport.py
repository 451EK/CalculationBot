import discord
from discord.ext import commands
import datetime

class BugReport(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def bugreport(self,ctx,*,message = None):
        if message==None:
            WARNembed=discord.Embed(title="**Error**",description=f"• **{ctx.message.author.mention},make sure you typed the command correctly!**\n• **Usage :** `-bugreport <bug_message>`",colour=discord.Color.red())
            await ctx.send(embed=WARNembed,delete_after=10)
            await ctx.message.delete()
            return
        else:
            channel = self.Bot.get_channel(870009763453345832)
            embed = discord.Embed(title="New Bug Report",description=f"🚨 {message}",colour=discord.Color.from_rgb(0,255,148),timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Sent by {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            scembed = discord.Embed(title="Your Report Has Successfully Been Sent!",colour=discord.Color.from_rgb(0,255,148))
            await ctx.send(embed=scembed,delete_after=8)
            await channel.send(embed=embed)
            await ctx.message.delete()

def setup(Bot):
    Bot.add_cog(BugReport(Bot))