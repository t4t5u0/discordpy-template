from typing import Any, Optional

import discord
from discord.ext.commands import Bot
from discord import app_commands

# from discord.ext.commands.bot import BotT, PrefixType
from discord.ext.commands.help import HelpCommand

from help.help_command import JapaneseHelpCommand
from libs.get_token import get_token

# MY_GUILD = discord.Object(id=0) # own server id


class MyBot(Bot):
    def __init__(
        self,
        command_prefix: Any,  # acctuary PrefixType[BotT],
        help_command: Optional[HelpCommand] = ...,
        **options: Any
    ) -> None:
        super().__init__(
            command_prefix=command_prefix, help_command=help_command, **options
        )
        # self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        # ここにCogを追加していく
        await self.load_extension("cog.on_ready")
        await self.load_extension("cog.test_command")
        await self.load_extension("cog.tasks")

        # Slash Command
        # self.tree.copy_global_to(guild=MY_GUILD)
        # await self.tree.sync(guild=MY_GUILD)
        await self.load_extension("cog.app_command_sample")


def main():
    TOKEN = get_token()
    if not TOKEN:
        print("TOKENが設定されていません。プログラムを終了します。")
        exit(1)

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    # プレフィックスを変更
    prefix = "!"
    bot: MyBot = MyBot(
        command_prefix=prefix,
        help_command=JapaneseHelpCommand(prefix=prefix),
        intents=intents,
    )

    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("TOKENが間違っています。プログラムを終了します。")
        exit(1)


if __name__ == "__main__":
    main()
