from common import *
UC=2002.12
ARC='劇場版第2作'
OUT='phantomwar.html'
TITLE='幻の戦争 3D俯瞰'
HEAD='幻の戦争'
ERA='2002年冬（推定）'
SE='柘植行人一派'; SA='特車二課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=34,sky='0x5a6878')+specials(labels([('東京', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"柘植一派",cmd:"柘植行人",side:'E',n:8,k:{0:{p:[-30,7,-30],s:'ready',l:"首都を攻撃"},1:{p:[-10,7,-10],s:'fight',l:"橋・通信を破壊"},2:{p:[-6,7,-6],s:'wait',l:"埋立地に潜む"},3:{p:[0,7,-2],s:'broken',l:"柘植逮捕"}}},
{name:"特車二課（旧第2小隊）",cmd:"南雲しのぶ",side:'A',n:6,k:{0:{p:[20,7,30],s:'wait'},1:{p:[20,7,20],s:'broken',l:"二課も攻撃される"},2:{p:[10,7,10],s:'move',l:"地下から進撃"},3:{p:[4,7,2],s:'charge',l:"突入"}}}
];
const PH=[
{time:"2002年",clock:"劇場版2",step:"攻撃",title:"首都への攻撃",text:"戦闘ヘリが東京の橋や通信施設、特車二課を攻撃した。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"麻痺",title:"都市の麻痺",text:"通信を断たれ、首都は戦時のような状態に置かれた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"反撃",title:"旧第2小隊の集結",text:"南雲と旧第2小隊は独自に動き、柘植の潜む埋立地へ向かった。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"逮捕",title:"柘植の逮捕",text:"防御を突破した一行は柘植を逮捕し、事件は終わった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "幻の戦争の結果", "when": "2002年、東京", "prev": "ベイブリッジ爆撃", "next": "—", "factors": ["警察と自衛隊が互いを疑い、対応が遅れた。", "旧第2小隊は命令外の行動で動いた。"], "winner": "A", "outcome": "柘植逮捕", "summary": "二課の独自行動で首謀者が捕まり、首都の混乱は終わった。", "sides": [{"name": "柘植一派", "side": "E", "cmdr": "柘植行人", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "特車二課", "side": "A", "cmdr": "南雲しのぶ", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["後藤らの責任が問われる。"], "note": "劇場版第2作にもとづく。人数・損害は不明。"};
"""
