from discord.ext import commands

class man(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def man(self, ctx, arg1=None):
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
        
def setup(bot):
    bot.add_cog(man(bot))
