import discord
from discord.ext import commands
from discord_components import *
import datetime

def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred,try again.'
    return result

class Calculator(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.Bot)

    @commands.command()
    async def calculator(self,ctx):
        buttons = [
        [
            Button(style=ButtonStyle.grey, label='1'),
            Button(style=ButtonStyle.grey, label='2'),
            Button(style=ButtonStyle.grey, label='3'),
            Button(style=ButtonStyle.blue, label='×'),
            Button(style=ButtonStyle.red, label='Exit')
        ],
        [
            Button(style=ButtonStyle.grey, label='4'),
            Button(style=ButtonStyle.grey, label='5'),
            Button(style=ButtonStyle.grey, label='6'),
            Button(style=ButtonStyle.blue, label='÷'),
            Button(style=ButtonStyle.red, label='←')
        ],
        [
            Button(style=ButtonStyle.grey, label='7'),
            Button(style=ButtonStyle.grey, label='8'),
            Button(style=ButtonStyle.grey, label='9'),
            Button(style=ButtonStyle.blue, label='+'),
            Button(style=ButtonStyle.red, label='Clear')
        ],
        [
            Button(style=ButtonStyle.grey, label='00'),
            Button(style=ButtonStyle.grey, label='0'),
            Button(style=ButtonStyle.grey, label='.'),
            Button(style=ButtonStyle.blue, label='-'),
            Button(style=ButtonStyle.green, label='=')
        ],
    ]
        m = await ctx.send(content='**Loading Calculator <a:an_loading:867491877811781683>**')
        expression = 'None'
        delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        e = discord.Embed(title=f'{ctx.author.name}\'s Calculator | {ctx.author.id}', description=expression,
                            timestamp=delta)
        await m.edit(components=buttons, embed=e)
        while m.created_at < delta:
            res = await self.Bot.wait_for('button_click')
            if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
                0].timestamp < delta:
                expression = res.message.embeds[0].description
                if expression == 'None' or expression == 'An error occurred.':
                    expression = ''
                if res.component.label == 'Exit':
                    await res.respond(content='Calculator Closed', type=7)
                    break
                elif res.component.label == '←':
                    expression = expression[:-1]
                elif res.component.label == 'Clear':
                    expression = 'None'
                elif res.component.label == '=':
                    expression = calculate(expression)
                else:
                    expression += res.component.label
                f = discord.Embed(title=f'{res.author.name}\'s Calculator|{res.author.id}', description=expression,
                                    timestamp=delta)
                await res.respond(content='', embed=f, components=buttons, type=7)

def setup(Bot):
    Bot.add_cog(Calculator(Bot))