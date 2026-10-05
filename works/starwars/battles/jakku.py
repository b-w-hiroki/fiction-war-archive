from common import *
UC=1005.0
ARC='新共和国'
OUT='jakku.html'
TITLE='ジャクーの戦い 3D俯瞰'
HEAD='ジャクー'
ERA='5 ABY（ヤヴィンの戦いの5年後）'
SE='銀河帝国（残存軍）'; SA='新共和国'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xc8a070','0xe0c890',amp=4,seed=17,sky='0xd8b890')+specials(labels([('ジャクー','砂漠の惑星','A',(0, 24, 0),3.4)]))
DATA=r"""
const U=[
 {name:'帝国残存艦隊',cmd:'ラックス元帥',side:'E',n:40,k:{0:{p:[0,7,-20],s:'ready',f:'line'},1:{p:[0,7,-10],s:'fight',b:1},2:{p:[0,7,-14],s:'broken',l:'艦が墜落'},3:{p:[0,7,-30],s:'gone',l:'降伏'}}},
 {name:'新共和国軍',cmd:'新共和国',side:'A',n:50,k:{0:{p:[0,7,40],s:'move',l:'帝国残党を追う'},1:{p:[0,7,10],s:'fight',b:1},2:{p:[0,7,0],s:'charge'},3:{p:[0,7,-10],s:'ready',l:'勝利'}}}
];
const PH=[
 {time:'5 ABY',clock:'（映画では残骸のみ）',step:'集結',title:'最後の集結',text:'帝国の残存艦隊は砂漠の惑星ジャクーに集まっていた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'攻撃',title:'新共和国の攻撃',text:'新共和国は残党を追ってジャクーを攻めた。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,40],[0,7,10]],c:'A'}]},
 {time:'',clock:'',step:'墜落',title:'巨艦の墜落',text:'大型艦が砂漠に落ち、その残骸は後の時代まで残った。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'講和',title:'帝国の降伏',text:'戦いの後、帝国は銀河協定を結んで降伏した。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'ジャクーの戦いの戦果',when:'5 ABY、惑星ジャクー',prev:'エンドアの戦い',next:'スターキラー基地の戦い',
 factors:['帝国はエンドア後に統一指揮を失っていた。'],winner:'A',outcome:'新共和国の勝利',
 summary:'銀河内戦の最後の大きな戦い。帝国は降伏した。',
 sides:[{name:'銀河帝国（残存軍）',side:'E',cmdr:'ガリアス・ラックス元帥（推定）',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'新共和国',side:'A',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['帝国の一部は未知領域へ逃れ、後のファースト・オーダーとなる。'],
 note:'年は記憶にもとづく（Wookieepedia年表では未確認）。兵力・損害の数値は確認できず「不明」とした。映画では戦場跡のみが描かれ、戦闘の内容は小説・コミック等の設定に拠る（推定）。'};
"""
