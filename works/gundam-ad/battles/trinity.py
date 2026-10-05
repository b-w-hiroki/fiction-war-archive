from common import *
UC=2307.1
ARC='国連軍'
OUT='trinity.html'
TITLE='トリニティの武力介入 3D俯瞰'
HEAD='トリニティの武力介入'
ERA='西暦2307年（月日不明）'
SE='各国軍'; SA='チームトリニティ'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=land_env('0x8a7a5a','0xd8c8a0',amp=5,seed=3,sky='0x9aa8b8')+specials(labels([('各地', '無差別な攻撃', 'A', (0, 14, 0), 3.0)]))
DATA=r"""
const U=[
 {"name": "各国軍", "cmd": "基地・部隊", "side": "E", "n": 20, "k": {"0": {"p": [0, 7, -20], "s": "ready"}, "1": {"p": [0, 7, -15], "s": "broken", "l": "一方的に撃破"}, "2": {"p": [0, 7, -20], "s": "broken"}, "3": {"p": [0, 7, -30], "s": "withdraw"}}},
 {"name": "トリニティ", "cmd": "3機", "side": "A", "n": 3, "k": {"0": {"p": [0, 30, 30], "s": "move", "l": "出現"}, "1": {"p": [0, 7, 5], "s": "fight", "b": 1}, "2": {"p": [0, 7, 0], "s": "fight", "l": "民間にも被害"}, "3": {"p": [0, 30, 40], "s": "gone"}}}
];
const PH=[
 {"time": "西暦2307年", "clock": "TV版第16話", "step": "出現", "title": "第二のガンダム", "text": "スローネ3機が現れた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第17〜18話（推定）", "step": "拡大", "title": "過激な介入", "text": "民間を巻き込む攻撃を重ねた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第19〜21話（推定）", "step": "反発", "title": "世界の反発", "text": "ソレスタルビーイングへの反発が強まった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第21話（推定）", "step": "消滅", "title": "トリニティ壊滅", "text": "トリニティは内部の裏切りで崩れた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "トリニティの介入の結果", "when": "西暦2307年", "prev": "タクラマカン砂漠", "next": "国連軍との最終決戦", "factors": ["ヴェーダの情報が外部に流れていた。"], "winner": "none", "outcome": "トリニティの自滅", "summary": "トリニティの過激な介入で、世界は一つにまとまる方向へ進んだ。", "sides": [{"name": "各国軍", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "チームトリニティ", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "ほぼ全滅", "rate": null, "deaths": "不明", "dead": []}], "after": ["GNドライヴ（疑似）が各国へ渡り、国連軍が生まれる。"], "note": "TV版第16話題名から登場話を確認。以後の話数は推定。"};
"""
