from common import *
UC=1913.01
ARC='遊郭編'
OUT='yukaku.html'
TITLE='遊郭の戦い 3D俯瞰'
HEAD='遊郭'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x3a2e2a','0x6a5242',amp=1,seed=6,sky='0x2a2232')+specials(labels([('吉原遊郭','花街','A',(0,20,0),3)]))
DATA=r"""
const U=[
{name:'堕姫',cmd:'上弦の陸',side:'E',n:10,k:{0:{p:[-6,7,-6],s:'ready',l:'花魁に化けて潜む'},1:{p:[-6,7,0],s:'fight',l:'帯で人を捕らえる'},2:{p:[-6,7,0],s:'fight'},3:{p:[-6,7,0],s:'broken',l:'頸を斬られる'}}},
{name:'妓夫太郎',cmd:'上弦の陸',side:'E',n:10,k:{0:{p:[6,7,-12],s:'hidden'},1:{p:[6,7,-12],s:'hidden'},2:{p:[6,7,-2],s:'fight',l:'毒の鎌'},3:{p:[6,7,-2],s:'broken',l:'頸を斬られる'}}},
{name:'宇髄天元',cmd:'音柱',side:'A',n:8,k:{0:{p:[0,7,24],s:'ready',l:'潜入を指揮'},1:{p:[4,7,10],s:'move'},2:{p:[6,7,4],s:'fight',l:'毒を受けて戦う'},3:{p:[6,7,6],s:'wait',l:'引退'}}},
{name:'炭治郎たち',cmd:'炭治郎・善逸・伊之助・禰豆子',side:'A',n:10,k:{0:{p:[-10,7,24],s:'move',l:'店に潜入'},1:{p:[-8,7,6],s:'fight'},2:{p:[-2,7,4],s:'fight'},3:{p:[-4,7,10],s:'ready'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'2期 遊郭編第1〜4話',step:'潜入',title:'遊郭への潜入',text:'音柱・宇髄天元が、消えた妻たちを探すため炭治郎たちを遊郭に潜り込ませた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'第5〜7話',step:'堕姫',title:'堕姫との戦い',text:'花魁に化けた上弦の陸・堕姫が正体を現す。禰豆子は鬼の力を強めて戦った。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'第8〜10話',step:'兄妹',title:'妓夫太郎の出現',text:'兄の妓夫太郎が現れる。二人の頸を同時に斬らないと倒せないとわかる。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'第11話',step:'撃破',title:'同時に頸を斬る',text:'宇髄と炭治郎たちが二人の頸を同時に斬り、百年以上変わらなかった上弦を初めて倒した。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'遊郭の結果',when:'大正時代（推定）、吉原遊郭',prev:'無限列車の戦い',next:'刀鍛冶の里の戦い',factors:["二人の頸を同時に斬った。", "禰豆子の血鬼術が毒を焼いた。"],winner:'A',outcome:'鬼殺隊の勝利（上弦の陸を討つ）',summary:'百年以上ぶりに上弦の鬼を倒した戦い。宇髄は引退する。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'宇髄天元が負傷し引退',rate:null,deaths:'不明',dead:[]}],after:["無惨は上弦を集め、刀鍛冶の里を狙う。"],note:'漫画9〜11巻、アニメ「遊郭編」全11話。「百年以上上弦が欠けなかった」は作中の説明（記憶による）。'};
"""
