# fiction-war-archive 作業メモ

## 会戦データ（works/<作品>/battles/*.py）の書き方

必須の変数:
- `UC`（並び順に使う数値。例 796.02＝宇宙暦796年2月）、`ARC`（時代区分。ポータルの区分名と一致させる）
- `OUT='<key>.html'`（キーは refs.py / impact.py / artifacts.json と共通）
- `TITLE`（末尾に「 3D俯瞰」）、`HEAD`（縦書きタイトル）、`ERA`、`NOTE`
- `ENV`：`common.env(...)` で恒星と光源。要塞は `common.fort(...)`、主砲演出は `common.fort_cannon(...)`
- `DATA`：JS文字列。`const U=[...]`（部隊）、`const PH=[...]`（場面）、`const RESULT={...}`（戦果）

任意: `SE`/`SA`（陣営名。既定は帝国軍/同盟軍）、`PAL`/`PALE`（陣営色。noble, coup, iser, rebel, ally, zeon, efsf）

地球圏・地上戦の環境（engine/common.py）:
- 宇宙：`space_env()`＋`planet(...)`／`colony(...)`／`rock_fortress(pos,r,'solomon'|'abaoaqu')`
- 地上：`land_env(low,high,water=None,amp,seed,sky)`。部隊は y=6〜7 に置く
- 演出は `specials(labels([...]), move_obj(名前,{場面:座標}), shot(発射位置,部隊名,場面))` でまとめる。ENV の末尾に必ず `specials(...)` を1つ置く（SPECIAL を定義するため）

部隊 `k` の場面ごとの指定:
- `p:[x,y,z]` 位置。帝国側は z 負、相手側は z 正に置くのが基本
- `s` 状態：ready / fight / charge / broken / withdraw / move / wait / gone / hidden（途中参戦）
- `l` ラベル、`f` 陣形（wedge, concave, convex, line, column, spindle, `{ring:[cx,cz,r,a0,a1,w]}`）、`h` 向き（度）
- `nf:1` その場面は発砲しない、`b:1` 砲撃を強める、`dl:秒` 移動開始を遅らせる

場面のカメラは `cam:{fit:1, th, ph, k}` を使うと部隊の配置から画角を自動で決める。

## 作品の設定（works/<作品>/work.json）

- `title` 年表の見出し、`short` 切り替えメニューの表示名、`span` 作品一覧に出す期間、`unit` 数え方（会戦／戦い）
- `date` 年の表記方式（ginei＝宇宙暦の整数、uc＝ERA中の「U.C.0079年1月3日」を読む）、`yl` 時代見出しの暦名
- `eras` 時代区分（ARC と一致）、`names` 陣営の勝利表記、`order` 凡例の並び、`colors` 陣営色（明・暗）
- `lead`・`notes` は HTML 断片（改行位置は span.nb で区切る）

## 確認

- `python3 tools/build.py all` は構文とデータの読み込みまで検査する（作品一覧・各年表・会戦ページをまとめて出力）
- 見た目は `python3 tools/shot.py docs/<作品>/<key>.html 1,3 res 6000` で撮影し `/tmp/cmp.png` を見る（three.js を /tmp に npm i しておく）

## 文章

- 結論から短く。原作の台詞は引用しない
- 数値は資料で確認できたものだけ。記憶にもとづくものは note に明記する
- 長い日本語は ポータル側で BudouX により文節改行される
