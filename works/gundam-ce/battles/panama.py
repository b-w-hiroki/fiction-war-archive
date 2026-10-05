from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=71.0525
ARC='地球の攻防'
OUT='panama.html'
TITLE='パナマ攻略戦 3D俯瞰'
HEAD='パナマ攻略戦'
ERA='C.E.71年5月25日'
SE='ザフト'; SA='地球連合軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は概略'
ENV=land_env('0x2f5a34','0x7a8a5a',amp=4,seed=7,water='0x2a5a80',sky='0x7090a8')+specials(labels([('パナマ基地','マスドライバー','A',(0,14,30),3.2)]))
DATA=r"""
const U=[
 {name:'ザフト攻略部隊',cmd:'ザフト',side:'E',n:40,k:{0:{"p": [0, 7, -50], "s": "move", "f": "wedge"},1:{"p": [0, 7, -20], "s": "charge"},2:{"p": [0, 7, 6], "s": "fight", "l": "EMP兵器使用"},3:{"p": [0, 7, 20], "s": "charge", "l": "基地を制圧"},4:{"p": [0, 7, 24], "s": "ready", "l": "マスドライバー破壊"}}},
 {name:'連合守備隊',cmd:'地球連合軍',side:'A',n:36,k:{0:{"p": [0, 7, 30], "s": "ready", "f": "line"},1:{"p": [0, 7, 20], "s": "fight", "b": 1},2:{"p": [0, 7, 22], "s": "broken", "l": "MSが動かない"},3:{"p": [0, 7, 34], "s": "broken", "l": "投降者も撃たれる"},4:{"s": "gone"}}}
];
const PH=[
 {"time": "C.E.71年5月25日", "clock": "TV版第37話", "step": "進攻", "title": "パナマへの進攻", "text": "アラスカの後、ザフトは連合の宇宙への出口パナマを攻めた。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 7, -50], [0, 7, -20]], "c": "E"}]},
 {"time": "同日", "clock": "", "step": "交戦", "title": "守備隊の迎撃", "text": "連合は量産MSで迎え撃つ。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "EMP", "title": "電磁パルス兵器", "text": "ザフトは電磁パルス兵器で連合の機体を止めた。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "制圧", "title": "基地制圧", "text": "ザフトは基地を制圧した。投降した兵が撃たれる惨事も起きた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "", "step": "破壊", "title": "マスドライバー破壊", "text": "マスドライバーが壊され、連合は宇宙への輸送手段を失った。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "パナマ攻略戦の結果", "when": "C.E.71年5月25日、パナマ", "prev": "アラスカ（JOSH-A）", "next": "オーブ解放作戦（6月15日）", "factors": ["EMP兵器で連合の機体が無力化された。", "アラスカの報復感情が両軍に強かった。"], "winner": "E", "outcome": "ザフトの勝利", "summary": "連合のマスドライバーをザフトが破壊した戦い。", "sides": [{"name": "ザフト", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連合軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "基地とマスドライバー", "rate": null, "deaths": "不明", "dead": []}], "after": ["連合はオーブのマスドライバーを狙うようになる。"], "note": "日付はfandom年表による。話数はPHASE-37「神のいかずち」（https://www.gundam-seed.net/seed/story/detail.php?id=35 ）。"};
"""
