import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
@commands.has_permissions(administrator=True)
async def chmod(self, ctx, arg1, member: discord.Role):
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
       
@commands.command()
@commands.has_permissions(administrator=True)
async def kill(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
@commands.command(aliases=["adduser"])
@commands.has_permissions(administrator=True)
async def useradd(self, ctx, arg1):
    guild = ctx.guild
    await guild.create_role(name=arg1)

@commands.command()
@commands.has_permissions(administrator=True)
async def userdel(self, ctx, role: discord.Role):
    await role.delete()
    
def setup(bot):
    bot.add_cog(moderation(bot))
