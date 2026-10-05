from common import *
UC=1942.06
ARC='漂流'
OUT='midway.html'
TITLE='ミッドウェー沖 3D俯瞰'
HEAD='ミッドウェー沖'
ERA='1942年6月'
SE='米海軍'; SA='みらい'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作・アニメにもとづく概略で、位置関係は推定'
ENV=land_env('0x1d3a52','0x2a4a62',water='0x1e4a6e',amp=1,seed=3,sky='0x7a8ea4')+specials(labels([('ミッドウェー北西海域','1942年6月','A',(0,16,0),3)]))
DATA=r"""
const U=[
{name:'第一航空艦隊',cmd:'南雲忠一',side:'E',n:20,k:{0:{p:[-40,7,-30],s:'fight',l:'史実どおり空母を失う',nf:1},1:{p:[-40,7,-30],s:'broken',nf:1},2:{s:'gone'},3:{s:'gone'}}},
{name:'米潜水艦',cmd:'不明',side:'E',n:3,k:{0:{s:'hidden'},1:{p:[0,7,-14],s:'move'},2:{p:[0,7,-12],s:'fight',l:'みらいを雷撃'},3:{p:[0,7,-20],s:'withdraw'}}},
{name:'みらい',cmd:'梅津三郎',side:'A',n:6,k:{0:{p:[10,7,20],s:'wait',l:'タイムスリップ',nf:1},1:{p:[6,7,10],s:'move',l:'草加を救助',nf:1},2:{p:[4,7,8],s:'fight',l:'魚雷を回避',nf:1},3:{p:[10,7,30],s:'withdraw',nf:1}}}
];
const PH=[
{time:'1942年6月',clock:'アニメ第2話',step:'漂着',title:'1942年への漂流',text:'演習中のイージス艦みらいが嵐を抜けると、ミッドウェー海戦の当日の海にいた。',cam:{fit:1,th:.5,ph:.9},arrows:[]},
{time:'',clock:'アニメ第3話',step:'救助',title:'草加を救う',text:'副長の角松は、墜落した水上機の海軍少佐・草加拓海を救助した。本来は死ぬはずの人物だった。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
{time:'',clock:'アニメ第4話',step:'雷撃',title:'米潜水艦の攻撃',text:'米潜水艦の雷撃を受けたが、みらいは撃沈せずに回避した。歴史に手を出さない方針を守った。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[0,7,-12],[4,7,8]],c:'E'}]},
{time:'',clock:'アニメ第5話',step:'離脱',title:'海戦から離れる',text:'みらいは戦いに加わらず海域を離れた。草加は未来の歴史を知り、独自に動き始める。',cam:{fit:1,th:.6,ph:1.0},arrows:[{p:[[4,7,8],[10,7,30]],c:'A'}]}
];
const RESULT={title:'ミッドウェー沖の結果',when:'1942年6月、ミッドウェー北西海域',prev:'—',next:'ガダルカナル（サジタリウス作戦）',
 factors:['みらいは歴史を変えないため、海戦に加わらなかった。','米潜水艦の攻撃は回避だけで切り抜けた。'],winner:'none',outcome:'決着なし（みらいは離脱）',
 summary:'みらいは1942年に漂着した。介入はしなかったが、草加を救ったことで歴史がずれ始める。',
 sides:[{name:'米海軍',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'なし',rate:null,deaths:'なし',dead:[]},
        {name:'みらい',side:'A',cmdr:'梅津三郎 艦長',flag:'みらい',others:'角松洋介 副長',before:'1隻',loss:'なし',rate:null,deaths:'なし',dead:[]}],
 after:['草加拓海が生き延び、未来の知識を得る。','みらいの存在が帝国海軍に知られる。'],
 note:'展開はアニメ第1〜5話の各話あらすじ（英語版Wikipedia「List of Zipang episodes」）に拠る。漫画の巻数は推定。'};
"""
