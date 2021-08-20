import discord
from discord.ext import commands
import requests
import datetime

class CryptoCurrency(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def crypto(self,ctx):
        url1 = "https://blockchain.info/ticker"
        stats = requests.get(url1)
        json_stats = stats.json()
        gbpprice = json_stats["GBP"]["last"]
        europrice = json_stats["EUR"]["last"]
        usdprice = json_stats["USD"]["last"]
        audprice = json_stats["AUD"]["last"]
        brlprice = json_stats["BRL"]["last"]
        cadprice = json_stats["CAD"]["last"]
        chfprice = json_stats["CHF"]["last"]
        clpprice = json_stats["CLP"]["last"]
        cnyprice = json_stats["CNY"]["last"]
        czkprice = json_stats["CZK"]["last"]
        dkkprice = json_stats["DKK"]["last"]
        hkdprice = json_stats["HKD"]["last"]
        hrkprice= json_stats["HRK"]["last"]
        hufprice = json_stats["HUF"]["last"]
        inrprice = json_stats["INR"]["last"]
        iskprice= json_stats["ISK"]["last"]
        jpyprice= json_stats["JPY"]["last"]
        krwprice = json_stats["KRW"]["last"]
        nzdprice = json_stats["NZD"]["last"]
        plnprice =json_stats["PLN"]["last"]
        ronprice = json_stats["RON"]["last"]
        rubprice = json_stats["RUB"]["last"]
        sekprice = json_stats["SEK"]["last"]
        sgdprice = json_stats["SGD"]["last"]
        thbprice = json_stats["THB"]["last"]
        tryprice = json_stats["TRY"]["last"]
        twdprice = json_stats["TWD"]["last"]

        ccbed2 = discord.Embed(title=f"**<:bitcoin:878288199405948969> Bitcoin Currency**", description=f"AUD {audprice} - BRL {brlprice}\nCAD {cadprice} - CHF {chfprice}\nCLP {clpprice} - CNY {cnyprice}\nCZK {czkprice} - DKK {dkkprice}\nEUR {europrice} - GBP {gbpprice}\nHKD {hkdprice} - HRK {hrkprice}\nHUF {hufprice} - INR {inrprice}\nISK {iskprice} - JPY {jpyprice}\nKRW {krwprice} - NZD {nzdprice}\nPLN {plnprice} - RON {ronprice}\nRUB {rubprice} - SEK {sekprice}\nSGD {sgdprice} - THB {thbprice}\nTRY {tryprice} - TWD {twdprice}\nUSD {usdprice}", colour=discord.Color.from_rgb(0,255,148), timestamp=datetime.datetime.utcnow())

        await ctx.send(embed=ccbed2)

    @crypto.error
    async def error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title=f"Slow it down man!",description=f"Try again in **{error.retry_after:.2f}** seconds.", colour=discord.Color.red())
            await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(CryptoCurrency(Bot))