import discord
import pymongo
import typing
import io
import datetime
import os
from io import BytesIO
from typing import Optional
from discord import TextChannel
from pymongo import MongoClient
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from dotenv import load_dotenv

load_dotenv()

cluster = MongoClient(os.environ["MONGODB_URL"])


class LoggingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="World - Logging")
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def logging(self, ctx, options, channel: Optional[discord.TextChannel]):

    	if options == "create":
    		try:
    			db = cluster["Logging"]
    			collection = db["Guilds"]
    			post = {
    			"_id": ctx.guild.id,
    			"Bans": 0,
    			"Kicks": 0,
    			"Mutes": 0,
    			"LockedChannel": 0,
    			"UnLockedChannel": 0,
    			"Unmute": 0,
    			"Slowmode": 0,
    			"DeletedMessage": 0,
    			"EditedMessage": 0,
    			"JoinedServer": 0,
    			"LeftServer": 0,
    			"Unbanned": 0,
    			"Poll": 0,
    			"Eval": 0,
    			"Extraslot": 0
    			}
    			collection.insert_one(post)
    			embed1 = discord.Embed(title="Logging Created.")
    			embed1.add_field(
    				name=f"**Success**",
    				value=f"{ctx.author.mention} I Have Succsesfully Set up `{ctx.guild.name}'s` Logging\nTo see logging options: `world logging help`\nTo remove logging: `world logging shutdown`.",
    				inline=True,
    				)
    			await ctx.channel.send(embed=embed1)
    		except pymongo.errors.DuplicateKeyError:
    			embed1 = discord.Embed(
    				title="Error!",
    				description=f"Sorry {ctx.author.mention} your guild is already registered.",
    				)
    			await ctx.send(embed=embed1)

    	if options == "shutdown":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		collection.remove({"_id": ctx.guild.id})
    		embed = discord.Embed(title="Logging Shutdown.", description=f"{ctx.author.mention} I have succsesfully shutdown `{ctx.guild.name}'s` Logging.")
    		await ctx.send(embed=embed)

    	if options == "help":
    		embed = discord.Embed()
    		embed.set_author(name='World - Logging help')
    		embed.add_field(name="Register your guild.", value="w/logging create", inline=True)
    		embed.add_field(name="Remove your guild.", value="w/logging shutdown", inline=True)
    		embed.add_field(name="Set Logging.", value="w/logging <option>", inline=True)
    		embed.set_footer(text="Use \"w/logging options>\" For logging info.")
    		await ctx.send(embed=embed)

    	if options == "options":
    		embed = discord.Embed()
    		embed.set_author(name='World - Logging Options')
    		embed.add_field(name="Set ban log.", value="w/logging bans <channel>", inline=False)
    		embed.add_field(name="Set unban log.", value="w/logging unbans <channel>", inline=False)
    		embed.add_field(name="Set deleted messages log.", value="w/logging deleted <channel>", inline=False)
    		embed.add_field(name="Set all.", value="w/logging all <channel>", inline=False)
    		embed.set_footer(text="More logging coming soon.")
    		await ctx.send(embed=embed)



    	if options == "bans":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		query = {"_id": ctx.guild.id}
    		banlog = collection.find(query)
    		post = {"Bans": channel.id}
    		for result in banlog:
    			if collection.find_one({"_id": ctx.guild.id})["Bans"] == channel.id:
    				embed = discord.Embed(title="Error!", description=f"Sorry {ctx.author.mention} <#{channel.id}> has already been set as your `Ban Log`.")
    				return await ctx.send(embed=embed)
    			ban = result["Bans"]
    			banresult = int(channel.id)
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"Bans": banresult}})
    			embed = discord.Embed(title="Logging - set", description=f"{ctx.author.mention} I have succsesfully updated your `Ban Log` to the channel: <#{channel.id}>")
    			await ctx.send(embed=embed)

    	if options == "unbans":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		query = {"_id": ctx.guild.id}
    		unbanlog = collection.find(query)
    		post = {"Unbanned": channel.id}
    		for result in unbanlog:
    			if collection.find_one({"_id": ctx.guild.id})["Unbanned"] == channel.id:
    				embed = discord.Embed(title="Error!", description=f"Sorry {ctx.author.mention} <#{channel.id}> has already been set as your `Unbanned Log`.")
    				return await ctx.send(embed=embed)
    			unban = result["Unbanned"]
    			unbanresult = int(channel.id)
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"Unbanned": unbanresult}})
    			embed = discord.Embed(title="Logging - set", description=f"{ctx.author.mention} I have succsesfully updated your `Unban Log` to the channel: <#{channel.id}>")
    			await ctx.send(embed=embed)

    	if options == "deleted":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		query = {"_id": ctx.guild.id}
    		deletedlog = collection.find(query)
    		post = {"DeletedMessage": channel.id}
    		for result in deletedlog:
    			if collection.find_one({"_id": ctx.guild.id})["DeletedMessage"] == channel.id:
    				embed = discord.Embed(title="Error!", description=f"Sorry {ctx.author.mention} <#{channel.id}> has already been set as your `Deleted message Log`.")
    				return await ctx.send(embed=embed)
    			deleted = result["DeletedMessage"]
    			deletedresult = int(channel.id)
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"DeletedMessage": deletedresult}})
    			embed = discord.Embed(title="Logging - set", description=f"{ctx.author.mention} I have succsesfully updated your `Deleted messages Log` to the channel: <#{channel.id}>")
    			await ctx.send(embed=embed)

    	if options == "edited":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		query = {"_id": ctx.guild.id}
    		editedlog = collection.find(query)
    		post = {"EditedMessage": channel.id}
    		for result in editedlog:
    			if collection.find_one({"_id": ctx.guild.id})["EditedMessage"] == channel.id:
    				embed = discord.Embed(title="Error!", description=f"Sorry {ctx.author.mention} <#{channel.id}> has already been set as your `Edited message Log`.")
    				return await ctx.send(embed=embed)
    			edited = result["EditedMessage"]
    			editedresult = int(channel.id)
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"EditedMessage": editedresult}})
    			embed = discord.Embed(title="Logging - set", description=f"{ctx.author.mention} I have succsesfully updated your `Edited messages Log` to the channel: <#{channel.id}>")
    			await ctx.send(embed=embed)


    	if options == "all":
    		db = cluster["Logging"]
    		collection = db["Guilds"]
    		query = {"_id": ctx.guild.id}
    		allc = collection.find(query)
    		post = {"_id": channel.id}
    		for result in allc:
    			edited = result["EditedMessage"]
    			deleted = result["DeletedMessage"]
    			unban = result["Unbanned"]
    			ban = result["Bans"]
    			allresult = int(channel.id)
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"EditedMessage": allresult}})
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"DeletedMessage": allresult}})
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"Unbanned": allresult}})
    			collection.update_one({"_id": ctx.guild.id}, {"$set": {"Bans": allresult}})
    			embed = discord.Embed(title="Logging - set", description=f"{ctx.author.mention} I have succsesfully updated all your `Logs` to the channel: <#{channel.id}>")
    			await ctx.send(embed=embed)


    @logging.error
    async def logging_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds.\nReason: `Could abuse database system.`"
            )

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
    	db = cluster["Logging"]
    	collection = db["Guilds"]
    	query = {"_id": guild.id}
    	memberban = collection.find(query)
    	post = {"Bans": 0}
    	for result in memberban:
    		ban = result["Bans"]
    		if collection.find_one({"_id": guild.id})["Bans"] == 0:
    			return
    		else:
    			ban1 = await guild.fetch_ban(user)
    			reason = ban1.reason
    			embed = discord.Embed(title="Ban Log", description=f"A user from this guild has been banned.\nName: `{user.name}`\nID: `{user.id}`\nReason: `{reason}`", timestamp=datetime.datetime.utcnow())
    			channel = self.bot.get_channel(ban)
    			await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
    	db = cluster["Logging"]
    	collection = db["Guilds"]
    	query = {"_id": guild.id}
    	memberunban = collection.find(query)
    	post = {"Unbanned": 0}
    	for result in memberunban:
    		unban = result["Unbanned"]
    		if collection.find_one({"_id": guild.id})["Unbanned"] == 0:
    			return
    		else:
    			embed = discord.Embed(title="Unban Log", description=f"A user from this guild has been unbanned.\nName: `{user.name}`\nID: `{user.id}`", timestamp=datetime.datetime.utcnow())
    			channel = self.bot.get_channel(unban)
    			await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
    	db = cluster["Logging"]
    	collection = db["Guilds"]
    	query = {"_id": message.guild.id}
    	messagedelete = collection.find(query)
    	post = {"DeletedMessage": 0}
    	for result in messagedelete:
    		deletedm = result["DeletedMessage"]
    		if collection.find_one({"_id": message.guild.id})["DeletedMessage"] == 0:
    			return
    		else:
    			embed = discord.Embed(title="Deleted message Log", description=f"A message was just deleted.\nContent: `{message.content}`\nUser: `{message.author}`\nChannel: `{message.channel}`", timestamp=datetime.datetime.utcnow())
    			channel = self.bot.get_channel(deletedm)
    			await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        db = cluster["Logging"]
        collection = db["Guilds"]
        query = {"_id": after.guild.id}
        editmessage = collection.find(query)
        post = {"EditedMessage": 0}
        for result in editmessage:
            editedm = result["EditedMessage"]
            if collection.find_one({"_id": after.guild.id})["EditedMessage"] == 0:
                return
            else:
                if before.content == after.content:
                    return
                beforec = (before.content)
                afterc = (after.content)
                for attachment in after.attachments:
                	return
                embed = discord.Embed(title="Edited message Log", description=f"A message was just edited.\nUser: `{after.author}`\nChannel: `{after.channel}`", timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Before content:", value=beforec)
                embed.add_field(name="After content:", value=afterc)
                channel = self.bot.get_channel(editedm)
                await channel.send(embed=embed)


    @logging.error
    async def logging_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
        	await ctx.send(f"Sorry {ctx.author.mention} - {error}")
        else:
        	await ctx.send(f"Sorry {ctx.author.mention} - {error}")



def setup(bot):
    bot.add_cog(LoggingCog(bot))
