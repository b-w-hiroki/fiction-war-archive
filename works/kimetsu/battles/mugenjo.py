from common import *
UC=1914.02
ARC='最終決戦'
OUT='mugenjo.html'
TITLE='無限城決戦 3D俯瞰'
HEAD='無限城'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x3a2e22','0x6a5236',amp=1,seed=9,sky='0x1a1420')+specials(labels([('無限城','鳴女の血鬼術の城','A',(0,24,0),3)]))
DATA=r"""
const U=[
{name:'猗窩座',cmd:'上弦の参',side:'E',n:8,k:{0:{p:[-14,7,-8],s:'ready'},1:{p:[-14,7,-2],s:'fight',l:'炭治郎・義勇と戦う'},2:{p:[-14,7,-2],s:'broken',l:'自ら消える'},3:{p:[-14,7,-2],s:'gone'}}},
{name:'童磨',cmd:'上弦の弐',side:'E',n:8,k:{0:{p:[0,7,-8],s:'ready'},1:{p:[0,7,-2],s:'fight',l:'しのぶを殺す'},2:{p:[0,7,-2],s:'broken',l:'カナヲ・伊之助が討つ'},3:{p:[0,7,-2],s:'gone'}}},
{name:'黒死牟',cmd:'上弦の壱',side:'E',n:10,k:{0:{p:[14,7,-8],s:'ready'},1:{p:[14,7,-2],s:'fight'},2:{p:[14,7,-2],s:'fight'},3:{p:[14,7,-2],s:'broken',l:'頸を斬られ崩れる'}}},
{name:'炭治郎・冨岡',cmd:'水柱',side:'A',n:6,k:{0:{p:[-14,7,16],s:'move'},1:{p:[-14,7,6],s:'fight'},2:{p:[-14,7,6],s:'ready'},3:{p:[-10,7,10],s:'move'}}},
{name:'胡蝶・カナヲ・伊之助',cmd:'蟲柱',side:'A',n:6,k:{0:{p:[0,7,16],s:'move'},1:{p:[0,7,6],s:'fight'},2:{p:[0,7,6],s:'ready'},3:{p:[0,7,10],s:'move'}}},
{name:'悲鳴嶼・不死川・時透・玄弥',cmd:'岩柱・風柱・霞柱',side:'A',n:10,k:{0:{p:[14,7,16],s:'move'},1:{p:[14,7,8],s:'move'},2:{p:[14,7,6],s:'fight'},3:{p:[14,7,6],s:'fight',l:'時透・玄弥が戦死'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'漫画16〜17巻',step:'分断',title:'城に落とされる',text:'鬼殺隊は無限城の中で分断され、それぞれ上弦と出会う。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'漫画18巻',step:'参・弐',title:'猗窩座と童磨',text:'炭治郎と義勇が猗窩座を追い詰める。しのぶは童磨に殺されるが、体内の毒で童磨を弱らせた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'漫画19巻',step:'撃破',title:'上弦の参・弐を討つ',text:'猗窩座は自ら消え、童磨はカナヲと伊之助に頸を斬られた。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'漫画19〜20巻',step:'壱',title:'黒死牟との戦い',text:'悲鳴嶼・不死川・時透・玄弥が黒死牟と戦う。時透と玄弥を失いながら倒した。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'無限城の結果',when:'大正時代（推定）、無限城',prev:'産屋敷邸襲撃',next:'無惨との最終決戦',factors:["しのぶが命と引き換えに毒を残した。", "柱たちが痣と赫刀で力を上げた。"],winner:'A',outcome:'鬼殺隊の勝利（上弦の壱・弐・参を討つ）',summary:'上弦をすべて失わせた戦い。柱を含む多くの犠牲を払った。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'上弦の壱・弐・参が消滅',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'多数（柱を含む）',rate:null,deaths:'不明',dead:["胡蝶しのぶ", "時透無一郎", "不死川玄弥"]}],after:["無限城が崩れ、戦いは地上に出る。"],note:'漫画16〜20巻（英語版Wikipedia巻リストで確認）。アニメは劇場版「無限城編」三部作（第一章は2025年公開）。上弦の陸の後任（獪岳）は善逸が討つが図では省略。'};
"""
