from common import *
UC=1913.05
ARC='刀鍛冶の里編'
OUT='katanakaji.html'
TITLE='刀鍛冶の里の戦い 3D俯瞰'
HEAD='刀鍛冶の里'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x2e3a2a','0x6a6a4e',amp=7,seed=7,sky='0x2a2e44')+specials(labels([('刀鍛冶の里','日輪刀を打つ里','A',(0,26,0),3)]))
DATA=r"""
const U=[
{name:'半天狗',cmd:'上弦の肆',side:'E',n:12,k:{0:{p:[-8,7,-14],s:'ready',l:'分身する鬼'},1:{p:[-8,7,-4],s:'fight'},2:{p:[-8,7,-4],s:'fight',l:'本体が逃げる'},3:{p:[-8,7,-4],s:'broken',l:'夜明けに頸を斬られる'}}},
{name:'玉壺',cmd:'上弦の伍',side:'E',n:8,k:{0:{p:[10,7,-14],s:'ready',l:'壺の鬼'},1:{p:[10,7,-4],s:'fight',l:'里の人々を襲う'},2:{p:[10,7,-4],s:'broken',l:'時透に斬られる'},3:{p:[10,7,-4],s:'gone'}}},
{name:'炭治郎・玄弥・禰豆子',cmd:'',side:'A',n:8,k:{0:{p:[-8,7,20],s:'ready'},1:{p:[-8,7,6],s:'fight'},2:{p:[-8,7,4],s:'fight'},3:{p:[-6,7,4],s:'ready',l:'禰豆子が日光を克服'}}},
{name:'甘露寺蜜璃・時透無一郎',cmd:'恋柱・霞柱',side:'A',n:8,k:{0:{p:[8,7,22],s:'ready'},1:{p:[10,7,6],s:'fight'},2:{p:[6,7,2],s:'fight',l:'時透が痣を出す'},3:{p:[2,7,4],s:'ready'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'3期第1〜2話',step:'来訪',title:'里で刀を待つ',text:'炭治郎は新しい刀を求めて刀鍛冶の里を訪れ、恋柱・霞柱と出会う。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'3期第3〜6話',step:'襲撃',title:'上弦二体の襲撃',text:'夜、上弦の肆・半天狗と上弦の伍・玉壺が里を襲った。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'3期第7〜9話',step:'痣',title:'痣の発現',text:'時透が痣を出して玉壺を斬った。甘露寺は半天狗の分身を押さえた。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'3期第10〜11話',step:'夜明け',title:'日光を克服',text:'夜明け、炭治郎は半天狗の本体を斬った。禰豆子は日光を浴びても消えなかった。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'刀鍛冶の里の結果',when:'大正時代（推定）、刀鍛冶の里',prev:'遊郭の戦い',next:'産屋敷邸襲撃',factors:["柱二人が痣を出して力を上げた。", "夜明けまで戦い抜いた。"],winner:'A',outcome:'鬼殺隊の勝利（上弦二体を討つ）',summary:'上弦二体を倒し、禰豆子が日光を克服した。無惨は禰豆子を狙い始める。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'不明（里の人々に犠牲）',rate:null,deaths:'不明',dead:[]}],after:["鬼殺隊は柱稽古で全体の力を上げる。"],note:'漫画12〜15巻、アニメ「刀鍛冶の里編」全11話。犠牲者数は作中に示されない。'};
"""
