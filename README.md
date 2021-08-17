# discordpy-template

Cogベースで開発する


開発する前にやるとよさそうなこと

pre-commitの設定
シークレットをコミットしようとしたら失敗するようにする
```bash
sudo apt install git-secrets
git secrets --add '[A-z0-9_]{24}\.[A-z0-9_]{6}\.[A-z0-9_]{27}\.'
git secrets install
```

記事はこちら
[git-secrets を活用して、Discord Bot のトークンの混入を防ぐ](https://zenn.dev/t4t5u0/articles/c89a32165f52dddae258)


git管理下にあるファイルの更新を無視する
```bash
git update-index --assume-unchanged config/discord_secret.json
```