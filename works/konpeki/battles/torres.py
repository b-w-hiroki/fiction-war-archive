from common import *
UC=1942.06
ARC='対米戦'
OUT='torres.html'
TITLE='トレス海峡封鎖・タスマン海戦 3D俯瞰'
HEAD='タスマン海戦'
ERA='1942年（推定）'
SE='米国'; SA='日本（後世）'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x1e4a6a','0x3a6a5a',water='0x1f5a86',amp=3,seed=11,sky='0x7f9ab8')+specials(labels([('タスマン海','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "米豪連合艦隊", "cmd": "—", "side": "E", "n": 30, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "豪州防衛"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "紺碧艦隊", "cmd": "前原一征", "side": "A", "n": 14, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "海峡封鎖"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1942年（推定）", "clock": "第5話「トレス海峡封鎖作戦」・第6話「一撃轟沈タスマン海戦」", "step": "封鎖", "title": "海峡を閉じる", "text": "日本はトレス海峡を封じ、豪州への補給路を断とうとした。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "索敵", "title": "敵艦隊を探る", "text": "潜水艦隊がタスマン海で米豪の艦隊を探した。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "雷撃", "title": "一撃で沈める", "text": "紺碧艦隊の雷撃で敵の主力艦が沈んだ。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "豪州の孤立", "text": "豪州は米国から切り離されていく（推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "トレス海峡封鎖・タスマン海戦の結果", "when": "1942年（推定）、タスマン海", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の勝利", "summary": "トレス海峡の封鎖とタスマン海の勝利で、南太平洋の連合軍は弱まった。", "sides": [{"name": "米豪連合艦隊", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "紺碧艦隊", "side": "A", "cmdr": "前原一征", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
