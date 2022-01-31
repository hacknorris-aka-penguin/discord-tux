import discord
from discord.ext import commands

class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def cowsay(self, ctx, *, arg=None):
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

@commands.command()
async def calc(self, ctx, *, equation):
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

@commands.command()
async def base64(self, ctx, arg1, *, arg):
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
        
@commands.command()
async def noot(self, ctx):
    await ctx.send(
        "https://tenor.com/view/pingu-noot-nootnoot-no-maby-gif-6123519")
        
def setup(bot):
    bot.add_cog(utils(bot))
