import discord
from discord.ext import commands
import datetime
import asyncio

class Remindme(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def remindme(self,ctx, time, *, reminder):
        embed = discord.Embed(color=0x55a7f7, timestamp=datetime.datetime.utcnow())
        seconds = 0
        if reminder is None:
            embed.add_field(name='**Error**', value='• Please specify a text to remind you.\n• **Usage :** `-remindme <time> <reminder>`')
        if time.lower().endswith("d"):
            seconds += int(time[:-1]) * 60 * 60 * 24
            counter = f"{seconds // 60 // 60 // 24} days"
        if time.lower().endswith("h"):
            seconds += int(time[:-1]) * 60 * 60
            counter = f"{seconds // 60 // 60} hours"
        elif time.lower().endswith("m"):
            seconds += int(time[:-1]) * 60
            counter = f"{seconds // 60} minutes"
        elif time.lower().endswith("s"):
            seconds += int(time[:-1])
            counter = f"{seconds} seconds"
        if seconds == 0:
            embed.add_field(name='**Error**',
                            value='You must specify a duration.\n• **Usage :** `-remindme <time> <reminder>`')
        elif seconds < 300:
            embed.add_field(name='**Error**',
                            value='• **You have specified a too short duration!**\n• **Minimum duration is 5 minutes.**')
        elif seconds > 1209600:
            embed.add_field(name='**Error**', value='• **You have specified a too long duration!**\n• **Maximum duration is 2 week/14 days.**')
        else:
            await ctx.send(f"{ctx.message.author.mention},successfully set a reminder in {counter}.")
            await asyncio.sleep(seconds)
            await ctx.send(f"**Reminder**\n{ctx.message.author.mention},\n{reminder}")
            return
        await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Remindme(Bot))