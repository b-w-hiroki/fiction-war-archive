from common import *
UC=2314.01
ARC='ELS'
OUT='els.html'
TITLE='ELSとの対話 3D俯瞰'
HEAD='ELSとの対話'
ERA='西暦2314年（月日不明）'
SE='ELS'; SA='地球連邦軍・ソレスタルビーイング'; PALE='titan'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略（抽象図形）'
ENV=space_env()+planet((0,-260,0),200)+specials(labels([('地球圏', '防衛線', 'A', (0, 20, 30), 3.0)]))
DATA=r"""
const U=[
 {"name": "ELS", "cmd": "異星体の大群", "side": "E", "n": 80, "k": {"0": {"p": [0, 0, -60], "s": "move"}, "1": {"p": [0, 0, -20], "s": "charge", "b": 1}, "2": {"p": [0, 0, 0], "s": "fight"}, "3": {"p": [0, 0, -10], "s": "wait", "l": "対話成立", "nf": 1}}},
 {"name": "地球連邦軍", "cmd": "防衛艦隊", "side": "A", "n": 40, "k": {"0": {"p": [0, 0, 30], "s": "ready", "f": "line"}, "1": {"p": [0, 0, 20], "s": "fight"}, "2": {"p": [0, 0, 25], "s": "broken", "l": "押される"}, "3": {"p": [0, 0, 30], "s": "wait", "nf": 1}}},
 {"name": "ダブルオークアンタ", "cmd": "刹那", "side": "A", "n": 1, "k": {"0": {"p": [20, 0, 40], "s": "hidden"}, "1": {"p": [20, 0, 30], "s": "move"}, "2": {"p": [10, 0, 0], "s": "charge", "l": "対話へ"}, "3": {"p": [0, 0, -15], "s": "wait", "l": "共存へ", "nf": 1}}}
];
const PH=[
 {"time": "西暦2314年", "clock": "劇場版", "step": "接近", "title": "ELS飛来", "text": "金属異星体ELSが地球へ向かった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同時期", "clock": "劇場版", "step": "迎撃", "title": "連邦軍の迎撃", "text": "連邦軍は全力で迎え撃ったが、ELSは止まらなかった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同時期", "clock": "劇場版", "step": "対話", "title": "クアンタの突入", "text": "刹那が中心へ飛び込み、意思を通わせた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "劇場版", "step": "終結", "title": "共存", "text": "ELSは攻撃をやめ、戦いは終わった。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "ELSとの対話の結果", "when": "西暦2314年", "prev": "アロウズとの最終決戦", "next": "—", "factors": ["ELSは敵意ではなく理解を求めていた。"], "winner": "none", "outcome": "対話による終結", "summary": "人類と異星体ELSの接触。戦闘ではなく対話で終わった。", "sides": [{"name": "ELS", "side": "E", "cmdr": "—", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連邦軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "多数（数は不明）", "rate": null, "deaths": "不明", "dead": []}], "after": ["人類と異星体の共存が始まる。"], "note": "劇場版『劇場版 機動戦士ガンダム00 -Awakening of the Trailblazer-』（2010年）。年は作中設定。"};
"""
