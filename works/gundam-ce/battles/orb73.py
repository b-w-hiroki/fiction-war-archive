from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=73.12
ARC='第二次大戦'
OUT='orb73.html'
TITLE='オーブ攻防 3D俯瞰'
HEAD='オーブ攻防'
ERA='C.E.73年（月日不明）'
SE='ザフト'; SA='オーブ軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。概略'
ENV=land_env('0x3a6a3a','0x9a9a70',amp=5,seed=9,water='0x2a6a90',sky='0x7aa0c0')+specials(labels([('オーブ','ジブリールの潜伏先','A',(0,14,30),3.2)]))
DATA=r"""
const U=[
 {name:'ザフト侵攻軍',cmd:'ザフト',side:'E',n:40,k:{0:{"p": [0, 7, -50], "s": "move", "f": "line"},1:{"p": [0, 7, -20], "s": "charge"},2:{"p": [0, 7, 0], "s": "fight", "b": 1},3:{"p": [0, 7, -6], "s": "fight"},4:{"p": [0, 7, -40], "s": "withdraw", "l": "撤退"}}},
 {name:'デスティニー',cmd:'シン・アスカ',side:'E',n:2,k:{0:{"p": [10, 7, -40], "s": "hidden"},1:{"p": [10, 7, -10], "s": "charge"},2:{"p": [12, 7, 4], "s": "fight", "l": "アカツキと交戦"},3:{"p": [10, 7, 0], "s": "fight"},4:{"p": [10, 7, -40], "s": "withdraw"}}},
 {name:'オーブ軍',cmd:'カガリ・ユラ・アスハ',side:'A',n:30,k:{0:{"p": [0, 7, 24], "s": "ready", "f": "concave"},1:{"p": [0, 7, 16], "s": "fight"},2:{"p": [0, 7, 14], "s": "fight"},3:{"p": [0, 7, 10], "s": "charge", "l": "カガリが復帰"},4:{"p": [0, 7, 20], "s": "ready", "l": "防衛成功"}}},
 {name:'ストライクフリーダム',cmd:'キラ・ヤマト',side:'A',n:2,k:{0:{"p": [20, 30, 40], "s": "hidden"},1:{"p": [20, 30, 40], "s": "hidden"},2:{"p": [16, 7, 8], "s": "charge", "l": "宇宙から参戦"},3:{"p": [14, 7, 4], "s": "fight"},4:{"p": [16, 7, 20], "s": "ready"}}}
];
const PH=[
 {"time": "C.E.73年", "clock": "DESTINY第39話（推定）", "step": "進攻", "title": "ザフトのオーブ攻撃", "text": "ジブリールの引き渡しを拒んだオーブに、ザフトが攻め込んだ。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 7, -50], [0, 7, -20]], "c": "E"}]},
 {"time": "同", "clock": "", "step": "防戦", "title": "オーブの防戦", "text": "オーブ軍はアカツキなどで防いだ。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "DESTINY第40話（推定）", "step": "参戦", "title": "キラの参戦", "text": "キラが新しい機体で戦場に現れた。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "復帰", "title": "カガリの復帰", "text": "カガリが国の指揮を取り戻し、オーブは反撃した。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "撤退", "title": "ザフトの撤退", "text": "ザフトは退いた。ジブリールは宇宙へ逃れた。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "オーブ攻防の結果", "when": "C.E.73年、オーブ連合首長国", "prev": "ヘブンズベース攻防戦", "next": "ダイダロス基地攻略（レクイエム）", "factors": ["キラらの参戦で戦況が変わった。", "カガリの復帰でオーブ軍がまとまった。"], "winner": "A", "outcome": "オーブの防衛成功", "summary": "ジブリールを追ったザフトがオーブを攻め、退けられた戦い。", "sides": [{"name": "ザフト", "side": "E", "cmdr": "不明", "flag": "不明", "others": "シン・アスカ", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "オーブ軍", "side": "A", "cmdr": "カガリ・ユラ・アスハ", "flag": "不明", "others": "キラ・ヤマト", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["オーブとデュランダルの対立が決定的になる。"], "note": "月日は確認できず不明。話数は推定。この戦いではオーブ側をA枠（緑）に置いた。"};
"""
