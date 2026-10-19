# 検索公開範囲と測定手順

## 生成方針

- `engine/` と `tools/build.py` を正本とし、トップ、作品年表、会戦ページへ description、canonical、OG を生成する。
- `docs/sitemap.xml` は `docs/` に生成された公開 HTML だけを列挙し、クエリやフラグメントは含めない。
- `docs/robots.txt` は公開 HTML を許可し、生成した sitemap を示す。生成物を手編集しない。

## 比較可能な測定

```sh
python3 tools/build.py all
python3 tools/qa_search_metadata.py
curl -sS -D headers.txt -o index.html https://fiction-war-archive.birdman-studio.com/
curl -sS -D robots-headers.txt -o robots.txt https://fiction-war-archive.birdman-studio.com/robots.txt
curl -sS -D sitemap-headers.txt -o sitemap.xml https://fiction-war-archive.birdman-studio.com/sitemap.xml
```

UTC 日時、実行環境、HTTP status、最終 URL、`content-type`、title、description、canonical、OG、sitemap URL 数を保存する。検索結果を観測するときは検索エンジン名、検索語、UTC 日時、ログイン状態を併記する。順位や AI 検索での引用は変動するため保証値にしない。

## 変更前の観測と既存作業との分担

- 2026-10-19 12:29 UTC、直接 HTTP 取得: `/` は 200。title は存在したが description、canonical、OG は見つからなかった。`/robots.txt` と `/sitemap.xml` は 404。
- 2026-10-19 12:48 UTC、Bing 通常検索（未ログイン相当の HTTP 取得、`site:fiction-war-archive.birdman-studio.com`）: 返却された上位10 organic 結果ブロックに対象ドメインの一致を確認できなかった。これはインデックス未登録の確定判定ではなく、地域・時刻・検索側の応答に依存する観測値。
- draft PR #48 で扱われていた公開用 HTML の更新漏れは、2026-10-19 の `main` に入った PR #49「公開用254戦HTMLの再生成と同期を修復」で解消済み。本変更はその生成同期を前提に、生成元へ検索メタ情報と crawl ファイルを追加する。
- ChatGPT、Gemini、Copilot への質問や外部 AI API 送信は実施していない。
