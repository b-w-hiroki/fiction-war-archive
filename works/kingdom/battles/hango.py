from common import land_env, specials, labels
UC=768.05
ARC='中華統一'
OUT='hango.html'
TITLE='番吾の戦い 3D俯瞰'
HEAD='番吾'
ERA='紀元前232年（秦王政15年）'
SE='趙軍'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6440','0x9a9068',amp=5,seed=18)+specials(labels([('番吾', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'李牧軍',cmd:'李牧',side:'E',n:70,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-4],s:'charge'},3:{p:[0,7,-20],s:'fight'}}},
{name:'王翦軍',cmd:'王翦',side:'A',n:60,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'兵力不明'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,6],s:'fight'},3:{p:[0,7,30],s:'withdraw'}}},
{name:'飛信隊',cmd:'信',side:'A',n:24,k:{0:{p:[-18,7,20],s:'move',f:'concave',l:''},1:{p:[-18,7,8],s:'fight'},2:{p:[-18,7,-6],s:'fight'},3:{p:[-18,7,30],s:'withdraw'}}}
];
const PH=[
{time:'紀元前232年',clock:'',step:'布陣',title:'番吾へ',text:'王翦を総大将に、秦は趙の番吾へ攻め込んだ。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'激戦',title:'李牧との決戦',text:'李牧の軍と正面から戦った。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'崩れ',title:'秦軍の劣勢',text:'趙軍が押し、秦軍の将が次々に倒れた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'撤退',title:'王翦の退却',text:'王翦は退き、秦は再び李牧に敗れた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'番吾の戦いの結果',when:'紀元前232年（秦王政15年）、番吾',prev:'肥下の戦い',next:'韓攻略',factors:["李牧が秦の攻めを読んで迎え撃った。"],winner:'E',outcome:'趙軍の勝利',summary:'秦は李牧に2年続けて敗れ、趙攻めは足踏みした。',sides:[{name:'趙軍',side:'E',cmdr:'李牧',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'秦軍',side:'A',cmdr:'王翦',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["亜光（推定）"]}],after:['秦は李牧に2年続けて敗れ、趙攻めは足踏みした。'],note:'第769〜799話。兵力・討死者は資料で確認できず不明／推定。'};
"""
