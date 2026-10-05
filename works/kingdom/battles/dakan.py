from common import land_env, specials, labels
UC=755.05
ARC='飛躍'
OUT='dakan.html'
TITLE='蛇甘平原の戦い 3D俯瞰'
HEAD='蛇甘平原'
ERA='紀元前245年（秦王政2年）'
SE='魏軍'; SA='秦軍'; PALE='misr'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x6a7040','0xa89a68',amp=5,seed=5)+specials(labels([('蛇甘平原', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'魏軍',cmd:'呉慶',side:'E',n:60,k:{0:{p:[0,7,-34],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-20],s:'fight'},2:{p:[0,7,-8],s:'broken'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'秦軍歩兵',cmd:'縛虎申ほか',side:'A',n:40,k:{0:{p:[0,7,30],s:'move',f:'concave',l:'兵力不明'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,0],s:'fight'},3:{p:[0,7,-4],s:'ready'}}},
{name:'麃公軍',cmd:'麃公',side:'A',n:30,k:{0:{p:[24,7,34],s:'wait',f:'concave',l:'右翼の騎馬'},1:{p:[24,7,30],s:'move'},2:{p:[24,7,-6],s:'charge'},3:{p:[24,7,-10],s:'ready'}}}
];
const PH=[
{time:'紀元前245年',clock:'',step:'布陣',title:'魏の侵攻',text:'魏軍が秦に攻め入り、秦軍は蛇甘平原で迎え撃った。信の初陣である。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'丘',title:'丘の奪い合い',text:'魏軍は丘に陣取り戦車で秦の歩兵を押した。歩兵は丘を目指して攻め上がった。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'突撃',title:'麃公の突撃',text:'麃公の騎馬隊が本陣へ突入し、魏の総大将呉慶が討たれた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'秦軍の勝利',text:'総大将を失った魏軍は退いた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'蛇甘平原の戦いの結果',when:'紀元前245年（秦王政2年）、蛇甘平原',prev:'王弟反乱',next:'馬陽の戦い',factors:["麃公の騎馬隊が敵本陣を直接突いた。", "歩兵が丘を奪い、戦車の動きを止めた。"],winner:'A',outcome:'秦軍の勝利',summary:'信の初陣。麃公の突撃で魏の総大将を討ち取った。',sides:[{name:'魏軍',side:'E',cmdr:'呉慶',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["呉慶"]},{name:'秦軍',side:'A',cmdr:'縛虎申ほか',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["縛虎申"]}],after:['信の初陣。麃公の突撃で魏の総大将を討ち取った。'],note:'章範囲は第48〜73話（buzz-beaver.com）。兵力は資料で確認できず不明。'};
"""
