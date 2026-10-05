from common import *
UC=1945.03
ARC='大西洋・対独戦'
OUT='iceland.html'
TITLE='アイスランド沖海戦 3D俯瞰'
HEAD='アイスランド沖'
ERA='1945年（推定）'
SE='ドイツ第三帝国'; SA='日本（後世）'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x1e4a6a','0x3a6a5a',water='0x1f5a86',amp=3,seed=29,sky='0x7f9ab8')+specials(labels([('アイスランド沖','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "ドイツ艦隊", "cmd": "—", "side": "E", "n": 30, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "北大西洋"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "wait"}}}, {"name": "日本艦隊", "cmd": "—", "side": "A", "n": 24, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "大西洋へ進出"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "wait"}}}];
const PH=[{"time": "1945年（推定）", "clock": "第28話「嗚呼、アイスランド沖海戦」", "step": "進出", "title": "北大西洋へ", "text": "日本の艦隊は大西洋に入り、ドイツと海で戦うことになった。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "会敵", "title": "アイスランド沖", "text": "アイスランド沖で両艦隊が出会った。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "海戦", "title": "激しい撃ち合い", "text": "激しい海戦になった（結果の細部は推定）。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "大西洋の足場", "text": "日本は大西洋での戦いを続けた（推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "アイスランド沖海戦の結果", "when": "1945年（推定）、アイスランド沖", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "none", "outcome": "不明（推定）", "summary": "北大西洋で日独の艦隊がぶつかった海戦。勝敗の細部は確認できていない。", "sides": [{"name": "ドイツ艦隊", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "日本艦隊", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
