import json
from pathlib import Path


def get_token() -> str | None:
    "JSONファイルからトークンを取得する"
    path = Path(__file__).resolve().parents[2] / "config" / "discord_secret.json"
    if not path.exists():
        print("discord_secret.jsonが存在しません。")
        return None
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["TOKEN"]
