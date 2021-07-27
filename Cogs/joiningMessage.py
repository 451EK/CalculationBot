import discord
from discord.ext import commands
import datetime

class joiningMessage(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        owner = guild.owner
        embed = discord.Embed(title=":green_heart: **Thanks For Adding The Calculator** :green_heart:",description="\n\n• You can change my prefix with `-setprefix <prefix>` command.\n• Use `help` or `info` commands to learn more about me!\n• If you need help,you can join our [Support Server](https://discord.gg/3BB8XS27Pw) and we also use it as community!\n\n\n:revolving_hearts: Have a great time with me!",colour=discord.Color.from_rgb(0,255,148),timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="Calculation#1494",icon_url=self.Bot.user.avatar_url)
        await owner.send(embed=embed)

def setup(Bot):
    Bot.add_cog(joiningMessage(Bot))
