from common import *
UC=1914.01
ARC='最終決戦'
OUT='ubuyashiki.html'
TITLE='産屋敷邸襲撃 3D俯瞰'
HEAD='産屋敷邸'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x2e3a2a','0x5a6046',amp=1,seed=8,sky='0x1e2030')+specials(labels([('産屋敷邸','鬼殺隊当主の屋敷','A',(0,18,0),3)]))
DATA=r"""
const U=[
{name:'鬼舞辻無惨',cmd:'鬼の始祖',side:'E',n:12,k:{0:{p:[0,7,-20],s:'move',l:'屋敷に現れる'},1:{p:[0,7,-4],s:'ready'},2:{p:[0,7,-2],s:'fight',l:'爆発に巻き込まれる'},3:{p:[0,7,-2],s:'fight',l:'柱に囲まれる'}}},
{name:'産屋敷耀哉',cmd:'鬼殺隊当主',side:'A',n:4,k:{0:{p:[0,7,6],s:'ready',l:'無惨を待つ'},1:{p:[0,7,4],s:'ready'},2:{p:[0,7,4],s:'gone',l:'自爆'},3:{p:[0,7,4],s:'gone'}}},
{name:'柱',cmd:'悲鳴嶼ほか',side:'A',n:14,k:{0:{p:[0,7,40],s:'move',l:'屋敷へ向かう'},1:{p:[0,7,30],s:'move'},2:{p:[0,7,16],s:'charge'},3:{p:[0,7,8],s:'fight',l:'無限城へ落とされる'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'4期第8話',step:'来訪',title:'無惨の来訪',text:'柱稽古の最中、無惨が産屋敷邸に現れた。当主・耀哉はそれを予期していた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'対話',title:'当主と無惨',text:'耀哉は家族とともに無惨を屋敷に引き留めた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'',step:'爆発',title:'自らを囮に',text:'屋敷が爆発し、珠世が無惨に人間に戻る薬を打ち込んだ。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'漫画16巻',step:'落下',title:'無限城へ',text:'駆けつけた柱が無惨に迫るが、鳴女の血鬼術で全員が無限城に落とされた。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'産屋敷邸の結果',when:'大正時代（推定）、産屋敷邸',prev:'刀鍛冶の里の戦い',next:'無限城決戦',factors:["耀哉が無惨の来訪を読んでいた。", "珠世の薬が無惨を弱らせた。"],winner:'none',outcome:'決着なし（最終決戦の始まり）',summary:'当主が命をかけて無惨を足止めし、最終決戦が始まった。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'産屋敷耀哉・妻子が死亡',rate:null,deaths:'不明',dead:["産屋敷耀哉"]}],after:["戦場は無限城に移る。"],note:'漫画16巻、アニメ「柱稽古編」第8話（最終話）。'};
"""
