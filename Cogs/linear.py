import discord
from discord.ext import commands
import matplotlib.pyplot as plt


class Linear(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot

    def plotlineareq(self, a, b, clr):
        x = [-10, 10]
        y = [(a * i + b) for i in x]
        plt.figure(figsize=(6, 6))
        plt.xlim(x)
        plt.ylim(x)
        axis = plt.gca()
        plt.plot(axis.get_xlim(), [0, 0], 'k--')
        plt.plot([0, 0], axis.get_ylim(), 'k--')
        plt.locator_params(axis="x", nbins=20)
        plt.locator_params(axis="y", nbins=20)
        plt.plot(x, y, label='linear', linestyle='-', color=clr)
        plt.ylabel('y')
        plt.xlabel('x')
        mm = str(a)
        bb = str(b)
        plt.title("y = " + mm + "x + " + bb)
        plt.grid()
        plt.savefig("foo.png")

    @commands.command()
    async def linear(self, ctx, equation):
        try:
            equation = equation.replace(" ", "")
            mx = equation.split("x")[0]
            mx = equation.replace("x", "").replace("y=", "")
            bx = equation.split("+")[1]
            self.plotlineareq(mx, bx, 'b')
            file = discord.File("foo.png", filename='foo.png')
            embed = discord.Embed(description=f"Not able to see `x`?\n`x`: ```m\n{mx + bx}\n```",color=discord.Color.dark_theme())
            embed = embed.set_image(url="attachment://foo.png")
            await ctx.send(file=file, embed=embed)
        
        except Exception as e:
            embed = discord.Embed(title="**Error**",description=e,colour=discord.Color.red())
            await ctx.send(embed=embed)

def setup(Bot):
    Bot.add_cog(Linear(Bot))