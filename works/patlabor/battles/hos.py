from common import *
UC=1999.08
ARC='劇場版第1作'
OUT='hos.html'
TITLE='HOS事件 3D俯瞰'
HEAD='方舟'
ERA='1999年8月'
SE='帆場暎一（故人）のウイルス'; SA='特車二課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=15,sky='0x5a6878')+specials(labels([('方舟', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"HOS搭載レイバー",cmd:"帆場暎一（故人）",side:'E',n:30,k:{0:{p:[-30,7,-20],s:'ready',l:"暴走が相次ぐ"},1:{p:[-20,7,-10],s:'move',l:"原因がHOSと分かる"},2:{p:[0,7,-4],s:'fight',l:"方舟が共振で暴走"},3:{p:[0,7,-4],s:'gone',l:"方舟解体"}}},
{name:"第2小隊",cmd:"後藤喜一",side:'A',n:6,k:{0:{p:[10,7,30],s:'wait',l:"原因調査"},1:{p:[10,7,20],s:'move',l:"帆場の足跡を追う"},2:{p:[4,7,6],s:'charge',l:"方舟に突入"},3:{p:[4,7,6],s:'ready',l:"停止"}}}
];
const PH=[
{time:"1999年8月",clock:"劇場版",step:"暴走",title:"レイバーの暴走",text:"東京各地で作業用レイバーの暴走が続いた。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"劇場版",step:"調査",title:"HOSの罠",text:"新しい制御ソフトHOSに、自殺した開発者が仕掛けを残していたと分かった。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"劇場版",step:"突入",title:"方舟へ",text:"台風の強風で一斉暴走が起きる前に、二課は巨大作業拠点「方舟」の解体に向かった。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"劇場版",step:"解体",title:"方舟の最期",text:"方舟は解体され、首都圏の一斉暴走は防がれた。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "HOS事件の結果", "when": "1999年8月、東京湾の方舟ほか", "prev": "二課の一番長い日", "next": "グリフォン事件", "factors": ["犯人はすでに死んでおり、仕掛けを止めるしかなかった。", "強風で起きる共振が引き金だった。"], "winner": "A", "outcome": "方舟解体・一斉暴走を阻止", "summary": "二課は方舟を壊して、HOSによる一斉暴走を防いだ。", "sides": [{"name": "HOS（帆場の仕掛け）", "side": "E", "cmdr": "帆場暎一（故人）", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "第2小隊", "side": "A", "cmdr": "後藤喜一", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["HOSは回収される。"], "note": "劇場版第1作（1989）。作中年1999年は英語版Wikipedia（https://en.wikipedia.org/wiki/Patlabor:_The_Movie）で確認。月は記憶にもとづく推定。"};
"""
