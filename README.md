# discordpy-template

## モチベーション

- Poetry と Docker を用いて環境を汚さずに Discord Bot を開発したい
- コマンドベース(Cog)の Discord Bot を手軽に開発したい

## 起動方法

1. リポジトリのコピーを作成．ページ上部の[Use this template](https://github.com/t4t5u0/discordpy-template/generate) をクリック．
1. [Discord Developer Portal](https://discord.com/developers/applications) にアクセスし，Bot を作成，トークンを取得(参照：[Botアカウント作成](https://discordpy.readthedocs.io/ja/latest/discord.html))
1. Botをサーバーに招待する
1. `./config/discord_secret.json` にトークンを書き込む
1. 下記の手順に従って起動

### with docker

```sh
docker compose up
```

OR 

```sh
docker compose up -D
```

### without docker

```sh
poetry install
python ./src/main.py
```

## 開発者向け

### 開発する前にやるとよさそうなこと

#### pre-commit の設定

シークレットをコミットしようとしたら失敗するようにする

```sh
sudo apt install git-secrets
git secrets --add '[A-z0-9_]{24}\.[A-z0-9_]{6}\.[A-z0-9_]{27}\.'
git secrets install
```

記事はこちら
[git-secrets を活用して、Discord Bot のトークンの混入を防ぐ](https://zenn.dev/t4t5u0/articles/c89a32165f52dddae258)

#### git 管理下にあるファイルの更新を無視する

```sh
git update-index --assume-unchanged config/discord_secret.json
```

### コマンドを追加する

`./src/cog` 配下にコマンドを生やしていく方針です．

`main.py` の以下の部分に追加したいファイル名を書き込みましょう．

```py
class MyBot(Bot):
    ...
    async def setup_hook(self) -> None:
        # ここにCogを追加していく
        await self.load_extension("cog.on_ready")
        await self.load_extension("cog.test_command")
```

わからなければ[@i4mwh4ti4m](https://twitter.com/i4mwh4ti4m)に聞いてください

### 公式ドキュメント

- [discord.py へようこそ。](https://discordpy.readthedocs.io/ja/latest/index.html)
