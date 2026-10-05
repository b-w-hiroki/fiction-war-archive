from common import *
UC=323.06
ARC='地球への旅'
OUT='dort.html'
TITLE='ドルトコロニーの戦い 3D俯瞰'
HEAD='ドルトコロニーの戦い'
ERA='P.D.323年（月日不明）'
SE='ギャラルホルン'; SA='鉄華団'; PALE='zeon'; PAL='sind'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=space_env()+colony((0,0,0),(0,0,0),40,4,'DORT')+specials(labels([('ドルト', '労働者の暴動', 'E', (0, 14, 0), 3.0)]))
DATA=r"""
const U=[
 {"name": "ギャラルホルン", "cmd": "鎮圧部隊", "side": "E", "n": 20, "k": {"0": {"p": [0, 0, -30], "s": "ready"}, "1": {"p": [0, 0, -10], "s": "fight", "b": 1}, "2": {"p": [0, 0, -5], "s": "fight"}, "3": {"p": [0, 0, -20], "s": "wait"}}},
 {"name": "ドルト労働者", "cmd": "暴動", "side": "A", "n": 30, "k": {"0": {"p": [0, 0, 10], "s": "ready"}, "1": {"p": [0, 0, 5], "s": "broken", "l": "鎮圧"}, "2": {"p": [0, 0, 8], "s": "broken"}, "3": {"p": [0, 0, 10], "s": "gone"}}},
 {"name": "鉄華団", "cmd": "イサリビ・MS", "side": "A", "n": 4, "k": {"0": {"p": [20, 0, 40], "s": "move"}, "1": {"p": [15, 0, 20], "s": "fight"}, "2": {"p": [10, 0, 5], "s": "fight", "l": "クーデリア救出"}, "3": {"p": [30, 0, 40], "s": "withdraw"}}}
];
const PH=[
 {"time": "P.D.323年", "clock": "TV版第14話（推定）", "step": "到着", "title": "ドルト入港", "text": "鉄華団はクーデリアを連れてドルトへ着いた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第15〜16話（推定）", "step": "鎮圧", "title": "暴動の鎮圧", "text": "ギャラルホルンは労働者の蜂起を力で抑えた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同時期", "clock": "TV版第16話", "step": "救出", "title": "クーデリアの救出", "text": "鉄華団が戦場へ入り、クーデリアを守った。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第17話", "step": "演説", "title": "演説と離脱", "text": "クーデリアが訴え、鉄華団は地球へ向かった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "ドルトコロニーの結果", "when": "P.D.323年", "prev": "CGS襲撃", "next": "エドモントンの戦い", "factors": ["暴動はギャラルホルンが仕組んだものだった（作中描写）。"], "winner": "E", "outcome": "ギャラルホルンの鎮圧", "summary": "労働者の蜂起が鎮圧され、クーデリアが名を上げた戦い。", "sides": [{"name": "ギャラルホルン", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "鉄華団", "side": "A", "cmdr": "オルガ・イツカ", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["クーデリアが革命の乙女として知られる。"], "note": "話数は題名（第16話「Fumitan Admoss」、第17話）からの推定。"};
"""
