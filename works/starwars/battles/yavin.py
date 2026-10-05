from common import *
UC=1000.0
ARC='帝国と反乱'
OUT='yavin.html'
TITLE='ヤヴィンの戦い 3D俯瞰'
HEAD='ヤヴィン'
ERA='0 BBY/ABY（暦の基点）'
SE='銀河帝国'; SA='反乱同盟'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet((0,-260,0),200,'0xc87a3a','0x8a5030')+rock_fortress((0,6,-44),14,'solomon','DS1')+specials(labels([('デス・スター','惑星を壊す帝国の宇宙要塞','E',(0, 30, -44),3.4)]))
DATA=r"""
const U=[
 {name:'デス・スター',cmd:'ターキン総督',side:'E',n:40,k:{0:{p:[0,0,-40],s:'ready',l:'ヤヴィン4へ接近'},1:{p:[0,0,-38],s:'fight',b:1},2:{p:[0,0,-36],s:'fight',l:'発射準備'},3:{p:[0,0,-36],s:'gone',l:'爆発'}}},
 {name:'ベイダー隊',cmd:'ダース・ベイダー',side:'E',n:4,k:{0:{p:[-10,0,-30],s:'wait'},1:{p:[-6,0,-20],s:'fight',l:'攻撃隊を撃墜'},2:{p:[-4,0,-22],s:'charge',l:'ルークを追う'},3:{p:[-30,0,-60],s:'withdraw',l:'宇宙へ弾き出される'}}},
 {name:'反乱攻撃隊',cmd:'ルーク・スカイウォーカー',side:'A',n:12,k:{0:{p:[0,0,30],s:'move',f:'wedge',l:'出撃'},1:{p:[0,0,-14],s:'fight',l:'溝を突進'},2:{p:[0,0,-18],s:'broken',l:'損害多数'},3:{p:[0,0,10],s:'ready',l:'排熱口に命中'}}},
 {name:'ハン・ソロ',cmd:'ミレニアム・ファルコン',side:'A',n:2,k:{0:{p:[30,0,40],s:'hidden'},1:{p:[30,0,40],s:'hidden'},2:{p:[10,0,-10],s:'charge',l:'ベイダーを妨害'},3:{p:[10,0,10],s:'ready'}}}
];
const PH=[
 {time:'0 BBY',clock:'エピソード4',step:'接近',title:'デス・スターの接近',text:'デス・スターは反乱同盟の基地があるヤヴィン4に迫った。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'攻撃',title:'溝への突入',text:'反乱同盟の戦闘機は設計図で見つけた弱点の排熱口を狙って溝を進んだ。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,0,30],[0,0,-14]],c:'A'}]},
 {time:'',clock:'',step:'危機',title:'ベイダーの追撃',text:'ベイダーが攻撃隊を次々に落とす。ハン・ソロが戻ってベイダーを退けた。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'撃破',title:'デス・スターの破壊',text:'ルークの一撃が排熱口に入り、デス・スターは爆発した。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'ヤヴィンの戦いの戦果',when:'0 BBY/ABY（年の基点）、ヤヴィン4上空',prev:'スカリフの戦い',next:'ホスの戦い',
 factors:['スカリフで得た設計図で弱点がわかっていた。','帝国は小型機の攻撃を軽く見ていた。'],winner:'A',outcome:'反乱同盟の勝利',
 summary:'デス・スターが破壊され、反乱同盟は初めて大きな勝利を得た。',
 sides:[{name:'銀河帝国',side:'E',cmdr:'ターキン総督',flag:'—',others:'ダース・ベイダー',before:'不明',loss:'デス・スター',rate:null,deaths:'不明',dead:['ターキン総督']},{name:'反乱同盟',side:'A',cmdr:'ドドンナ将軍',flag:'—',others:'ルーク・スカイウォーカー',before:'不明',loss:'不明（攻撃隊の多く）',rate:null,deaths:'不明',dead:[]}],
 after:['この戦いがBBY/ABYの年の数え方の基点になる。'],
 note:'年はWookieepedia（https://starwars.fandom.com/wiki/Battle_of_Yavin）で0 BBYと確認。兵力・損害の数値は確認できず「不明」とした。'};
"""
