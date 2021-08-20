import discord
from discord.ext import commands
from random import *

class Quiz(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def quiz(self,ctx,type = type):
        def check(msg):
            return msg.author.id == ctx.author.id
        type = randint(1,4)
        if type == 1:
            number1 = randint(1,1000)
            number2 = randint(1,1000)
            question = discord.Embed(title="What's the answer of following question?",description=f"\n__Question__\n{number1} + {number2} = ?",colour=discord.Color.random())
            await ctx.send(embed = question)
            answer = number1 + number2
            answerr = str(answer)
            msg = await self.Bot.wait_for('message', check=check)
            if msg.content == answerr:
                embed = discord.Embed(title="Correct Answer!",colour=discord.Color.from_rgb(0,255,148))
                embed.set_footer(text=f"Good one {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
            else:
                embed = discord.Embed(title="Wrong Answer!",description=f"{ctx.message.author.mention},\nCorrect answer was `{answerr}`.",colour=discord.Color.red())
                embed.set_footer(text=f"Maybe next time {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
        elif type == 2:
            number1 = randint(500,1000)
            number2 = randint(1,500)
            question = discord.Embed(title="What's the answer of following question?",description=f"\n__Question__\n{number1} - {number2} = ?",colour=discord.Color.random())
            await ctx.send(embed = question)
            answer = number1 - number2
            answerr = str(answer)
            msg = await self.Bot.wait_for('message', check=check)
            if msg.content == answerr:
                embed = discord.Embed(title="Correct Answer!",colour=discord.Color.from_rgb(0,255,148))
                embed.set_footer(text=f"Good one {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
            else:
                embed = discord.Embed(title="Wrong Answer!",description=f"{ctx.message.author.mention},\nCorrect answer was `{answerr}`.",colour=discord.Color.red())
                embed.set_footer(text=f"Maybe next time {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
        elif type == 3:
            number1 = randint(1,70)
            number2 = randint(1,50)
            question = discord.Embed(title="What's the answer of following question?",description=f"\n__Question__\n{number1} × {number2} = ?",colour=discord.Color.random())
            await ctx.send(embed = question)
            answer = number1 * number2
            answerr = str(answer)
            msg = await self.Bot.wait_for('message', check=check)
            if msg.content == answerr:
                embed = discord.Embed(title="Correct Answer!",colour=discord.Color.from_rgb(0,255,148))
                embed.set_footer(text=f"Good one {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
            else:
                embed = discord.Embed(title="Wrong Answer!",description=f"{ctx.message.author.mention},\nCorrect answer was `{answerr}`.",colour=discord.Color.red())
                embed.set_footer(text=f"Maybe next time {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
        elif type == 4:
            number1 = randint(1,70)
            number2 = randint(1,20)
            question = discord.Embed(title="What's the answer of following question?",description=f"\n__Question__\n{number1} ÷ {number2} = ?\n\nAnswer can be given as integer.",colour=discord.Color.random())
            await ctx.send(embed = question)
            answer = number1 // number2
            answe = number1 / number2
            answ = str(answe)
            answerr = str(answer)
            msg = await self.Bot.wait_for('message', check=check)
            if msg.content == answerr:
                embed = discord.Embed(title="Correct Answer!",colour=discord.Color.from_rgb(0,255,148))
                embed.set_footer(text=f"Good one {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
            elif msg.content == answ:
                embed = discord.Embed(title="Correct Answer!",colour=discord.Color.from_rgb(0,255,148))
                embed.set_footer(text=f"Good one {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)
            else:
                embed = discord.Embed(title="Wrong Answer!",description=f"{ctx.message.author.mention},\nCorrect answer was `{answerr}`.",colour=discord.Color.red())
                embed.set_footer(text=f"Maybe next time {ctx.message.author.display_name}!",icon_url=ctx.message.author.avatar_url)
                await msg.reply(embed=embed)


def setup(Bot):
    Bot.add_cog(Quiz(Bot))