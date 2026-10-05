from common import land_env, specials, labels
UC=756.05
ARC='飛躍'
OUT='bayou.html'
TITLE='馬陽の戦い 3D俯瞰'
HEAD='馬陽'
ERA='紀元前244年（秦王政3年）'
SE='趙軍'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6a40','0x9a9468',amp=5,seed=6)+specials(labels([('馬陽', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'趙軍本軍',cmd:'龐煖・李牧',side:'E',n:60,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'約10万（推定）'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-8],s:'charge'},3:{p:[0,7,-24],s:'ready'}}},
{name:'李牧軍',cmd:'李牧',side:'E',n:36,k:{0:{p:[-30,7,-60],s:'hidden',f:'line',l:'伏兵'},1:{p:[-30,7,-60],s:'hidden'},2:{p:[-30,7,6],s:'charge'},3:{p:[-30,7,6],s:'fight'}}},
{name:'王騎軍',cmd:'王騎',side:'A',n:60,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'約10万（推定）'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,0],s:'charge'},3:{p:[0,7,24],s:'withdraw'}}}
];
const PH=[
{time:'紀元前244年',clock:'',step:'布陣',title:'趙の侵攻',text:'趙軍が馬陽へ攻め込み、秦は王騎を総大将に立てた。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'激戦',title:'両軍の押し合い',text:'王騎軍が趙の将を討ち、優勢に進めた。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'伏兵',title:'李牧の伏兵',text:'王騎が龐煖と一騎打ちのさなか、李牧の伏兵が背後から現れ包囲した。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'撤退',title:'王騎の死',text:'王騎は討たれ、秦軍は退いた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'馬陽の戦いの結果',when:'紀元前244年（秦王政3年）、馬陽',prev:'蛇甘平原の戦い',next:'山陽攻略',factors:["李牧が隠していた別働隊で背後を取った。", "総大将同士の一騎打ちの最中に包囲が成った。"],winner:'E',outcome:'趙軍の勝利',summary:'秦の六大将軍王騎が討たれた戦い。李牧が初めて表に出る。',sides:[{name:'趙軍',side:'E',cmdr:'龐煖・李牧',flag:'—',others:'—',before:'約10万（推定）',loss:'不明',rate:null,deaths:'不明',dead:["馮忌", "趙荘（推定）"]},{name:'秦軍',side:'A',cmdr:'王騎',flag:'—',others:'—',before:'約10万（推定）',loss:'不明',rate:null,deaths:'不明',dead:["王騎"]}],after:['秦の六大将軍王騎が討たれた戦い。李牧が初めて表に出る。'],note:'第108〜173話。兵力は記憶にもとづく推定で、資料で未確認。'};
"""
