from common import *
UC=2032.06
ARC='2nd GIG'
OUT='eleven.html'
TITLE='個別の11人の決起 3D俯瞰'
HEAD='個別の11人'
ERA='2032年（推定）'
SE='個別の11人'; SA='公安9課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=49,sky='0x5a6878')+specials(labels([('厳島', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"個別の11人",cmd:"クゼ・ヒデオ",side:'E',n:11,k:{0:{p:[-20,7,-20],s:'ready',l:"ウイルスに感染した11人"},1:{p:[-10,7,-10],s:'fight',l:"難民を標的にテロ"},2:{p:[-6,7,-6],s:'fight',l:"厳島で決起"},3:{p:[-10,7,-10],s:'gone',l:"自決（クゼ以外）"}}},
{name:"公安9課",cmd:"荒巻大輔",side:'A',n:6,k:{0:{p:[20,7,20],s:'move',l:"捜査"},1:{p:[10,7,10],s:'move',l:"追跡"},2:{p:[4,7,4],s:'charge',l:"現場へ"},3:{p:[4,7,4],s:'ready',l:"クゼを追う"}}}
];
const PH=[
{time:"2032年",clock:"2nd GIG（話数推定）",step:"感染",title:"個別の11人ウイルス",text:"論文を読ませるウイルスで、思想を植え付けられた者たちが現れた。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG（話数推定）",step:"テロ",title:"難民へのテロ",text:"個別の11人は難民を標的にした行動を起こした。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG（話数推定）",step:"決起",title:"厳島",text:"11人は厳島で決起し、9課が追った。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG（話数推定）",step:"結末",title:"クゼの離反",text:"クゼ以外は自決し、クゼは難民の側に去った。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "個別の11人の決起の結果", "when": "2032年（推定）、厳島ほか", "prev": "中国大使館占拠", "next": "出島の難民蜂起", "factors": ["合田一人がウイルスで11人を作り出していた。"], "winner": "none", "outcome": "クゼが難民側へ", "summary": "事件の裏に内閣情報庁の合田の工作があった。", "sides": [{"name": "個別の11人", "side": "E", "cmdr": "クゼ・ヒデオ", "flag": "—", "others": "—", "before": "11人", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "公安9課", "side": "A", "cmdr": "荒巻大輔", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["クゼが出島の難民を率いる。"], "note": "2nd GIG中盤。話数・年は推定。"};
"""
