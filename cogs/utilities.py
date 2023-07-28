import discord
from discord.ext import commands
from decimal import Decimal

class utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def aslashcommand(self, ctx: discord.ApplicationContext):
        await ctx.respond("# what a useful slash command")


def setup(bot):
    bot.add_cog(utilities(bot))
