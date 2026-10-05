from common import land_env, specials, labels
UC=767.05
ARC='中華統一'
OUT='hika.html'
TITLE='肥下の戦い 3D俯瞰'
HEAD='肥下'
ERA='紀元前233年（秦王政14年）'
SE='趙軍'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6a40','0x9a9468',amp=5,seed=17)+specials(labels([('肥下', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'李牧軍',cmd:'李牧',side:'E',n:70,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-6],s:'charge'},3:{p:[0,7,-24],s:'fight'}}},
{name:'桓騎軍',cmd:'桓騎',side:'A',n:60,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'兵力不明'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,10],s:'broken'}}}
];
const PH=[
{time:'紀元前233年',clock:'',step:'布陣',title:'赤麗・宜安',text:'桓騎軍は趙の北へ攻め入った。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'誘い',title:'肥下の包囲',text:'李牧は桓騎軍を肥下へ引き寄せて囲んだ。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'包囲',title:'逃げ場のない戦い',text:'秦軍は囲みの中で戦い続けた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'敗北',title:'桓騎の死',text:'桓騎は討たれ、秦軍は大きく崩れた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'肥下の戦いの結果',when:'紀元前233年（秦王政14年）、肥下',prev:'鄴攻め',next:'番吾の戦い',factors:["李牧が戦場を選び、敵を囲んだ。"],winner:'E',outcome:'趙軍の勝利',summary:'秦の大将軍桓騎が討たれた。史実の肥下の戦いにあたる。',sides:[{name:'趙軍',side:'E',cmdr:'李牧',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'秦軍',side:'A',cmdr:'桓騎',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["桓騎"]}],after:['秦の大将軍桓騎が討たれた。史実の肥下の戦いにあたる。'],note:'第702〜755話。兵力は資料で確認できず不明。'};
"""
