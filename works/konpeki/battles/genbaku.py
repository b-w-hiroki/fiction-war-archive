from common import *
UC=1943.03
ARC='対米戦'
OUT='genbaku.html'
TITLE='原爆阻止作戦 3D俯瞰'
HEAD='原爆阻止'
ERA='1943年（推定）'
SE='米国'; SA='日本（後世）'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は抽象化した概略で、兵力の大きさは目安（数値は不明）'
ENV=land_env('0x8a7a4a','0xc8a868',amp=5,seed=13,sky='0x9aa8b8')+specials(labels([('米国の原爆開発拠点','','A',(0,24,0),3.2)]))
DATA=r"""
const U=[{"name": "米国の原爆計画", "cmd": "—", "side": "E", "n": 16, "k": {"0": {"p": [0, 7, -40], "s": "ready", "l": "開発施設"}, "1": {"p": [0, 7, -32], "s": "fight"}, "2": {"p": [0, 7, -24], "s": "fight"}, "3": {"p": [0, 7, -16], "s": "withdraw"}}}, {"name": "日本の攻撃隊", "cmd": "—", "side": "A", "n": 12, "k": {"0": {"p": [10, 7, 40], "s": "ready", "l": "阻止に向かう"}, "1": {"p": [10, 7, 32], "s": "fight"}, "2": {"p": [10, 7, 24], "s": "fight"}, "3": {"p": [10, 7, 16], "s": "ready"}}}];
const PH=[{"time": "1943年（推定）", "clock": "第8話「原爆阻止作戦」", "step": "察知", "title": "原爆の開発", "text": "日本は米国が原子爆弾を開発していることを知った。", "cam": {"fit": 1, "th": 0.3, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "出撃", "title": "長距離の攻撃", "text": "開発拠点を叩くため、攻撃隊が送られた。", "cam": {"fit": 1, "th": 0.44999999999999996, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "攻撃", "title": "施設を叩く", "text": "攻撃隊は開発施設に損害を与えた（細部は推定）。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []}, {"time": "", "clock": "", "step": "結果", "title": "原爆の遅れ", "text": "米国の原爆開発は止まるか大きく遅れた（推定）。", "cam": {"fit": 1, "th": 0.75, "ph": 0.9}, "arrows": []}];
const RESULT={"title": "原爆阻止作戦の結果", "when": "1943年（推定）、米国の原爆開発拠点", "prev": "—", "next": "—", "factors": ["展開はOVAの話数タイトルと英語版Wikipediaの概要にもとづく概略。細部は推定を含む。"], "winner": "A", "outcome": "日本の作戦成功（推定）", "summary": "原爆の使用を防ぐことが、後世世界の大きな目標とされる。", "sides": [{"name": "米国の原爆計画", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "日本の攻撃隊", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": [], "note": "OVA話数はビデオマーケットの話数一覧で確認。年月・兵力・損害は確認できず、年は推定。小説の巻は未確認。"};
"""
