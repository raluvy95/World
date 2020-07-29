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

mysql_connection = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="join_connector",
    pool_size=2,
    pool_reset_session=True,
    host="not",
    database="your",
    user="buissness",
    passwd="lol"
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
            cursor.execute("INSERT INTO joins VALUES(" + str(ctx.guild.id + ",NULL)"))
            mydb.commit()
    @commands.command(help="Set welcomes channel")
    async def welcomes(self, ctx, channel=None):
        if channel == None:
            embed = discord.Embed(title="Error!", description="Usage: `<prefix>welcomes #channel`", color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.name}', icon_url=ctx.author.avatar_url)
            return await ctx.send(embed=embed)
        cursor = mydb.cursor()
        channels = channel.strip('<#').strip('>')
        cursor.execute("UPDATE joins SET channel = " + str(channels) + " WHERE server_id = " + str(ctx.guild.id))
        mydb.commit()
        embed = discord.Embed(title="Sucsess!", color=ctx.author.color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
        embed.add_field(name="I have set the welcomes channel to:", value=f"<#{channels}>")
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
            embed = discord.Embed(title="Welcome to " + str(member.guild.name))
            embed.set_image(url=f"https://welcome-imgs.some-random-api.ml/img/4/sunset?type=join&username={member.name}&discriminator={member.discriminator}&guildName={member.guild.name}&memberCount={member.guild.member_count}&avatar={member.avatar_url_as(format='png')}&textcolor=blue")
            embed.set_footer(text="World | Joins", icon_url="https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png")
            await channels.send(embed=embed)
def setup(bot):
    bot.add_cog(JoinCog(bot))
