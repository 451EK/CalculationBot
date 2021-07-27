import discord
from discord.ext import commands
import secrets
import datetime
import asyncio

class GeneratePassword(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def genpassw(self,ctx,passwlength : int = None):
        if passwlength == None:
            embed=discord.Embed(title="**Error**",description="Make sure you typed the command correctly!\n**Usage :** `-genpassw <password_length>`\n**Note : Password length must be an integer and must not be longer than 300.**",colour=discord.Color.red())
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return
        elif passwlength > 300:
            embed=discord.Embed(title="**Error**",description=f"**{ctx.message.author.mention},password length can't be longer than 300!**",colour=discord.Color.red())
            await ctx.send(embed=embed,delete_after=7)
            await ctx.message.delete()
            return
        else:
            r1 = "🔐"
            r2 = "🔓"
            length = passwlength
            passw = str(secrets.token_urlsafe(length))
            pw = passw[:-1]
            embed = discord.Embed(title="**Password Successfully Generated**",description=f"Password : ||Password is private||\n\n**React with 🔐 to get your password in private messages,🔓 to reveal your password.You have 10 seconds.**")
            embed.set_footer(text=f"Requested by {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
            secret = await ctx.send(embed=embed)
            await secret.add_reaction(r1)
            await secret.add_reaction(r2)
            DMembed = discord.Embed(title="Password Successfully Sent in Private Message",colour=discord.Color.from_rgb(0,255,148),timestamp = datetime.datetime.utcnow())
            RVembed = discord.Embed(title="Password Successfully Generated And Revealed",description = f"Password : `{pw}`",colour=discord.Color.from_rgb(0,255,148),timestamp = datetime.datetime.utcnow())
            RVembed.set_author(name=f"{ctx.message.author.name}'s Password",icon_url=ctx.message.author.avatar_url)

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in [r1, r2]

            member = ctx.author

            while True:
                try:
                    reaction, user = await self.Bot.wait_for("reaction_add", timeout=10.0, check=check)

                    if str(reaction.emoji) == r1:
                        Pembed = discord.Embed(title="Here you go!",description=f"__Your Password Is__\n`{pw}`",colour=discord.Color.from_rgb(0,255,148),timestamp = datetime.datetime.utcnow())
                        Pembed.set_footer(text="Do not share your password with anyone!")
                        await member.send(embed=Pembed)
                        await secret.edit(embed = DMembed)   
                        break               

                    elif str(reaction.emoji) == r2:
                        await secret.edit(embed = RVembed)
                        break
                        
                except asyncio.TimeoutError:
                    TEembed = discord.Embed(title="**Timeout!**",description=f"{ctx.message.author.mention},I can't give you your password.Time is over!",colour=discord.Color.red(),timestamp = datetime.datetime.utcnow())
                    await secret.edit(embed = TEembed)
                    break
            
def setup(Bot):
    Bot.add_cog(GeneratePassword(Bot))
