import discord
import json
import discord

from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


def get_prefix(bot, message):
    prefixes = ['t/']
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, description='Discord Bot Made For All', case_insensitive=True)
bot.remove_command("help")


initial_extensions = ['cogs.owner', 'cogs.ping', 'cogs.help',
 'cogs.info', 'cogs.economy', 'cogs.fun', 'cogs.mod', 'cogs.logging']


if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="w/help")
    )
    print(
        f"""        ----------------
        Bot is ready!
        ---------------
        Author: Sean/Worlds Owner
        ---------------
        Logged in as: {bot.user.name}
        ---------------
        Current Version: 433634.128947
        ---------------"""
    )


@bot.command(aliases=["firstmessage"], help="Pull first sent message in a channel.")
@commands.has_permissions(manage_messages=True)
async def fm(ctx, channel: discord.TextChannel=None):
	if channel is None:
		channel = ctx.channel
		fm = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(description=fm.content, timestamp=ctx.message.created_at)
		embed.add_field(name="First Ever Message!", value=f"[Click To Go To Message]({fm.jump_url})\nChannel: <#{channel.id}>")
		embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
		embed.set_footer(text=f"World - First Message")
		embed.color = (ctx.author.color)
		await ctx.send(embed=embed)
	else:
		fm = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(description=fm.content, timestamp=ctx.message.created_at)
		embed.add_field(name="First Ever Message!", value=f"[Click To Go To Message]({fm.jump_url})\nChannel: <#{channel.id}>")
		embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
		embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
		embed.set_footer(text=f"World - First Message")
		embed.color = (ctx.author.color)
		await ctx.send(embed=embed)


@fm.error
async def fm_error(ctx, error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Dont Have `manage messages` Permission')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if bot.user in message.mentions:
        embed = discord.Embed(
        title='', description=f'Here Are My Prefixes: `w/`, `world `' , colour=message.author.color)
        embed.set_footer(text="Type <prefix>help for more info.")
        await message.channel.send(embed = embed)
    await bot.process_commands(message)


@bot.event
async def on_message(message: discord.Message) -> None:
    with open("blacklisted.json") as file:
        blacklisted_users = json.load(file)
        if message.author.id in blacklisted_users["blacklisted"]:
            return

    await bot.process_commands(message)


@bot.command(help="[Nsfw], Screenshot a website.")
async def screenshot(ctx, site):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(title="World - Screenshot", timestamp=ctx.message.created_at, color=ctx.author.color)
        embed.set_image(url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{site}")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Nsfw Only!", timestamp=ctx.message.created_at, color=ctx.author.color)
        embed.set_image(url=f"https://media.discordapp.net/attachments/265156286406983680/728328135942340699/nsfw.gif")
        await ctx.send(embed=embed)
	
@bot.event
async def on_command_error(ctx, error):
    if ctx.author.id == 662334026098409480 or ctx.author.id == 393859835331870721:
        channels = bot.get_channel(746028290455634032)
        embed = discord.Embed(description=f":x: New Logged Error By A World Developer!\n```{error}```\nInvoker: `{ctx.author}`", color=discord.Color.blue())
        embed.set_thumbnail(url=bot.user.avatar_url)
        await channels.send(embed=embed)

bot.run("no token for u", bot=True, reconnect=True)
