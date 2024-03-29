import discord
from discord.ext import commands

class StartMessage(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        # Bot起動時にターミナルに通知を出す
        print('-'*20)
        print('ログインしました')
        print('-'*20)
        await self.bot.change_presence(activity=discord.Game(name='!help'))

async def setup(bot: commands.Bot):
    await bot.add_cog(StartMessage(bot))