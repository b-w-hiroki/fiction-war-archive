from common import *
UC=1004.0
ARC='帝国と反乱'
OUT='endor.html'
TITLE='エンドアの戦い 3D俯瞰'
HEAD='エンドア'
ERA='4 ABY（ヤヴィンの戦いの4年後）'
SE='銀河帝国'; SA='反乱同盟'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet((0,-260,0),200,'0x2a6a3a','0x4a8a4a')+rock_fortress((0,6,-44),14,'solomon','DS2')+specials(labels([('第2デス・スター','建造中の宇宙要塞','E',(0, 30, -44),3.4)]))
DATA=r"""
const U=[
 {name:'帝国艦隊',cmd:'皇帝パルパティーン',side:'E',n:60,k:{0:{p:[0,0,-20],s:'ready',f:'line',l:'罠を張る'},1:{p:[0,0,-10],s:'fight',b:1},2:{p:[0,0,-8],s:'fight'},3:{p:[0,0,-30],s:'broken',l:'旗艦を失う'}}},
 {name:'反乱艦隊',cmd:'アクバー提督',side:'A',n:50,k:{0:{p:[0,0,40],s:'move',l:'奇襲のはずが罠'},1:{p:[0,0,20],s:'fight',f:'concave'},2:{p:[0,0,10],s:'fight',b:1},3:{p:[0,0,10],s:'ready'}}},
 {name:'ファルコン隊',cmd:'ランド・カルリジアン',side:'A',n:6,k:{0:{p:[10,0,30],s:'move'},1:{p:[10,0,10],s:'wait'},2:{p:[0,0,-40],s:'charge',l:'要塞内部へ'},3:{p:[10,0,20],s:'ready',l:'炉を破壊'}}},
 {name:'地上攻撃隊',cmd:'ハン・ソロ',side:'A',n:8,k:{0:{p:[-20,0,0],s:'move',l:'衛星に降下'},1:{p:[-20,0,-10],s:'broken',l:'捕まる'},2:{p:[-20,0,-10],s:'fight',l:'イウォークと反撃'},3:{p:[-20,0,-10],s:'ready',l:'シールドを破壊'}}}
];
const PH=[
 {time:'4 ABY',clock:'エピソード6',step:'罠',title:'皇帝の罠',text:'反乱同盟は建造中の第2デス・スターを攻めたが、それは皇帝が仕掛けた罠だった。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'攻防',title:'シールドが消えない',text:'シールドは働いたままで、反乱艦隊は帝国艦隊とデス・スターの砲撃にさらされた。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'逆転',title:'衛星での反撃',text:'ハンたちはイウォークとともに地上のシールド発生装置を壊した。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'撃破',title:'第2デス・スターの破壊',text:'ランドたちが中の炉を壊し、デス・スターは爆発した。皇帝もこの戦いで倒れた。',cam:{fit:1,th:.5,ph:.9},arrows:[{p:[[10,0,10],[0,0,-40]],c:'A'}]}
];
const RESULT={title:'エンドアの戦いの戦果',when:'4 ABY、衛星エンドア',prev:'ホスの戦い',next:'ジャクーの戦い',
 factors:['地上でのシールド破壊が宇宙の勝敗を決めた。','ベイダーが皇帝を倒した。'],winner:'A',outcome:'反乱同盟の勝利',
 summary:'皇帝とベイダーが死に、帝国は中心を失った。',
 sides:[{name:'銀河帝国',side:'E',cmdr:'皇帝パルパティーン',flag:'—',others:'ダース・ベイダー',before:'不明',loss:'第2デス・スター、旗艦',rate:null,deaths:'不明',dead:['ダース・ベイダー']},{name:'反乱同盟',side:'A',cmdr:'アクバー提督',flag:'—',others:'ランド、ハン、レイア',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['帝国は分裂し、新共和国が生まれる。'],
 note:'年は記憶にもとづく（Wookieepedia年表では未確認）。兵力・損害の数値は確認できず「不明」とした。皇帝はのちの作品で生存していたことが描かれる。'};
"""
