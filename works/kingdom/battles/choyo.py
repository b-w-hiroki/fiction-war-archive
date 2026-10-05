from common import land_env, specials, labels
UC=761.05
ARC='中華統一'
OUT='choyo.html'
TITLE='著雍の戦い 3D俯瞰'
HEAD='著雍'
ERA='紀元前239年（秦王政8年）'
SE='魏軍'; SA='秦軍'; PALE='misr'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6440','0x9a9068',amp=5,seed=11,water='0x3a5a68')+specials(labels([('著雍', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'魏軍',cmd:'呉鳳明',side:'E',n:60,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-14],s:'fight'},2:{p:[0,7,-6],s:'fight'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'騰軍',cmd:'騰',side:'A',n:50,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'兵力不明'},1:{p:[0,7,14],s:'fight'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,0],s:'ready'}}},
{name:'玉鳳・飛信隊',cmd:'王賁・信',side:'A',n:24,k:{0:{p:[-22,7,20],s:'move',f:'concave',l:'別働'},1:{p:[-22,7,-30],s:'move'},2:{p:[-22,7,-6],s:'charge'},3:{p:[-22,7,-8],s:'ready'}}}
];
const PH=[
{time:'紀元前239年',clock:'',step:'布陣',title:'著雍へ',text:'秦は騰を総大将に、魏の要地著雍を攻めた。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'攻防',title:'呉鳳明の守り',text:'呉鳳明は三か所に陣を置いて守った。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'突入',title:'本陣への突入',text:'王賁と信の隊が本陣へ攻め込んだ。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'著雍を取る',text:'魏軍は退き、秦は著雍を取った。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'著雍の戦いの結果',when:'紀元前239年（秦王政8年）、著雍',prev:'蕞の防衛',next:'黒羊丘の戦い',factors:["若い将の隊が本陣を突いた。"],winner:'A',outcome:'秦軍の勝利',summary:'秦が魏の著雍を取り、東進の拠点とした。',sides:[{name:'魏軍',side:'E',cmdr:'呉鳳明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["紫伯"]},{name:'秦軍',side:'A',cmdr:'騰',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['秦が魏の著雍を取り、東進の拠点とした。'],note:'第379〜401話。兵力は資料で確認できず不明。'};
"""
