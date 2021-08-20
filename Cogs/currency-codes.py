import discord
from discord.ext import commands
import datetime
from discord_components import *

class CurrencyCodes(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command(aliases=["cc","currencycodes","currency-codes"])
    async def curcodes(self,ctx):
        button = [
        [
            Button(style=ButtonStyle.URL, label='Click Here', url="https://paste.gg/p/anonymous/a8be7bc6c9eb48e6bf315148ce04324f",emoji="💵"),
        ]
    ]
        embed = discord.Embed(title="Currency Codes",description="Click the button below to see all currency codes.",colour=discord.Color.from_rgb(0,255,148),timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=self.Bot.user.avatar_url)
        await ctx.send(components=button,embed=embed)

def setup(Bot):
    Bot.add_cog(CurrencyCodes(Bot))