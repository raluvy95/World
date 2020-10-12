import os
import random
import textwrap

from datetime import datetime
from typing import Literal, Union

import motor.motor_asyncio

from discord import Color, Embed, Member
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from dotenv import load_dotenv


class User:
    """Represents a World Economy user."""
    def __init__(
        self,
        id_: int,
        coins: int,
        cookie: int,
        choc: int,
        poop: int,
        apple: int,
        afk: str
    ) -> None:
        """Sets up the class."""
        self._id = id_
        self.coins = coins
        self.cookie = cookie
        self.choc = choc
        self.poop = poop
        self.apple = apple
        self.afk = afk

    def __repr__(self) -> str:
        """Returns the representation of this user."""
        return f"<User _id={self._id} coins={self.coins} cookie={self.cookie} choc={self.choc} poop={self.poop} apple={self.apple} afk={self.afk}>"

    def __str__(self) -> str:
        """Returns the string representation of this user."""
        return self.__repr__()


class Item(type):
    """Base class for a World item."""


class Cookie(metaclass=Item):
    """Represents a World cookie."""

    name = "cookie"
    price = 1


class Choc(metaclass=Item):
    """Represents a World chocolatebar."""

    name = "choc"
    price = 4


class Poop(metaclass=Item):
    """Represents a World poop."""

    name = "poop"
    price = 6


class Apple(metaclass=Item):
    """Represents a World item."""

    name = "apple"
    price = 10


class ItemConverter(commands.Converter):
    """Converts a string into a World item."""
    
    async def convert(self, ctx: commands.Context, argument: str) -> Item:
        """Converts a string into a World item."""
        if argument.lower() in ("cookie", "cookies"):
            return Cookie
        elif argument.lower() in ("chocbar", "choc", "chocbars", "chocs"):
            return Choc
        elif argument.lower() in ("poop", "poops"):
            return Poop
        elif argument.lower() in ("apple", "apples"):
            return Apple
        else:
            raise commands.errors.BadArgument("Invalid item provided.")


class UnsignedIntegerConverter(commands.Converter):
    """Converts a string into an unsigned integer."""

    async def convert(self, ctx: commands.Context, argument: str) -> int:
        """Converts a string into an unsigned integer."""
        try:
            if (number := int(argument)) <= 0:
                raise commands.errors.BadArgument("No signed integers or 0!")
        except ValueError:
            raise commands.errors.BadArgument("This is not a number.")

        return number


class EconomyError(Exception):
    """Base exception for economy-related (the cog) errors."""


class NotEnoughCoins(EconomyError):
    """Exception raised when the user doesn't have enough coins."""


class NotEnoughItems(EconomyError):
    """Exception raised when the user doesn't have enough items to perform the operation."""


class UserNotFound(EconomyError):
    """Exception raised when the user is not found."""


class EconomyCog(commands.Cog):
    """Cog for World's economy system."""

    def __init__(self) -> None:
        """Sets up the cog."""
        self._connect_to_database()

    @commands.command(name="shop", aliases=("items",))
    async def shop(self, ctx: commands.Context) -> None:
        """Returns all items you can buy or sell."""
        shop_embed = Embed(
            title="Shop",
            description=textwrap.dedent("""
                - Cookies
                - Chocbars
                - Poops
                - Apples
            """),
            color=0x2F3136
        )
        await ctx.send(embed=shop_embed)

    @commands.command(name="inventory", aliases=("inv",))
    async def inventory(self, ctx: commands.Context) -> None:
        """Returns the current items from the user inventory."""
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        author = await self._get_user(ctx.author.id)
        inventory_embed = Embed(
            title=f"{ctx.author}'s inventory",
            color=0x2F3136
        )
        inventory_embed.add_field(
            name="Coins",
            value=f":moneybag: {author.coins}"
        )
        inventory_embed.add_field(
            name="Apples",
            value=f":apple: {author.apple}"
        )
        inventory_embed.add_field(
            name="Cookies",
            value=f":cookie: {author.cookie}"
        )
        inventory_embed.add_field(
            name="Chocolate bars",
            value=f":chocolate_bar: {author.choc}"
        )
        inventory_embed.add_field(
            name="Poops",
            value=f":poop: {author.poop}"
        )
        inventory_embed.add_field(
            name="Status",
            value=author.afk
        )
        inventory_embed.set_thumbnail(url=ctx.author.avatar_url)
        await ctx.send(embed=inventory_embed)

    @commands.command(name="buy")
    async def buy(self, ctx: commands.Context, item: ItemConverter, amount: UnsignedIntegerConverter) -> None:
        """
        Buys items.
        
        Items you can buy:
        - `cookie`
        - `chocbar`
        - `poop`
        - `apple`
        """
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        await self._buy(item, amount, user)
        await ctx.send(f"You successfully bought {amount} {item.name}{'s' if amount > 1 else ''}.")

    @buy.error
    async def buy_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when buying something."""
        error = getattr(error, "original", error)
        if isinstance(error, NotEnoughCoins):
            await ctx.send(error)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(error)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"You missed the `item` or `amount` arguments.")

    @commands.command(name="sell")
    @commands.cooldown(1, 60, BucketType.member)
    async def sell(self, ctx: commands.Context, item: ItemConverter, amount: UnsignedIntegerConverter) -> None:
        """
        Sells items.
        
        Items you can sell:
        - `cookie`
        - `chocbar`
        - `poop`
        - `apple`
        """
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        coins_earned = await self._sell(item, amount, user)
        if not coins_earned:
            await ctx.send("Sorry, but your items couldn't be sold because you got robbed. Good luck the next time!")
        else:
            await ctx.send(f"You sold your items successfully! You earned **{coins_earned}** coins.")

    @sell.error
    async def sell_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when buying something."""
        error = getattr(error, "original", error)
        if isinstance(error, NotEnoughItems):
            await ctx.send(error)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(error)
        elif isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f"You're on cooldown. Try again in {error.retry_after:.2f} seconds.")
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"You missed the `item` or `amount` arguments.")

    @commands.command(name="delete")
    async def delete(self, ctx: commands.Context) -> None:
        """Deletes the economy account associated to the user."""
        if not (await self._has_account(ctx.author.id)):
            await ctx.send(
                f"You don't have an account. To create an account, run `w/create`.")
        else:
            await self._database_collection.delete_one({"_id": ctx.author.id})
            await ctx.send("Account deleted successfully.")

    @commands.command(name="create")
    async def create(self, ctx: commands.Context) -> None:
        """Creates an account."""
        if (await self._has_account(ctx.author.id)):
            await ctx.send("You already have an account.")
        else:
            await self._create_account(ctx.author.id)
            await ctx.send("Account created successfully.")

    @commands.command(name="status")
    async def status(self, ctx: commands.Context, status: str) -> None:
        """Sets a custom status for the user."""
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        if len(status) > 80:
            await ctx.send("Your status message is too big. Try to keep it smaller than 80 chars.")
            return

        await self._database_collection.update_one(
            {
                "_id": ctx.author.id
            },
            {
                "$set": {
                    "afk": status
                }
            }
        )
        await ctx.send("Status updated successfully.")

    @status.error
    async def status_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when running the status command."""
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("You missed the `status` argument.")

    @commands.command(name="gamble")
    async def gamble(self, ctx: commands.Context, amount: UnsignedIntegerConverter) -> None:
        """
        Gambles your amount money.
        
        If you win, you get your money back but doubled, Otherwise, you lose it.
        The winning percentage is 5%.
        """
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        if user.coins < amount:
            raise NotEnoughCoins("The amount of money to gamble is larger than your money amount.")

        await self._database_collection.update_one(
            {
                "_id": ctx.author.id
            },
            {
                "$set": {
                    "coins": user.coins - amount
                }
            }
        )

        # Get percentage
        random.seed(datetime.now().timestamp())
        percentage = random.randint(0, 100)
        if percentage <= 95:
            await ctx.send(f"You lost. You lose {amount} coin{'s' if amount > 1 else ''}.")
            return

        await self._database_collection.update_one(
            {
                "_id": ctx.author.id
            },
            {
                "$set": {
                    "coins": user.coins + (amount * 2)
                }
            }
        )
        await ctx.send(f":tada: :tada: YOU WON! You win {amount * 2} coins.")

    @gamble.error
    async def gamble_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when running the gamble command."""
        error = getattr(error, "original", error)
        if isinstance(error, NotEnoughCoins):
            await ctx.send(error)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("You missed the `amount` argument.")

    @commands.command(name="daily")
    @commands.cooldown(1, 86400, BucketType.member)
    async def daily(self, ctx: commands.Context) -> None:
        """Gives to the user a daily account of money."""
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    "coins": user.coins + 200
                }
            }
        )
        await ctx.send("You successfully received your daily amount of 200 coins.")

    @daily.error
    async def daily_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when running the daily command."""
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f"Try again in {error.retry_after / 3600:.2f} hours.")

    @commands.command(name="weekly")
    @commands.cooldown(1, 604800, BucketType.member)
    async def weekly(self, ctx: commands.Context) -> None:
        """Gives to the user a weekly account of money."""
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    "coins": user.coins + 1500
                }
            }
        )
        await ctx.send("You successfully received your weekly amount of 1500 coins.")

    @weekly.error
    async def weekly_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when running the weekly command."""
        if isinstance(error, commands.errors.CommandOnCooldown):
            await ctx.send(f"Try again in {error.retry_after / 86400:.2f} days.")

    @commands.command(name="transfer")
    async def transfer(self, ctx: commands.Context, target: Member, amount: UnsignedIntegerConverter) -> None:
        """
        Transfers an amount of money to the target specified.
        
        The target is a member from your Discord server.
        """
        if not (await self._has_account(ctx.author.id)):
            await ctx.send("You don't have an account, I am creating one just for you real quick...")
            await self._create_account(ctx.author.id)

        user = await self._get_user(ctx.author.id)
        target_user_object = await self._get_user(target.id)

        if amount > user.coins:
            raise NotEnoughCoins("You don't have enough coins to perform this operation.")

        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    "coins": user.coins - amount
                }
            }
        )
        await self._database_collection.update_one(
            {
                "_id": target_user_object._id
            },
            {
                "$set": {
                    "coins": target_user_object.coins + amount
                }
            }
        )
        await ctx.send("Operation succeed.")

    @transfer.error
    async def tranfer_error(self, ctx: commands.Context, error: commands.errors.CommandInvokeError) -> None:
        """Handles errors when running the tranfer command."""
        error = getattr(error, "original", error)
        if isinstance(error, NotEnoughCoins):
            await ctx.send(error)
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("You missed the `target` parameter.")
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send("Member not found, or invalid coin amount.")
        elif isinstance(error, UserNotFound):
            await ctx.send("Your target does not have a World account.")

    def _connect_to_database(self) -> None:
        """
        Connects into the MongoDB database.

        The URL is specified on the `MONGODB_URL` key in the `.env` file
        in the root directory of this folder.

        This doesn't return anything, in fact, this just sets `self._database_collection`.
        """
        load_dotenv()
        self._database_collection = motor.motor_asyncio.AsyncIOMotorClient(
            os.environ["MONGODB_URL"]
        )["Coins"]["UserCoins"]

    async def _get_user(self, user_id: int) -> User:
        """
        Gets a user from the Coins collection.

        Returns a `User` object.
        Raises `UserNotFound` if the user was not found.
        """
        user_data = await self._database_collection.find_one(
            {"_id": user_id}
        )
        if not user_data:
            raise UserNotFound(f"User with ID {user_id} is not found on the Coins collection")

        user_object = User(
            user_id, user_data["coins"], user_data["cookie"], user_data["choc"],
            user_data["poop"], user_data["apple"], user_data["afk"]
        )
        return user_object

    async def _buy(self, item: Item, amount: int, user: User) -> None:
        """
        The core of the `buy` command.
        
        This performs the buy operation. This will check if the user has enough coins,
        substract the coins from the user account, and add the specified item into the
        user inventory.
        """
        if user.coins - (item.price * amount) < 0:
            raise NotEnoughCoins("You don't have enough coins to buy this item.")

        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    "coins": user.coins - (item.price * amount),
                    item.name: getattr(user, item.name) + amount
                }
            }
        )

    async def _sell(self, item: Item, amount: int, user: User) -> Union[Literal[False], int]:
        """
        The core of the `sell` command.

        You have a 75% chance to sell the items successfully, and a 25% chance to loose it.
        Returns False if the user was robbed, or the coins amount (int) if the items were sold
        successfully.
        """
        if getattr(user, item.name) < amount:
            raise NotEnoughItems("You don't have enough items to perform this operation.")

        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    item.name: getattr(user, item.name) - amount
                }
            }
        )

        # Get the chance
        random.seed(datetime.now().timestamp())
        chance = random.randint(0, 100)
        if chance >= 75:
            return False

        coins_earned = (item.price * amount / 100 * 15) + item.price * amount

        await self._database_collection.update_one(
            {
                "_id": user._id
            },
            {
                "$set": {
                    "coins": user.coins + coins_earned
                }
            }
        )

        return coins_earned

    async def _create_account(self, user_id: int) -> None:
        """Creates a record, setting the record's author as user_id."""
        await self._database_collection.insert_one({
            "_id": user_id,
            "coins": 100,
            "cookie": 0,
            "choc": 0,
            "poop": 0,
            "apple": 0,
            "afk": "No status set, run `w/status` to set a status"
        })

    async def _has_account(self, user_id: int) -> None:
        """Returns True if the user_id has an account. Otherwise False."""
        return bool(await self._database_collection.find_one(
            {"_id": user_id}
        ))


def setup(bot: commands.Bot) -> None:
    """Adds the EconomyBot into the bot."""
    bot.add_cog(EconomyCog())