from common import *
UC=1999.1
ARC='グリフォン事件'
OUT='griffon.html'
TITLE='グリフォン事件 3D俯瞰'
HEAD='黒いレイバー'
ERA='1999年ごろ（推定）'
SE='シャフト企画7課'; SA='特車二課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=32,sky='0x5a6878')+specials(labels([('東京湾', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"グリフォン",cmd:"内海（シャフト企画7課）",side:'E',n:4,k:{0:{p:[-20,7,-20],s:'move',l:"各地に出没"},1:{p:[-6,7,-6],s:'fight',l:"イングラムと交戦"},2:{p:[0,7,-2],s:'fight',l:"東京湾で決戦"},3:{p:[0,7,-2],s:'broken',l:"捕獲"}}},
{name:"第2小隊",cmd:"後藤喜一",side:'A',n:6,k:{0:{p:[10,7,30],s:'wait'},1:{p:[4,7,6],s:'fight',l:"泉が迎え撃つ"},2:{p:[2,7,4],s:'fight',l:"最終戦"},3:{p:[2,7,4],s:'ready',l:"逮捕"}}}
];
const PH=[
{time:"1999年ごろ（推定）",clock:"漫画・TV",step:"出没",title:"黒いレイバー",text:"高性能の黒いレイバーが現れ、警察や自衛隊のレイバーを次々に倒した。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"",step:"交戦",title:"二課との戦い",text:"泉のイングラムが何度も対決するが、性能差で苦戦した。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"",step:"決戦",title:"東京湾の決戦",text:"二課は黒幕のシャフト企画7課を追い詰め、決戦を挑んだ。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"",step:"逮捕",title:"事件の終わり",text:"グリフォンは止められ、首謀者は捕まった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "グリフォン事件の結果", "when": "1999年ごろ（推定）、東京湾ほか", "prev": "HOS事件", "next": "ベイブリッジ爆撃", "factors": ["企業の違法な兵器開発が背景にあった。"], "winner": "A", "outcome": "グリフォン停止・首謀者逮捕", "summary": "二課は長く続いた黒いレイバー事件を終わらせた。", "sides": [{"name": "シャフト企画7課", "side": "E", "cmdr": "内海", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "第2小隊", "side": "A", "cmdr": "後藤喜一", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["媒体ごとに結末が異なる。"], "note": "漫画とTV版で筋・時期が異なる。年は記憶にもとづく推定。"};
"""
