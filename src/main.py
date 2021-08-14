import json
from pathlib import Path

import discord
from discord.ext.commands import Bot

from lib.get_token import get_token


def main():
    TOKEN = get_token()
    if not TOKEN:
        print("TOKENが設定されていません。プログラムを終了します")
        return 
    bot: Bot = Bot(command_prefix="!")
    # ここにコグを追加していく
    bot.load_extension("cog.on_ready")
    bot.load_extension("cog.bot")
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("Login failed")

if __name__ == "__main__":
    main()
