from common import *
UC=2002.11
ARC='劇場版第2作'
OUT='baybridge.html'
TITLE='横浜ベイブリッジ爆撃 3D俯瞰'
HEAD='ベイブリッジ'
ERA='2002年冬（推定）'
SE='柘植行人一派'; SA='特車二課'; PALE='serpent'; PAL='efsf'
NOTE='配置は概略。部隊の大きさは規模の目安'
ENV=land_env('0x3a3f48','0x6a6e74',water='0x2a4a6a',amp=2,seed=48,sky='0x5a6878')+specials(labels([('ベイブリッジ', '', 'A', (0, 26, 0), 3)]))
DATA=r"""
const U=[
{name:"正体不明機",cmd:"柘植行人一派",side:'E',n:3,k:{0:{p:[-30,7,-30],s:'move',l:"ミサイル発射"},1:{p:[-10,7,-10],s:'fight',l:"ベイブリッジ破壊"},2:{p:[-30,7,-30],s:'withdraw',l:"姿を消す"},3:{p:[-30,7,-30],s:'gone'}}},
{name:"警察",cmd:"後藤喜一",side:'A',n:8,k:{0:{p:[20,7,30],s:'wait',l:"平常"},1:{p:[20,7,30],s:'wait',l:"騒然"},2:{p:[10,7,20],s:'move',l:"捜査開始"},3:{p:[10,7,20],s:'ready',l:"疑心暗鬼"}}}
];
const PH=[
{time:"2002年",clock:"劇場版2",step:"発射",title:"ミサイル攻撃",text:"横浜ベイブリッジがミサイルで破壊された。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"混乱",title:"自衛隊機の影",text:"自衛隊機の仕業と見える映像が流れ、自衛隊と警察の間に不信が広がった。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"捜査",title:"後藤の捜査",text:"後藤と南雲は元自衛官の柘植行人の存在をつかむ。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:"",clock:"劇場版2",step:"緊張",title:"戒厳の前夜",text:"政府の対応は割れ、首都に緊張が高まった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "ベイブリッジ爆撃の結果", "when": "2002年、横浜", "prev": "グリフォン事件", "next": "幻の戦争", "factors": ["偽の情報で組織どうしを疑わせた。"], "winner": "E", "outcome": "橋の破壊・犯人不明", "summary": "犯人は姿を見せず、首都の機関どうしが疑い合った。", "sides": [{"name": "柘植一派", "side": "E", "cmdr": "柘植行人", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "警察", "side": "A", "cmdr": "後藤喜一", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["自衛隊の出動へつながる。"], "note": "劇場版第2作（1993）。英語版Wikipediaで作中年2002年を確認。月は推定。"};
"""
