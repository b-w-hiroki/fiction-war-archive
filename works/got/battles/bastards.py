from common import *
UC=303.01
ARC='ドラマ独自'
OUT='bastards.html'
TITLE='落とし子の戦い（ドラマ） 3D俯瞰'
HEAD='落とし子'
ERA='AC303年'
SE='ボルトン軍'; SA='スターク・野人連合'; PALE='marley'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6a48','0x7a8060',amp=3,seed=7,sky='0x8a909a')+specials(labels([('ウィンターフェル', '', 'E', (0, 22, -40), 3)]))
DATA=r"""
const U=[
{name:'ボルトン軍',cmd:'ラムジー・ボルトン',side:'E',n:30,k:{0:{p:[0,7,-24],s:'ready',f:'line'},1:{p:[0,7,-14],s:'fight'},2:{p:[0,7,4],s:'fight',f:'concave',l:'盾の壁で包囲'},3:{p:[0,7,-6],s:'broken'}}},
 {name:'ジョン軍',cmd:'ジョン・スノウ',side:'A',n:12,k:{0:{p:[0,7,24],s:'ready'},1:{p:[0,7,4],s:'charge',l:'挑発に乗り突撃'},2:{p:[0,7,6],s:'fight',l:'包囲される'},3:{p:[0,7,-10],s:'charge'}}},
 {name:'谷間の騎士',cmd:'ピーター・ベイリッシュ',side:'A',n:20,k:{0:{s:'hidden',p:[30,7,30]},1:{s:'hidden',p:[30,7,30]},2:{s:'hidden',p:[30,7,30]},3:{p:[16,7,0],s:'charge',l:'サンサが呼んだ援軍'}}}
];
const PH=[
{time:'AC303年（推定）',clock:'S6E9',step:'布陣',title:'布陣',text:'ジョンとサンサは北部を取り戻すため、ウィンターフェルのボルトン軍と向き合った。',cam:{fit:1,th:0.5,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'挑発',title:'挑発',text:'ラムジーの挑発でジョンが突撃し、計画が崩れた。',cam:{fit:1,th:0.4,ph:0.9},arrows:[{p:[[0,7,24],[0,7,4]],c:'A'}]},
 {time:'',clock:'',step:'包囲',title:'盾の壁',text:'ボルトン軍の盾の壁と死体の山に囲まれ、ジョン軍は追い詰められた。',cam:{fit:1,th:0.7,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'援軍',title:'谷間の騎士',text:'サンサが呼んだ谷間の騎士が背後を突き、形勢が逆転した。',cam:{fit:1,th:0.5,ph:1.0},arrows:[{p:[[30,7,30],[16,7,0]],c:'A'}]}
];
const RESULT={title:'落とし子の戦いの結果',when:'ドラマS6、ウィンターフェル前',prev:'堅牢な家の戦い',next:'長い夜',factors:['ボルトン軍は兵数で勝っていた。','ジョンが挑発に乗り陣が崩れた。','サンサの呼んだ谷間の騎士が決め手になった。'],winner:'A',outcome:'スターク側の勝利（ウィンターフェル奪還）',summary:'ドラマ独自の戦い。ジョンが北の王に推される。',sides:[{name:'ボルトン軍',side:'E',cmdr:'ラムジー・ボルトン',flag:'—',others:'—',before:'不明',loss:'壊滅',rate:null,deaths:'不明',dead:['ラムジー・ボルトン']},{name:'スターク・野人連合',side:'A',cmdr:'ジョン・スノウ',flag:'—',others:'サンサ・スターク、トアマンド',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['リコン・スターク','ワン・ワン']}],after:['ジョンが北の王に推される。'],note:'ドラマS6E9「落とし子の戦い」による小説未刊行部分。AC年はドラマで明示されず、303年は推定。'};
"""
