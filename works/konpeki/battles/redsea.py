from common import *
UC=1944.02
ARC='インド洋・対独戦'
OUT='redsea.html'
TITLE='紅海雷撃作戦 3D俯瞰'
HEAD='紅海雷撃'
ERA='1944年（推定）'
SE='ドイツ第三帝国'; SA='日本（後世）'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x1e4a6a','0x3a6a5a',water='0x1f5a86',amp=3,seed=17,sky='0x7f9ab8')+specials(labels([('紅海','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "ドイツ軍", "cmd": "—", "side": "E", "n": 24, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "中東へ進む"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "紺碧艦隊", "cmd": "前原一征", "side": "A", "n": 14, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "雷撃"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1944年（推定）", "clock": "第14話「紅海雷撃作戦」", "step": "転換", "title": "新しい敵", "text": "米国との戦いが落ち着くと、ドイツ第三帝国が新しい脅威になった。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "潜入", "title": "紅海へ", "text": "紺碧艦隊は紅海に入り、ドイツ側の海上輸送を狙った。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "雷撃", "title": "輸送を断つ", "text": "雷撃でドイツの艦船を沈めた（細部は推定）。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "インド洋の守り", "text": "ドイツのインド洋進出を遅らせた（推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "紅海雷撃作戦の結果", "when": "1944年（推定）、紅海", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の勝利（推定）", "summary": "対独戦の序盤で、紺碧艦隊が紅海の海上輸送を叩いた。", "sides": [{"name": "ドイツ軍", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "紺碧艦隊", "side": "A", "cmdr": "前原一征", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
