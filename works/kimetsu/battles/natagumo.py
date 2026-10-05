from common import *
UC=1912.06
ARC='立志編'
OUT='natagumo.html'
TITLE='那田蜘蛛山の戦い 3D俯瞰'
HEAD='那田蜘蛛山'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x22301e','0x4a5a3a',amp=8,seed=4,sky='0x1e2236')+specials(labels([('那田蜘蛛山','蜘蛛の鬼の一家の巣','A',(0,28,0),3)]))
DATA=r"""
const U=[
{name:'累',cmd:'下弦の伍',side:'E',n:8,k:{0:{p:[0,7,-20],s:'ready',l:'山の奥で待つ'},1:{p:[0,7,-14],s:'wait'},2:{p:[0,7,-6],s:'fight',l:'炭治郎と戦う'},3:{p:[0,7,-6],s:'broken',l:'冨岡に斬られる'}}},
{name:'蜘蛛の鬼の一家',cmd:'累の「家族」',side:'E',n:14,k:{0:{p:[-14,7,-10],s:'ready'},1:{p:[-10,7,0],s:'charge',l:'隊士を糸で操る'},2:{p:[-10,7,0],s:'broken',l:'伊之助・胡蝶が討つ'},3:{p:[-10,7,0],s:'gone'}}},
{name:'先発の隊士',cmd:'炭治郎・善逸・伊之助',side:'A',n:10,k:{0:{p:[0,7,24],s:'move',l:'山に入る'},1:{p:[-4,7,10],s:'fight',l:'多数の隊士が倒れる'},2:{p:[0,7,6],s:'fight',l:'ヒノカミ神楽'},3:{p:[0,7,12],s:'ready'}}},
{name:'柱',cmd:'冨岡義勇・胡蝶しのぶ',side:'A',n:6,k:{0:{p:[10,7,30],s:'hidden'},1:{p:[10,7,30],s:'hidden'},2:{p:[8,7,14],s:'move',l:'救援に入る'},3:{p:[2,7,0],s:'fight',l:'累の頸を斬る'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'1期第15話',step:'潜入',title:'山へ',text:'鬼殺隊の隊士が那田蜘蛛山に送り込まれるが、次々と連絡を絶つ。炭治郎たちも後を追う。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'1期第16〜18話',step:'家族',title:'蜘蛛の鬼の一家',text:'累が作った「家族」の鬼が糸で隊士を操り、多くの隊士が倒れた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'1期第19話',step:'神楽',title:'ヒノカミ神楽',text:'炭治郎は累と戦い、父の神楽を思い出して技を放つ。禰豆子も血鬼術で加勢した。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'1期第20〜21話',step:'柱',title:'柱の到着',text:'冨岡義勇が累を斬り、胡蝶しのぶが残る鬼を討った。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'那田蜘蛛山の結果',when:'大正時代（推定）、那田蜘蛛山',prev:'藤襲山 最終選別',next:'無限列車の戦い',factors:["柱二人が救援に入った。", "禰豆子が血鬼術で炭治郎を助けた。"],winner:'A',outcome:'鬼殺隊の勝利（下弦の伍を討つ）',summary:'炭治郎たちが初めて十二鬼月と戦った山。柱の力の大きさが示された。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'不明（多数の隊士が死亡）',rate:null,deaths:'不明',dead:[]}],after:["炭治郎と禰豆子は柱合会議にかけられ、お館様が二人を認める。"],note:'漫画4〜5巻、アニメ第1期第15〜21話（英語版Wikipediaのエピソード一覧で範囲を確認、区切りは一部推定）。隊士の死者数は作中に示されない。'};
"""
