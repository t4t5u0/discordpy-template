from discord.ext import commands


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self, prefix: str = "!"):
        super().__init__()
        self.prefix = prefix
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (
            f"各コマンドの説明: {self.prefix}help <コマンド名>\n"
            f"各カテゴリの説明: {self.prefix}help <カテゴリ名>\n"
        )
