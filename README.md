# fiction-war-archive

物語に描かれた戦いを、作中の暦で並べた年表と、各戦いの3D再現・損害・原作/アニメの該当箇所をまとめるアーカイブ。

収録作品：『銀河英雄伝説』（28会戦）、『機動戦士ガンダム』一年戦争（18の戦い）、『アルスラーン戦記』（15の戦い）、『進撃の巨人』（11の戦い）、『宇宙戦艦ヤマト』1974年版（5）、ガンダム0083〜逆襲のシャア（12）、キングダム（11）、スター・ウォーズ正史（11）、指輪物語（8）、パトレイバー（5事件）、攻殻機動隊S.A.C.（5事件）。

## 構成

```
engine/                 3D再現ページの共通エンジン
  template.html           描画・陣形・戦果パネル・倍速などを含むHTMLテンプレート
  portal.html             年表の共通テンプレート（全作品を1ページに収め、見出しのメニューで切り替え）
  hub.html                作品一覧（トップ）のテンプレート
  common.py               恒星や要塞など、環境を組み立てる補助関数
works/<作品>/            作品ごとのデータ
  battles/*.py            1会戦＝1ファイル（部隊・場面・戦果）
  refs.py                 原作・アニメの該当箇所
  impact.py               後世への影響（3段階）と一文
  work.json               作品の設定（名前・時代区分・陣営名と色・暦の表記・注記）
  artifacts.json          claude.ai に公開済みのURL対応表
tools/
  build.py                会戦ページとポータルを生成
  shot.py                 スマホ幅での表示確認（Playwright）
docs/                   公開用の出力（GitHub Pages を想定）
  index.html              作品一覧
  ginei/                  銀英伝の会戦ページとポータル
  gundam-uc0079/          一年戦争の戦いページとポータル
site.json               サイト共通設定（サイト名、収録作品の並び、ga_id）
artifacts.json          claude.ai に公開した作品一覧（トップ）のURL
extras/                 本体に含めない試作（関ヶ原の3D再現）
notes/                  設計メモ（作品の選定基準など）
```

## ビルド

```sh
python3 tools/build.py all              # 全作品と作品一覧を docs/ に出力（GitHub Pages 用）
python3 tools/build.py all --artifact   # build/artifact/ に出力（claude.ai 用）
python3 tools/build.py ginei            # 1作品だけ
```

Node.js（構文チェックとデータ読み込みに使用）と Python 3 が必要。

## Google Analytics

`site.json` の `ga_id` に測定ID（G-XXXXXXXXXX）を入れてビルドすると、docs/ 配下（GitHub Pages 用）にだけタグが入る。claude.ai 用（--artifact）には入らない。

## 作品を追加する

1. `works/<作品>/` に battles/、refs.py、impact.py、work.json を置く（既存作品をひな形にする）
2. `site.json` の `works` にキーを足す
3. `python3 tools/build.py all` を実行する。作品一覧と各年表の切り替えメニューに自動で載る

## 会戦を追加する

1. `works/<作品>/battles/` に既存ファイルを参考に `.py` を1つ追加する
2. `refs.py` と `impact.py` に同じキーで項目を足す
3. `python3 tools/build.py all` を実行する

データの書き方は `CLAUDE.md` に詳しく書いてある。

## 方針

- 艦艇・紋章・キャラクターは原作デザインを使わず、抽象的な形で表す
- 原作の文章や台詞は転載しない
- 兵力・損害は原作の記述に拠り、確かめられない値は「不明」とする。推定には「推定」と書く
