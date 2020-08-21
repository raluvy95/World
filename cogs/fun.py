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


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="World is funny.")
    async def joke(self, ctx):
        headers = {"Accept": "application/json"}
        async with aiohttp.ClientSession() as session:
            async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
                r = await req.json()
        await ctx.send(r["joke"])

    @commands.command(help="Make a user wasted.")
    async def wasted(self, ctx, user : discord.Member=None):
        if user == None:
            user = ctx.author
        embed=discord.Embed(title=f"Wasted Machine", color=0xb921e4)
        embed.set_image(url=f'https://some-random-api.ml/canvas/wasted?avatar={user.avatar_url_as(format="png")}')
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)



    @commands.command()
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
        em.colour = (0xadd8e6)
        await ctx.send(embed=em)


    @commands.command(help="Ask fatina a question.")
    async def asktafina(self, ctx, *, desc):
        responses = [
            "Tafina Kills Himself",
            "Tafina Ignores And Works On Mama Ping Command",
            "Tafina Approves",
            "Tafina Doesn't Approve"
        ]
        em = discord.Embed(title="Ask Tafina")
        em.description = (f"{ctx.author.mention} - {random.choice(responses)}")
        em.add_field(name=f"**Question**", value=f'{desc}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/265156286406983680/720797722600407121/Avatar.gif')
        em.colour = (0xadd8e6)
        await ctx.send(embed=em)


    @commands.command(help="Generate some P*rn Hub text.")
    async def phtext(self,ctx,text1,line,text):
        if line == '&':
            embed = discord.Embed(title='P*rn Hub Text', description=f'Requested By {ctx.author.mention}')
            embed.set_image(url=f'https://api.alexflipnote.dev/pornhub?text={text1}{line}text2={text}')
            embed.color = 0xffa31a
            await ctx.send(embed=embed)

    @phtext.error
    async def phtext_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/phtext text & text`")


    @commands.command(help="Show love between users.")
    async def ship(self, ctx, text1: discord.Member, line, text: discord.Member):
        if line == '&':
            embed = discord.Embed(title='Cuties', description=f'Requested By {ctx.author.mention}')
            embed.set_image(url=f'https://api.alexflipnote.dev/ship?user={text1.avatar_url}{line}user2={text.avatar_url}')
            await ctx.send(embed=embed)

    @ship.error
    async def ship_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Sorry {ctx.author.mention} Please Type `w/ship @user & @user`")


    @commands.command(help="Generate supreme text.")
    async def supreme(self, ctx,*,message=''):
        sent = message.lower()
        embed = discord.Embed(title='Supreme', description=f'Requested By {ctx.author.mention}')
        embed.set_image(url=f'https://api.alexflipnote.dev/supreme?text={urllib.parse.quote(sent)}')
        embed.add_field(name='**Supreme Machine!**', value='Supreme Text Was Generated')
        embed.color=0xff0202
        await ctx.send(embed=embed)


    @commands.command(help="Fatina is a qt")
    async def fatina(self, ctx):
        coronastats = ('https://discord.com/oauth2/authorize?client_id=711632711743438888&permissions=0&scope=bot')
        em = discord.Embed(title='Invite Mama Music!', url=(coronastats), icon_url='https://cdn.discordapp.com/attachments/265156286406983680/720627340375359498/Avatar.png')
        em.set_author(name='Fatina', url='https://discord.com/oauth2/authorize?client_id=711632711743438888&permissions=0&scope=bot' , icon_url='https://cdn.discordapp.com/attachments/265156286406983680/720626298040352838/Avatar.gif')
        em.description = ('Fatina, Is a WonderFull Person\n I Really Like Fatina Hes A Talented Guy and i hope he does good in life.\n Fatina Your The Best!!')
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/265156286406983680/720626298040352838/Avatar.gif')
        em.set_footer(text='Made with love by seañ#1718')
        em.colour = (0xFF0000)
        await ctx.send(embed=em)


    @commands.command(help="Show real love between a user.")
    async def Love(self, ctx, *, user: discord.Member):
        responses = [
            "█ - 1% In Love",
            "█ - 2% In Love",
            "█ - 4% In Love",
            "██ - 5% In Love",
            "███ - 6% In Love",
            "████ - 8% In Love",
            "███████ - 25% In Love",
            "████ - 12% In Love",
            "█████ - 15 % In Love",
            "██████ - 23% In Love",
            "████████████ - 46% In Love",
            "█████████████████████ - 72 % In Love",
            "██████████████████████ - 79% In Love",
            "█████████████████ - 69% In Love",
            "███████████████████████████ - 100% In Love",
            "███████████████████████ - 82% In Love",
            "████████████████████████ - 89% In Love",
            "█████████████ - 50% In Love",
        ]
        em = discord.Embed(title=":heart: The Love Machine :heart: ")
        em.description = (f"**{user}** And **{ctx.author.mention}** are {random.choice(responses)}")
        em.add_field(name=f"**Love Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/710141167722824070/717771350449717288/sean.jpg')
        em.colour = (0xFF0000)
        em1 = discord.Embed(title=":heart: The Love Machine :heart: ")
        em1.description = (f"**{user}** And **{ctx.author.mention}** are ███████████████████████████ - 100% In Love")
        em1.add_field(name=f"**Love Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
        em1.set_thumbnail(url='https://cdn.discordapp.com/attachments/710141167722824070/717771350449717288/sean.jpg')
        em1.colour = (0xFF0000)
        if user.id == 662334026098409480:
            await ctx.send(embed=em1)
        else:
            await ctx.send(embed=em)

    @commands.command(name="f", help="Sad times.")
    async def f(self, ctx, *, text: commands.clean_content = None):
        """ Press F to pay respect """
        sean = ['💔', '💝', '💚', '💙', '💜']
        reason = f"for **{text}** " if text else ""
        finchat = discord.Embed(title = f"**{ctx.author.name}** has paid their respect {reason}{random.choice(sean)}", color =ctx.author.color)
        await ctx.send(embed=finchat)

    @commands.command(help="Shows a meme from random subreddits.")
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(rate=4, per=7, type=commands.BucketType.member)
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
        em.color = 0x00FF
        em.set_footer(text=f"👍Ups:{ups} 👎Downs:{downs}")
        await ctx.send(embed=em)

    @meme.error
    async def meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds.")

    @commands.command(aliases=["pepe"], help="Shows users pp size.")
    async def pp(self, ctx, *, user: discord.Member = None):
        if user is None:
            user = ctx.author
        size = random.randint(1, 15)
        dong = ""
        for _i in range(0, size):
            dong += "="
        em = discord.Embed(
            title=f"{user}'s pepe size", description=f"8{dong}D", colour=0x00FF
        )
        await ctx.send(embed=em)

    @commands.command(help="Make a custom embed.")
    async def embed(self, ctx, *, desc):
            colors = [
                0xFF8686,
                0x331A1A,
                0xF3031B,
                0xFEF200,
                0xDCCCCD,
                0x403585,
                0xf82b00,
            ]
            em = discord.Embed()
            em.title =None
            em.description = (f'{desc}')
            em.colour = (random.choice(colors))
            await ctx.send(embed=em)

    @commands.command(help="Steal a users avatar.")
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
    async def tweet(self, ctx, username: str, *, message: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}"
            ) as r:
                res = await r.json()
                em = discord.Embed()
                em.color = 0x00FF
                em.set_image(url=res["message"])
                await ctx.send(embed=em)

    @commands.command(help="Very fancy.")
    async def ascii(self, ctx, *, text):
        r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
        if len('```'+r+'```') > 2000:
            return
        await ctx.send(f"```{r}```")

    @commands.command(help="Secret.")
    async def cum(self, ctx):
        responses = [
            "Where Do You Mant Me To Come?",
            "Come Where, Huh?",
            "Im Already Coming Over Chill",
            "What You Mean Come, Im Already Here",
            "Dummy I Aint Got Legs i Cant Come Over"
        ]
        em = discord.Embed(title="SECRET COMMAND FOUND!!")
        em.description = (f"**{ctx.author.mention}** - {random.choice(responses)}")
        em.add_field(name=f"**Secret Command | Found! **", value=f'Found By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url=ctx.author.avatar_url)
        em.colour = (0x00FF)
        await ctx.send(embed=em)

    @commands.command(help="Is that user gay?.")
    async def gay(self, ctx, *, user: discord.Member):
        randomPercentage = random.randint(1, 100)
        em = discord.Embed(title=":rainbow_flag:Gay Machine | No Mistakes Were Made:rainbow_flag:")
        em.description = (f"**{user}** You Are 0% Gay")
        em.add_field(name=f"**Gay Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
        em.set_thumbnail(url=user.avatar_url)
        em.colour = (0x00FF)
        em1 = discord.Embed(title=":rainbow_flag:Gay Machine | No Mistakes Were Made:rainbow_flag:")
        em1.description = (f"**{user}** is {randomPercentage}% gay")
        em1.add_field(name=f"**Gay Machine**", value=f'Requested By {ctx.author.mention}', inline=False)
        em1.set_thumbnail(url=user.avatar_url)
        em1.colour = (0x00FF)
        if user.id == 662334026098409480:
            await ctx.send(embed=em)
        else:
            await ctx.send(embed=em1)

    @gay.error
    async def gay_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f':regional_indicator_x: Sorry {ctx.author.mention} Please Mention A User')

    @commands.command(aliases=["8ball"], help="Magical answers.")
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

    @commands.command(help="Turn text into emojis!.")
    async def emojify(self, ctx, *, stuff):
    	emj = ("".join([":regional_indicator_"+l+":"  if l in "abcdefghijklmnopqrstuvwyx" else [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"][int(l)] if l.isdigit() else ":question:" if l == "?" else ":exclamation:" if l == "!" else l for l in f"{stuff}"]))
    	embed = discord.Embed(title='Emojify', description=f'Requested By {ctx.author.mention}', color=ctx.author.color)
    	embed.add_field(name='Your Message Was Emojifyed', value=f'{emj}')
    	await ctx.send(embed=embed)

    @commands.command(help="Ask the boss.")
    async def asktrump(self, ctx, *, question):
        r = requests.get(f"https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}")
        r = r.json()
        em = discord.Embed(color=ctx.author.color, title="Ask Mr Presendent?")
        em.description = f"**Question:** {question}\n\n**Trump:** {r['message']}"
        em.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        em.set_footer(text="World - Ask Trump")
        await ctx.send(embed=em)

    @commands.command(help="Sends a random gif.")
    async def gif(self, ctx):
        try:
            em = discord.Embed(color=ctx.author.color, title="Random GIF")
            r = requests.get(f'https://api.giphy.com/v1/gifs/trending?api_key=oh nonno')
            r = r.json()
            em.set_image(url=f"https://media.giphy.com/media/{r['data'][random.randint(0, len(r['data']) - 1)]['id']}/giphy.gif")
            em.set_author(name=f"Requested by: {ctx.author.name}", icon_url=ctx.author.avatar_url)
            em.set_footer(text='World - Random Gif')
            await ctx.send(embed=em)
        except Exception as e:
            em = discord.Embed(color=discord.Color(value=0xf44242), title="An error occurred.")
            em.description = f"ERROR: \n\n```{e}```"
            await ctx.send(embed=em)


    @commands.command(aliases=["russianrulette"], help="Play Russian rulette.")
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
        em.colour = (0x808080)
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(FunCog(bot))
