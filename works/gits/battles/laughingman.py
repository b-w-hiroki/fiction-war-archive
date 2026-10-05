from common import *
UC=2030.03
ARC='1st GIG'
OUT='laughingman.html'
TITLE='笑い男の再来 3D俯瞰'
HEAD='笑い男'
ERA='2030年（推定で春）'
SE='笑い男'; SA='公安9課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=25,sky='0x5a6878')+specials(labels([('厚生労働省', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"笑い男",cmd:"正体不明のハッカー",side:'E',n:2,k:{0:{p:[-20,7,-20],s:'hidden'},1:{p:[-6,7,-6],s:'fight',l:"視覚をハックして現れる"},2:{p:[-20,7,-20],s:'withdraw',l:"姿を消す"},3:{p:[-20,7,-20],s:'gone'}}},
{name:"公安9課",cmd:"荒巻大輔",side:'A',n:8,k:{0:{p:[20,7,20],s:'move',l:"捜査"},1:{p:[8,7,6],s:'fight',l:"会場で対峙"},2:{p:[10,7,10],s:'move',l:"背後を追う"},3:{p:[10,7,10],s:'ready',l:"薬害の疑いをつかむ"}}}
];
const PH=[
{time:"2030年",clock:"1st GIG第4話",step:"再来",title:"笑い男の再来",text:"6年前の企業テロ「笑い男事件」の再来を思わせる予告が出た。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第4〜5話",step:"対峙",title:"会場での遭遇",text:"笑い男は周りの人の視覚をハックし、顔を隠して現れた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第9・11話",step:"追跡",title:"模倣犯と噂",text:"模倣犯や噂が増え、本物の姿はかえって見えなくなった。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第20〜22話",step:"核心",title:"薬害の影",text:"事件の裏に、電脳硬化症の治療をめぐる不正があると分かった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "笑い男の再来の結果", "when": "2030年、新浜市ほか", "prev": "—", "next": "9課強制捜査", "factors": ["笑い男は視覚ハックで正体を隠した。", "模倣犯が「オリジナルなき模倣」を生んだ。"], "winner": "none", "outcome": "正体追跡は続く", "summary": "9課は笑い男を追ううちに、企業と官僚の不正に近づいた。", "sides": [{"name": "笑い男", "side": "E", "cmdr": "不明", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "公安9課", "side": "A", "cmdr": "荒巻大輔", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["9課が政府に疎まれ始める。"], "note": "英語版Wikipediaのエピソード一覧で関連話数を確認。月は推定。"};
"""
