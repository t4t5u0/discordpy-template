from discord.ext import commands


class TestCog(commands.Cog, name="テスト"):
    """
    Botのメイン部分
    """

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command()
    async def neko(self, ctx: commands.Context):
        """にゃーんと返す"""
        await ctx.send("にゃーん")

    @commands.command()
    async def echo(self, ctx: commands.Context, *, msg: str):
        """文字列を返す"""
        await ctx.send(msg)


def setup(bot: commands.Bot):
    return bot.add_cog(TestCog(bot))
