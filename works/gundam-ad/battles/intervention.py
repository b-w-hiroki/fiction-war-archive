from common import *
UC=2307.01
ARC='武力介入'
OUT='intervention.html'
TITLE='武力介入開始 3D俯瞰'
HEAD='武力介入開始'
ERA='西暦2307年（月日不明）'
SE='AEU・人革連など'; SA='ソレスタルビーイング'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=land_env('0x8a7a5a','0xd8c8a0',amp=5,seed=3,sky='0x9aa8b8')+specials(labels([('演習場', 'AEU新型の公開', 'E', (0, 14, -20), 3.0)]))
DATA=r"""
const U=[
 {"name": "AEU部隊", "cmd": "新型MSの公開演習", "side": "E", "n": 8, "k": {"0": {"p": [0, 7, -20], "s": "ready", "f": "line"}, "1": {"p": [0, 7, -15], "s": "fight"}, "2": {"p": [0, 7, -12], "s": "broken", "l": "無力化"}, "3": {"p": [0, 7, -30], "s": "withdraw"}}},
 {"name": "ガンダム", "cmd": "4機のマイスター", "side": "A", "n": 4, "k": {"0": {"p": [0, 40, 40], "s": "hidden"}, "1": {"p": [0, 7, 10], "s": "charge", "l": "突如出現", "b": 1}, "2": {"p": [0, 7, 0], "s": "fight"}, "3": {"p": [0, 30, 40], "s": "withdraw", "l": "離脱"}}}
];
const PH=[
 {"time": "西暦2307年", "clock": "TV版第1話", "step": "前夜", "title": "新型の公開", "text": "AEUが新型MSの公開演習を行っていた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "TV版第1話", "step": "出現", "title": "ガンダム出現", "text": "正体不明のMSが現れ、演習中の機体を退けた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第1〜2話", "step": "宣言", "title": "武力介入の宣言", "text": "ソレスタルビーイングは紛争を武力で止めると世界に宣言した。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "TV版第2話以降", "step": "拡大", "title": "各地への介入", "text": "各地の紛争に介入を始め、三大陣営は対応を迫られた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "武力介入開始の結果", "when": "西暦2307年", "prev": "—", "next": "モラリア介入", "factors": ["GN粒子を使うガンダムの性能が既存MSを上回っていた。"], "winner": "A", "outcome": "ソレスタルビーイングの一方的介入", "summary": "ガンダムが世界に姿を見せ、武力による紛争根絶を始めた出来事。", "sides": [{"name": "AEUほか", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "演習機など（数は不明）", "rate": null, "deaths": "不明", "dead": []}, {"name": "ソレスタルビーイング", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "なし", "rate": null, "deaths": "不明", "dead": []}], "after": ["三大陣営がガンダム対策を考え始める。"], "note": "年は作中設定（西暦2307年）。月日・数値は不明。"};
"""
