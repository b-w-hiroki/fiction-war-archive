from common import *
UC=1034.0
ARC='続三部作'
OUT='starkiller.html'
TITLE='スターキラー基地の戦い 3D俯瞰'
HEAD='スターキラー'
ERA='34 ABY（ヤヴィンの戦いの34年後）'
SE='ファースト・オーダー'; SA='レジスタンス'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xd8e0e8','0x6a7a6a',amp=4,seed=19,sky='0x9ab0c8')+specials(labels([('振動装置','基地のシールドと砲の要','E',(0, 24, -20),3.4)]))
DATA=r"""
const U=[
 {name:'基地守備隊',cmd:'ハックス将軍',side:'E',n:40,k:{0:{p:[0,7,-20],s:'ready',l:'惑星級の兵器'},1:{p:[0,7,-16],s:'fight',b:1},2:{p:[0,7,-18],s:'fight'},3:{p:[0,7,-30],s:'gone',l:'惑星ごと崩壊'}}},
 {name:'潜入班',cmd:'ハン・ソロ',side:'A',n:4,k:{0:{p:[20,7,10],s:'move',l:'地上に潜入'},1:{p:[4,7,-10],s:'fight',l:'シールドを下ろす'},2:{p:[0,7,-18],s:'broken',l:'ハン死亡'},3:{p:[20,7,30],s:'withdraw'}}},
 {name:'Xウイング隊',cmd:'ポー・ダメロン',side:'A',n:10,k:{0:{p:[0,7,50],s:'wait'},1:{p:[0,7,10],s:'fight'},2:{p:[0,7,-10],s:'fight',b:1},3:{p:[0,7,30],s:'ready',l:'振動装置を破壊'}}}
];
const PH=[
 {time:'34 ABY',clock:'エピソード7',step:'発射',title:'惑星を撃つ兵器',text:'ファースト・オーダーは惑星を改造した兵器で新共和国の星系を撃った。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'潜入',title:'シールドを下ろす',text:'ハンたちが基地に入り込み、シールドを下ろした。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[20,7,10],[4,7,-10]],c:'A'}]},
 {time:'',clock:'',step:'悲劇',title:'ハンの死',text:'ハンは息子カイロ・レンに討たれた。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'撃破',title:'基地の崩壊',text:'ポーの隊が振動装置を壊し、基地は惑星ごと崩れた。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'スターキラー基地の戦いの戦果',when:'34 ABY、スターキラー基地',prev:'ジャクーの戦い',next:'クレイトの戦い',
 factors:['潜入班がシールドを下ろした。'],winner:'A',outcome:'レジスタンスの勝利',
 summary:'基地は破壊されたが、新共和国の首都星系はすでに失われていた。',
 sides:[{name:'ファースト・オーダー',side:'E',cmdr:'ハックス将軍',flag:'—',others:'カイロ・レン',before:'不明',loss:'基地',rate:null,deaths:'不明',dead:[]},{name:'レジスタンス',side:'A',cmdr:'レイア将軍',flag:'—',others:'ポー、レイ、フィン',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['ハン・ソロ']}],
 after:['新共和国は大きく弱まり、レジスタンスが追われる立場になる。'],
 note:'年はWookieepedia（https://starwars.fandom.com/wiki/Battle_of_Starkiller_Base）で34 ABYと確認。兵力・損害の数値は確認できず「不明」とした。'};
"""
