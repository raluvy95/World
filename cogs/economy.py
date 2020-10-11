import asyncio
import discord
import pymongo
import random
import os
from pymongo import MongoClient
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


cluster = MongoClient(os.environ["MONGODB_URL"])



class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Register in Worlds database.")
    async def create(self, ctx):
        try:
            db = cluster["Coins"]
            collection = db["Coins"]
            post = {
                "_id": ctx.author.id,
                "coins": 0,
                "cookie": 0,
                "apple": 0,
                "choc": 0,
                "poop": 0,
                "afk": "No Status Set",
            }
            collection.insert_one(post)
            embed1 = discord.Embed(title="Register!")
            embed1.add_field(
                name=f"**Success**",
                value=f"{ctx.author.mention} I Have Succsesfully Registered You!",
                inline=True,
                color=0x2F3136
            )
            await ctx.channel.send(embed=embed1)
        except pymongo.errors.DuplicateKeyError:
            embed1 = discord.Embed(
                title="Error!",
                description=f"Sorry {ctx.author.mention} your already registered!",
                color=0x2F3136
            )
            await ctx.send(embed=embed1)
            return

    @commands.command(help="Buy a item from the shop.")
    @commands.cooldown(rate=8, per=15, type=commands.BucketType.member)
    async def buy(self, ctx, product, amount: int):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            userbal = result["coins"]
        if amount < 0:
            return await ctx.send("No abusing the system!")

        if product == "cookie":
            if collection.find_one({"_id": ctx.author.id})["coins"] < amount:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `Cookies`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)
        
        if product == "apple":
            if collection.find_one({"_id": ctx.author.id})["coins"] < amount *10:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `Apples`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "chocbar":
            if collection.find_one({"_id": ctx.author.id})["coins"] < amount *4:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `Chocolate bars`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "poop":
            if collection.find_one({"_id": ctx.author.id})["coins"] < amount *6:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `Poops`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "cookie":
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "cookie": 10}
            for result in user:
                coins = result["cookie"]
                coins1 = result["coins"]
                coins = coins + int(amount)
                coins1 = coins1 - int(amount)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"cookie": coins}}
                )
                embed1 = discord.Embed(title="Cookie Shop!", color=0x2F3136)
                embed1.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You Bought `{amount}` Cookies For {amount} Coins, You Now Have {coins1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "apple":
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "apple": 10}
            for result in user:
                coins = result["apple"]
                coins1 = result["coins"]
                coins = coins + int(amount)
                coins1 = coins1 - int(amount * 10)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"apple": coins}}
                )
                embed2 = discord.Embed(title="Apple Shop!", color=0x2F3136)
                embed2.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You Bought `{amount}` Apples For {int(amount*10)} Coins, You Now Have {coins1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed2)
        if product == "chocbar":
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "choc": 10}
            for result in user:
                coins = result["choc"]
                coins1 = result["coins"]
                coins = coins + int(amount)
                coins1 = coins1 - int(amount * 3)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                collection.update_one({"_id": ctx.author.id}, {"$set": {"choc": coins}})
                embed3 = discord.Embed(title="Chocolate Shop!", color=0x2F3136)
                embed3.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You Bought `{amount}` Chocolate Bars For {int(amount*3)} Coins, You Now Have {coins1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed3)
        if product == "poop":
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "poop": 10}
            for result in user:
                coins = result["poop"]
                coins1 = result["coins"]
                coins = coins + int(amount)
                coins1 = coins1 - int(amount * 5)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                collection.update_one({"_id": ctx.author.id}, {"$set": {"poop": coins}})
                embed3 = discord.Embed(title="Poop Shop!", color=0x2F3136)
                embed3.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You Bought `{amount}` Poops For {int(amount*5)} Coins, You Now Have {coins1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed3)

    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Sorry {ctx.author.mention} Please Type `w/buy [product] [amount]`"
            )

    @commands.command(help="Eat a item from your inventory.")
    @commands.cooldown(rate=8, per=15, type=commands.BucketType.member)
    async def eat(self, ctx, product, amount: int):
        db = cluster["Coins"]
        collection = db["Coins"]
        if amount < 0:
            await ctx.send(f"Sorry {ctx.author.mention} you cannot eat negative.")
            return

        if product == "chocbar":
        	if collection.find_one({"_id": ctx.author.id})["choc"] < amount:
        		embed = discord.Embed(title="Not enough chocbars", description=f"Sorry {ctx.author.mention} You dont have enough chocolate bars in your inventory. You can buy more with the command `w/buy chocbar <amount>`", color=0x2F3136)
        		return await ctx.send(embed=embed)

        if product == "apple":
        	if collection.find_one({"_id": ctx.author.id})["apple"] < amount:
        		embed = discord.Embed(title="Not enough apples", description=f"Sorry {ctx.author.mention} You dont have enough apples in your inventory. You can buy more with the command `w/buy apple <amount>`", color=0x2F3136)
        		return await ctx.send(embed=embed)

        if product == "cookie":
        	if collection.find_one({"_id": ctx.author.id})["cookie"] < amount:
        		embed = discord.Embed(title="Not enough cookies", description=f"Sorry {ctx.author.mention} You dont have enough cookies in your inventory. You can buy more with the command `w/buy cookie <amount>`", color=0x2F3136)
        		return await ctx.send(embed=embed)

        if product == "poop":
        	if collection.find_one({"_id": ctx.author.id})["poop"] < amount:
        		embed = discord.Embed(title="Not enough poops", description=f"Sorry {ctx.author.mention} You dont have enough poops in your inventory. You can buy more with the command `w/buy poop <amount>`", color=0x2F3136)
        		return await ctx.send(embed=embed)
        if product == "chocbar":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "choc": 1}
            for result in user:
                coins = result["choc"]
                coins = coins - int(amount)
                collection.update_one({"_id": ctx.author.id}, {"$set": {"choc": coins}})
                embed1 = discord.Embed(title="Hmm Yummy Chocolate!", color=0x2F3136)
                embed1.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You ate `{amount}` Chocolate Bars! You Now Have {coins} Chocolate Bars!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "apple":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "apple": 1}
            for result in user:
                coins = result["apple"]
                coins = coins - int(amount)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"apple": coins}}
                )
                embed1 = discord.Embed(title="Healthy Apples!", color=0x2F3136)
                embed1.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You ate `{amount}` Apples! You Now Have {coins} Apples!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "cookie":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "cookie": 1}
            for result in user:
                coins = result["cookie"]
                coins = coins - int(amount)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"cookie": coins}}
                )
                embed1 = discord.Embed(title="Cookies From Granny!", color=0x2F3136)
                embed1.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You ate `{amount}` Cookies! You Now Have {coins} Cookies",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "poop":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "poop": 1}
            for result in user:
                coins = result["poop"]
                coins = coins - int(amount)
                collection.update_one({"_id": ctx.author.id}, {"$set": {"poop": coins}})
                embed1 = discord.Embed(title="Poop Eater!", color=0x2F3136)
                embed1.add_field(
                    name=f"**Success**",
                    value=f"{ctx.author.mention} You ate `{amount}` Poops! You Now Have {coins} Poops",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        
        
    @commands.command(help="Sell a item from your inventory.")
    @commands.cooldown(rate=6, per=15, type=commands.BucketType.member)
    async def sell(self, ctx, product, amount: int):
        db = cluster["Coins"]
        collection = db["Coins"]
        if amount < 0:
            await ctx.send(f"Sorry {ctx.author.mention} you cannot sell negative.")
            return
        
        if product == "chocbar":
            if collection.find_one({"_id": ctx.author.id})["choc"] < amount:
                embed = discord.Embed(title="Not enough chocbars", description=f"Sorry {ctx.author.mention} You dont have enough `Chocolate bars` in your inventory. You can buy more with the command `w/buy {product} <amount>`", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "apple":
            if collection.find_one({"_id": ctx.author.id})["apple"] < amount:
                embed = discord.Embed(title="Not enough chocbars", description=f"Sorry {ctx.author.mention} You dont have enough `Apples` in your inventory. You can buy more with the command `w/buy {product} <amount>`", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "poop":
            if collection.find_one({"_id": ctx.author.id})["poop"] < amount:
                embed = discord.Embed(title="Not enough chocbars", description=f"Sorry {ctx.author.mention} You dont have enough `Poops` in your inventory. You can buy more with the command `w/buy {product} <amount>`", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "cookie":
            if collection.find_one({"_id": ctx.author.id})["cookie"] < amount:
                embed = discord.Embed(title="Not enough chocbars", description=f"Sorry {ctx.author.mention} You dont have enough `Cookies` in your inventory. You can buy more with the command `w/buy {product} <amount>`", color=0x2F3136)
                return await ctx.send(embed=embed)



        if product == "chocbar":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "choc": 1}
            for result in user:
                coins = result["choc"]
                mon = result["coins"]
                coins = coins - int(amount)
                mon1 = mon + int(amount * 3)
                collection.update_one({"_id": ctx.author.id}, {"$set": {"choc": coins}})
                collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": mon1}})
                embed1 = discord.Embed(title="MarketPlace!", color=0x2F3136)
                embed1.add_field(
                    name=f"**SOLD!**",
                    value=f"{ctx.author.mention} You Sold `{amount}` Chocolate Bars! For {int(amount*3)} Coins, You Now Have {mon1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "apple":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "apple": 1}
            for result in user:
                coins = result["apple"]
                mon = result["coins"]
                coins = coins - int(amount)
                mon1 = mon + int(amount * 9)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"apple": coins}}
                )
                collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": mon1}})
                embed1 = discord.Embed(title="MarketPlace!", color=0x2F3136)
                embed1.add_field(
                    name=f"**SOLD!**",
                    value=f"{ctx.author.mention} You Sold `{amount}` Apples! For {int(amount*9)} Coins, You Now Have {mon1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "poop":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "poop": 1}
            for result in user:
                coins = result["poop"]
                mon = result["coins"]
                coins = coins - int(amount)
                mon1 = mon + int(amount * 5)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"poops": coins}}
                )
                collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": mon1}})
                embed1 = discord.Embed(title="MarketPlace!", color=0x2F3136)
                embed1.add_field(
                    name=f"**SOLD**",
                    value=f"{ctx.author.mention} You Sold `{amount}` Poops! For {int(amount*5)} Coins, You Now Have {mon1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
        if product == "cookie":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "cookie": 1}
            for result in user:
                coins = result["cookie"]
                mon = result["coins"]
                coins = coins - int(amount)
                mon1 = mon + int(amount * 1)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"cookie": coins}}
                )
                collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": mon1}})
                embed1 = discord.Embed(title="MarketPlace!", color=0x2F3136)
                embed1.add_field(
                    name=f"**SOLD**",
                    value=f"{ctx.author.mention} You Sold `{amount}` Cookies! For {int(amount*1)} Coins, You Now Have {mon1} Coins!",
                    inline=True,
                )
                await ctx.send(embed=embed1)
                
    @commands.command(aliases=["ff"], help="Eat some nice fast food.")
    @commands.cooldown(rate=8, per=15, type=commands.BucketType.member)
    async def fastfood(self, ctx, product):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            userbal = result["coins"]

        if product == "mcworlds":
            if collection.find_one({"_id": ctx.author.id})["coins"] < 12:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `McWorlds`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)

        if product == "worldhut":
            if collection.find_one({"_id": ctx.author.id})["coins"] < 20:
                embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to buy `World Hut`.\nCurrent balance: `{userbal}` Coins.", color=0x2F3136)
                return await ctx.send(embed=embed)
        
        if product == "mcworlds":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "coins": 0}
            for result in user:
                user_coins = result["coins"]
                cost_of_mcworlds = user_coins - int(12)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": cost_of_mcworlds}}
                )
                burgers = ["Hamburger",
                "Cheeseburger",
                "Triple Cheeseburger",
                "Mayo Chicken",
                ]
                others = ["20 McNuggets",
                "McWorlds Fries",
                "Quarter Pounder",
                "Chicken Legend",
                "Apple pie",
                "Nacho Cheese Wedges",
                "Hash Brown",
                "Egg McMuffin"
                ]
                drinks = ["Coke",
                "Irn Bru",
                "Fanta",
                "Pepsi",
                "Diet Coke",
                "Pepsi Max",
                "Sprite",
                "Bannana Milkshake",
                "Chocolate Milkshake",
                "Strawberry Milkshake",
                "Vanilla Milkshake",
                ]
                embed1 = discord.Embed(title="Welcome to McWorlds.", color=0x2F3136)
                embed1.add_field(
                    name=f"That cost `12` coins!",
                    value=f"{ctx.author.mention} You have just had the following:\nBurger: `{random.choice(burgers)}`\nDrink: `{random.choice(drinks)}`\nOther: `{random.choice(others)}`",
                    inline=True,
                )
                return await ctx.send(embed=embed1)

        if product == "worldhut":
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "coins": 0}
            for result in user:
                user_coins = result["coins"]
                cost_of_worldhut = user_coins - int(20)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": cost_of_worldhut}}
                )
                burgers = ["Python Burger",
                "Juiced Burger",
                "Musical Burger",
                "Triple Wrldburger",
                "Triple Juiced",
                ]
                others = ["World Fries",
                "Juiced Pounder",
                "Quad Fried Chicken",
                "World pie",
                "Nachos",
                "Chicken Wrld meal",
                ]
                drinks = ["Coke",
                "Irn Bru",
                "Fanta",
                "Pepsi",
                "Diet Coke",
                "Pepsi Max",
                "Sprite",
                "Fizzy Viper",
                "Juiced shoot",
                "World - No Sugar"
                ]
                embed2 = discord.Embed(title="Welcome to WorldHut.", color=0x2F3136)
                embed2.add_field(
                    name=f"That cost `20` coins!",
                    value=f"{ctx.author.mention} You have just had the following:\nBurger: `{random.choice(burgers)}`\nDrink: `{random.choice(drinks)}`\nSide: `{random.choice(others)}`",
                    inline=True,
                )
                return await ctx.send(embed=embed2)

        if product == "options":
        	embed3 = discord.Embed(color=ctx.author.color)
        	embed3.set_author(name='Fast food')
        	embed3.add_field(name="Buy and eat McWorlds", value="w/fastfood [mcworlds]\n`12 Coins`", inline=True)
        	embed3.add_field(name="Buy and eat World Hut", value="w/buy cookie [worldhut]\n`20 Coins`", inline=True)
        	await ctx.send(embed=embed3)

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @buy.error
    async def buy_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @eat.error
    async def eat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Sorry {ctx.author.mention} Please Type `w/sell [product] [amount]`"
            )

    @eat.error
    async def eat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"Sorry {ctx.author.mention} Please Type `w/eat [product] [amount]`"
            )

    @commands.command(help="Shows your inventory.")
    @commands.cooldown(rate=8, per=50, type=commands.BucketType.member)
    async def inv(self, ctx):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            coins = result["cookie"]
            mon = result["coins"]
            apple = result["apple"]
            choc = result["choc"]
            poop = result["poop"]
            coins5 = result["afk"]
            embed1 = discord.Embed(title=f"{ctx.author}'s Inventory!", color=0x2F3136)
            embed1.add_field(
                name=f"**Cookies**", value=f":cookie: {coins} Cookies", inline=True
            )
            embed1.add_field(
                name=f"**Apples**", value=f":apple: {apple} Apples", inline=True
            )
            embed1.add_field(
                name=f"**Chocolate**",
                value=f":chocolate_bar: {choc} Chocolate Bars",
                inline=True,
            )
            embed1.add_field(
                name=f"**Poops**", value=f":poop: {poop} Poops", inline=True
            )
            embed1.add_field(
                name=f"**Coins**", value=f":moneybag: {mon} Coins", inline=True
            )
            embed1.add_field(
                name=f"**You Want Inventory?**", value=f"Type `w/create`", inline=True
            )
            embed1.set_footer(text=f"Status: {coins5}")
            await ctx.send(embed=embed1)

    @inv.error
    async def inv_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @commands.command(help="Get daily coins.")
    @commands.cooldown(rate=1, per=86400, type=commands.BucketType.member)
    async def daily(self, ctx):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        post = {"_id": ctx.author.id, "coins": 0}
        for result in user:
            coins = result["coins"]
            coins = coins + 200
            collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": coins}})
            embed1 = discord.Embed(title="Daily Coins!", color=0x2F3136)
            embed1.add_field(
                name=f"**Success**",
                value=f"{ctx.author.mention} I Have Added `200` Coins To Your Balance",
                inline=True,
            )
            await ctx.send(embed=embed1)
            

    @commands.command(
        aliases=["afk", "ss", "activity", "act"], help="Set a custom status."
    )
    @commands.cooldown(rate=8, per=230, type=commands.BucketType.member)
    async def setstatus(self, ctx, *, afk1):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        post = {"_id": ctx.author.id, "coins": 500}
        for result in user:
            coins = result["afk"]
            coins = coins + afk1
            collection.update_one({"_id": ctx.author.id}, {"$set": {"afk": afk1}})
            embed1 = discord.Embed(title="Status!", color=0x2F3136)
            embed1.add_field(
                name=f"**Success**",
                value=f"{ctx.author.mention} I Have Set Your Status To `{afk1}`",
                inline=True,
            )
            embed1.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=embed1)

    @setstatus.error
    async def setstatus_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @commands.command(help="Shows users status")
    @commands.cooldown(rate=11, per=80, type=commands.BucketType.member)
    async def status(self, ctx, users: discord.Member=None):
    	users = users or ctx.author
    	db = cluster["Coins"]
    	collection = db["Coins"]
    	query = {"_id": users.id}
    	user = collection.find(query)
    	for result in user:
    		status = result["afk"]
    		embed1 = discord.Embed(title="Status", color=0x2F3136)
    		embed1.add_field(
    			name=f"**Success**",
    			value=f"{users.mention}'s Status Is: `{status}`\nTo Set Your Own Status Just Type `setstatus [status]`",
    			inline=True,
    			)
    		embed1.set_thumbnail(url=users.avatar_url)
    		await ctx.send(embed=embed1)

    @status.error
    async def status_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )


    @commands.command(help="Beg for coins.")
    @commands.cooldown(rate=1, per=15, type=commands.BucketType.member)
    async def beg(self, ctx):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        post = {"_id": ctx.author.id, "coins": 25}
        for result in user:
            coins = result["coins"]
            coins = coins + 25
            collection.update_one({"_id": ctx.author.id}, {"$set": {"coins": coins}})
            embed1 = discord.Embed(title="Begger!", color=0x2F3136)
            embed1.add_field(
                name=f"**Success**",
                value=f"{ctx.author.mention} I Have Added `25` Coins To Your Balance Because you have been a good girl/boy",
                inline=True,
            )
            await ctx.send(embed=embed1)

    @commands.command(help="Sorry Buddy only owner.")
    @commands.is_owner()
    @commands.cooldown(rate=1, per=15, type=commands.BucketType.member)
    async def give(self, ctx, users: discord.Member, *, coin):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": users.id}
        user = collection.find(query)
        post = {"_id": users.id, "coins": 5000}
        for result in user:
            coins = result["coins"]
            coins = coins + int(coin)
            collection.update_one({"_id": users.id}, {"$set": {"coins": coins}})
            embed1 = discord.Embed(title="Success!", color=0x2F3136)
            embed1.add_field(
                name=f"**Stop Cheating!**",
                value=f"{ctx.author.mention} I Have Added `{coin}` Coins To {users.mention}'s Balance",
                inline=True,
            )
            await ctx.send(embed=embed1)

    @commands.command(help="Only owner buddy.")
    @commands.is_owner()
    @commands.cooldown(rate=1, per=15, type=commands.BucketType.member)
    async def remove(self, ctx, users: discord.Member, *, coin):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": users.id}
        user = collection.find(query)
        post = {"_id": users.id, "coins": 5000}
        for result in user:
            coins = result["coins"]
            coins = coins - int(coin)
            collection.update_one({"_id": users.id}, {"$set": {"coins": coins}})
            embed1 = discord.Embed(title="Success!", color=0x2F3136)
            embed1.add_field(
                name=f"**Why Would You Do This?!?**",
                value=f"{ctx.author.mention} I Have Removed `{coin}` Coins From {users.mention}'s Balance",
                inline=True,
            )
            await ctx.send(embed=embed1)

    @commands.command(aliases=["balance"], help="Shows users balance.")
    async def bal(self, ctx):
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            coins = result["coins"]
            embed1 = discord.Embed(title="Balance!", color=0x2F3136)
            embed1.add_field(
                name=f"**Success**",
                value=f"{ctx.author.mention} You Have {coins} coins",
                inline=True,
            )
            await ctx.send(embed=embed1)

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )

    @commands.command(aliases=["bet", "slot", "gam"], help="Gamble for some coins.")
    @commands.cooldown(rate=2, per=8, type=commands.BucketType.member)
    async def gamble(self, ctx):
        amount = 15
        db = cluster["Coins"]
        collection = db["Coins"]
        query = {"_id": ctx.author.id}
        user = collection.find(query)
        for result in user:
            userbal = result["coins"]

        if collection.find_one({"_id": ctx.author.id})["coins"] < amount:
            embed = discord.Embed(title="Not enough coins", description=f"Sorry {ctx.author.mention} You dont have enough coins to gamble.\n Current balance: `{userbal}` Coins.", color=0x2F3136)
            return await ctx.send(embed=embed)

        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        if a == b == c:
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "coins": 300}
            for result in user:
                coins = result["coins"]
                coins1 = result["coins"]
                coins = coins + 300
                coins1 = coins - int(15)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins}}
                )
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                await ctx.send(
                    pypyembed=discord.Embed.from_dict(
                        {
                            "title": "Slot machine",
                            "description": f"{slotmachine} All matchings, you won `300` coins!",
                            "color": 0x2F3136
                        }
                    )
                )
        elif (a == b) or (a == c) or (b == c):
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "coins": 150}
            for result in user:
                coins = result["coins"]
                coins = coins + 150
                coins1 = coins - int(15)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins}}
                )
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins1}}
                )
                await ctx.send(
                    embed=discord.Embed.from_dict(
                        {
                            "title": "Slot machine",
                            "description": f"{slotmachine} 2 in a row, you won `150` coins!",
                            "color": 0x2F3136
                        }
                    )
                )
        else:
            db = cluster["Coins"]
            collection = db["Coins"]
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            post = {"_id": ctx.author.id, "coins": 0}
            for result in user:
                coins = result["coins"]
                coins = coins - int(15)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"coins": coins}}
                )
                await ctx.send(
                    embed=discord.Embed.from_dict(
                        {
                            "title": "Slot machine",
                            "description": f"{slotmachine} No match, you lost `15` coins!",
                            "color": 0x2F3136
                        }
                    )
                )

    @gamble.error
    async def gamble_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            a = error.retry_after
            a = round(a)
            await ctx.send(
                f"Sorry {ctx.author.mention} This command in on cooldown, Try again in {a} seconds."
            )
            


def setup(bot):
    bot.add_cog(EconomyCog(bot))
