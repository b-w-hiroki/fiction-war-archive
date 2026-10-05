from common import *
UC=96.05
ARC='ラプラス事変'
OUT='torrington96.html'
TITLE='トリントン基地攻防 3D俯瞰'
HEAD='トリントン'
ERA='U.C.0096年5月（推定）'
SE='ジオン残党'; SA='地球連邦軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。OVA第4話にもとづく概略'
ENV=land_env('0x6a5a3a','0xb09a6a',amp=4,seed=31,sky='0x48506a')+specials(labels([('トリントン基地','オーストラリアの連邦基地','A',(0,14,30),3.4)]))
DATA=r"""
const U=[
 {"name": "ジオン残党（地上）", "cmd": "ロニ・ガーベイら", "side": "E", "n": 12, "k": {"0": {"p": [0, 7, -50], "s": "move", "l": "砂漠から進軍"}, "1": {"p": [0, 7, -20], "s": "charge"}, "2": {"p": [0, 7, -6], "s": "fight"}, "3": {"p": [0, 7, -20], "s": "broken"}, "4": {"s": "gone"}}},
 {"name": "基地守備隊", "cmd": "連邦トリントン基地", "side": "A", "n": 16, "k": {"0": {"p": [0, 7, 30], "s": "ready", "f": "line"}, "1": {"p": [0, 7, 16], "s": "fight"}, "2": {"p": [0, 7, 8], "s": "fight"}, "3": {"p": [0, 7, 14], "s": "fight"}, "4": {"p": [0, 7, 20], "s": "ready"}}},
 {"name": "ユニコーン（バナージ）", "cmd": "バナージ・リンクス", "side": "A", "n": 1, "k": {"0": {"p": [10, 7, 20], "s": "hidden"}, "1": {"p": [10, 7, 20], "s": "move", "l": "戦場に介入"}, "2": {"p": [6, 7, 0], "s": "fight"}, "3": {"p": [4, 7, -10], "s": "fight"}, "4": {"p": [4, 7, 0], "s": "ready"}}}
];
const PH=[
 {"time": "5月（推定）", "clock": "OVA第4話", "step": "進軍", "title": "残党の総攻撃", "text": "地球に潜んでいたジオン残党が、連邦のトリントン基地を襲った。", "cam": {"fit": 1, "th": 0.4, "ph": 0.9}, "arrows": []},
 {"time": "同日", "clock": "", "step": "攻撃", "title": "基地への突入", "text": "残党の旧式機が基地の防衛線に迫った。", "cam": {"fit": 1, "th": 0.4, "ph": 0.9}, "arrows": [{"p": [[0, 7, -20], [0, 7, -6]], "c": "E"}]},
 {"time": "同日", "clock": "", "step": "激戦", "title": "ユニコーン参戦", "text": "連邦側にいたバナージのユニコーンも戦いに加わる。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []},
 {"time": "同日", "clock": "", "step": "終結", "title": "残党の壊滅", "text": "撃てないバナージのユニコーンからリディのデルタプラスがビーム・マグナムを奪い、シャンブロのロニを討った。", "cam": {"fit": 1, "th": 0.1, "ph": 1.0}, "arrows": []}
];
const RESULT={"title": "トリントン基地攻防の結果", "when": "U.C.0096年、オーストラリア", "prev": "インダストリアル7襲撃", "next": "ダカール襲撃", "factors": ["連邦基地の戦力が残党を上回った。"], "winner": "A", "outcome": "連邦の防衛成功", "summary": "地上の残党が大きく傷ついた。", "sides": [{"name": "ジオン残党", "side": "E", "cmdr": "ロニ・ガーベイ", "flag": "シャンブロ", "others": "—", "before": "不明", "loss": "シャンブロ", "rate": null, "deaths": "不明", "dead": ["ロニ・ガーベイ"]}, {"name": "地球連邦軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["小説版では、この後シャンブロがダカールを襲う。"], "note": "OVA第4話「重力の井戸の底で」（https://en.wikipedia.org/wiki/List_of_Mobile_Suit_Gundam_Unicorn_episodes 、https://dic.pixiv.net/a/%E3%83%AD%E3%83%8B%E3%83%BB%E3%82%AC%E3%83%BC%E3%83%99%E3%82%A4 ）。時期（月）は記憶にもとづく推定。"};
"""
