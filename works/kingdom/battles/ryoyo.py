from common import land_env, specials, labels
UC=764.04
ARC='中華統一'
OUT='ryoyo.html'
TITLE='橑陽の戦い 3D俯瞰'
HEAD='橑陽'
ERA='紀元前236年（秦王政11年）'
SE='趙軍（橑陽）'; SA='秦軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a40','0x988c68',amp=5,seed=14)+specials(labels([('橑陽', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'橑陽守備',cmd:'舜水樹・犬戎',side:'E',n:50,k:{0:{p:[0,7,-28],s:'ready',f:'line',l:'兵力不明'},1:{p:[0,7,-12],s:'fight'},2:{p:[0,7,-8],s:'broken'},3:{p:[0,7,-30],s:'withdraw'}}},
{name:'楊端和軍',cmd:'楊端和',side:'A',n:50,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'約6万'},1:{p:[0,7,12],s:'fight'},2:{p:[0,7,4],s:'charge'},3:{p:[0,7,0],s:'ready'}}}
];
const PH=[
{time:'紀元前236年',clock:'',step:'布陣',title:'橑陽へ',text:'楊端和の山の民の軍が趙の橑陽を攻めた。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'苦戦',title:'犬戎の守り',text:'犬戎の兵が城外で迎え撃ち、苦しい戦いとなった。',cam:{fit:1,th:0.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'反撃',title:'犬戎王を討つ',text:'楊端和が犬戎の王を討ち、敵を崩した。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'勝利',title:'橑陽を取る',text:'橑陽は落ち、鄴の救援の道が断たれた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]}
];
const RESULT={title:'橑陽の戦いの結果',when:'紀元前236年（秦王政11年）、橑陽',prev:'鄴攻め',next:'肥下の戦い',factors:["楊端和が敵の王を討った。"],winner:'A',outcome:'秦軍の勝利',summary:'鄴攻めの一角。鄴への援軍の道を断った。',sides:[{name:'趙軍（橑陽）',side:'E',cmdr:'舜水樹・犬戎',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:["ロゾ（犬戎王）"]},{name:'秦軍',side:'A',cmdr:'楊端和',flag:'—',others:'—',before:'約60,000',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['鄴攻めの一角。鄴への援軍の道を断った。'],note:'兵力6万は note.com/tanakasuke の要約（壁軍を含む）。'};
"""
