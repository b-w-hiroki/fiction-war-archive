from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=70.05
ARC='開戦'
OUT='endymion.html'
TITLE='エンデュミオン・クレーター 3D俯瞰'
HEAD='エンデュミオン・クレーター'
ERA='C.E.70年（月日不明）'
SE='ザフト'; SA='地球連合軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。月面。回想描写にもとづく概略（推定）'
ENV=space_env()+planet((0,-220,0),180,color='0x8a8a8a',land='0x6a6a6a',label=('月','グリマルディ戦線','A'))+specials(labels([('エンデュミオン基地','連合の月面基地','A',(0,10,30),3)]))
DATA=r"""
const U=[
 {name:'ザフト月面部隊',cmd:'ザフト',side:'E',n:30,k:{0:{"p": [0, 0, -40], "s": "move", "f": "wedge"},1:{"p": [0, 0, -10], "s": "charge", "b": 1},2:{"p": [0, 0, 10], "s": "fight", "l": "基地に迫る"},3:{"p": [0, 0, 20], "s": "broken", "l": "サイクロプスに巻き込まれる"},4:{"s": "gone"}}},
 {name:'連合月面部隊',cmd:'地球連合軍',side:'A',n:24,k:{0:{"p": [0, 0, 30], "s": "ready", "f": "line"},1:{"p": [0, 0, 20], "s": "fight"},2:{"p": [0, 0, 24], "s": "broken", "l": "押される"},3:{"p": [0, 0, 30], "s": "broken", "l": "味方ごと自爆"},4:{"p": [0, 0, 40], "s": "withdraw"}}},
 {name:'ムウ機',cmd:'ムウ・ラ・フラガ',side:'A',n:2,k:{0:{"p": [14, 0, 26], "s": "ready"},1:{"p": [14, 0, 6], "s": "fight"},2:{"p": [16, 0, 0], "s": "fight", "l": "MA部隊で奮戦"},3:{"p": [20, 0, 30], "s": "withdraw", "l": "脱出"},4:{"p": [20, 0, 40], "s": "ready", "l": "エンデュミオンの鷹"}}}
];
const PH=[
 {"time": "C.E.70年", "clock": "TV版回想", "step": "進攻", "title": "ザフトの月面進攻", "text": "グリマルディ戦線で、ザフトは連合の月面基地エンデュミオンに迫った。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 0, -40], [0, 0, -10]], "c": "E"}]},
 {"time": "同", "clock": "", "step": "攻防", "title": "MAとMSの戦い", "text": "連合のMA部隊は性能で勝るMSに苦戦した。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "劣勢", "title": "基地の劣勢", "text": "連合は基地を守り切れなくなる。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "自爆", "title": "サイクロプス作動", "text": "連合は基地のマイクロ波施設（サイクロプス）を作動させ、敵味方ごと吹き飛ばした。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "その後", "clock": "", "step": "名声", "title": "鷹の名", "text": "生還したムウ・ラ・フラガは「エンデュミオンの鷹」と呼ばれた。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "エンデュミオン・クレーターの戦いの結果", "when": "C.E.70年、月面グリマルディ戦線", "prev": "グリマルディ戦線開始（5月3日）", "next": "ヘリオポリス崩壊", "factors": ["MSの性能差で連合は劣勢だった。", "連合はサイクロプスによる自爆を選んだ。"], "winner": "none", "outcome": "双方大損害", "summary": "連合が基地ごとザフト部隊を吹き飛ばした月面の戦い。", "sides": [{"name": "ザフト", "side": "E", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連合軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "ムウ・ラ・フラガ", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["ムウ・ラ・フラガの名が知られる。", "アラスカでのサイクロプス使用の前例となる。"], "note": "月日は確認できず不明。戦線の開始日（C.E.70年5月3日）はfandom年表による。展開はTV版の回想にもとづく（推定）。"};
"""
