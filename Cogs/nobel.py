import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import io

class Nobel(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def nobel(self,ctx,member:discord.Member=None):
        if member==None:
            member = ctx.message.author
        IMAGE_WIDTH = 600
        IMAGE_HEIGHT = 300

        image = Image.open('C:\\Users\\cilma\\Desktop\\Calculator-main\\Images\\nobel.png')

        AVATAR_SIZE = 256

        avatar_asset = member.avatar_url_as(format='jpg', size=AVATAR_SIZE)

        buffer_avatar = io.BytesIO()
        await avatar_asset.save(buffer_avatar)
        buffer_avatar.seek(0)

        avatar_image = Image.open(buffer_avatar)

        avatar_image = avatar_image.resize((AVATAR_SIZE, AVATAR_SIZE)) # 

        x = 333
        y = 18
        image.paste(avatar_image, (x, y))
        buffer = io.BytesIO()

        image.save(buffer, format='PNG')    

        buffer.seek(0) 

        await ctx.send(file=discord.File(buffer, 'myimage.png'))


def setup(Bot):
    Bot.add_cog(Nobel(Bot))