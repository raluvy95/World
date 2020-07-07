#MIT License

#Copyright (c) 2020 Shuana

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import discord
import asyncio
import random
import os
import time
import requests
import aiohttp
import urllib
import json
import discord
import sys
import inspect
import traceback
import datetime
import platform
import pip
import io
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


def get_prefix(bot, message):
    prefixes = ['world ', 'w/']
    return commands.when_mentioned_or(*prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, description='Discord Bot Made For All', case_insensitive=True)
bot.remove_command("help")


initial_extensions = ['cogs.owner', 'cogs.ping', 'cogs.help', 'cogs.info', 'cogs.economy', 'cogs.fun', 'cogs.mod']


if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.online, activity=discord.Game("w/help | For More Info")
    )
    print(
        """        ----------------
        Bot is ready!
        ---------------
        Author: Sean/Worlds Owner
        ---------------
        Logged in as: World
        ---------------
        Current Version: 433634.128947
        ---------------"""
    )             


@bot.command(aliases=["firstmessage"])
@commands.has_permissions(manage_messages=True)
async def fm(ctx, channel: discord.TextChannel = None):  
	if channel is None:
		channel = ctx.channel
		fm = (await channel.history(limit=1, oldest_first=True).flatten())[0]
		embed = discord.Embed(description=fm.content, timestamp=ctx.message.created_at)
		embed.add_field(name="First Ever Message!", value=f"[Click To Go To Message]({fm.jump_url})\nChannel: <#{channel.id}>")
		embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
		embed.set_thumbnail(url="https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024")
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
	

@bot.command()
async def screenshot(ctx, site):
    if ctx.channel.is_nsfw():
        embed=discord.Embed(title="World - Screenshot", timestamp=ctx.message.created_at, color=ctx.author.color)
        embed.set_image(url=f"https://image.thum.io/get/width/1920/crop/675/maxAge/1/noanimate/{site}") 
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="Nsfw Only!", timestamp=ctx.message.created_at, color=ctx.author.color)
        embed.set_image(url=f"https://media.discordapp.net/attachments/265156286406983680/728328135942340699/nsfw.gif") 
        await ctx.send(embed=embed)
   
bot.run("really think i would leave my token here LOL", bot=True, reconnect=True)
