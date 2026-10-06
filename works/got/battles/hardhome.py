from common import *
UC=301.01
ARC='ドラマ独自'
OUT='hardhome.html'
TITLE='堅牢な家の戦い（ドラマ） 3D俯瞰'
HEAD='堅牢な家'
ERA='AC301年'
SE='ホワイト・ウォーカー'; SA='冥夜の守人・野人'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xdfe6ea','0xf4f8fa',water='0x2a3a48',amp=3,seed=6,sky='0x7a8a96')+specials(labels([('堅牢な家', '北の海岸', 'A', (0, 20, 10), 3)]))
DATA=r"""
const U=[
{name:'亡者の群れ',cmd:'夜の王',side:'E',n:40,k:{0:{p:[0,7,-40],s:'hidden'},1:{p:[0,7,-20],s:'charge',l:'雪崩のように'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,14],s:'fight'}}},
 {name:'ホワイト・ウォーカー',cmd:'夜の王',side:'E',n:4,k:{0:{s:'hidden',p:[0,7,-50]},1:{p:[0,7,-40],s:'ready'},2:{p:[0,7,-36],s:'fight'},3:{p:[0,7,-36],s:'ready',l:'死者を起こす'}}},
 {name:'野人の集落',cmd:'トアマンド',side:'A',n:16,k:{0:{p:[0,7,10],s:'ready'},1:{p:[0,7,10],s:'fight'},2:{p:[0,7,16],s:'broken'},3:{p:[0,7,26],s:'withdraw',l:'船で脱出'}}},
 {name:'ジョン一行',cmd:'ジョン・スノウ',side:'A',n:4,k:{0:{p:[10,7,20],s:'move'},1:{p:[8,7,6],s:'fight'},2:{p:[6,7,0],s:'fight',l:'ヴァリリア鋼で倒す'},3:{p:[8,7,28],s:'withdraw'}}}
];
const PH=[
{time:'AC301年（推定）',clock:'S5E8',step:'交渉',title:'野人との交渉',text:'ジョンは野人を壁の南へ逃がすため堅牢な家を訪れた。',cam:{fit:1,th:0.5,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'襲来',title:'亡者の襲来',text:'亡者の大群が集落を襲った。',cam:{fit:1,th:0.4,ph:0.9},arrows:[{p:[[0,7,-20],[0,7,4]],c:'E'}]},
 {time:'',clock:'',step:'剣',title:'ヴァリリア鋼',text:'ジョンの剣がホワイト・ウォーカーを倒せることが分かった。',cam:{fit:1,th:0.7,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'脱出',title:'脱出と夜の王',text:'生き残りは船で逃げ、夜の王は死者を亡者として起こした。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'堅牢な家の戦いの結果',when:'ドラマS5、北の海岸 堅牢な家',prev:'黒の城の戦い',next:'落とし子の戦い',factors:['亡者の数が圧倒的だった。','ヴァリリア鋼が効くと分かった。'],winner:'E',outcome:'ホワイト・ウォーカー側の勝利',summary:'ドラマ独自の戦い。死者の軍の脅威がはっきりする。',sides:[{name:'ホワイト・ウォーカー',side:'E',cmdr:'夜の王',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'冥夜の守人・野人',side:'A',cmdr:'ジョン・スノウ',flag:'—',others:'トアマンド',before:'不明',loss:'不明（多数の野人）',rate:null,deaths:'不明',dead:[]}],after:['一部の野人が壁の南へ渡る。'],note:'小説にない場面（ドラマS5E8「堅牢な家」）。AC年はドラマで明示されず、301年は年表上の推定。'};
"""
