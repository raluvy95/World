import discord
import asyncio
import time
import requests
from discord import Spotify
from datetime import timedelta
from discord.ext import commands
starttime = time.time()

class InfoCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Show users information.")
    async def userinfo(self, ctx, *, user: discord.Member = None):
      if user is None:
          user = ctx.author
      date_format = "%a, %d %b %Y %I:%M %p"
      em = discord.Embed(description=user.mention)
      em.set_author(name=f"{str(user)}'s Userinfo!", icon_url=user.avatar_url)
      em.color = 0x00FF
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
      em.color = (ctx.author.color)
      await ctx.send(embed=em)
    
    @commands.command(help="Show guilds information.")
    async def serverinfo(self, ctx):
      em = discord.Embed(description=f"Name: {ctx.guild}")
      em.color = (ctx.author.color)
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
      embed = discord.Embed(title=None,colour=ctx.author.color,description="Connected on " + str(len(servers)) + " servers")
      await ctx.send(embed=embed)

    @commands.command(help="Show World's Info.")
    async def botinfo(self, ctx):
      dpyVersion = discord.__version__
      serverCount = len(self.bot.guilds)
      memberCount = len(set(self.bot.get_all_members()))

      embed = discord.Embed(title=f'{self.bot.user.name} - Info', description='World - Discord Bot Made For all', colour=ctx.author.colour, timestamp=ctx.message.created_at)

      embed.add_field(name="Name:", value="World#4520", inline=True)
      embed.add_field(name='Library:', value="Discord.py")
      embed.add_field(name='Library Discord.py Version:', value=dpyVersion)
      embed.add_field(name='Total Servers:', value=serverCount)
      embed.add_field(name='Total Users:', value=memberCount)
      embed.add_field(name='Bot Made By:', value="<@662334026098409480>")

      embed.set_footer(text=f"World - Botinfo | Made By seañ#1718")
      embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

      await ctx.send(embed=embed)



    @commands.command(help="Show World's Info.")
    async def botstats(self, ctx):
      dpyVersion = discord.__version__
      serverCount = len(bot.guilds)
      memberCount = len(set(bot.get_all_members()))

      embed = discord.Embed(title=f'{bot.user.name} - Stats', description='Updated Just Now:', colour=ctx.author.colour, timestamp=ctx.message.created_at)

      embed.add_field(name='Library Discord.py Version:', value=dpyVersion)
      embed.add_field(name='Total Servers:', value=serverCount)
      embed.add_field(name='Total Users:', value=memberCount)
      embed.add_field(name='Bot Made By:', value="<@662334026098409480>")

      embed.set_footer(text=f"World - Botstats | Made By seañ#1718")
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
            	embed = discord.Embed(title=f"Sorry {ctx.author} you're not currenty listening to `Spotify`.")
            	return await ctx.send(embed=embed)


    @commands.command(help="Invite World.")
    async def invite(self, ctx):
        coronastats = ('https://discord.com/api/oauth2/authorize?client_id=700292147311542282&permissions=8&scope=bot')
        em = discord.Embed(title='Click Me To Invite Me :)', url=(coronastats), icon_url='https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png')
        em.set_author(name='World - Invite', url='https://discord.com/api/oauth2/authorize?client_id=700292147311542282&permissions=8&scope=bot' , icon_url='https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png')
        em.description = ('Link Above Directs To My Invite Link!')
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png')
        em.set_image(url="https://cdn.discordapp.com/attachments/717867341333004328/730137118499799232/unknown.png")
        em.set_footer(text='World - Invite')
        em.colour = (0x00FF)
        await ctx.send(embed=em)


    @commands.command(help="Vote for world.")
    async def vote(self, ctx):
        coronastats = ('https://top.gg/bot/700292147311542282')
        em = discord.Embed(title='Click Me To Vote For Me', url=(coronastats), icon_url='https://top.gg/bot/700292147311542282')
        em.set_author(name='World - Vote!', url='https://top.gg/bot/700292147311542282' , icon_url='https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png')
        em.description = ('Link Above Directs To Top.gg')
        em.set_thumbnail(url='https://cdn.discordapp.com/attachments/717029914360020992/730135115673370684/contest1replace.png')
        em.set_image(url="https://top.gg/api/widget/700292147311542282.png?cache=poor")
        em.set_footer(text='World - Top.gg')
        em.colour = (0x00FF)
        await ctx.send(embed=em)


    @commands.command(help="Show Guilds Bans.")
    @commands.has_permissions(ban_members=True)
    async def bans(self, ctx):
        try:
            bans = await ctx.guild.bans()
        except:
            return await ctx.send("You dont have the perms to see bans.")

        em = discord.Embed(title=f"Here Is A List of Banned Members ({len(bans)}):")
        em.description = ", ".join([str(b.user) for b in bans])
        em.color = 0x00FF

        await ctx.send(embed=em)


    @commands.command(help="Corona Virus information")
    async def corona(self, ctx):
        r = requests.get("https://api.covid19api.com/world/total")
        res = r.json()
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
        em.colour = (0xFEF200)
        await ctx.send(embed=em)

    @commands.command(help="Adds emoji")
    async def addemoji(self, ctx, emoji: str, name=None):
        # You can upload emoji, id or url!
        defurl = "https://cdn.discordapp.com/emojis/"
        async def upload(name, id=None, url=defurl):
            async with ClientSession() as s:
                def URL():
                    if not id:
                        return url
                    else:
                        return f"{url}{id}"
                async with s.get(URL()) as r:
                    if r.status != 200:
                        return await ctx.send(f"I can't upload the emoji's url\nStatus: {r.status}")
                    img = await r.read()
                    edit = await ctx.send("Creating...")
                    await ctx.guild.create_custom_emoji(name=name, image=img)
                    await edit.edit(content="Created new emoji!")
        try:
            emoji = int(emoji)
            if not name:
                return await ctx.send("I can't create an emoji without name")
            return await upload(name, emoji)
        except ValueError:
            if emoji.startswith("http://") or emoji.startswith("https://"):
                if not name:
                    return await ctx.send("I can't create an emoji without name")
                return await upload(name, url=emoji)
            emoji = emoji.split(":")
            name = emoji[1]
            id = emoji[2].replace(">", "")
            return await upload(name, id)

    @commands.command(help="Show World's uptime.")
    async def uptime(self, ctx):
        seconds = time.time()-starttime
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        formatted = "%d Days %02d Hours %02d Minutes %02d Seconds" % (d, h, m, s)
        em = discord.Embed()
        em.add_field(name="Here Is My Uptime:", value="`" + formatted + "`", inline=False)
        em.color = ctx.author.color
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(InfoCog(bot))
