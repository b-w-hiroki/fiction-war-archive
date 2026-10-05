from common import *
UC=1003.0
ARC='帝国と反乱'
OUT='hoth.html'
TITLE='ホスの戦い 3D俯瞰'
HEAD='ホス'
ERA='3 ABY（ヤヴィンの戦いの3年後）'
SE='銀河帝国'; SA='反乱同盟'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xd8e0e8','0xf0f4f8',amp=4,seed=13,sky='0xc8d8e8')+specials(labels([('エコー基地','反乱同盟の雪原の基地','A',(0, 24, 30),3.4)]))
DATA=r"""
const U=[
 {name:'ウォーカー部隊',cmd:'ヴィアーズ将軍',side:'E',n:20,k:{0:{p:[0,7,-40],s:'move',f:'line',l:'AT-AT'},1:{p:[0,7,-20],s:'fight',b:1},2:{p:[0,7,0],s:'fight',l:'発電機を破壊'},3:{p:[0,7,20],s:'charge',l:'基地を占領'}}},
 {name:'反乱守備隊',cmd:'リーコン将軍',side:'A',n:30,k:{0:{p:[0,7,10],s:'ready',f:'line'},1:{p:[0,7,4],s:'fight'},2:{p:[0,7,10],s:'broken'},3:{p:[0,7,40],s:'withdraw',l:'撤退'}}},
 {name:'スノースピーダー',cmd:'ルーク',side:'A',n:6,k:{0:{p:[10,7,20],s:'wait'},1:{p:[10,7,-14],s:'fight',l:'脚に綱を絡める'},2:{p:[10,7,-6],s:'broken'},3:{p:[20,7,50],s:'withdraw'}}},
 {name:'輸送船団',cmd:'反乱同盟',side:'A',n:10,k:{0:{p:[-10,7,30],s:'ready'},1:{p:[-10,7,40],s:'withdraw',l:'順次脱出'},2:{p:[-10,7,50],s:'withdraw',b:1},3:{p:[-10,7,60],s:'gone'}}}
];
const PH=[
 {time:'3 ABY',clock:'エピソード5',step:'発見',title:'基地の発見',text:'帝国は氷の惑星ホスに反乱同盟の基地を見つけた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'地上戦',title:'ウォーカーの前進',text:'AT-ATが雪原を進み、スピーダーが脚に綱を絡めて1機を倒した。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-10]],c:'E'}]},
 {time:'',clock:'',step:'脱出',title:'輸送船の脱出',text:'守備隊が時間を稼ぎ、イオン砲の援護で輸送船が逃げた。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'陥落',title:'基地の陥落',text:'発電機が壊され、基地は落ちた。反乱同盟は散り散りに脱出した。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'ホスの戦いの戦果',when:'3 ABY、氷の惑星ホス',prev:'ヤヴィンの戦い',next:'エンドアの戦い',
 factors:['帝国艦隊が早すぎる超空間離脱で奇襲を失敗した。'],winner:'E',outcome:'帝国の勝利（反乱同盟は脱出）',
 summary:'帝国は基地を奪ったが、反乱同盟の主力は逃れた。',
 sides:[{name:'銀河帝国',side:'E',cmdr:'ダース・ベイダー',flag:'—',others:'ヴィアーズ将軍',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'反乱同盟',side:'A',cmdr:'リーコン将軍',flag:'—',others:'レイア、ルーク',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['ルークはダゴバへ、ハンたちはベスピンへ向かう。'],
 note:'年は記憶にもとづく（Wookieepedia年表では未確認）。兵力・損害の数値は確認できず「不明」とした。'};
"""
