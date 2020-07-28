import discord
from discord.ext import commands
TOKEN = '||Think Ima Give You My Token!?||'


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True, help="Load a python file.")
    @commands.is_owner()
    async def load(self, ctx, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            embed = discord.Embed(title='load!', description=f"I Have loaded `{module}`", colour=ctx.author.colour)
            await ctx.send(content=None, embed=embed)

    @commands.command(hidden=True, help="Unload a python file.")
    @commands.is_owner()
    async def unload(self, ctx, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            embed = discord.Embed(title='Unload!', description=f"I Have Unloaded `{module}`", colour=ctx.author.colour)
            await ctx.send(content=None, embed=embed)

    @commands.command(name='reload', hidden=True, help="Reload python file.")
    @commands.is_owner()
    async def _reload(self, ctx, module):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            embed = discord.Embed(title='Reload!', description=f"I Have Reloaded `{module}`", colour=ctx.author.colour)
            await ctx.send(content=None, embed=embed)

    @commands.command(name='eval', help="Eval some code.")
    @commands.is_owner()
    async def eval_(self, ctx, *, code):
        await eval(code)

    @eval_.error
    async def eval__error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(
                title='Eval', description='' , colour=discord.Colour.blue())
            embed.add_field(name='Output', value=f'ERROR ```\n{error}\n```', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title='Eval', description='' , colour=discord.Colour.blue())
            embed.add_field(name='Output', value=f'ERROR ```\n{error}\n```', inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(OwnerCog(bot))
