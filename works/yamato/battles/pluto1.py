from common import *
UC=2199.01
ARC='旅立ち'
OUT='pluto1.html'
TITLE='冥王星沖海戦 3D俯瞰'
HEAD='冥王星沖'
ERA='2199年'
SE='ガミラス艦隊'; SA='地球防衛艦隊'; PALE='gamilas'; PAL='earth'
NOTE='交戦中／健在の部隊。展開は1974年版TVシリーズにもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet(pos=(0,-120,-40),r=60,color='0x8a8a9a',land='0x6a6a7a',label=('冥王星','','E'))+specials(labels([]))
DATA=r"""
const U=[
{name:'ガミラス艦隊',cmd:'ガミラス冥王星前線',side:'E',n:60,k:{0:{p:[0,0,-30],s:'ready',f:'concave'},1:{p:[0,0,-20],s:'fight',b:1},2:{p:[0,0,-14],s:'fight'},3:{p:[0,0,-20],s:'ready',l:'地球艦隊を圧倒'}}},
 {name:'沖田艦隊',cmd:'沖田十三',side:'A',n:30,k:{0:{p:[0,0,30],s:'move',f:'line',l:'地球最後の艦隊'},1:{p:[0,0,20],s:'fight'},2:{p:[0,0,24],s:'broken',l:'艦艇の大半を失う'},3:{p:[0,0,60],s:'withdraw',l:'旗艦のみ帰還'}}},
 {name:'ゆきかぜ',cmd:'古代守',side:'A',n:3,k:{0:{p:[10,0,28],s:'move'},1:{p:[8,0,16],s:'fight'},2:{p:[6,0,6],s:'charge',l:'殿として残る'},3:{p:[4,0,0],s:'broken',l:'消息を絶つ'}}}
];
const PH=[
{time:'2199年',clock:'第1話',step:'対峙',title:'地球最後の艦隊',text:'遊星爆弾で地上が焼かれた地球は、残った艦隊で冥王星のガミラス前線に挑んだ。指揮をとるのは沖田十三。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,0,30],[0,0,20]],c:'A'}]},
 {time:'',clock:'',step:'劣勢',title:'通じない砲撃',text:'地球艦の砲はガミラス艦の装甲を貫けず、艦隊は一方的に撃たれていった。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'殿',title:'ゆきかぜの殿',text:'沖田は撤退を命じる。古代守の駆逐艦ゆきかぜは、旗艦を逃がすため敵の前に残った。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[8,0,16],[6,0,6]],c:'A'}]},
 {time:'',clock:'',step:'帰還',title:'旗艦だけの帰還',text:'地球艦隊は壊滅し、沖田の艦だけが帰った。この敗戦のあと、地球はイスカンダルからのメッセージに望みを託す。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'冥王星沖海戦の結果',when:'2199年、冥王星宙域',prev:'ガミラスの遊星爆弾攻撃',next:'ヤマト発進／冥王星前線基地攻略',
 factors:['ガミラス艦と地球艦の技術差が大きく、砲撃が通じなかった。','沖田は全滅を避けるため撤退を決めた。'],winner:'E',outcome:'ガミラスの勝利（地球艦隊壊滅）',
 summary:'地球最後の艦隊がガミラスに敗れた戦い。この敗戦が、イスカンダルへの旅とヤマトの出発につながる。',
 sides:[{name:'ガミラス艦隊',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'小',rate:null,deaths:'不明',dead:[]},
        {name:'地球防衛艦隊',side:'A',cmdr:'沖田十三',flag:'沖田の旗艦',others:'古代守',before:'不明',loss:'旗艦を除くほぼ全艦',rate:null,deaths:'不明',dead:['古代守（消息不明。のちに生存が判明）']}],
 after:['地球に残る艦隊はほぼなくなる。','火星でイスカンダルからの通信カプセルが回収される。','沖田は宇宙戦艦ヤマトの艦長となる。'],
 note:'展開は1974年版TV第1話にもとづく。兵力・損害の数値は確認できなかった。'};
"""
