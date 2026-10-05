from common import *
UC=2030.1
ARC='1st GIG'
OUT='raid.html'
TITLE='9課強制捜査 3D俯瞰'
HEAD='強制捜査'
ERA='2030年（推定）'
SE='政府側の特殊部隊'; SA='公安9課'; PALE='zeon'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=1,sky='0x5a6878')+specials(labels([('9課本部', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"強制捜査部隊",cmd:"政府（推定）",side:'E',n:20,k:{0:{p:[-30,7,-30],s:'ready',l:"9課解体を決定"},1:{p:[-10,7,-10],s:'charge',l:"本部を急襲"},2:{p:[0,7,-6],s:'fight',l:"少佐を追い詰める"},3:{p:[-20,7,-20],s:'withdraw'}}},
{name:"公安9課",cmd:"荒巻大輔",side:'A',n:6,k:{0:{p:[10,7,10],s:'ready'},1:{p:[4,7,4],s:'fight',l:"散開して抗戦"},2:{p:[2,7,2],s:'broken',l:"少佐とバトーが孤立"},3:{p:[10,7,10],s:'ready',l:"再結成"}}}
];
const PH=[
{time:"2030年",clock:"1st GIG第23話",step:"解体",title:"9課の解体",text:"笑い男事件の真相に近づいた9課に、解体と強制捜査が下された。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第24話",step:"急襲",title:"本部への強襲",text:"武装部隊が9課を襲い、メンバーは散り散りになった。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第25話",step:"孤立",title:"少佐の最期？",text:"少佐は追い詰められ、死んだと報じられた。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"1st GIG第26話",step:"再結成",title:"9課の再生",text:"実は生き延びたメンバーが再び集まり、事件の裏の不正が明らかになった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "9課強制捜査の結果", "when": "2030年、新浜市", "prev": "笑い男の再来", "next": "中国大使館占拠", "factors": ["9課は解体を装って生き延びた。"], "winner": "A", "outcome": "9課は偽装解体のうえ再結成", "summary": "強制捜査を逃れた9課は、不正を暴いて復活した。", "sides": [{"name": "強制捜査部隊", "side": "E", "cmdr": "不明", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "公安9課", "side": "A", "cmdr": "荒巻大輔", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["タチコマが身を挺してバトーを守った。"], "note": "1st GIG第23〜26話を確認。兵数は不明。"};
"""
