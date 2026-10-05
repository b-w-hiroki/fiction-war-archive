from common import *
UC=1942.02
ARC='対米戦'
OUT='panama.html'
TITLE='パナマ運河爆撃 3D俯瞰'
HEAD='パナマ運河'
ERA='1942年（推定）'
SE='米国'; SA='日本（後世）'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x8a7a4a','0xc8a868',amp=5,seed=7,sky='0x9aa8b8')+specials(labels([('ガトゥン閘門','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "運河防衛隊", "cmd": "—", "side": "E", "n": 20, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "運河の守り"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "紺碧艦隊", "cmd": "前原一征", "side": "A", "n": 14, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "潜水艦から発進"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1942年（推定）", "clock": "第2話「パナマ運河爆撃す」", "step": "潜行", "title": "太平洋を渡る", "text": "紺碧艦隊の潜水艦は気づかれずにパナマ沖へ近づいた。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "発進", "title": "潜水艦から攻撃機", "text": "潜水艦に積んだ攻撃機が発進し、運河へ向かう。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "爆撃", "title": "閘門を壊す", "text": "攻撃隊は閘門を破壊し、運河を使えなくした。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "離脱", "title": "海中へ戻る", "text": "攻撃隊を収容し、艦隊は海中に消えた。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "パナマ運河爆撃の結果", "when": "1942年（推定）、ガトゥン閘門", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の勝利（運河の閘門を破壊）", "summary": "米海軍は大西洋と太平洋の間で艦艇を回せなくなった。", "sides": [{"name": "運河防衛隊", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "紺碧艦隊", "side": "A", "cmdr": "前原一征", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
