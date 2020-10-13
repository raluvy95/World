import discord
import asyncio
import time
import aiohttp
import datetime
from discord import Spotify
from datetime import timedelta
from discord.ext import commands
starttime = time.time()

world_pfp = ("https://cdn.discordapp.com/attachments/727241613901824563/764885646162395156/world.png")

class InfoCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ui"], help="Show users information.")
    async def userinfo(self, ctx, *, user: discord.Member = None):
      if user is None:
          user = ctx.author
      date_format = "%a, %d %b %Y %I:%M %p"
      em = discord.Embed(description=user.mention)
      em.set_author(name=f"{str(user)}'s Userinfo!", icon_url=user.avatar_url)
      em.color = 0x2F3136
      members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
      em.add_field(name="**Users Guild Info**", value=f"Joined: `{user.joined_at.strftime(date_format)}`\nJoined Server: `Place {str(members.index(user) + 1)}`\nTop Role: `{user.top_role}`\nNickname: `{user.nick}`")
      em.add_field(name="**Normal Info**", value=f"ID: `{str(user.id)}`\nStatus: `{user.status}`\nProfile Gif: `{user.is_avatar_animated()}`\nColor: `{user.color}`\nAvatar: [Click For Avatar]({user.avatar_url})")
      em.add_field(name="**Other Info**", value=f"Is Bot: `{user.bot}`\nBooster Since: `{user.premium_since}`\nActivity: `{user.activity}`\nIs Mobile: `{user.is_on_mobile()}`\nSystem User: `{user.system}`")
      if len(user.roles) > 1:
          role_string = " ".join([r.mention for r in user.roles][1:])
          em.add_field(
              name=" **User Roles** `[{}]`".format(len(user.roles) - 1),
              value=role_string,
              inline=False,
          )
      perm_string = ", ".join(
          [str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]]
      )
      em.add_field(name="**Users permissions**", value=f"```{perm_string}```", inline=False)
      em.set_footer(text=f"World Userinfo | {user}'s Info", icon_url=user.avatar_url)
      return await ctx.send(embed=em)

    @commands.command(help="Show guilds avatar.")
    async def servericon(self, ctx):
      em = discord.Embed(title=ctx.guild.name)
      em.set_image(url=ctx.guild.icon_url)
      em.color = (0x2F3136)
      await ctx.send(embed=em)
    
    @commands.command(help="Show guilds information.")
    async def serverinfo(self, ctx):
      em = discord.Embed(description=f"Name: {ctx.guild}")
      em.color = (0x2F3136)
      em.add_field(name="**Name**", value=f"{ctx.guild}", inline=True)
      em.add_field(name="**Owner**", value=f"{ctx.guild.owner}", inline=True)
      em.add_field(name="**Region**", value=f"{ctx.guild.region}", inline=True)
      em.add_field(name="**Boosts**", value=f"{ctx.guild.premium_subscription_count}", inline=True)
      em.add_field(name="**Boost Tier**", value=f"{ctx.guild.premium_tier}", inline=True)
      em.add_field(name="**Locale**", value=f"{ctx.guild.preferred_locale}", inline=True)
      em.add_field(name="**Members**", value=f"{len(ctx.guild.members)}", inline=True)
      em.add_field(name="**Roles**", value=f"{len(ctx.guild.roles)}", inline=True)
      em.add_field(name="**Channels**", value=f"{len(ctx.guild.channels)}", inline=True)
      em.add_field(name="**Emojis**", value=f"{len(ctx.guild.emojis)}", inline=True)
      em.add_field(name="**2FA**", value=f"{ctx.guild.mfa_level}")
      em.add_field(name="**Emoji limit**", value=f"{int(ctx.guild.emoji_limit)}", inline=True)
      em.add_field(name="**Verify Level**", value=f"{ctx.guild.verification_level}")
      em.add_field(name="**File Size limit**", value=f"{int(ctx.guild.filesize_limit)}", inline=True)
      em.add_field(name="**Birate Limit**", value=f"{int(ctx.guild.bitrate_limit)}", inline=True)
      em.set_thumbnail(url=ctx.guild.icon_url)
      em.set_footer(text=f"World ServerInfo | {ctx.guild}'s Info", icon_url=ctx.guild.icon_url)
      await ctx.send(embed=em)

    @commands.command(help="List of connected servers.")
    async def servers(self, ctx):
      servers = list(self.bot.guilds)
      embed = discord.Embed(title=None,colour=0x2F3136,description="Connected on " + str(len(servers)) + " servers")
      await ctx.send(embed=embed)

    @commands.command(help="Show World's Info.")
    async def botinfo(self, ctx):
      dpyVersion = discord.__version__
      serverCount = len(self.bot.guilds)
      memberCount = len(set(self.bot.get_all_members()))

      embed = discord.Embed(title=f'{self.bot.user.name} - Info', description='World - Discord Bot Made For all', colour=0x2F3136, timestamp=ctx.message.created_at)

      embed.add_field(name="Name:", value="World#4520", inline=True)
      embed.add_field(name='Library:', value="Discord.py")
      embed.add_field(name='Library Discord.py Version:', value=dpyVersion)
      embed.add_field(name='Total Servers:', value=serverCount)
      embed.add_field(name='Total Users:', value=memberCount)
      embed.add_field(name='Bot Made By:', value="<@662334026098409480>")

      embed.set_footer(text=f"World - Botinfo | Made By seaÃ±#1718")
      embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

      await ctx.send(embed=embed)



    @commands.command(help="Show World's Info.")
    async def botstats(self, ctx):
      dpyVersion = discord.__version__
      serverCount = len(bot.guilds)
      memberCount = len(set(bot.get_all_members()))

      embed = discord.Embed(title=f'{bot.user.name} - Stats', description='Updated Just Now:', colour=0x2F3136, timestamp=ctx.message.created_at)

      embed.add_field(name='Library Discord.py Version:', value=dpyVersion)
      embed.add_field(name='Total Servers:', value=serverCount)
      embed.add_field(name='Total Users:', value=memberCount)
      embed.add_field(name='Bot Made By:', value="<@662334026098409480>")

      embed.set_footer(text=f"World - Botstats | Made By seaÃ±#1718")
      embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

      await ctx.send(embed=embed)


    @commands.command(help="Show users spotify info.")
    async def spotify(self, ctx, user: discord.Member=None):
        user = user or ctx.author
        for activity in user.activities:
            if isinstance(activity, discord.Spotify):
                embed1 = discord.Embed(title=f"World - Spotify")
                embed1.set_author(name=f"Spotify Info For {user}", icon_url=user.avatar_url)
                embed1.add_field(name=f"**Song:**", value=f"{str(activity.title)}", inline=True)
                embed1.add_field(name=f"**Artist:**", value=f"{str(activity.artist)}", inline=True)
                embed1.add_field(name=f"**Album:**", value=f"{str(activity.album)}", inline=True)
                embed1.add_field(name=f"**ID:**", value=f"{str(activity.track_id)}", inline=True)
                m1, s1 = divmod(int(activity.duration.seconds), 60)
                song_length = f'{m1}:{s1}'
                embed1.add_field(name="**Duration**", value=song_length, inline=True)
                embed1.add_field(name=f"**Song Link:**", value=f"[{activity.title}](https://open.spotify.com/track/{activity.track_id})", inline=True)
                embed1.set_thumbnail(url=f"{activity.album_cover_url}")
                embed1.set_footer(text=f"All Artists: {activity.artists}", icon_url=activity.album_cover_url)
                embed1.colour = (activity.color)
                await ctx.send(embed=embed1)
            else:
              embed = discord.Embed(title=f"Sorry {ctx.author} your not currenty listening to `Spotify`.")
              return await ctx.send(embed=embed)

    @commands.command(help="Invite World.")
    async def invite(self, ctx):
        coronastats = ('https://discord.com/api/oauth2/authorize?client_id=700292147311542282&permissions=8&scope=bot')
        em = discord.Embed(title='Click Me To Invite Me :)', url=(coronastats), icon_url=world_pfp)
        em.set_author(name='World - Invite', url='https://discord.com/api/oauth2/authorize?client_id=700292147311542282&permissions=8&scope=bot' , icon_url=world_pfp)
        em.description = ('Link Above Directs To My Invite Link!')
        em.set_thumbnail(url=worldpfp)
        em.set_image(url="https://cdn.discordapp.com/attachments/717867341333004328/730137118499799232/unknown.png")
        em.set_footer(text='World - Invite')
        em.colour = (0x2F3136)
        await ctx.send(embed=em)


    @commands.command(help="Vote for world.")
    async def vote(self, ctx):
        bot_link = ('https://top.gg/bot/700292147311542282/vote')
        em = discord.Embed(title='Click to vote', url=(bot_link), icon_url='https://top.gg/bot/700292147311542282')
        em.set_author(name='World - Vote!', url='https://top.gg/bot/700292147311542282' , icon_url=world_pfp)
        em.description = ('Click the link above to vote.')
        em.colour = (0x2F3136)
        em.set_image(url=f"https://cdn.discordapp.com/attachments/715214583865802844/764573991565656094/example.png")
        em.set_thumbnail(url=world_pfp)
        await ctx.send(embed=em)
       
    @commands.command()
    async def translate(self, ctx, *, translation):
        try:
            translator = Translator()
            result = translator.translate(translation)
            embed = discord.Embed(title=f"Translator", description=f"`{result.origin}`", color=0x2F3136)
            embed.add_field(name=f"Translation", value=f"`{result.text}`", inline=False)
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(title=f"Error: `{e}`")
            await ctx.send(embed=embed)

    @commands.command(help="Show Guilds Bans.")
    @commands.has_permissions(ban_members=True)
    async def bans(self, ctx):
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send("You dont have the perms to see bans.")

        em = discord.Embed(title=f"Here Is A List of Banned Members ({len(bans)}):")
        em.description = ", ".join([str(b.user) for b in bans])
        em.color = 0x2F3136

        await ctx.send(embed=em)


    @commands.command(help="Corona Virus information")
    async def corona(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://api.covid19api.com/world/total") as r:
                res = await r.json()
                totalc = 'TotalConfirmed'
                totald = 'TotalDeaths'
                totalr = 'TotalRecovered'
                em = discord.Embed(title='Updated Just Now:')
                em.set_author(name='Corona stats', url='https://www.worldometers.info/coronavirus/' , icon_url='https://pbs.twimg.com/profile_images/587949417577066499/3uCD4xxY.jpg')
                em.add_field(name='Total Confirmed', value=f'{res[totalc]}', inline=False)
                em.add_field(name='Total Deaths', value=f'{res[totald]}', inline=False)
                em.add_field(name='Total Recovered', value=f'{res[totalr]}', inline=False)
                em.set_thumbnail(url='https://unic.un.org.pl/files/496/koronawirus%20zdjecie.jpg')
                em.set_footer(text='World')
                em.colour = (0x2F3136)
                await ctx.send(embed=em)

    @commands.command(help="Suggest a command or report a bug.")
    async def suggest(self, ctx, *, message):
      suggestion_user = ctx.author
      embed = discord.Embed(title="New suggestion", description=f"Suggestion: `{message}`\nSuggestor: `{suggestion_user}`\nSuggestor ID: `{suggestion_user.id}`", timestamp=datetime.datetime.utcnow(), color=0xb0b9ff)
      embed.set_footer(text='If abused, the bot logs the user id and the owner will blacklist you from using world.')
      embed1 = discord.Embed(title="Done!", description=f"{ctx.author.mention} i have told my developers the following report/suggestion:\n`{message}`", color=0x2F3136)
      embed.set_footer(text=f'World - Suggest')
      await ctx.send(embed=embed1)
      channel = self.bot.get_channel(763110868791459860)
      await channel.send(embed=embed)

    @commands.command(help="Show World's uptime.")
    async def uptime(self, ctx):
        seconds = time.time()-starttime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        formatted = "%d Days %02d Hours %02d Minutes %02d Seconds" % (d, h, m, s)
        em = discord.Embed()
        em.add_field(name="Here Is My Uptime:", value="`" + formatted + "`", inline=False)
        em.color = 0x2F3136
        await ctx.send(embed=em)
        
    @commands.command(help="Urban Dictionary")
    @commands.is_nsfw()
    async def urban(self, ctx, *name):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://api.urbandictionary.com/v0/define?term={'%20'.join(name)}") as r:
                if r.status != 200:
                    return await ctx.send("It looks like the API did an oppsie...")
                json = await r.json()
                list1 = json['list']
                if len(list1) < 1:
                    return await ctx.send("No urban word found :(")
                res = list1[0]
                embed = discord.Embed(title=res['word'])
                embed.description = res['definition']
                embed.add_field(name="Example", value=res['example'])
                embed.set_footer(text=f"👍 {res['thumbs_up']} | 👎{res['thumbs_down']}")
                await ctx.send(embed=embed)
     


def setup(bot):
    bot.add_cog(InfoCog(bot))
