import discord
import inspect
import traceback
import asyncio
from discord.ext import commands
TOKEN = '||Think Ima Give You My Token!?||'

import mysql.connector
from mysql.connector import pooling
mysql_connection = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="join_connector",
    pool_size=2,
    pool_reset_session=True,
    host="107.161.23.32",
    database="ohlhifit_world",
    user="ohlhifit_world",
    passwd="Uox7B$3qAu$W"
)
mydb = mysql_connection.get_connection()


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

    @commands.command(hidden=True, help="IDK")
    async def sqleval(self, ctx, *, code):
    	if ctx.author.id == 662334026098409480 or ctx.author.id == 393859835331870721:
    		cursor = mydb.cursor()
    		cursor.execute(str(code))
    		result = cursor.fetchall()
    		await ctx.send(f'{result}')     
    	else:
    		await ctx.send("Sorry this command can only be used by my owner.")   

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

    @commands.command(name="eval")
    @commands.is_owner()
    async def eval_(self, ctx: commands.Context, *, code: str):
        import traceback
        code = code.strip("`")
        if code.startswith(("py\n", "python\n")):
            code = "\n".join(code.split("\n")[1:])

        try:
            exec(
                "async def __function():\n"
                + "".join(f"\n    {line}" for line in code.split("\n")),
                locals()
            )

            await locals()["__function"]()
        except Exception:
            res = discord.Embed(title="Error!", description=f"```{traceback.format_exc()}```", color=discord.Color.red())
            res.set_footer(text=f"Invoker: {ctx.author}", icon_url=ctx.author.avatar_url_as(format="png"))
            await ctx.send(embed=res)
    @eval_.error
    async def eval__error(self, ctx, error):
        embed = discord.Embed(title="Error!", description=f"```{error}```", color=discord.Color.red())
        embed.set_footer(text=f"Invoker: {ctx.author}", icon_url=ctx.author.avatar_url_as(format="png"))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def selfpurge(self, ctx, amount: int):
    	def world(m):
    		return m.author == self.bot.user
    	await ctx.message.channel.purge(limit=amount, check=world)
    	embed = discord.Embed(title="Purged", description=f"{ctx.author.mention} i have successfully purged `{amount}` of messages in <#{ctx.message.channel.id}>", color=ctx.author.color)
    	yes = await ctx.send(embed=embed)
    	await asyncio.sleep(3)
    	await yes.delete()
    	await ctx.message.delete()



def setup(bot):
    bot.add_cog(OwnerCog(bot))
