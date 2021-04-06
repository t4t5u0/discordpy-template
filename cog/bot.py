import discord
from discord import channel
from discord.ext import commands


class BotCog(commands.Cog, name="bot"):
    """
    Botのメイン部分
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def neko(self, ctx: commands.Context):
        await ctx.send("にゃーん")

def setup(bot: commands.Bot):
    return bot.add_cog(BotCog(bot))