from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=71.0505
ARC='地球の攻防'
OUT='alaska.html'
TITLE='アラスカ（JOSH-A） 3D俯瞰'
HEAD='アラスカ（JOSH-A）'
ERA='C.E.71年5月5日'
SE='ザフト'; SA='地球連合軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は概略'
ENV=land_env('0x5a6a6a','0xd8dde0',amp=5,seed=4,sky='0x8a98a8')+specials(labels([('JOSH-A','連合総司令部','A',(0,12,30),3.4)]))
DATA=r"""
const U=[
 {name:'ザフト降下部隊',cmd:'スピットブレイク',side:'E',n:60,k:{0:{"p": [0, 30, -60], "s": "move", "l": "パナマと偽装"},1:{"p": [0, 7, -10], "s": "charge", "b": 1},2:{"p": [0, 7, 14], "s": "fight", "l": "基地へ突入"},3:{"p": [0, 7, 20], "s": "broken", "l": "サイクロプスで壊滅"},4:{"p": [0, 7, -40], "s": "withdraw"}}},
 {name:'連合守備隊',cmd:'ユーラシア部隊中心',side:'A',n:30,k:{0:{"p": [0, 7, 30], "s": "ready", "f": "line"},1:{"p": [0, 7, 20], "s": "fight"},2:{"p": [0, 7, 24], "s": "broken", "l": "捨て駒にされる"},3:{"p": [0, 7, 26], "s": "broken"},4:{"s": "gone"}}},
 {name:'アークエンジェル',cmd:'マリュー・ラミアス',side:'A',n:6,k:{0:{"p": [20, 7, 30], "s": "ready"},1:{"p": [20, 7, 18], "s": "fight"},2:{"p": [22, 7, 20], "s": "fight", "l": "真相を知る"},3:{"p": [30, 7, 50], "s": "withdraw", "l": "離脱"},4:{"p": [34, 7, 60], "s": "move", "l": "オーブへ"}}},
 {name:'フリーダム',cmd:'キラ・ヤマト',side:'A',n:2,k:{0:{"p": [-30, 30, -40], "s": "hidden"},1:{"p": [-30, 30, -40], "s": "hidden"},2:{"p": [16, 7, 14], "s": "charge", "l": "救援に現れる"},3:{"p": [28, 7, 46], "s": "withdraw"},4:{"p": [32, 7, 58], "s": "move"}}}
];
const PH=[
 {"time": "C.E.71年5月5日", "clock": "TV版第34話", "step": "降下", "title": "スピットブレイク発動", "text": "ザフトはパナマ攻撃と見せかけ、実際には連合総司令部JOSH-Aに大軍を降ろした。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 30, -60], [0, 7, -10]], "c": "E"}]},
 {"time": "同日", "clock": "", "step": "攻防", "title": "守備隊の抵抗", "text": "基地にはユーラシア系の部隊が残され、主力はすでに去っていた。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "TV版第35話", "step": "救援", "title": "フリーダムの介入", "text": "キラがフリーダムで現れ、アークエンジェルを助けた。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "自爆", "title": "サイクロプス作動", "text": "連合は基地地下のサイクロプスを作動させ、ザフト部隊と味方の守備隊をまとめて焼いた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "", "step": "離脱", "title": "アークエンジェル離脱", "text": "アークエンジェルは連合を離れ、オーブへ向かった。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "アラスカ攻防戦の結果", "when": "C.E.71年5月5日、アラスカ・JOSH-A", "prev": "第二次カサブランカ沖海戦など", "next": "パナマ攻略戦（5月25日）", "factors": ["作戦は事前に連合へ漏れていた。", "連合は基地ごと自爆する罠を用意していた。"], "winner": "A", "outcome": "連合の「勝利」（基地自爆による罠）", "summary": "ザフトの大攻勢を連合が基地の自爆で迎えた戦い。両軍とも大損害を出した。", "sides": [{"name": "ザフト", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "降下部隊の大半（数は不明）", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連合軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "アークエンジェル", "before": "不明", "loss": "基地と守備隊", "rate": null, "deaths": "不明", "dead": []}], "after": ["ザフトの地上戦力が大きく減る。", "アークエンジェルが連合を離れ、第三勢力への道が開く。"], "note": "発動日5月5日はfandom年表による（JOSH-A攻撃日を5月8日とする資料もある）。損害数は不明。話数はPHASE-34「まなざしの先」でスピットブレイク発動、PHASE-35「舞い降りる剣」でフリーダム登場（https://k-rakuraku.com/see1/seed-stt34.html 、https://www.oricon.co.jp/news/2358678/full/ ）。"};
"""
