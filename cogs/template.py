import discord
from discord.ext import commands

class template(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def slash_command(self, ctx: discord.ApplicationContext):
        await ctx.respond("# what a useful slash command")


def setup(bot):
    bot.add_cog(template(bot))
