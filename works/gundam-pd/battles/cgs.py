from common import *
UC=323.01
ARC='火星'
OUT='cgs.html'
TITLE='CGS襲撃 3D俯瞰'
HEAD='CGS襲撃'
ERA='P.D.323年（月日不明）'
SE='ギャラルホルン'; SA='鉄華団'; PALE='zeon'; PAL='sind'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=land_env('0x8a4a30','0xd09070',amp=5,seed=5,sky='0xb08070')+specials(labels([('CGS基地', 'クリュセ郊外', 'A', (0, 14, 25), 3.0)]))
DATA=r"""
const U=[
 {"name": "ギャラルホルン火星支部", "cmd": "MS3機と歩兵", "side": "E", "n": 10, "k": {"0": {"p": [0, 7, -30], "s": "move"}, "1": {"p": [0, 7, -10], "s": "charge", "b": 1}, "2": {"p": [0, 7, 0], "s": "fight"}, "3": {"p": [0, 7, -30], "s": "withdraw", "l": "撤退"}}},
 {"name": "CGS参番組", "cmd": "少年兵", "side": "A", "n": 20, "k": {"0": {"p": [0, 7, 25], "s": "ready", "f": "line"}, "1": {"p": [0, 7, 20], "s": "fight", "l": "囮にされる"}, "2": {"p": [0, 7, 15], "s": "fight"}, "3": {"p": [0, 7, 15], "s": "wait"}}},
 {"name": "バルバトス", "cmd": "三日月", "side": "A", "n": 1, "k": {"0": {"p": [10, 7, 30], "s": "hidden"}, "1": {"p": [10, 7, 30], "s": "hidden"}, "2": {"p": [5, 7, 5], "s": "charge", "l": "起動", "b": 1}, "3": {"p": [0, 7, 0], "s": "fight", "l": "撃退"}}}
];
const PH=[
 {"time": "P.D.323年", "clock": "TV版第1話", "step": "襲撃", "title": "基地への奇襲", "text": "ギャラルホルンがクーデリア護衛中のCGSを襲った。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "TV版第1話", "step": "見捨て", "title": "一軍の逃亡", "text": "大人の一軍は少年兵を囮にして逃げた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "TV版第1〜2話", "step": "起動", "title": "バルバトス出撃", "text": "三日月が動力源だった機体で出撃した。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第3話", "step": "撃退", "title": "鉄華団へ", "text": "襲撃を退け、少年たちは会社を乗っ取り鉄華団を作った。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "CGS襲撃の結果", "when": "P.D.323年", "prev": "—", "next": "ドルトコロニーの戦い", "factors": ["バルバトスが想定外の戦力になった。"], "winner": "A", "outcome": "CGS参番組の撃退", "summary": "鉄華団誕生のきっかけになった戦い。", "sides": [{"name": "ギャラルホルン火星支部", "side": "E", "cmdr": "クランク・ゼントほか（推定）", "flag": "不明", "others": "—", "before": "不明", "loss": "MSなど（数は不明）", "rate": null, "deaths": "不明", "dead": []}, {"name": "CGS参番組", "side": "A", "cmdr": "オルガ・イツカ", "flag": "不明", "others": "—", "before": "不明", "loss": "少年兵多数（数は不明）", "rate": null, "deaths": "不明", "dead": []}], "after": ["参番組が実権を握り、鉄華団が生まれる。"], "note": "話数は第1〜3話の題名から確認。兵力は不明。"};
"""
