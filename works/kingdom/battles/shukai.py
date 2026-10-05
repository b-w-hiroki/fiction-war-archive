from common import land_env, specials, labels
UC=764.03
ARC='中華統一'
OUT='shukai.html'
TITLE='朱海平原の戦い 3D俯瞰'
HEAD='朱海平原'
ERA='紀元前236年（秦王政11年）'
SE='趙軍'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x6a6a40','0xa49868',amp=5,seed=14)+specials(labels([('朱海平原', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'李牧軍',cmd:'李牧',side:'E',n:80,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'約12万'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-8],s:'fight'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'王翦軍',cmd:'王翦',side:'A',n:60,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'約8万8千'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,6],s:'ready'}}},
{name:'飛信隊',cmd:'信',side:'A',n:24,k:{0:{p:[-18,7,20],s:'move',f:'concave',l:'中央'},1:{p:[-18,7,8],s:'fight'},2:{p:[-18,7,-6],s:'charge'},3:{p:[-18,7,-4],s:'ready'}}}
];
const PH=[
{time:'紀元前236年',clock:'',step:'布陣',title:'鄴へ',text:'秦は王翦を総大将に趙の鄴を攻め、李牧と朱海平原で対した。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'消耗',title:'長い戦い',text:'十数日にわたる戦いで両軍とも兵糧が尽きかけた。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'討取',title:'龐煖を討つ',text:'最終日、信が龐煖を討った。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'鄴の陥落',text:'李牧は退き、鄴は落ちた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'朱海平原の戦いの結果',when:'紀元前236年（秦王政11年）、朱海平原',prev:'黒羊丘の戦い',next:'肥下の戦い',factors:["王翦が鄴の兵糧を絶つ策を立てた。", "信が敵の大将格を討った。"],winner:'A',outcome:'秦軍の勝利',summary:'趙の要地鄴を取り、趙の守りが大きく崩れた。',sides:[{name:'趙軍',side:'E',cmdr:'李牧',flag:'—',others:'—',before:'約120,000',loss:'不明',rate:null,deaths:'不明',dead:["龐煖"]},{name:'秦軍',side:'A',cmdr:'王翦',flag:'—',others:'—',before:'約88,000',loss:'不明',rate:null,deaths:'不明',dead:["麻鉱"]}],after:['趙の要地鄴を取り、趙の守りが大きく崩れた。'],note:'朱海平原の兵力は48巻時点の各翼合計（秦は左翼5千・中央5万8千・右翼2万5千、趙は3万・6万・3万）。note.com/tanakasuke の要約による。'};
"""
