from common import *
UC=968.0
ARC='共和国の黄昏'
OUT='naboo.html'
TITLE='ナブーの戦い 3D俯瞰'
HEAD='ナブー'
ERA='32 BBY（ヤヴィンの戦いの32年前）'
SE='通商連合'; SA='ナブー・グンガン'; PALE='serpent'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x3d5a3a','0x8a8268',amp=4,seed=3,sky='0x7a9ab8')+specials(labels([('大草原','グンガン軍とドロイド軍の陸戦','A',(0, 24, 0),3.4)]))
DATA=r"""
const U=[
 {name:'ドロイド軍',cmd:'通商連合',side:'E',n:50,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'バトル・ドロイド'},1:{p:[0,7,-10],s:'charge',l:'草原へ前進'},2:{p:[0,7,0],s:'fight',b:1},3:{p:[0,7,-4],s:'broken',l:'司令船を失い停止'}}},
 {name:'グンガン軍',cmd:'ボス・ナス',side:'A',n:30,k:{0:{p:[0,7,30],s:'ready',f:'line',l:'シールドで布陣'},1:{p:[0,7,16],s:'fight',l:'陽動'},2:{p:[0,7,14],s:'broken',l:'劣勢'},3:{p:[0,7,14],s:'ready',l:'生き残る'}}},
 {name:'ナブー戦闘機隊',cmd:'ナブー王室保安軍',side:'A',n:8,k:{0:{p:[20,7,30],s:'wait'},1:{p:[20,7,0],s:'move',l:'宇宙へ発進'},2:{p:[20,7,-30],s:'fight',l:'司令船を攻撃'},3:{p:[20,7,-40],s:'ready',l:'司令船を撃破'}}},
 {name:'アミダラ女王',cmd:'パドメ・アミダラ',side:'A',n:4,k:{0:{p:[-20,7,20],s:'wait'},1:{p:[-20,7,0],s:'move',l:'宮殿へ潜入'},2:{p:[-20,7,-16],s:'fight',l:'総督を捕らえる'},3:{p:[-20,7,-16],s:'ready'}}}
];
const PH=[
 {time:'32 BBY',clock:'エピソード1',step:'布陣',title:'二つの陽動',text:'女王アミダラはグンガンに助けを求めた。グンガン軍が草原でドロイド軍を引きつけ、その間に女王が宮殿へ潜入する作戦をとった。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'陸戦',title:'草原の戦い',text:'ドロイド軍はシールドを突破し、グンガン軍は押されていった。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,-30],[0,7,0]],c:'E'}]},
 {time:'',clock:'',step:'宮殿',title:'宮殿と宇宙',text:'女王は宮殿に入り総督を捕らえた。宇宙ではナブーの戦闘機がドロイド司令船を攻撃する。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'決着',title:'司令船の破壊',text:'ドロイドを動かす司令船が破壊され、地上のドロイド軍は一斉に止まった。',cam:{fit:1,th:.5,ph:.9},arrows:[{p:[[20,7,0],[20,7,-40]],c:'A'}]}
];
const RESULT={title:'ナブーの戦いの戦果',when:'32 BBY、惑星ナブー',prev:'—',next:'ジオノーシスの戦い',
 factors:['ドロイド軍が軌道上の司令船に頼っていた。','陽動と潜入、宇宙攻撃を同時に行った。'],winner:'A',outcome:'ナブー・グンガン連合の勝利',
 summary:'通商連合の封鎖は終わり、ナブーは解放された。',
 sides:[{name:'通商連合',side:'E',cmdr:'ヌート・ガンレイ総督',flag:'—',others:'ダース・モール',before:'不明',loss:'不明（司令船を失う）',rate:null,deaths:'不明',dead:['ダース・モール（とされた）']},{name:'ナブー・グンガン',side:'A',cmdr:'アミダラ女王',flag:'—',others:'ボス・ナス、クワイ＝ガン・ジン',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['クワイ＝ガン・ジン']}],
 after:['パルパティーンが最高議長に選ばれる。','アナキンがジェダイの訓練を受け始める。'],
 note:'年はWookieepedia（https://starwars.fandom.com/wiki/Battle_of_Naboo）でクローン戦争開戦の10年前＝32 BBYと確認。兵力・損害の数値は確認できず「不明」とした。モールはのちの作品で生存が描かれる。'};
"""
