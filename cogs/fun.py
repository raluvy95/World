import discord
import asyncio
import urllib
import akinator
import random
import requests
import io
import datetime
import aiohttp
import json
from discord.ext import commands, tasks
from urllib.parse import urlparse, quote
from akinator.async_aki import Akinator

akiObj = akinator.async_aki.Akinator()

world_pfp = ("https://cdn.discordapp.com/attachments/727241613901824563/764885646162395156/world.png")

class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gameCache = {}

    @commands.command(help="World is funny.")
    @commands.guild_only()
    async def joke(self, ctx):
        headers = {"Accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                r = await req.json()
        await ctx.send(r["joke"])

    @commands.command(help="Make a user wasted.")
    @commands.guild_only()
    async def wasted(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        embed=discord.Embed(title=f"Wasted Machine", color=0x2F3136)
        embed.set_image(url=f'https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url_as(format="png")}')
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)



    @commands.command()
    @commands.guild_only()
    async def askali(self, ctx, *, desc):
        responses = [
            "Ali A Kills Himself",
            "Ali A Ignores And Hits A 360 Noscope",
            "Ali A Approves",
            "Ali A Dosnt Approve"
        ]
        em = discord.Embed(title="Ask Alister-A ")
        em.description = (f"{ctx.author.mention} - {random.choice(responses)}")
        em.add_field(name=f"**Question**", value=f'{desc}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/710141167722824070/717777626877395004/aaaaa.png')
        em.colour = (0x2F3136)
        await ctx.send(embed=em)

    @askali.error
    async def askali_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/askali <question>`")


    @commands.command(help="Generate some P*rn Hub text.")
    @commands.guild_only()
    async def phtext(self,ctx,text1,line,text):
        if line == '&':
            embed = discord.Embed(title='P*rn Hub Text', description=f'Requested By {ctx.author.mention}', color=0xffa31a)
            embed.set_image(url=f'https://api.alexflipnote.dev/pornhub?text={quote(text1)}{line}text2={quote(text)}')
            await ctx.send(embed=embed)

    @phtext.error
    async def phtext_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/phtext text & text`")


    @commands.command(help="Show love between users.")
    @commands.guild_only()
    async def ship(self, ctx, text1: discord.Member, line, text: discord.Member):
        if line == '&':
            embed = discord.Embed(title='Cuties', description=f'Requested By {ctx.author.mention}', color=0x2F3136)
            embed.set_image(url=f'https://api.alexflipnote.dev/ship?user={text1.avatar_url}{line}user2={text.avatar_url}')
            await ctx.send(embed=embed)

    @ship.error
    async def ship_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/ship <@user> <&> <@user>`")


    @commands.command(help="Generate supreme text.")
    @commands.guild_only()
    async def supreme(self, ctx,*,message=''):
        sent = message.lower()
        embed = discord.Embed(title='Supreme', description=f'Requested By {ctx.author.mention}')
        embed.set_image(url=f'https://api.alexflipnote.dev/supreme?text={urllib.parse.quote(sent)}')
        embed.add_field(name='**Supreme Machine!**', value='Supreme Text Was Generated')
        embed.color=0x2F3136
        await ctx.send(embed=embed)

    @supreme.error
    async def supreme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/supreme <text>`")


    @commands.command(name="f", help="Sad times.")
    @commands.guild_only()
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        sean = ['💔', '💝', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        finchat = discord.Embed(title = f"**{ctx.author.name}** has paid their respect {reason}{random.choice(sean)}", color =0x2F3136)
        await ctx.send(embed=finchat)

    @commands.command(help="Shows a meme from random subreddits.")
    @commands.cooldown(rate=4, per=7, type=commands.BucketType.member)
    @commands.guild_only()
    async def meme(self, ctx):
        r = requests.get("https://memes.blademaker.tv/api?lang=en")
        res = r.json()
        title = res["title"]
        ups = res["ups"]
        downs = res["downs"]
        subr = res["subreddit"]
        em = discord.Embed()
        em.title = f"Title: {title}\nSubreddit: r/{subr}"
        em.set_image(url=res["image"])
        em.color = 0x2F3136
        em.set_footer(text=f"👍Ups:{ups} 👎Downs:{downs}")
        await ctx.send(embed=em)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds.")

    @commands.command(aliases=["pepe"], help="Shows users pp size.")
    @commands.guild_only()
    async def pp(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(
            title=f"{user}'s pepe size", description=f"8{dong}D", colour=0x2F3136
        )
        await ctx.send(embed=em)


    @commands.command(help="Steal a users avatar.")
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member=None):
        format = "gif"
        user = user or ctx.author
        if user.is_avatar_animated() != True:
            format = "png"
        avatar = user.avatar_url_as(format = format if format != "gif" else None)
        async with aiohttp.ClientSession() as session:
            async with session.get(str(avatar)) as resp:
                image = await resp.read()
        with io.BytesIO(image) as file:
            await ctx.send(file = discord.File(file, f"Avatar.{format}"))


    @commands.command(help="Fake tweet text.")
    @commands.guild_only()
    async def tweet(self, ctx, username: str, *, message: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}"
            ) as r:
                res = await r.json()
                em = discord.Embed()
                em.color = 0x2F3136
                em.set_image(url=res["message"])
                await ctx.send(embed=em)

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/tweet <username> <message>`")


    @commands.command(help="Is that user gay?.")
    @commands.guild_only()
    async def gay(self, ctx, *, user: discord.Member=None):
    	user = user or (ctx.author)
    	randomPercentage = random.randint(1, 100)
    	em = discord.Embed(title=":rainbow_flag:Gay Machine | No Mistakes Were Made:rainbow_flag:")
    	em.description = (f"**{user}** You Are 0% Gay")
    	em.add_field(name=f"**Gay Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
    	em.set_thumbnail(url=user.avatar_url)
    	em.colour = (0x2F3136)
    	em1 = discord.Embed(title=":rainbow_flag:Gay Machine | No Mistakes Were Made:rainbow_flag:")
    	em1.description = (f"**{user}** is {randomPercentage}% gay")
    	em1.add_field(name=f"**Gay Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
    	em1.set_thumbnail(url=user.avatar_url)
    	em1.colour = (0x2F3136)
    	if user.id == 662334026098409480:
    		await ctx.send(embed=em)
    	else:
    		await ctx.send(embed=em1)

    @gay.error
    async def gay_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} Please Mention A User')


    @commands.command(aliases=["aki"], help="Can the akinator beat you?")
    @commands.guild_only()
    async def akinator(self, ctx: commands.Context):
        if ctx.channel.id in self.gameCache.keys():
            return await ctx.send(
                "Sorry, {0[user]} is already playing akinator in <#{0[channel]}>, try again when they finish or move to another channel!"
                .format(self.gameCache[ctx.channel.id]))

        gameObj = await akiObj.start_game(child_mode=True)

        currentChannel = ctx.channel

        self.gameCache.update(
            {ctx.channel.id: {
                "user": ctx.author,
                "channel": ctx.channel.id
            }})

        while akiObj.progression <= 80:
            try:
                message1 = await ctx.send(
                    embed=discord.Embed(title="Question", description=gameObj))
                resp = await ctx.bot.wait_for(
                    "message",
                    check=lambda message: message.author == ctx.author and
                    message.channel == ctx.channel and message.guild == ctx.
                    guild and message.content.lower(), timeout=15)
            except asyncio.TimeoutError:
                await ctx.send(embed=discord.Embed(
                    title="Hurry next time!",
                    description=
                    f"{ctx.author.mention} took too long to respond so we ended the game\nCurrent timeout: `15` Seconds.", color=0x2F3136))
                del self.gameCache[ctx.channel.id]
                return await message1.delete(delay=None)
            if resp.content == "b":
                try:
                    gameObj = await akiObj.back()
                except akinator.CantGoBackAnyFurther:
                    await ctx.send(embed=discord.Embed(
                        title="Cannot go back any further :(",
                        description="Continue playing anyway", color=0x2F3136))
            elif resp.content == "q" or resp.content == "quit":
                await ctx.send(embed=discord.Embed(
                    title="Game over",
                    description=
                    "You have left the game.",
                    color=0x2F3136
                    ))
                del self.gameCache[ctx.channel.id]
                break
            else:
                try:
                    gameObj = await akiObj.answer(resp.content)
                except:
                    del self.gameCache[ctx.channel.id]
                    return await ctx.send(embed=discord.Embed(
                        title="Invalid Answer",
                        description=
                        "You typed a invalid answer the only answer options are:\n`y` OR `yes` for yes\n`n` OR `no` for no\n`i` OR `idk` for i dont know\n`p` OR `probably` for probably\n`pn` OR `probably not` for probably not\n`b` for back\n`q` or `quit` for stop the game",
                        color=0x2F3136
                    ))

        await akiObj.win()

        embed = discord.Embed(
            title="I have outsmarted your outsmarting",
            color=0x2F3136
        ).add_field(
            name="I think...",
            value="it is {0.first_guess[name]} {0.first_guess[description]}?\n\nSorry if im wrong, Akinator has tried.".
            format(akiObj)).set_image(
                    url=akiObj.first_guess['absolute_picture_path']
                ).set_footer(text="Thanks to nomadiccode for helping!")

        del self.gameCache[ctx.channel.id]
        await ctx.send(embed=embed)


    @commands.command(aliases=["8ball"], help="Magical answers.")
    @commands.guild_only()
    async def _8ball(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Sean Says Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Dont count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Sean Thinks Its Very doubtful.",
        ]
        em = discord.Embed(title=":8ball: The Almighty 8ball :8ball:")
        em.description = (f"Question = `{question}`\n **Answer**: :8ball: {random.choice(responses)} :8ball:")
        em.add_field(name=f"**8ball - World**", value=f'Requested By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/717038947846455406/717784205249085470/aaaaaaaaaaaaaaaaaaa.png')
        em.colour = (0x000000)
        await ctx.send(embed=em)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/8ball <question>`")

    @commands.command(help="Turn text into emojis!.")
    @commands.guild_only()
    async def emojify(self, ctx, *, stuff):
        emj = ("".join([":regional_indicator_"+l+":"  if l in "abcdefghijklmnopqrstuvwyx" else [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"][int(l)] if l.isdigit() else ":question:" if l == "?" else ":exclamation:" if l == "!" else l for l in f"{stuff}"]))
        embed = discord.Embed(title='Emojify', description=f'Requested By {ctx.author.mention}', color=0x2F3136)
        embed.add_field(name='Your Message Was Emojifyed', value=f'{emj}')
        await ctx.send(embed=embed)

    @emojify.error
    async def emojify_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/emojify <text>`")

    @commands.command(help="Ask the boss.")
    @commands.guild_only()
    async def asktrump(self, ctx, *, question):
        r = requests.get(f"https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}")
        r = r.json()
        em = discord.Embed(color=0x2F3136, title="Ask Mr Presendent?")
        em.description = f"**Question:** {question}\n\n**Trump:** {r['message']}"
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        em.set_footer(text="World - Ask Trump")
        await ctx.send(embed=em)

    @asktrump.error
    async def asktrump_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/asktrump <question>`")

    @commands.command(help="Sends a random gif.")
    @commands.guild_only()
    async def gif(self, ctx):
        try:
            em = discord.Embed(color=0x2F3136, title="Random GIF")
            r = requests.get(f'https://api.giphy.com/v1/gifs/trending?api_key=5LLc05m7k8Ws5wj8F2Xsbe2HHXeFMfCQ')
            r = r.json()
            em.set_image(url=f"https://media.giphy.com/media/{r['data'][random.randint(0, len(r['data']) - 1)]['id']}/giphy.gif")
            em.set_author(name=f"Requested by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
            em.set_footer(text='World - Random Gif')
            await ctx.send(embed=em)
        except Exception as e:
            em = discord.Embed(color=discord.Color(value=0x2F3136), title="An error occurred.")
            em.description = f"ERROR: \n\n```{e}```"
            await ctx.send(embed=em)


    @commands.command(aliases=["russianrulette"], help="Play Russian rulette.")
    @commands.guild_only()
    async def rr(self, ctx):
        responses = [
            "🔫Pow Your Dead!, Try again?",
            "🎉You lived!!!",
            "🔫SPLAT!, You died. Try again?",
            "🎉You were lucky enough to survive!!",
        ]
        em = discord.Embed(title=":gun: Russian roulette :gun:")
        em.description = (f"\n{random.choice(responses)}")
        em.add_field(name=f"**Have Another Go!!**", value=f'Requested By {ctx.author.mention}', inline=False)
        em.colour = (0x2F3136)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(FunCog(bot))
