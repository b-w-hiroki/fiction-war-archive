from common import *
UC=999.9
ARC='帝国と反乱'
OUT='scarif.html'
TITLE='スカリフの戦い 3D俯瞰'
HEAD='スカリフ'
ERA='0 BBY（ヤヴィンの戦いの直前）'
SE='銀河帝国'; SA='反乱同盟'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xd8c890','0x4a8a5a',water='0x2a8ab0',amp=3,seed=11,sky='0x8ab8d8')+specials(labels([('シタデル','帝国のデータ保管塔','E',(0, 30, -30),3.4)]))
DATA=r"""
const U=[
 {name:'帝国守備軍',cmd:'クレニック長官',side:'E',n:40,k:{0:{p:[0,7,-20],s:'ready',l:'シタデル'},1:{p:[0,7,-10],s:'fight',b:1},2:{p:[0,7,-12],s:'fight'},3:{p:[0,7,-20],s:'broken',l:'デス・スターに焼かれる'}}},
 {name:'ローグ・ワン',cmd:'ジン・アーソ',side:'A',n:6,k:{0:{p:[10,7,20],s:'move',l:'潜入'},1:{p:[4,7,-6],s:'fight'},2:{p:[0,7,-24],s:'fight',l:'設計図を送信'},3:{p:[0,7,-24],s:'gone'}}},
 {name:'反乱艦隊',cmd:'ラダス提督',side:'A',n:30,k:{0:{p:[-20,7,40],s:'hidden'},1:{p:[-20,7,30],s:'fight',l:'シールドを破る'},2:{p:[-20,7,30],s:'fight',b:1},3:{p:[-20,7,50],s:'withdraw',l:'設計図を持ち出す'}}}
];
const PH=[
 {time:'0 BBY',clock:'ローグ・ワン',step:'潜入',title:'少数での潜入',text:'ジンたちは許可なくスカリフに降り、デス・スターの設計図を盗もうとした。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'増援',title:'艦隊の到着',text:'反乱同盟の艦隊が後から加わり、惑星を覆うシールドを破った。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'送信',title:'設計図の送信',text:'ジンは塔の頂上から設計図を艦隊へ送った。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'終局',title:'デス・スターの砲撃',text:'帝国はデス・スターで基地ごと焼き払った。設計図はレイアの船に渡った。',cam:{fit:1,th:.5,ph:.9},arrows:[{p:[[-20,7,30],[-20,7,50]],c:'A'}]}
];
const RESULT={title:'スカリフの戦いの戦果',when:'0 BBY、惑星スカリフ',prev:'コルサントの戦い',next:'ヤヴィンの戦い',
 factors:['シールドの破壊で地上から艦隊へ送信できた。'],winner:'A',outcome:'反乱同盟の戦略的勝利（地上部隊は全滅）',
 summary:'反乱同盟は多くを失ったが、デス・スターの設計図を手に入れた。',
 sides:[{name:'銀河帝国',side:'E',cmdr:'クレニック長官',flag:'—',others:'ターキン総督',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['クレニック長官']},{name:'反乱同盟',side:'A',cmdr:'ラダス提督',flag:'—',others:'ジン・アーソ',before:'不明',loss:'不明（地上部隊全滅）',rate:null,deaths:'不明',dead:['ジン・アーソ','キャシアン・アンドー','ラダス提督']}],
 after:['設計図がヤヴィンの戦いの勝利につながる。'],
 note:'年は記憶にもとづく（Wookieepedia年表では未確認）。兵力・損害の数値は確認できず「不明」とした。'};
"""
