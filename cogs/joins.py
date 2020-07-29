import discord
import asyncio
import urllib
import random
import requests
import io
import aiohttp
import json
from discord.ext import commands
from urllib.parse import urlparse
import mysql.connector
from mysql.connector import pooling
import aiohttp
import io

mysql_connection = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="join_connector",
    pool_size=2,
    pool_reset_session=True,
    host="not",
    database="your",
    user="buissness",
    passwd="fxcilities was here"
)
mydb = mysql_connection.get_connection()
class JoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @bot.Cog.listener()
    async def on_message(self, ctx):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM joins WHERE server_id = " + str(ctx.guild.id))
        result = cursor.fetchone()
        if(len(result) == 0):
            cursor.execute("INSERT INTO joins VALUES(" + str(ctx.guild.id + ",NULL,NULL)"))
            mydb.commit()
    @commands.command(help="Set welcomes channel")
    async def welcomes(self, ctx, channel=None):
        if ctx.author.guild_permissions.manage_messages:
            pass
        else:
            return await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have Perms To Execute This Command!')
        if channel == None:
            embed = discord.Embed(title="Error!", description="Usage: `<prefix>welcomes #channel`", color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)
        if channel.startswith('<#'):
            cursor = mydb.cursor()
            channels = channel.strip('<#').strip('>')
            cursor.execute("UPDATE joins SET channel = " + str(channels) + " WHERE server_id = " + str(ctx.guild.id))
            mydb.commit()
            embed = discord.Embed(title="Sucsess!", color=ctx.author.color)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
            embed.add_field(name="I have set the welcomes channel to:", value=f"<#{channels}>")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error!", description'Usage: `<prefix>welcomes #channel`', color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
            return await ctx.send(embed=embed)
    @commands.command(help='Sets join role')
    async def joinrole(self, ctx, role=None):
        if ctx.author.guild_permissions.manage_messages:
            pass
        else:
            return await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} You Do Not Have Perms To Execute This Command!')
        if role == None:
            embed = discord.Embed(title="Error!", description="Usage: `<prefix>welcomes #channel`", color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)
        if role.startswith('<@&'):
            pass
        else:
            embed = discord.Embed(title="Error!", description="Usage: `<prefix>joinrole @role`", color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)
        cursor = mydb.cursor()
        newrole = role.strip('<@&').strip('>')
        cursor.execute("UPDATE joins SET role = " + str(newrole) + " WHERE server_id = " + str(ctx.guild.id))
        mydb.commit()
        embed = discord.Embed(title="Sucsess!", color=ctx.author.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
        embed.add_field(name="I have set the join auto-role to:", value=f"<@&{newrole}>")
        await ctx.send(embed=embed)
    @bot.Cog.listener()
    async def on_member_join(self, member):
        cursor = mydb.cursor()
        cursor.execute("SELECT channel FROM joins WHERE server_id = " + str(member.guild.id))
        result = cursor.fetchall()
        newresult = result[0][0]
        try:
            intsCover(newresult)
            if intsCover <= 15:
                pass
            channels = self.bot.get_channel(intsCover)
            async with aiohttp.ClientSession().get(f"https://welcome-imgs.some-random-api.ml/img/4/sunset?type=join&username={member.name}&discriminator={member.discriminator}&guildName={member.guild.name}&memberCount={member.guild.member_count}&avatar={member.avatar_url_as(format='png')}&textcolor=blue") as r:
                if r.status != 200:
                    return
                else:
                    data = io.BytesIO(await r.read())
                    embed = discord.Embed(title="Welcome to " + str(member.guild.name))
                    embed.set_image(file=discord.File(data, 'sunset.png'))
                    embed.set_footer(text="World | Joins", icon_url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
                    await channels.send(embed=embed)
        except:
            pass
        cursor.execute("SELECT role FROM joins WHERE server_id = " + str(member.guild.id))
        res = cursor.fetchall()
        newres = res[0][0]
        try:
        intsCoverr = int(newres)
        if intsCoverr <= 15:
            pass
        role = member.guild.get_role(intsCoverr)
        await member.add_roles(role)
def setup(bot):
    bot.add_cog(JoinCog(bot))
