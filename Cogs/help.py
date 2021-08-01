import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def help(self,ctx,command = None):
        if command == None:
            embed=discord.Embed(title="**Commands (17)**",description="➜ **Moderation**\n`setprefix`\n➜ **Utility**\n`bugreport`\n➜ **Info**\n`help`,`info`,`ping`\n➜**Calculation**\n`calculator`,`add`,`sub`,`mul`,`div`,`sqrt`,`factorial`,`random`,`length`\n➜ **More**\n`time`,`genpassw`,`remindme`",colour=discord.Color.from_rgb(0,255,148))
            await ctx.send(embed=embed)
        elif command == "setprefix".lower():
            SETPREFIXembed=discord.Embed(title="**Command 'setprefix'**",description="\n• **Usage** : `-setprefix <prefix>`\n• **Description** : Changes the prefix in server.\n• **Note** : Administrator permission is required to use this command.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SETPREFIXembed)
        elif command == "setprefix".upper():
            SETPREFIXembed=discord.Embed(title="**Command 'setprefix'**",description="\n• **Usage** : `-setprefix <prefix>`\n• **Description** : Changes the prefix in server.\n• **Note** : Administrator permission is required to use this command.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SETPREFIXembed)
        elif command == "help".lower():
            HELPembed=discord.Embed(title="**Command 'help'**",description="\n• **Usage** : `-help`\n• **Description** : Shows the help message.",colour=discord.Color.dark_theme())           
            await ctx.send(embed=HELPembed)
        elif command == "help".upper():
            HELPembed=discord.Embed(title="**Command 'help'**",description="\n• **Usage** : `-help`\n• **Description** : Shows the help message.",colour=discord.Color.dark_theme())           
            await ctx.send(embed=HELPembed)
        elif command == "info".lower():
            CREDITSembed=discord.Embed(title="**Command 'info'**",description="\n• **Usage** : `-info`\n• **Description** : Shows informations about the bot.",colour=discord.Color.dark_theme())
            await ctx.send(embed=CREDITSembed)
        elif command == "info".upper():
            CREDITSembed=discord.Embed(title="**Command 'info'**",description="\n• **Usage** : `-info`\n• **Description** : Shows informations about the bot.",colour=discord.Color.dark_theme())
            await ctx.send(embed=CREDITSembed)
        elif command == "ping".lower():
            PINGembed=discord.Embed(title="**Command 'ping'**",description="\n• **Usage** : `-ping`\n• **Description** : Shows bot's latency.",colour=discord.Color.dark_theme())
            await ctx.send(embed=PINGembed)
        elif command == "ping".upper():
            PINGembed=discord.Embed(title="**Command 'ping'**",description="\n• **Usage** : `-ping`\n• **Description** : Shows bot's latency.",colour=discord.Color.dark_theme())
            await ctx.send(embed=PINGembed)
        elif command == "add".upper():
            ADDembed=discord.Embed(title="**Command 'add'**",description="\n• **Usage** : `-add <number1> <number2>`\n• **Description** : Adds up entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=ADDembed)
        elif command == "add".lower():
            ADDembed=discord.Embed(title="**Command 'add'**",description="\n• **Usage** : `-add <number1> <number2>`\n• **Description** : Adds up entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=ADDembed)
        elif command == "sub".lower():
            SUBembed=discord.Embed(title="**Command 'sub'**",description="\n• **Usage** : `-sub <number1> <number2>`\n• **Description** : Subtracts entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SUBembed)
        elif command == "sub".upper():
            SUBembed=discord.Embed(title="**Command 'sub'**",description="\n• **Usage** : `-sub <number1> <number2>`\n• **Description** : Subtracts entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SUBembed)
        elif command == "mul".lower():
            MULembed=discord.Embed(title="**Command 'mul'**",description="\n• **Usage** : `-mul <number1> <number2>`\n• **Description** : Multiplies entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=MULembed)
        elif command == "mul".upper():
            MULembed=discord.Embed(title="**Command 'mul'**",description="\n• **Usage** : `-mul <number1> <number2>`\n• **Description** : Multiplies entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=MULembed)
        elif command == "div".lower():
            DIVembed=discord.Embed(title="**Command 'div'**",description="\n• **Usage** : `-div <number1> <number2>`\n• **Description** : Divides entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DIVembed)
        elif command == "div".upper():
            DIVembed=discord.Embed(title="**Command 'div'**",description="\n• **Usage** : `-div <number1> <number2>`\n• **Description** : Divides entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DIVembed)
        elif command == "sqrt".lower():
            SQRTembed=discord.Embed(title="**Command 'sqrt'**",description="\n• **Usage** : `-sqrt <number>`\n• **Description** : Takes the square root of entered number.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        elif command == "sqrt".upper():
            SQRTembed=discord.Embed(title="**Command 'sqrt'**",description="\n• **Usage** : `-sqrt <number>`\n• **Description** : Takes the square root of the entered number.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        elif command == "factorial".lower():
            FACTORIALembed=discord.Embed(title="**Command 'factorial'**",description="\n• **Usage** : `-factorial <number>`\n• **Description** : Shows the factorial of the entered number.\n• **Note** : Entered number must be integer and length must be less than four.",colour=discord.Color.dark_theme())
            await ctx.send(embed=FACTORIALembed)
        elif command == "factorial".upper():
            FACTORIALembed=discord.Embed(title="**Command 'factorial'**",description="\n• **Usage** : `-factorial <number>`\n• **Description** : Shows the factorial of the entered number.\n• **Note** : Entered number must be integer and length must be less than four.",colour=discord.Color.dark_theme())
            await ctx.send(embed=FACTORIALembed)
        elif command == "time".lower():
            DATEembed=discord.Embed(title="**Command 'time'**",description="\n• **Usage** : `-time`\n• **Description** : Displays the time in UTC.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DATEembed)
        elif command == "time".upper():
            DATEembed=discord.Embed(title="**Command 'time'**",description="\n• **Usage** : `-time`\n• **Description** : Displays the time in UTC.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DATEembed)
        elif command == "genpassw".lower():
            PASSWembed=discord.Embed(title="**Command 'genpassw'**",description="\n• **Usage** : `-genpassw`\n• **Description** : Generates a random password.")
            await ctx.send(embed=PASSWembed)
        elif command == "genpassw".upper():
            PASSWembed=discord.Embed(title="**Command 'genpassw'**",description="\n• **Usage** : `-genpassw`\n• **Description** : Generates a random password.")
            await ctx.send(embed=PASSWembed)
        elif command == "random".lower():
            RANDembed=discord.Embed(title="**Command 'random'**",description="\n• **Usage** : `-random <number1> <number2>`\n• **Description** : Generates a random number between given numbers.")
            await ctx.send(embed=RANDembed)
        elif command == "random".upper():
            RANDembed=discord.Embed(title="**Command 'random'**",description="\n• **Usage** : `-random <number1> <number2>`\n• **Description** : Generates a random number between given numbers.")
            await ctx.send(embed=RANDembed)
        elif command == "remindme".lower():
            REMINDMEembed=discord.Embed(title="**Command 'remindme'**",description="\n• **Usage** : `-remindme <time/s/m/h/d> <reminder-text>`\n• **Description** : Sets a reminder for specified time.\n• **Note** : Time must be at least 5 minutes and at most 14 days/2 weeks.")
            await ctx.send(embed=REMINDMEembed)
        elif command == "remindme".upper():
            REMINDMEembed=discord.Embed(title="**Command 'remindme'**",description="\n• **Usage** : `-remindme <time/s/m/h/d> <reminder-text>`\n• **Description** : Sets a reminder for specified time.\n• **Note** : Time must be at least 5 minutes and at most 14 days/2 weeks.")
            await ctx.send(embed=REMINDMEembed)
        elif command == "length".lower():
            LENGTHembed =discord.Embed(title="**Command 'length'**",description="\n• **Usage** : `-length <message>`\n• **Description** : Shows the length of entered message.\n• **Note** : Spaces don't count.")
            await ctx.send(embed=LENGTHembed)
        elif command == "length".upper():
            LENGTHembed =discord.Embed(title="**Command 'length'**",description="\n• **Usage** : `-length <message>`\n• **Description** : Shows the length of entered message.\n• **Note** : Spaces don't count.")
            await ctx.send(embed=LENGTHembed)
        elif command == "bugreport".lower():
            BUGembed =discord.Embed(title="**Command 'bugreport'**",description="\n• **Usage** : `-bugreport <bug_message>`\n• **Description** : Sends a bug report message to developer.\n• **Note** : Please do not abuse this command.")
            await ctx.send(embed=BUGembed)
        elif command == "bugreport".upper():
            BUGembed =discord.Embed(title="**Command 'bugreport'**",description="\n• **Usage** : `-bugreport <bug_message>`\n• **Description** : Sends a bug report message to developer.\n• **Note** : Please do not abuse this command.")
            await ctx.send(embed=BUGembed)
        elif command == "calculator".lower():
            CALCULATORembed =discord.Embed(title="**Command 'calculator'**",description="\n• **Usage** : `-calculator`\n• **Description** : Displays a virtual calculator.")
            await ctx.send(embed=CALCULATORembed)
        elif command == "calculator".upper():
            CALCULATORembed =discord.Embed(title="**Command 'calculator'**",description="\n• **Usage** : `-calculator`\n• **Description** : Displays a virtual calculator.")
            await ctx.send(embed=CALCULATORembed)
        else:
            UNKNOWNembed=discord.Embed(title="**Unknown Command**",description="Use the `-help` command to see all commands.",colour=discord.Color.red())
            reaction = "❌"
            await ctx.message.add_reaction(reaction)
            await ctx.send(embed=UNKNOWNembed)

def setup(Bot):
    Bot.add_cog(Help(Bot))
