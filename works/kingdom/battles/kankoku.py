from common import land_env, specials, labels
UC=759.05
ARC='合従軍'
OUT='kankoku.html'
TITLE='函谷関の戦い 3D俯瞰'
HEAD='函谷関'
ERA='紀元前241年（秦王政6年）'
SE='合従軍'; SA='秦軍'; PALE='serpent'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a40','0x988c68',amp=5,seed=9)+specials(labels([('函谷関', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'合従軍',cmd:'李牧・春申君',side:'E',n:90,k:{0:{p:[0,7,-36],s:'ready',f:'line',l:'約54万'},1:{p:[0,7,-18],s:'fight'},2:{p:[0,7,-14],s:'fight'},3:{p:[0,7,-34],s:'withdraw'}}},
{name:'函谷関守備',cmd:'蒙驁・張唐ほか',side:'A',n:40,k:{0:{p:[0,7,16],s:'ready',f:'concave',l:'関を守る'},1:{p:[0,7,10],s:'fight'},2:{p:[0,7,10],s:'fight'},3:{p:[0,7,16],s:'ready'}}},
{name:'麃公軍',cmd:'麃公',side:'A',n:24,k:{0:{p:[24,7,30],s:'ready',f:'concave',l:'野戦'},1:{p:[24,7,8],s:'charge'},2:{p:[24,7,30],s:'gone'},3:{p:[24,7,30],s:'gone'}}}
];
const PH=[
{time:'紀元前241年',clock:'',step:'侵攻',title:'五国の合従',text:'楚・趙・魏・韓・燕の五国が連合して秦へ攻め入った。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'攻防',title:'関の攻防',text:'各国軍が函谷関と周辺の陣を攻め、秦軍は持ちこたえた。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'別働',title:'李牧の転進',text:'李牧は別働隊を率いて南の道から咸陽を目指した。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'撤退',title:'関を守り抜く',text:'函谷関は落ちず、合従軍は退き始めた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'函谷関の戦いの結果',when:'紀元前241年（秦王政6年）、函谷関',prev:'山陽攻略',next:'蕞の防衛',factors:["天然の要害函谷関を最後まで落とさせなかった。", "各国の思惑が揃わず連携が弱かった。"],winner:'A',outcome:'秦軍の勝利（防衛成功）',summary:'秦存亡の危機。五国連合を函谷関で食い止めた。',sides:[{name:'合従軍',side:'E',cmdr:'李牧・春申君',flag:'—',others:'—',before:'約540,000',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'秦軍',side:'A',cmdr:'蒙驁・張唐ほか',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["張唐"]}],after:['秦存亡の危機。五国連合を函谷関で食い止めた。'],note:'合従軍の兵力は楚15万・趙12万・燕12万・魏10万・韓5万の計54万（mirumiruworld.com）。「50万超」と言われる数字。秦軍の数は不明。'};
"""
