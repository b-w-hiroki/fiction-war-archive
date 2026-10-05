from common import *
UC=2032.01
ARC='2nd GIG'
OUT='embassy.html'
TITLE='中国大使館占拠 3D俯瞰'
HEAD='再起動'
ERA='2032年（推定）'
SE='個別の11人を名乗る集団'; SA='公安9課'; PALE='zeon'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=10,sky='0x5a6878')+specials(labels([('大使館', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"占拠グループ",cmd:"個別の11人を名乗る",side:'E',n:8,k:{0:{p:[-6,7,-6],s:'ready',l:"大使館を占拠"},1:{p:[-6,7,-6],s:'fight',l:"人質を取る"},2:{p:[-4,7,-4],s:'broken',l:"制圧される"},3:{p:[-4,7,-4],s:'gone'}}},
{name:"公安9課",cmd:"荒巻大輔",side:'A',n:6,k:{0:{p:[20,7,20],s:'wait',l:"出動許可を待つ"},1:{p:[14,7,14],s:'move',l:"新首相が許可"},2:{p:[4,7,4],s:'charge',l:"突入"},3:{p:[4,7,4],s:'ready',l:"解決"}}}
];
const PH=[
{time:"2032年",clock:"2nd GIG第1話",step:"占拠",title:"大使館の占拠",text:"武装集団が大使館を占拠し、自らを個別の11人と名乗った。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第1話",step:"許可",title:"9課の再起動",text:"新首相茅葺が9課の出動を認めた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第1話",step:"突入",title:"突入と制圧",text:"9課は突入して犯人を制圧した。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"2nd GIG第1話",step:"余波",title:"名前の謎",text:"「個別の11人」という名の正体が新たな謎として残った。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "中国大使館占拠の結果", "when": "2032年（推定）、新浜市", "prev": "9課強制捜査", "next": "個別の11人の決起", "factors": ["9課が首相直属として再出発した。"], "winner": "A", "outcome": "犯人制圧", "summary": "9課は再起動直後の事件を解決した。", "sides": [{"name": "占拠グループ", "side": "E", "cmdr": "不明", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "公安9課", "side": "A", "cmdr": "荒巻大輔", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["難民問題が物語の軸になる。"], "note": "2nd GIG第1話（通算27話）を確認。年は推定。"};
"""
