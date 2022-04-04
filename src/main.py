import discord
from discord.ext.commands import Bot

from libs.get_token import get_token


def main():
    TOKEN = get_token()
    if not TOKEN:
        print("TOKENが設定されていません。プログラムを終了します。")
        exit(1)
    bot: Bot = Bot(command_prefix="!")
    # ここにコグを追加していく
    bot.load_extension("cog.on_ready")
    bot.load_extension("cog.bot")
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("TOKENが間違っています。プログラムを終了します。")
        exit(1)


if __name__ == "__main__":
    main()
