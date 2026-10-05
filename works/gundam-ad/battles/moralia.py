from common import *
UC=2307.05
ARC='武力介入'
OUT='moralia.html'
TITLE='モラリア介入 3D俯瞰'
HEAD='モラリア介入'
ERA='西暦2307年（月日不明）'
SE='AEU・PMC'; SA='ソレスタルビーイング'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=land_env('0x8a7a5a','0xd8c8a0',amp=5,seed=3,sky='0x9aa8b8')+specials(labels([('モラリア', '民間軍事会社の国', 'E', (0, 14, -25), 3.0)]))
DATA=r"""
const U=[
 {"name": "AEU軍", "cmd": "モラリア派遣部隊", "side": "E", "n": 20, "k": {"0": {"p": [0, 7, -25], "s": "ready", "f": "line"}, "1": {"p": [0, 7, -15], "s": "fight"}, "2": {"p": [0, 7, -10], "s": "broken"}, "3": {"p": [0, 7, -35], "s": "withdraw"}}},
 {"name": "PMC部隊", "cmd": "民間軍事会社", "side": "E", "n": 12, "k": {"0": {"p": [20, 7, -20], "s": "ready"}, "1": {"p": [15, 7, -10], "s": "fight"}, "2": {"p": [10, 7, -5], "s": "broken"}, "3": {"p": [20, 7, -30], "s": "withdraw"}}},
 {"name": "ガンダム", "cmd": "4機", "side": "A", "n": 4, "k": {"0": {"p": [0, 30, 30], "s": "move", "l": "降下"}, "1": {"p": [0, 7, 5], "s": "charge", "b": 1}, "2": {"p": [0, 7, 0], "s": "fight", "l": "長時間の戦闘"}, "3": {"p": [0, 30, 30], "s": "withdraw"}}}
];
const PH=[
 {"time": "西暦2307年", "clock": "TV版第5話（推定）", "step": "開戦", "title": "AEUとモラリアの共同演習", "text": "ガンダムが介入の対象に選んだ。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "突入", "title": "ガンダム降下", "text": "4機が降下し、軍事施設を狙った。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "消耗", "title": "長い戦闘", "text": "AEUは数で押したが、ガンダムを止められなかった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "", "step": "停戦", "title": "戦闘の終結", "text": "モラリア側は戦闘を止めた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "モラリア介入の結果", "when": "西暦2307年", "prev": "武力介入開始", "next": "タクラマカン砂漠の合同軍事演習", "factors": ["数で押す戦い方はガンダムの性能に届かなかった。"], "winner": "A", "outcome": "ソレスタルビーイングの勝利", "summary": "民間軍事会社の国モラリアへの介入。ガンダムが大部隊を相手に耐え抜いた。", "sides": [{"name": "AEU・PMC", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "多数（数は不明）", "rate": null, "deaths": "不明", "dead": []}, {"name": "ソレスタルビーイング", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "なし", "rate": null, "deaths": "不明", "dead": []}], "after": ["ガンダムを数で倒す難しさが示される。"], "note": "話数は推定。兵力・損害は不明。"};
"""
