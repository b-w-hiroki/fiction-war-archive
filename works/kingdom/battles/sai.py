from common import land_env, specials, labels
UC=759.09
ARC='合従軍'
OUT='sai.html'
TITLE='蕞の戦い 3D俯瞰'
HEAD='蕞'
ERA='紀元前241年（秦王政6年）'
SE='趙軍（李牧別働隊）'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6440','0x9a9068',amp=5,seed=9)+specials(labels([('蕞', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'李牧軍',cmd:'李牧',side:'E',n:60,k:{0:{p:[0,7,-30],s:'move',f:'line',l:'別働隊'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-10],s:'fight'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'蕞守備',cmd:'嬴政',side:'A',n:30,k:{0:{p:[0,7,20],s:'ready',f:'concave',l:'城と民兵'},1:{p:[0,7,8],s:'fight'},2:{p:[0,7,8],s:'fight'},3:{p:[0,7,10],s:'ready'}}},
{name:'山の民',cmd:'楊端和',side:'A',n:30,k:{0:{p:[24,7,60],s:'hidden',f:'concave',l:'援軍'},1:{p:[24,7,60],s:'hidden'},2:{p:[24,7,-24],s:'charge'},3:{p:[24,7,-10],s:'ready'}}}
];
const PH=[
{time:'紀元前241年',clock:'',step:'迫る',title:'李牧の進軍',text:'李牧の軍が咸陽の手前、蕞の城に迫った。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'籠城',title:'王が前に出る',text:'嬴政が自ら蕞に入り、民を兵として城を守った。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'援軍',title:'山の民の到着',text:'楊端和の山の民が駆けつけ、李牧軍の背を突いた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'撤退',title:'李牧の退却',text:'李牧軍は退き、合従軍の侵攻は終わった。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'蕞の戦いの結果',when:'紀元前241年（秦王政6年）、蕞',prev:'函谷関の戦い',next:'著雍の戦い',factors:["王みずからが城に立ち、民の士気を保った。", "山の民の援軍が間に合った。"],winner:'A',outcome:'秦軍の勝利',summary:'合従軍の最後の一手を防ぎ、秦は滅亡を免れた。',sides:[{name:'趙軍（李牧別働隊）',side:'E',cmdr:'李牧',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'秦軍',side:'A',cmdr:'嬴政',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['合従軍の最後の一手を防ぎ、秦は滅亡を免れた。'],note:'第331〜352話前後（buzz-beaver.com）。兵力は資料で確認できず不明。'};
"""
