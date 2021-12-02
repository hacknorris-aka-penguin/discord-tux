# bot (and also linux) support server → https://discord.gg/Trev9WEga5
#
#license - at the bottom of this file 
# (i couldnt make license.txt cause wasnt displaying in preview :'D)
# sorry for uncommented imports but my bot got discontinued as discord.py got 
# deleted and developer got banned from top.gg server. sorry
# •w•
#imports :
#
import discord
from discord.ext import commands
import json, random, requests, datetime, time, urllib.request, io, os, aiohttp
from datetime import datetime, timedelta
import math
import base64 as b64
#
# code:


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', help_command=None, intents=intents)


with open("bad-words.txt", 'r') as f:
    global badwords
    words = f.read()
    badwords = words.splitlines()

@bot.listen("on_message")
async def swears(ctx):
    msg = ctx.content.lower()
    for word in badwords:
        if word in msg:
            await ctx.delete()

@bot.listen("on_message")
async def pingraid(ctx):
  msg = ctx.content.lower()
  if len(ctx.mentions) >= 10:
    await ctx.channel.send(f"why are you pinging too much @{ctx.author} ?")
    if ctx.guild.role(name="muted") in ctx.guild.roles :
      await ctx.author.add_roles("muted")
    else:
      await ctx.guild.create_role(name="muted")
      await ctx.author.add_roles("muted")

l = []
scam = requests.get("https://script.googleusercontent.com/macros/echo?user_content_key=V1VRkcLy79NqRzGszzki5IwoqgfiRS0CPnpSth1jVdX0Z88w39o7tC71MMkAARMFYXSZIe5ysMkkTdp_V8q-gLFNUefAtxy5m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnA1zRMJcOWhp5p8-TrasYiLfc8s82yHYvncMdEYM4VMzrAWyr3_vgWcPkd2qwPRs1bz0TAVXLS4Dleb--x_lwbJ0QrOacq8a_9z9Jw9Md8uu&lib=Mvhguv8KrjGlroshaZkuz2rjldAiTUHuJ")
Data = scam.json()
for i in Data:
    for key in i:
        l.append(i["put here stean scam: ↓↓↓"])

@bot.listen("on_message")
async def scam(ctx):
    global l
    for thing in l:
        if thing in ctx.content:
            await ctx.delete()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$man command..."))

@bot.command()
@commands.has_permissions(administrator=True)
async def rm(ctx, arg1):
    channel = ctx.channel
    msg = await channel.fetch_message(arg1)
    await msg.delete()

@bot.command()
async def stat(ctx, member: discord.Member = None):
    if member == None:
        await ctx.send(f"```{ctx.message.author.status}```")
    else:
        await ctx.send(f"```{member.status}```")

@bot.command()
@commands.has_permissions(administrator=True)
async def rename(ctx, channel: discord.TextChannel, arg1):
    await channel.edit(name=arg1)

@bot.command()
async def id(ctx, member: discord.Member):
    id = member.id
    await ctx.send(f"```{id}```")

@bot.command()
async def find(ctx, *, arg):
    return

@bot.command()
async def wget(ctx, arg1):
    url = arg1
    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]
    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(file_name, 'wb') as file:
            for data in r:
                await ctx.send(file=data)

@bot.command()
@commands.has_permissions(administrator=True)
async def mkdir(ctx, arg1):
    guild = ctx.message.guild
    await guild.create_text_channel(arg1)

@bot.command()
async def noot(ctx):
    await ctx.send(
        "https://tenor.com/view/pingu-noot-nootnoot-no-maby-gif-6123519")

@bot.command()
async def man(ctx, arg1=None):
    if arg1 is None:
        await ctx.send(
            "available commands: \n```fix\nrm, rename, id, noot, stat, man (this command), kill, adduser/useradd, userdel, time, cowsay, calc, base64, clear, echo, ping, whoami, whois, rmdir, neofetch, chmod, mkdir\n```\n```\nfor info about one command type '$man (command)', optional values are in [] and required values in ()\n```"
        )
    elif arg1 == "rm":
        await ctx.send(
            "usage:\n $rm (message id)\n this command delete messages by their id"
        )
    elif arg1 == "noot":
        await ctx.send("NOOT NOOT!!!")
    elif arg1 == "man":
        await ctx.send(
            "usage:\n $man [optional - command] \n show all commands and also how to use them"
        )
    elif arg1 == "kill":
        await ctx.send(
            "usage:\n $kill (user mention or id)\n kicks mentioned user")
    elif arg1 == "time":
        await ctx.send("usage:\n $time \n shows current time in UTC 0 timezone"
                       )
    elif arg1 == "cowsay":
        await ctx.send(
            "usage:\n $cowsay [optional message] \n shows a meme-ified cow saying random jokes or custom message"
        )
    elif arg1 == "calc":
        await ctx.send(
            "usage:\n $calc (number)(operator)(number) \n do a simple maths")
    elif arg1 == "base64":
        await ctx.send(
            "usage:\n $base64 (encode/decode) (text to encrypt or decrypt) \n codes messages using known base64 algorithm"
        )
    elif arg1 == "clear":
        await ctx.send(
            "usage:\n $clear \n deletes recent 100 messages. Never blocked by discord"
        )
    elif arg1 == "echo":
        await ctx.send("usage:\n $echo (text to resend) \n resends typed text")
    elif arg1 == "ping":
        await ctx.send("usage:\n $echo \n checks speed and connection with bot"
                       )
    elif arg1 == "whoami":
        await ctx.send("usage:\n $whoami \n sends your username with hash")
    elif arg1 == "whois":
        await ctx.send(
            "usage:\n $whois (user mention) \n sends someone username with hash"
        )
    elif arg1 == "rmdir":
        await ctx.send(
            "usage:\n $rmdir (channel mention)\n deletes mentioned channel")
    elif arg1 == "neofetch":
        await ctx.send(
            "usage:\n $neofetch \n sends some info (like number of users and name) of your server"
        )
    elif arg1 == "chmod":
        await ctx.send(
            "usage:\n $chmod (argument) (role mention) \n variables for argument:\n```fix\n 0 - dont see channels \n 1 - embed links and files, use emojis, tts messages, video/streams, uses voice activity, is prioritied speaker, changes nick, creates invites and use slash commands\n 2 - speaks, sends messages\n 3 - uses both permissions from 1 arg and 2 \n 4 - reads message history, connect to VC \n 5 - uses permissions from 1 and 4 arg \n 6 - uses permissions from 2 and 4 arg \n 7 - uses permissions from 1, 2 and 4 arg\n mod - makes role moderator of a server\n```\n manages roles permissions"
        )
    elif arg1 == "adduser" or arg1 == "useradd":
        await ctx.send(
            "usage:\n $adduser (role name) OR $useradd (role name) \n add roles with custom name"
        )
    elif arg1 == "userdel":
        await ctx.send(
            "usage:\n $userdel (role mention \n removes selected role from server)"
        )
    elif arg1 == "mkdir":
        await ctx.send(
            "usage:\n $mkdir (channel name)\ncreates channel with custom name")
    elif arg1 == "stat":
        await ctx.send(
            "usage:\n $stat [optional user] \n shows status af a user")
    elif arg1 == "id":
        await ctx.send("usage:\n $id (user) \n shows id of a user")
    elif arg1 == "rename":
        await ctx.send(
            "usage: \n $rename (channel) (new name)\n renames channel using cutom name (if channel contains spaces - put it in quote. but even if - will get converted to '-' signs)"
        )
    else:
        return

@bot.command(aliases=["adduser"])
@commands.has_permissions(administrator=True)
async def useradd(ctx, arg1):
    guild = ctx.guild
    await guild.create_role(name=arg1)

@bot.command()
@commands.has_permissions(administrator=True)
async def userdel(ctx, role: discord.Role):
    await role.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def kill(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("What was that ?!\n:eyes:")
    else:
        raise error

@bot.command()
async def time(ctx):
    now = datetime.now()
    now2 = now.timestamp()
    await ctx.send(f"`now? its `<t:{round(now2)}:T>")

@bot.command()
async def cowsay(ctx, *, arg=None):
    if arg is None:
        url = 'https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Pun?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart'
        joker = requests.get(url)
        joke = json.loads(joker.text)
        await ctx.send(
            f" \_\_\_\_\_\_\_\_\_\_\_\n | Q: {joke['setup']} | \n | A: {joke['delivery']} | \n ------------- \n        \\      ^\_\_^ \n          \\    (oo)\\_\_\_\_\_\_\_ \n                (\_\_)\\             )\\/\\ \n                        \|\|-------w \| \n                        \|\|              \|\|"
        )
    else:
        await ctx.send(
            f" \_\_\_\_\_\_\_\_\_\_\_\n < {arg} > \n ------------- \n        \\      ^\_\_^ \n          \\    (oo)\\_\_\_\_\_\_\_ \n                (\_\_)\\             )\\/\\ \n                        \|\|-------w \| \n                        \|\|              \|\|"
        )

@bot.command()
async def calc(ctx, *, equation):
    allOperators = ['+', '-', '*', '/', '^', '%', '=', '>=', '<=', '>', '<']
    operator = ''
    for x in allOperators:
        if x in equation:
            operator = x
    equation = equation.split(operator)
    num1, num2 = float(equation[0]), float(equation[1])
    result = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x**y,
        '%': lambda x, y: x % y,
        '=': lambda x, y: x == y,
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y
    }[operator](num1, num2)
    if result % 1 == 0:
        result = int(result)
    await ctx.send(f"```{result}```")

@bot.command()
async def base64(ctx, arg1, *, arg):
    if arg1 == "encode":
        var1 = arg.encode("ascii")
        var2 = b64.b64encode(var1)
        var3 = var2.decode("ascii")
        await ctx.send(f"```{var3}```")
    elif arg1 == "decode":
        var1 = arg.strip()
        var2 = var1.encode("ascii")
        var3 = b64.b64decode(var2)
        await ctx.send(f"```{var3}```")
    else:
        return

@bot.command()
@commands.has_permissions(administrator=True)
async def chmod(ctx, arg1, member: discord.Role):
    if arg1 == "0":
        await member.edit(permissions=discord.Permissions(view_channel=False))
    elif arg1 == "1":
        await member.edit(
            permissions=discord.Permissions(embed_links=True,
                                            attach_files=True,
                                            add_reactions=True,
                                            use_external_emojis=True,
                                            send_tts_messages=True,
                                            use_slash_commands=True,
                                            stream=True,
                                            use_voice_activation=True,
                                            priority_speaker=True,
                                            change_nickname=True,
                                            create_instant_invite=True))
    elif arg1 == "2":
        await member.edit(
            permissions=discord.Permissions(send_messages=True, speak=True))
    elif arg1 == "3":
        await member.edit(
            permissions=discord.Permissions(embed_links=True,
                                            attach_files=True,
                                            add_reactions=True,
                                            use_external_emojis=True,
                                            send_tts_messages=True,
                                            use_slash_commands=True,
                                            stream=True,
                                            use_voice_activation=True,
                                            priority_speaker=True,
                                            send_messages=True,
                                            speak=True,
                                            change_nickname=True,
                                            create_instant_invite=True))
    elif arg1 == "4":
        await member.edit(permissions=discord.Permissions(
            read_message_history=True, connect=True))
    elif arg1 == "5":
        await member.edit(
            permissions=discord.Permissions(embed_links=True,
                                            attach_files=True,
                                            add_reactions=True,
                                            use_external_emojis=True,
                                            send_tts_messages=True,
                                            use_slash_commands=True,
                                            stream=True,
                                            use_voice_activation=True,
                                            priority_speaker=True,
                                            read_message_history=True,
                                            connect=True,
                                            change_nickname=True,
                                            create_instant_invite=True))
    elif arg1 == "6":
        await member.edit(
            permissions=discord.Permissions(send_messages=True,
                                            read_message_history=True,
                                            connect=True,
                                            speak=True))
    elif arg1 == "7":
        await member.edit(
            permissions=discord.Permissions(embed_links=True,
                                            attach_files=True,
                                            add_reactions=True,
                                            use_external_emojis=True,
                                            send_tts_messages=True,
                                            use_slash_commands=True,
                                            stream=True,
                                            use_voice_activation=True,
                                            priority_speaker=True,
                                            send_messages=True,
                                            read_message_history=True,
                                            connect=True,
                                            change_nickname=True,
                                            create_instant_invite=True))
    elif arg1 == "mod":
        await member.edit(permissions=discord.Permissions(administrator=True))
    else:
        return

@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx):
    await ctx.channel.purge()

@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(f"{arg}")

@bot.command()
async def ping(ctx):
    replytime = bot.latency * 1000
    await ctx.send(f'Hi! I answered in {replytime} ms!')

@bot.command()
async def whoami(ctx):
    await ctx.send(f'```{ctx.author}```')
    return

@bot.command()
async def whois(ctx, member: discord.Member):
    await ctx.send(f"```{member.name}#{member.discriminator}```")

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def rmdir(ctx, channel: discord.TextChannel):
    await channel.delete()

@bot.command()
async def neofetch(ctx):
    await ctx.send(
        f"```fix\n          /--\         OS NAME : {ctx.guild.name}\n       -- \--/ -- \n     /            \    STORAGE : {ctx.guild.member_count} users \n     |            | \n   /--\          /--\  INSTALLATION DATE : {ctx.guild.created_at}\n   \--/          \--/ \n     \            /    DIRECTORIES : {len(ctx.guild.channels)} \n       ---------- ```"
    )


token = "ODUzMzQ4OTU3OTUzOTgyNTAy.YMUFJg.UASw3bQx9wvICVjsL8Apz_OqvYI"
bot.run(token)

