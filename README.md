# 車両データを活用した子ども向け交通安全マップの提案
## Weｂサーバー
交通安全マップを配信するWebサーバーです。

## 構成
- PythonのWebフレームワークであるFlaskを使います。
- Pythonの実行環境としてuvを使います。localhostで交通安全マップを閲覧するには、お手元のマシンにuvが必要です。

## 手順
1. このリポジトリをcloneしてください。
2. .envファイルを作成して、環境変数を書き込んでください。
3. ```uv sync```コマンドを実行します。
4. ```uv run main.py```コマンドを実行します。
5. localhost:8000にアクセスすると交通安全マップが表示されます。

## 環境変数
| 項目 | 内容 |
| - | - |
| SUPABASE_URL | supabaseのエンドポイントURLを記載します。<br>https://xxx.supabase.co の形式です。 |
| SUPABASE_KEY | supabaseのシークレットキーを記載します。 |