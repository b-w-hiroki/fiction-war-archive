from common import land_env, specials, labels
UC=763.08
ARC='中華統一'
OUT='kokuyou.html'
TITLE='黒羊丘の戦い 3D俯瞰'
HEAD='黒羊丘'
ERA='紀元前237年（秦王政10年）'
SE='趙軍'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x3a5a30','0x6a8a50',amp=5,seed=13)+specials(labels([('黒羊丘', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'慶舎軍',cmd:'慶舎',side:'E',n:60,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-6],s:'broken'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'桓騎軍',cmd:'桓騎',side:'A',n:50,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'兵力不明'},1:{p:[0,7,14],s:'fight'},2:{p:[0,7,10],s:'fight'},3:{p:[0,7,8],s:'ready'}}},
{name:'飛信隊',cmd:'信',side:'A',n:24,k:{0:{p:[-18,7,20],s:'move',f:'concave',l:''},1:{p:[-18,7,8],s:'fight'},2:{p:[-18,7,-4],s:'charge'},3:{p:[-18,7,-8],s:'ready'}}}
];
const PH=[
{time:'紀元前237年',clock:'',step:'布陣',title:'森の戦場',text:'秦の桓騎軍が黒羊丘の森で趙軍とぶつかった。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'攻防',title:'丘の取り合い',text:'森と丘をめぐって数日戦った。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'討取',title:'慶舎を討つ',text:'信が趙の総大将慶舎を討ち取った。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'黒羊を取る',text:'桓騎は敵の背後を脅かし、趙軍は退いた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'黒羊丘の戦いの結果',when:'紀元前237年（秦王政10年）、黒羊丘',prev:'著雍の戦い',next:'鄴攻め',factors:["飛信隊が総大将を討った。", "桓騎が敵の背後を脅かした。"],winner:'A',outcome:'秦軍の勝利',summary:'趙の総大将慶舎が討たれ、秦は黒羊を得た。',sides:[{name:'趙軍',side:'E',cmdr:'慶舎',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["慶舎"]},{name:'秦軍',side:'A',cmdr:'桓騎',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['趙の総大将慶舎が討たれ、秦は黒羊を得た。'],note:'第438〜484話。兵力は資料で確認できず不明。'};
"""
