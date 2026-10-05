from common import *
UC=1943.03
ARC='北と南'
OUT='dampier.html'
TITLE='ダンピール海峡 3D俯瞰'
HEAD='ダンピール海峡'
ERA='1943年3月（推定）'
SE='米陸軍航空隊'; SA='帝国海軍・みらい'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略で、位置関係・兵力は推定'
ENV=land_env('0x1d3a52','0x2a4a62',water='0x1e4a6e',amp=1,seed=7,sky='0x7a8ea4')+specials(labels([('ダンピール海峡','ニューギニア沖','E',(0,16,-40),3)]))
DATA=r"""
const U=[
{name:'米陸軍航空隊',cmd:'不明',side:'E',n:20,k:{0:{p:[0,12,-50],s:'move'},1:{p:[0,12,-10],s:'charge',l:'輸送船団を狙う'},2:{p:[0,12,-20],s:'broken'},3:{p:[0,12,-60],s:'withdraw'}}},
{name:'輸送船団',cmd:'不明',side:'A',n:12,k:{0:{p:[-10,7,10],s:'move',nf:1},1:{p:[-10,7,10],s:'move',nf:1},2:{p:[-10,7,0],s:'move',nf:1},3:{p:[-10,7,-20],s:'move',nf:1,l:'航行を続ける'}}},
{name:'海鳥（みらい艦載機）',cmd:'佐竹',side:'A',n:3,k:{0:{p:[10,12,20],s:'move'},1:{p:[6,12,0],s:'fight',l:'迎撃'},2:{p:[4,12,-10],s:'fight'},3:{p:[10,12,20],s:'withdraw'}}},
{name:'みらい',cmd:'梅津三郎',side:'A',n:6,k:{0:{p:[20,7,30],s:'move'},1:{p:[20,7,30],s:'fight'},2:{p:[20,7,30],s:'fight'},3:{p:[20,7,30],s:'wait',nf:1}}}
];
const PH=[
{time:'1943年3月（推定）',clock:'',step:'護衛',title:'船団の護衛',text:'帝国海軍の輸送船団が海峡を進んだ。史実ではここで船団が空襲で全滅する。',cam:{fit:1,th:.5,ph:.9},arrows:[]},
{time:'',clock:'',step:'空襲',title:'米軍機の来襲',text:'米陸軍航空隊が船団を襲った。みらいの艦載機「海鳥」が迎え撃つ。',cam:{fit:1,th:.8,ph:.8},arrows:[{p:[[0,12,-50],[0,12,-10]],c:'E'}]},
{time:'',clock:'',step:'迎撃',title:'迎撃の成功',text:'海鳥とみらいの対空戦闘で、攻撃はそらされた。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'通過',title:'船団の通過',text:'船団は航行を続けた。史実とは違う結果になった。',cam:{fit:1,th:.6,ph:1.0},arrows:[]}
];
const RESULT={title:'ダンピール海峡の結果',when:'1943年（月は推定）、ダンピール海峡',prev:'空母ワスプ撃沈',next:'キスカ撤退',
 factors:['1943年にはない垂直離着陸機「海鳥」が迎撃に使われた。'],winner:'A',outcome:'帝国海軍・みらいの迎撃成功',
 summary:'史実では全滅した輸送船団を、みらいと艦載機海鳥が守った。細部は資料で確認できていない。',
 sides:[{name:'米陸軍航空隊',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'帝国海軍・みらい',side:'A',cmdr:'不明',flag:'みらい',others:'海鳥',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['みらいは帝国海軍と協力しながら行動する場面が増える。'],
 note:'「海鳥」による迎撃成功はネタバレ解説サイト（k-diary24.com）に拠る。年月は史実のビスマルク海海戦（1943年3月）からの推定。漫画の巻数・作中の兵力は未確認。アニメ化されていない。'};
"""
