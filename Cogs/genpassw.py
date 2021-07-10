import discord
from discord.ext import commands
import secrets

class GeneratePassword(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def genpassw(self,ctx,passwlength : int = None):
        if passwlength == None:
            embed=discord.Embed(title="**Error**",description="Make sure you typed the command correctly!\n**Usage :** `-genpassw <password_length>`\n**Note : Password length must be an integer.**")
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
        else:
            length = passwlength
            passw = secrets.token_urlsafe(length)
            embed = discord.Embed(title="**Password Successfully Generated**",description=f"Password : `{passw}`")
            embed.set_footer(text=f"Requested by {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
            
def setup(Bot):
    Bot.add_cog(GeneratePassword(Bot))