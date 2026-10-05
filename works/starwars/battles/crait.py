from common import *
UC=1034.1
ARC='続三部作'
OUT='crait.html'
TITLE='クレイトの戦い 3D俯瞰'
HEAD='クレイト'
ERA='34 ABY（ヤヴィンの戦いの34年後）'
SE='ファースト・オーダー'; SA='レジスタンス'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xe8e8e8','0xb04030',amp=4,seed=23,sky='0xd0d8e0')+specials(labels([('旧反乱同盟基地','塩の平原の要塞','A',(0, 24, 30),3.4)]))
DATA=r"""
const U=[
 {name:'ファースト・オーダー地上軍',cmd:'カイロ・レン',side:'E',n:40,k:{0:{p:[0,7,-40],s:'move',f:'line',l:'ウォーカー'},1:{p:[0,7,-20],s:'fight',b:1},2:{p:[0,7,-10],s:'fight',l:'ルークを砲撃'},3:{p:[0,7,10],s:'charge',l:'基地は空'}}},
 {name:'レジスタンス',cmd:'レイア将軍',side:'A',n:12,k:{0:{p:[0,7,30],s:'ready',l:'基地に立てこもる'},1:{p:[0,7,10],s:'fight',l:'旧式機で出撃'},2:{p:[0,7,30],s:'wait'},3:{p:[0,7,60],s:'withdraw',l:'ファルコンで脱出'}}},
 {name:'ルーク',cmd:'ルーク・スカイウォーカー',side:'A',n:2,k:{0:{p:[0,7,30],s:'hidden'},1:{p:[0,7,30],s:'hidden'},2:{p:[0,7,0],s:'fight',l:'時間を稼ぐ'},3:{p:[0,7,0],s:'gone'}}}
];
const PH=[
 {time:'34 ABY',clock:'エピソード8',step:'追撃',title:'追い詰められる',text:'レジスタンスは塩の惑星クレイトの古い基地に逃げ込んだ。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'出撃',title:'旧式機の出撃',text:'レジスタンスは旧式機で砲を止めようとしたが、果たせなかった。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-20]],c:'E'}]},
 {time:'',clock:'',step:'時間稼ぎ',title:'ルークの出現',text:'ルークが一人で現れ、カイロ・レンを引きつけた。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'脱出',title:'わずかな生存者',text:'その間に生き残りはファルコンで脱出した。ルークは力を使い果たして世を去った。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'クレイトの戦いの戦果',when:'34 ABY、惑星クレイト',prev:'スターキラー基地の戦い',next:'エクセゴルの戦い',
 factors:['ルークの時間稼ぎで退路が開けた。'],winner:'E',outcome:'ファースト・オーダーの勝利（レジスタンスは脱出）',
 summary:'レジスタンスはわずかな人数まで減ったが、全滅は免れた。',
 sides:[{name:'ファースト・オーダー',side:'E',cmdr:'カイロ・レン最高指導者',flag:'—',others:'ハックス将軍',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'レジスタンス',side:'A',cmdr:'レイア将軍',flag:'—',others:'ポー・ダメロン',before:'不明',loss:'不明（大部分を失う）',rate:null,deaths:'不明',dead:['ルーク・スカイウォーカー']}],
 after:['ルークの姿が銀河に伝わり、抵抗の希望になる。'],
 note:'年はWookieepedia（https://starwars.fandom.com/wiki/Battle_of_Crait）で34 ABYと確認。兵力・損害の数値は確認できず「不明」とした。'};
"""
