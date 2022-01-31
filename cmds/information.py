import discord
from discord.ext import commands

class information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def neofetch(self, ctx):
    await ctx.send(
        f"```fix\n          /--\         OS NAME : {ctx.guild.name}\n       -- \--/ -- \n     /            \    STORAGE : {ctx.guild.member_count} users \n     |            | \n   /--\          /--\  INSTALLATION DATE : {ctx.guild.created_at}\n   \--/          \--/ \n     \            /    DIRECTORIES : {len(ctx.guild.channels)} \n       ---------- ```"
    )
    
@commands.command()
async def echo(self, ctx, *, arg):
    await ctx.send(f"{arg}")

@commands.command()
async def ping(self, ctx):
    replytime = bot.latency * 1000
    await ctx.send(f'Hi! I answered in {replytime} ms!')

@commands.command()
async def whoami(self, ctx):
    await ctx.send(f'```{ctx.author}```')
    return

@commands.command()
async def whois(self, ctx, member: discord.Member):
    await ctx.send(f"```{member.name}#{member.discriminator}```")
    
@commands.command()
async def time(self, ctx):
    now = datetime.now()
    now2 = now.timestamp()
    await ctx.send(f"`now? its `<t:{round(now2)}:T>")
    
@commands.command()
async def id(self, ctx, member: discord.Member):
    id = member.id
    await ctx.send(f"```{id}```")
    
@commands.command()
async def stat(self, ctx, member: discord.Member = None):
    if member == None:
        await ctx.send(f"```{ctx.message.author.status}```")
    else:
        await ctx.send(f"```{member.status}```")
        
def setup(bot):
    bot.add_cog(information(bot))
