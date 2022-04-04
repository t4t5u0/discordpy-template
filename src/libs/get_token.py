import json
from pathlib import Path


def get_token() -> str | None:
    "JSONファイルからトークンを取得する"
    local_path = Path(__file__).resolve().parents[2] / "config" / "discord_secret.json"
    path = Path("/") / "run" / "secrets" / "discord_secret"
    if not path.exists():
        if not local_path.exists():
            print("discord_secret.jsonが存在しません。")
            return None
        else:
            path = local_path
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["TOKEN"]
