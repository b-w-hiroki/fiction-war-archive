from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=71.0923
ARC='ヤキン・ドゥーエ'
OUT='boaz.html'
TITLE='ボアズ攻略戦 3D俯瞰'
HEAD='ボアズ攻略戦'
ERA='C.E.71年9月23日'
SE='ザフト'; SA='地球連合軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。概略'
ENV=space_env()+rock_fortress((0,6,-44),12,'solomon','BOAZ')+specials(labels([('ボアズ','ザフトの宇宙要塞','E',(0,26,-44),3.2)]))
DATA=r"""
const U=[
 {name:'ボアズ守備隊',cmd:'ザフト',side:'E',n:30,k:{0:{"p": [0, 0, -24], "s": "ready", "f": "concave"},1:{"p": [0, 0, -16], "s": "fight", "b": 1},2:{"p": [0, 0, -18], "s": "fight"},3:{"p": [0, 0, -24], "s": "broken", "l": "核攻撃で壊滅"},4:{"p": [0, 0, -60], "s": "withdraw"}}},
 {name:'連合艦隊',cmd:'地球連合軍',side:'A',n:40,k:{0:{"p": [0, 0, 50], "s": "move", "f": "line"},1:{"p": [0, 0, 24], "s": "fight"},2:{"p": [0, 0, 20], "s": "fight"},3:{"p": [0, 0, 14], "s": "charge"},4:{"p": [0, 0, 0], "s": "ready", "l": "要塞を奪う"}}},
 {name:'核攻撃隊',cmd:'ピースメーカー隊',side:'A',n:8,k:{0:{"p": [20, 0, 50], "s": "hidden"},1:{"p": [20, 0, 40], "s": "move"},2:{"p": [16, 0, 10], "s": "charge", "l": "核ミサイル発射"},3:{"p": [20, 0, 30], "s": "ready"},4:{"p": [20, 0, 30], "s": "ready"}}}
];
const PH=[
 {"time": "C.E.71年9月23日", "clock": "TV版第46話（推定）", "step": "進攻", "title": "ボアズへの進攻", "text": "連合は核を手にし、プラント防衛の要塞ボアズを攻めた。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 0, 50], [0, 0, 24]], "c": "A"}]},
 {"time": "同日", "clock": "", "step": "攻防", "title": "要塞前の攻防", "text": "ザフトは要塞の火力で抵抗した。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "核攻撃", "title": "核ミサイル発射", "text": "ピースメーカー隊が核ミサイルを要塞に撃ち込んだ。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": [{"p": [[16, 0, 10], [0, 0, -30]], "c": "A"}]},
 {"time": "同日", "clock": "", "step": "崩壊", "title": "ボアズ陥落", "text": "要塞は壊滅し、守備隊は退いた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "", "step": "次へ", "title": "ヤキン・ドゥーエへ", "text": "連合はプラント本国に迫り、ザフトはジェネシスを用意した。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "ボアズ攻略戦の結果", "when": "C.E.71年9月23日、ボアズ", "prev": "オーブ解放作戦", "next": "第二次ヤキン・ドゥーエ攻防戦（9月26〜27日）", "factors": ["連合がNジャマーキャンセラーで核兵器を再び使えるようになった。"], "winner": "A", "outcome": "連合の勝利", "summary": "核攻撃で要塞ボアズが落ちた戦い。", "sides": [{"name": "ザフト", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "要塞ボアズ", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連合軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["ザフトはジェネシスの使用に踏み切る。"], "note": "日付はfandom年表による。話数は推定。"};
"""
