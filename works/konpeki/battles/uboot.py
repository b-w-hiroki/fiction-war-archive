from common import *
UC=1944.06
ARC='インド洋・対独戦'
OUT='uboot.html'
TITLE='独水中襲撃艦隊殲滅戦 3D俯瞰'
HEAD='独潜殲滅'
ERA='1944年（推定）'
SE='ドイツ第三帝国'; SA='日本（後世）'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x1e4a6a','0x3a6a5a',water='0x1f5a86',amp=3,seed=19,sky='0x7f9ab8')+specials(labels([('インド洋','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "独水中襲撃艦隊", "cmd": "—", "side": "E", "n": 20, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "インド洋で通商破壊"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "紺碧艦隊", "cmd": "前原一征", "side": "A", "n": 14, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "潜水艦戦"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1944年（推定）", "clock": "第17話「暗雲印度洋浪高し!」・第18話「殲滅独逸水中襲撃艦隊」", "step": "脅威", "title": "独潜水艦の進出", "text": "ドイツの潜水艦隊がインド洋に入り、日本の航路を脅かした。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "追跡", "title": "海中の探り合い", "text": "紺碧艦隊は海中でドイツ艦隊を追った。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "決戦", "title": "海中の戦い", "text": "潜水艦同士の戦いで、ドイツ艦隊を壊滅させた。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "航路の回復", "text": "インド洋の日本の航路が守られた（推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "独水中襲撃艦隊殲滅戦の結果", "when": "1944年（推定）、インド洋", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の勝利", "summary": "ドイツの水中襲撃艦隊を壊滅させた戦い。", "sides": [{"name": "独水中襲撃艦隊", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "紺碧艦隊", "side": "A", "cmdr": "前原一征", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
