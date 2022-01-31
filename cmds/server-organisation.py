import discord
from discord.ext import commands

class organisation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rm(self, ctx, arg1):
        channel = ctx.channel
        msg = await channel.fetch_message(arg1)
        await msg.delete()
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rename(self, ctx, channel: discord.TextChannel, arg1):
        await channel.edit(name=arg1)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mkdir(self, ctx, arg1):
        guild = ctx.message.guild
        await guild.create_text_channel(arg1)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx):
        await ctx.channel.purge()
    
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def rmdir(self, ctx, channel: discord.TextChannel):
        await channel.delete()
    
def setup(bot):
    bot.add_cog(organisation(bot))
