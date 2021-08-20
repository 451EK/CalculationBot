import discord
from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self,ctx,amount=5):
        await ctx.channel.purge(limit=amount)
        embed=discord.Embed(title=f"{amount} messages deleted!",colour=discord.Color.from_rgb(0,255,148))
        await ctx.send(embed=embed,delete_after=5)

    @purge.error
    async def info_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply(f'You need `administrator` permission to be able to use this command!')

def setup(Bot):
    Bot.add_cog(Purge(Bot))