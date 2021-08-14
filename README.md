# discordpy-template




開発する前にやるとよさそうなこと

pre-commitの設定
シークレットをコミットしようとしたら失敗するようにする
```bash
sudo apt install git-secrets
git secrets --add '[a-zA-Z0-9.]{60}' 
git secrets install
```


git管理下にあるファイルの更新を無視する
```bash
git update-index --assume-unchanged config/discord_secret.json
```