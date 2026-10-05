from common import *
UC=1945.06
ARC='大西洋・対独戦'
OUT='equator.html'
TITLE='赤道大海戦 3D俯瞰'
HEAD='赤道大海戦'
ERA='1945年（推定）'
SE='ドイツ第三帝国'; SA='日本（後世）'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x1e4a6a','0x3a6a5a',water='0x1f5a86',amp=3,seed=31,sky='0x7f9ab8')+specials(labels([('大西洋 赤道付近','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "ドイツ艦隊", "cmd": "—", "side": "E", "n": 40, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "主力艦隊"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "日本艦隊（紺碧艦隊ほか）", "cmd": "—", "side": "A", "n": 36, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "決戦へ"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1945年（推定）", "clock": "第30話「赤道大海戦」〜第32話「亜細亜の曙」", "step": "集結", "title": "決戦の準備", "text": "日独とも主力を集め、大西洋で決戦に臨んだ。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "会敵", "title": "赤道の海", "text": "赤道付近で両軍の主力艦隊がぶつかった。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "海戦", "title": "大海戦", "text": "潜水艦と水上艦が入り乱れる大海戦になった。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "OVAの結末へ", "text": "この戦いを経て、OVAは最終話へ向かう（勝敗の細部は推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "赤道大海戦の結果", "when": "1945年（推定）、大西洋 赤道付近", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の勝利（推定）", "summary": "OVA終盤の日独主力の決戦。", "sides": [{"name": "ドイツ艦隊", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "日本艦隊（紺碧艦隊ほか）", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
