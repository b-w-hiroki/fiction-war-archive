from common import *
UC=2032.12
ARC='2nd GIG'
OUT='dejima.html'
TITLE='出島の難民蜂起 3D俯瞰'
HEAD='出島'
ERA='2032年（推定）'
SE='出島の難民・クゼ'; SA='公安9課'; PALE='zeon'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=46,sky='0x5a6878')+specials(labels([('出島', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"出島の難民",cmd:"クゼ・ヒデオ",side:'E',n:30,k:{0:{p:[-10,7,-10],s:'ready',l:"出島に籠る"},1:{p:[-10,7,-10],s:'fight',l:"独立を宣言"},2:{p:[-6,7,-6],s:'fight',l:"自衛隊と交戦"},3:{p:[-6,7,-6],s:'broken',l:"クゼ確保"}}},
{name:"公安9課",cmd:"荒巻大輔",side:'A',n:6,k:{0:{p:[20,7,20],s:'move',l:"クゼを追う"},1:{p:[10,7,10],s:'move',l:"核攻撃の計画を探る"},2:{p:[4,7,4],s:'charge',l:"出島に潜入"},3:{p:[4,7,4],s:'ready',l:"核攻撃を阻止"}}},
{name:"自衛隊",cmd:"合田一人（工作）",side:'E',n:20,k:{0:{p:[-30,7,30],s:'wait'},1:{p:[-30,7,24],s:'ready',l:"包囲"},2:{p:[-14,7,10],s:'charge',l:"攻撃"},3:{p:[-20,7,20],s:'withdraw'}}}
];
const PH=[
{time:"2032年",clock:"2nd GIG第19話〜",step:"籠城",title:"出島の独立",text:"出島の難民がクゼを中心に独立を掲げた。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第20話〜",step:"包囲",title:"核の脅威",text:"政府内の一派は、出島を核で処理しようとした。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第24〜25話",step:"潜入",title:"9課の潜入",text:"9課は出島に入ってクゼを確保し、核ミサイルを止めた。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第26話",step:"終結",title:"合田の逮捕",text:"合田は捕まり、難民の暴発は避けられた。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "出島の難民蜂起の結果", "when": "2032年（推定）、出島", "prev": "個別の11人の決起", "next": "—", "factors": ["合田の工作が難民と政府を衝突させた。", "9課と首相が核攻撃を阻んだ。"], "winner": "A", "outcome": "核攻撃阻止・クゼ確保", "summary": "9課は核攻撃を防ぎ、難民蜂起は大規模な虐殺なしに終わった。", "sides": [{"name": "出島の難民", "side": "E", "cmdr": "クゼ・ヒデオ", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "公安9課", "side": "A", "cmdr": "荒巻大輔", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["タチコマが衛星ごと身を捧げてミサイルを防いだ。"], "note": "2nd GIG第19〜26話（通算45〜52話）を英語版Wikipediaで確認。年は推定。"};
"""
