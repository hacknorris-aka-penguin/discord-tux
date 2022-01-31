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
from keep_alive import keep_alive
import json, random, requests, datetime, time, urllib.request, io, os, aiohttp
from datetime import datetime, timedelta
import math
import base64 as b64
#
# code:


intents = discord.Intents.all()
bot = commands.Bot(
        command_prefix='$', 
        help_command=None, 
        case_insensitive=False,
        intents=intents
        )

commands = [
"cmds.information",
"cmds.man",
"cmds.moderation",
"cmds.server-organisation",
"cmds.utils",
"cmds.errors"
]

if __name__ == '__main__':
    for command in commands:
        bot.load_extension(command)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$man command..."))

        
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

keep_alive()
token = os.environ.get("token")
bot.run(token)

