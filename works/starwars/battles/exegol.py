from common import *
UC=1035.0
ARC='続三部作'
OUT='exegol.html'
TITLE='エクセゴルの戦い 3D俯瞰'
HEAD='エクセゴル'
ERA='35 ABY（ヤヴィンの戦いの35年後）'
SE='ファイナル・オーダー（シス）'; SA='レジスタンスと市民艦隊'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+specials(labels([('エクセゴル','シスの隠れた惑星','E',(0, 30, -30),3.4)]))
DATA=r"""
const U=[
 {name:'シス艦隊',cmd:'皇帝パルパティーン',side:'E',n:60,k:{0:{p:[0,0,-20],s:'ready',f:'line',l:'惑星を撃てる艦隊'},1:{p:[0,0,-14],s:'fight',b:1},2:{p:[0,0,-12],s:'fight'},3:{p:[0,0,-20],s:'broken',l:'壊滅'}}},
 {name:'レジスタンス',cmd:'ポー・ダメロン',side:'A',n:20,k:{0:{p:[0,0,30],s:'charge',l:'航法塔を狙う'},1:{p:[0,0,10],s:'broken',l:'劣勢'},2:{p:[0,0,6],s:'fight'},3:{p:[0,0,0],s:'ready'}}},
 {name:'市民艦隊',cmd:'ランド・カルリジアン',side:'A',n:50,k:{0:{p:[20,0,50],s:'hidden'},1:{p:[20,0,50],s:'hidden'},2:{p:[20,0,20],s:'charge',l:'銀河中から援軍'},3:{p:[10,0,0],s:'ready'}}},
 {name:'レイ',cmd:'レイ',side:'A',n:2,k:{0:{p:[-10,0,-30],s:'move',l:'玉座へ'},1:{p:[-10,0,-30],s:'fight'},2:{p:[-10,0,-30],s:'broken'},3:{p:[-10,0,-30],s:'ready',l:'皇帝を倒す'}}}
];
const PH=[
 {time:'35 ABY',clock:'エピソード9',step:'攻撃',title:'隠れ星への攻撃',text:'レジスタンスはシスの惑星エクセゴルに乗り込み、艦隊の発進を止めようとした。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'劣勢',title:'押される攻撃隊',text:'レジスタンスは数で劣り、押し込まれていった。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'援軍',title:'市民の艦隊',text:'ランドが集めた銀河中の船が駆けつけた。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[20,0,50],[20,0,20]],c:'A'}]},
 {time:'',clock:'',step:'決着',title:'皇帝の最期',text:'レイが皇帝を倒し、シス艦隊は崩れた。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'エクセゴルの戦いの戦果',when:'35 ABY、惑星エクセゴル',prev:'クレイトの戦い',next:'—',
 factors:['市民の艦隊が数の差を埋めた。'],winner:'A',outcome:'レジスタンスの勝利',
 summary:'シスとファースト・オーダーの支配は終わった。',
 sides:[{name:'ファイナル・オーダー',side:'E',cmdr:'皇帝パルパティーン',flag:'—',others:'プライド元帥',before:'不明',loss:'艦隊',rate:null,deaths:'不明',dead:['皇帝パルパティーン']},{name:'レジスタンス',side:'A',cmdr:'ポー・ダメロン',flag:'—',others:'ランド、フィン、レイ',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['ベン・ソロ']}],
 after:['銀河各地でファースト・オーダーへの反乱が広がる。'],
 note:'年はWookieepedia（https://starwars.fandom.com/wiki/Battle_of_Exegol）で35 ABYと確認。兵力・損害の数値は確認できず「不明」とした。'};
"""
