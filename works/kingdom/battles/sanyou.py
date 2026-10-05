from common import land_env, specials, labels
UC=758.05
ARC='飛躍'
OUT='sanyou.html'
TITLE='山陽の戦い 3D俯瞰'
HEAD='山陽'
ERA='紀元前242年（秦王政5年）'
SE='魏軍'; SA='秦軍'; PALE='misr'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x6a6a40','0xa49868',amp=5,seed=8)+specials(labels([('山陽', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'魏軍',cmd:'廉頗',side:'E',n:60,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-14],s:'fight'},2:{p:[0,7,-6],s:'fight'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'蒙驁軍',cmd:'蒙驁',side:'A',n:60,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'兵力不明'},1:{p:[0,7,14],s:'fight'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,0],s:'ready'}}},
{name:'飛信隊',cmd:'信',side:'A',n:18,k:{0:{p:[-18,7,20],s:'move',f:'concave',l:'千人隊'},1:{p:[-18,7,8],s:'fight'},2:{p:[-18,7,-4],s:'charge'},3:{p:[-18,7,-8],s:'ready'}}}
];
const PH=[
{time:'紀元前242年',clock:'',step:'布陣',title:'山陽へ',text:'秦は蒙驁を総大将に魏の山陽を攻めた。魏には趙から亡命した廉頗がいた。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'包囲',title:'廉頗の攻め',text:'廉頗の四天王が秦の陣を攻め立てた。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'討取',title:'輪虎を討つ',text:'信の隊が廉頗配下の将輪虎を討った。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'山陽を取る',text:'廉頗は退き、秦は山陽を取って東郡を置いた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'山陽の戦いの結果',when:'紀元前242年（秦王政5年）、山陽',prev:'馬陽の戦い',next:'函谷関の戦い',factors:["蒙驁が守りを固めて廉頗の攻めを受け止めた。", "若い隊長たちが敵の将を討った。"],winner:'A',outcome:'秦軍の勝利',summary:'秦が魏の山陽を取り、東へ進む足場を得た。',sides:[{name:'魏軍',side:'E',cmdr:'廉頗',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["輪虎"]},{name:'秦軍',side:'A',cmdr:'蒙驁',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['秦が魏の山陽を取り、東へ進む足場を得た。'],note:'第189〜243話。兵力は資料で確認できず不明。'};
"""
