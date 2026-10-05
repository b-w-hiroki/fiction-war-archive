from common import *
UC=981.0
ARC='クローン戦争'
OUT='coruscant.html'
TITLE='コルサントの戦い 3D俯瞰'
HEAD='コルサント'
ERA='19 BBY（ヤヴィンの戦いの19年前）'
SE='独立星系連合'; SA='銀河共和国'; PALE='serpent'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet((0,-260,0),200,'0x8a7a60','0x5a5040')+specials(labels([('コルサント上空','首都の軌道上の艦隊戦','A',(0, 30, 0),3.4)]))
DATA=r"""
const U=[
 {name:'分離主義艦隊',cmd:'グリーヴァス将軍',side:'E',n:50,k:{0:{p:[0,0,-20],s:'fight',f:'line'},1:{p:[0,0,-16],s:'fight',b:1},2:{p:[0,0,-14],s:'fight'},3:{p:[0,0,-30],s:'withdraw',l:'撤退'}}},
 {name:'旗艦（議長拘束）',cmd:'グリーヴァス将軍',side:'E',n:6,k:{0:{p:[-10,0,-24],s:'ready',l:'議長を拘束'},1:{p:[-10,0,-20],s:'fight'},2:{p:[-10,0,-18],s:'broken',l:'艦が損傷'},3:{p:[-10,0,-10],s:'broken',l:'不時着'}}},
 {name:'共和国艦隊',cmd:'共和国軍',side:'A',n:60,k:{0:{p:[0,0,20],s:'fight',f:'line'},1:{p:[0,0,14],s:'fight',b:1},2:{p:[0,0,10],s:'fight'},3:{p:[0,0,4],s:'ready',l:'首都を守る'}}},
 {name:'ジェダイ',cmd:'オビ＝ワン、アナキン',side:'A',n:3,k:{0:{p:[16,0,20],s:'move',l:'救出に向かう'},1:{p:[-6,0,-20],s:'charge',l:'旗艦に乗り込む'},2:{p:[-10,0,-18],s:'fight',l:'ドゥークーを倒す'},3:{p:[-10,0,-10],s:'ready',l:'議長を救出'}}}
];
const PH=[
 {time:'19 BBY',clock:'エピソード3',step:'奇襲',title:'首都への奇襲',text:'分離主義勢力は首都コルサントを襲い、パルパティーン議長をさらった。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'突入',title:'旗艦への突入',text:'オビ＝ワンとアナキンは艦隊戦の中を抜けて敵旗艦に乗り込んだ。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[16,0,20],[-6,0,-20]],c:'A'}]},
 {time:'',clock:'',step:'決闘',title:'ドゥークーの死',text:'アナキンはドゥークーを倒し、議長の求めに応じてとどめを刺した。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'帰還',title:'旗艦の不時着',text:'グリーヴァスは逃れ、損傷した旗艦はアナキンの操縦で地上に降りた。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'コルサントの戦いの戦果',when:'19 BBY、首都惑星コルサント上空',prev:'ジオノーシスの戦い',next:'スカリフの戦い',
 factors:['救出はパルパティーン自身が仕組んだ筋書きの一部だった。'],winner:'A',outcome:'共和国の勝利（議長救出）',
 summary:'議長は救われたが、それはシスの計画の一歩だった。',
 sides:[{name:'独立星系連合',side:'E',cmdr:'グリーヴァス将軍',flag:'—',others:'ドゥークー伯爵',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['ドゥークー伯爵']},{name:'銀河共和国',side:'A',cmdr:'—',flag:'—',others:'オビ＝ワン、アナキン',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['まもなくジェダイ粛清（オーダー66）が起き、共和国は帝国になる。'],
 note:'年は記憶にもとづく（Wookieepedia年表では未確認）。兵力・損害の数値は確認できず「不明」とした。'};
"""
