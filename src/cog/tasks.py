from typing import Optional
from discord.ext import tasks, commands

class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.index = 0
        self.bot = bot
        self.ctx: Optional[commands.Context] = None
    
    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        # print(self.index)
        await self.ctx.send(f"{self.index}")
        self.index += 1

    @commands.group()
    async def per(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            await ctx.send('invalid command')

    @per.command()
    async def start(self, ctx: commands.Context):
        self.ctx = ctx
        self.printer.start()
        await ctx.send('start periodically task')

    @per.command()
    async def stop(self, ctx: commands.Context):
        self.printer.cancel()
        self.index = 0
        await ctx.send('stop periodically task')


def setup(bot: commands.Bot):
    return bot.add_cog(MyCog(bot))