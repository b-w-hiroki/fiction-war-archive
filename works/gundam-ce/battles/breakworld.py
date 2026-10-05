from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=73.1003
ARC='第二次大戦'
OUT='breakworld.html'
TITLE='ブレイク・ザ・ワールド 3D俯瞰'
HEAD='ブレイク・ザ・ワールド'
ERA='C.E.73年10月3日'
SE='テロリスト'; SA='ザフト'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。テロリストを赤、ザフト正規軍を青で表示'
ENV=space_env()+planet((0,-300,0),220,label=('地球','','A'))+colony((0,0,-10),(1.2,0,.3),36,5,'JUNIUS')+specials(labels([('ユニウスセブン','落下する残骸','E',(0,14,-10),3)]))
DATA=r"""
const U=[
 {name:'テロリスト',cmd:'サトー（旧ザフト兵）',side:'E',n:8,k:{0:{"p": [-10, 0, -20], "s": "ready", "l": "残骸を動かす"},1:{"p": [-10, 0, -10], "s": "fight"},2:{"p": [-10, 0, -6], "s": "fight"},3:{"p": [-10, 0, -6], "s": "broken", "l": "全滅"},4:{"s": "gone"}}},
 {name:'ミネルバ隊',cmd:'ザフト',side:'A',n:10,k:{0:{"p": [20, 0, 30], "s": "move"},1:{"p": [10, 0, 4], "s": "fight", "l": "破砕作業"},2:{"p": [8, 0, 0], "s": "fight"},3:{"p": [10, 0, 10], "s": "fight", "l": "大気圏で砲撃"},4:{"p": [20, -40, 20], "s": "move", "l": "地球に降下"}}},
 {name:'ジュール隊',cmd:'イザーク・ジュール',side:'A',n:8,k:{0:{"p": [-20, 0, 30], "s": "move"},1:{"p": [-6, 0, 6], "s": "fight", "l": "破砕作業"},2:{"p": [-4, 0, 4], "s": "fight"},3:{"p": [-10, 0, 30], "s": "withdraw"},4:{"s": "gone"}}}
];
const PH=[
 {"time": "C.E.73年10月3日", "clock": "DESTINY第3話（推定）", "step": "落下", "title": "ユニウスセブン動く", "text": "旧ザフト兵が、ユニウスセブンの残骸を地球へ落とそうとした。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "破砕", "title": "破砕作業", "text": "ザフトは破砕作業に向かい、テロリストと戦った。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "DESTINY第4話（推定）", "step": "交戦", "title": "破砕作業中の戦い", "text": "連合のファントムペインも介入して混戦となる。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "突入", "title": "大気圏突入", "text": "ミネルバは大気圏に入りながら砲撃し、残骸を砕いた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "DESTINY第5話（推定）", "step": "落着", "title": "破片の落下", "text": "砕ききれない破片が地球各地に落ち、大きな被害が出た。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "ブレイク・ザ・ワールドの結果", "when": "C.E.73年10月3日、地球軌道", "prev": "アーモリーワン事件（10月2日）", "next": "開戦（連合のプラント攻撃）", "factors": ["残骸が大きく、破砕しきれなかった。"], "winner": "none", "outcome": "落下阻止に一部失敗", "summary": "ユニウスセブン残骸の地球落下事件。第二次連合・プラント大戦の引き金になった。", "sides": [{"name": "旧ザフト兵", "side": "E", "cmdr": "サトー", "flag": "不明", "others": "—", "before": "不明", "loss": "全滅", "rate": null, "deaths": "不明", "dead": []}, {"name": "ザフト", "side": "A", "cmdr": "不明", "flag": "不明", "others": "ミネルバ、ジュール隊", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["連合はプラントを非難し、再び開戦する。"], "note": "日付はfandom年表による。この戦いはザフト正規軍を右側（A枠）に置いた。話数は推定。"};
"""
