from common import *
UC=1998.11
ARC='OVA期'
OUT='ichibancho.html'
TITLE='二課の一番長い日 3D俯瞰'
HEAD='二課の一番長い日'
ERA='1998年ごろ（推定）'
SE='甲斐率いる決起部隊'; SA='特車二課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=45,sky='0x5a6878')+specials(labels([('首都圏', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"決起部隊",cmd:"甲斐冽次郎",side:'E',n:20,k:{0:{p:[-20,7,-30],s:'ready',l:"自衛隊の一部が決起"},1:{p:[-10,7,-15],s:'move',l:"首都の要所を押さえる"},2:{p:[0,7,-6],s:'fight',l:"核ミサイル搭載艦を確保"},3:{p:[0,7,-6],s:'broken',l:"投降"}}},
{name:"第2小隊",cmd:"後藤喜一",side:'A',n:6,k:{0:{p:[0,7,30],s:'wait',l:"待機"},1:{p:[10,7,20],s:'move',l:"出動"},2:{p:[4,7,4],s:'fight',l:"進入して制圧"},3:{p:[4,7,8],s:'ready',l:"鎮圧"}}}
];
const PH=[
{time:"1998年ごろ（推定）",clock:"OVA第5話",step:"決起",title:"自衛隊の決起",text:"自衛隊の一部が首都で決起し、政府に要求を突きつけた。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"OVA第5〜6話",step:"要所制圧",title:"首都の混乱",text:"決起部隊は要所を押さえ、警察は手を出せない状態になった。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"OVA第6話",step:"突入",title:"二課の出動",text:"後藤の判断で第2小隊が動き、首謀者の居場所へ向かった。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"OVA第6話",step:"鎮圧",title:"決起の終わり",text:"首謀者が押さえられ、決起は終わった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "二課の一番長い日の結果", "when": "1998年ごろ（推定）、首都圏", "prev": "—", "next": "HOS事件", "factors": ["政府が対応を決めかね、二課が独自に動いた。"], "winner": "A", "outcome": "決起鎮圧", "summary": "特車二課が首謀者を押さえ、決起は大きな戦闘なしに終わった。", "sides": [{"name": "決起部隊", "side": "E", "cmdr": "甲斐冽次郎", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "第2小隊", "side": "A", "cmdr": "後藤喜一", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["のちの柘植事件の伏線となる。"], "note": "OVA初期シリーズ第5〜6話にもとづく。年と細部は推定。"};
"""
