import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        author = ctx.message
        author
    

        embed = discord.Embed(colour=ctx.author.color)
        embed.set_author(name='World - Help', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
        embed.add_field(
            name="Shows multiple categories.", value="w/categories", inline=True
        )
        embed.add_field(name="Server", value="[Join Support Server](https://discord.gg/zenM2Kd)", inline=True)
        embed.add_field(name="Vote", value="[Vote For World](https://top.gg/bot/700292147311542282/vote)", inline=True)
        embed.add_field(name="> World is a discord bot made for all", value="> World is a discord bot made a while after juice wrld's death(Jarad Higgins).\n> My owner was very upset that juice wrld passed away so he decided to make me.", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def categories(self, ctx):
        author = ctx.message
        author

        embed1 = discord.Embed(colour=ctx.author.color)
        embed1.set_author(name='World - Categories', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
        embed1.add_field(
            name="Show this message", value="w/categories", inline=False
        )
        embed1.add_field(name="Shows Mod Categorie", value="w/mod", inline=False)
        embed1.add_field(name="Shows Fun Categorie", value="w/fun", inline=False)
        embed1.add_field(name="Shows Useful Categorie", value="w/useful", inline=False)
        embed1.add_field(name="Shows Eeconomy Categorie", value="w/economy", inline=False)
        embed1.add_field(name="Shows Other Categorie", value="w/other", inline=False)
        await ctx.send(embed=embed1)


    @commands.command()
    async def other(self, ctx):
        author = ctx.message
        author

        embed = discord.Embed(colour=ctx.author.color)
        embed.set_author(name='World - Other', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
        embed.add_field(
            name="Show this message", value="w/other", inline=True
        )
        embed.add_field(name="Shows info on world", value="w/botinfo", inline=True)
        embed.add_field(name="Invite world", value="w/invite", inline=True)
        embed.add_field(name="Shows servers", value="w/servers", inline=True)
        embed.add_field(name="Vote for world", value="w/vote", inline=True)
        embed.add_field(name="Shows bots latency", value="w/ping", inline=True)
        embed.add_field(name="Shows bots uptime", value="w/uptime", inline=True)
        embed.add_field(name="Shows spotify info", value="w/spotify", inline=True)
        await ctx.send(embed=embed)


    @commands.command()
    async def useful(self, ctx):
        author = ctx.message
        author

        embed = discord.Embed(colour=ctx.author.color)
        embed.set_author(name='World - Useful', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
        embed.add_field(
            name="Show this message", value="w/useful", inline=True
        )
        embed.add_field(name="kick member", value="w/kick [user]", inline=True)
        embed.add_field(
            name="Ban M=member", value="w/ban [user]", inline=True
        )
        embed.add_field(name="Starts a Poll!", value="w/poll [thing]", inline=True)
        embed.add_field(name="Get servericon", value="w/servericon", inline=True)
        embed.add_field(name="First ever message!", value="w/fm", inline=True)
        embed.add_field(name="Deletes messages", value="w/purge [amount]", inline=True)
        embed.add_field(name="Ascii message", value="w/ascii [message]", inline=True)
        embed.add_field(name="Shortens a link", value="w/shorten [link]", inline=True)
        embed.add_field(name="Users status", value="w/status [user]", inline=True)
        embed.add_field(name="Set a status", value="w/setstatus", inline=True)
        embed.add_field(
            name="Screenshot [NSFW]", value="w/screenshot [website]", inline=True
        )
        await ctx.send(embed=embed)


    @commands.command()
    async def mod(self, ctx):
      author = ctx.message
      author

      embed = discord.Embed(colour=ctx.author.color)
      embed.set_author(name='World - Moderation', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
      embed.add_field(
          name="Show this message", value="w/mod", inline=True
      )
      embed.add_field(name="kicks member", value="w/kick [user]", inline=True)
      embed.add_field(name="Bans member", value="w/ban [user]", inline=True)
      embed.add_field(name="Unbans member", value="w/unban [username then #]", inline=True)
      embed.add_field(name="Get users info", value="w/userinfo [user]", inline=True)
      embed.add_field(name="Shows all bans", value="w/bans", inline=True)
      embed.add_field(name="Mutes member", value="w/mute [user]", inline=True)
      embed.add_field(name="Unmute a user", value="w/unmute [user]", inline=True)
      embed.add_field(name="First ever message", value="w/fm", inline=True)
      embed.add_field(name="Channel lockdown", value="w/lock", inline=True)
      embed.add_field(name="Unlock channel", value="w/unlock", inline=True)
      embed.add_field(name="Direct Message a user", value="w/dm [user] [message]", inline=True)
      embed.add_field(
          name="Shows server info", value="w/serverinfo", inline=True
      )
      await ctx.send(embed=embed)


    @commands.command()
    async def fun(self, ctx):
      author = ctx.message
      author

      embed = discord.Embed(colour=ctx.author.color)
      embed.set_author(name='World - Fun', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
      embed.add_field(name="Show this message", value="w/fun", inline=True)
      embed.add_field(name="Are you gay?", value="w/gay [user]", inline=True)
      embed.add_field(name="Play Russian roulette", value="w/rr", inline=True)
      embed.add_field(name="Ask Ali A", value="w/askali [question]", inline=True)
      embed.add_field(
      name="Show user pp size", value="w/pp", inline=True
      )
      embed.add_field(name="Get a random gif!", value="w/gif", inline=True)
      embed.add_field(
          name="Supreme text", value="w/supreme [text]", inline=True
      )
      embed.add_field(name="Ask Mr Trump", value="w/asktrump [question]", inline=True)
      embed.add_field(
          name="Sad Times :(", value="w/f [sad thing]", inline=True
      )
      embed.add_field(name="Magical answers", value="w/8ball [question]", inline=True)
      embed.add_field(
          name="PH text", value="w/phtext [text1] & [text2]", inline=True
      )
      embed.add_field(
      name="Love O nator", value="w/love [user]", inline=True
      )
      await ctx.send(embed=embed)


    @commands.command()
    async def economy(self, ctx):
      author = ctx.message
      author
    

      embed = discord.Embed(colour=ctx.author.color)
      embed.set_author(name='World - Economy', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
      embed.add_field(
          name="Show this message", value="w/economy", inline=True
      )
      embed.add_field(name="Create An Account", value="w/create", inline=True)
      embed.add_field(name="Show balance", value="w/bal", inline=True)
      embed.add_field(name="Beg for Coins", value="w/beg", inline=True)
      embed.add_field(name="Slots [cost 15 coins]", value="w/gamble", inline=True)
      embed.add_field(name="Get daily Coins", value="w/daily", inline=True)
      embed.add_field(name="Get weekly Coins", value="w/weekly", inline=True)
      embed.add_field(name="Show inventory", value="w/inv", inline=True)
      embed.add_field(name="Buy a Product", value="w/buy [product] [amount]", inline=True)
      embed.add_field(name="Eat a Product", value="w/eat [product] [amount]", inline=True)
      embed.add_field(name="Sell a Product", value="w/sell [product] [amount]", inline=True)
      embed.add_field(name="List of items", value="w/shop", inline=True)
      await ctx.send(embed=embed)
    
   
    @commands.command()
    async def shop(self, ctx):
      author = ctx.message
      author
    

      embed = discord.Embed(colour=ctx.author.color)
      embed.set_author(name='World - Economy', icon_url='https://cdn.discordapp.com/icons/708396963229466645/6f90d6bd3209281acaa607d8a2dabed4.webp?size=1024')
      embed.add_field(
          name="Show this message", value="w/shop", inline=True
      )
      embed.add_field(name="Create An Account", value="w/create\n`FREE`", inline=True)
      embed.add_field(name="Buy Some Cookies", value="w/buy cookie [amount]\n`1 Coins`", inline=True)
      embed.add_field(name="Buy Some Chocolate", value="w/buy chocbar [amount]\n`4 Coins`", inline=True)
      embed.add_field(name="Buy Some Poop", value="w/buy poop [amount]\n`6 Coins`", inline=True)
      embed.add_field(name="Buy Some Apples", value="w/buy apple [amount]\n`10 Coins`", inline=True)
      await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, ctx):
    	if ctx.author.bot:
        	return
    	if self.bot.user in ctx.mentions: 
        	embed = discord.Embed(
        	title='', description=f'Here Are My Prefixes: `w/`, `world `' , colour=ctx.author.color)
        	embed.set_footer(text="Type <prefix>help for more info.")
        	await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(HelpCog(bot))
