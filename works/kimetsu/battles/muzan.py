from common import *
UC=1914.03
ARC='最終決戦'
OUT='muzan.html'
TITLE='無惨との最終決戦 3D俯瞰'
HEAD='夜明け'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x3a3a34','0x6a6a5a',amp=1,seed=10,sky='0x2a3044')+specials(labels([('市街','無限城が崩れた後の地上','A',(0,22,0),3)]))
DATA=r"""
const U=[
{name:'鬼舞辻無惨',cmd:'鬼の始祖',side:'E',n:16,k:{0:{p:[0,7,-4],s:'ready',l:'地上に出る'},1:{p:[0,7,0],s:'fight',l:'柱を圧倒する'},2:{p:[0,7,0],s:'fight',l:'薬で弱る'},3:{p:[0,7,0],s:'broken',l:'日光で消える'}}},
{name:'柱',cmd:'悲鳴嶼・不死川・冨岡・伊黒・甘露寺',side:'A',n:14,k:{0:{p:[0,7,20],s:'charge'},1:{p:[0,7,8],s:'fight',l:'夜明けまで引き留める'},2:{p:[0,7,8],s:'fight'},3:{p:[0,7,12],s:'ready'}}},
{name:'炭治郎たち',cmd:'炭治郎・善逸・伊之助・カナヲ',side:'A',n:10,k:{0:{p:[-12,7,20],s:'move'},1:{p:[-10,7,10],s:'fight'},2:{p:[-6,7,6],s:'fight',l:'日の呼吸'},3:{p:[-8,7,12],s:'ready'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'漫画21巻',step:'地上',title:'地上での戦い',text:'無惨は無限城を出て地上で戦う。夜明けまで引き留めることが鬼殺隊の目標になった。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'漫画21〜22巻',step:'消耗',title:'柱の消耗',text:'無惨の攻撃で柱と隊士が次々と倒れる。珠世の薬が無惨を少しずつ弱らせた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'漫画22〜23巻',step:'日の呼吸',title:'日の呼吸',text:'炭治郎が日の呼吸の型をつなぎ、無惨を押さえ込む。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'漫画23巻',step:'夜明け',title:'夜明け',text:'日が昇り、無惨は消えた。鬼殺隊はその後、解散した。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'夜明けの結果',when:'大正時代（推定）、市街地',prev:'無限城決戦',next:'—',factors:["夜明けまで無惨を引き留めた。", "珠世としのぶの薬が無惨を弱らせた。"],winner:'A',outcome:'鬼殺隊の勝利（無惨の消滅）',summary:'千年続いた鬼と鬼殺隊の戦いが終わった。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'無惨が消滅',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'多数（柱を含む）',rate:null,deaths:'不明',dead:["悲鳴嶼行冥", "伊黒小芭内", "甘露寺蜜璃", "珠世"]}],after:["鬼殺隊は解散した。"],note:'漫画21〜23巻（英語版Wikipedia巻リストで確認）。アニメ化は2026年時点で未確認。'};
"""
