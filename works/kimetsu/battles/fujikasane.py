from common import *
UC=1912.02
ARC='立志編'
OUT='fujikasane.html'
TITLE='藤襲山 最終選別 3D俯瞰'
HEAD='藤襲山'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x3a4a32','0x6a7a52',amp=5,seed=2,sky='0x3a3e52')+specials(labels([('藤襲山','藤の花に囲まれた山','A',(0,24,0),3)]))
DATA=r"""
const U=[
{name:'手鬼',cmd:'鬼',side:'E',n:12,k:{0:{p:[0,7,-14],s:'ready',l:'山に閉じ込められた鬼'},1:{p:[0,7,-6],s:'charge',l:'受験者を襲う'},2:{p:[0,7,-2],s:'broken',l:'頸を斬られる'},3:{p:[0,7,-2],s:'gone'}}},
{name:'竈門炭治郎',cmd:'受験者',side:'A',n:4,k:{0:{p:[0,7,20],s:'ready',l:'鱗滝の弟子'},1:{p:[0,7,8],s:'fight'},2:{p:[0,7,4],s:'fight',l:'頸を斬る'},3:{p:[0,7,10],s:'ready',l:'七日を生き延びる'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'漫画1巻',step:'選別',title:'最終選別',text:'炭治郎は鬼殺隊に入るため、鬼が閉じ込められた藤襲山で七日間を生き延びる試験に臨んだ。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'手鬼',title:'手鬼との戦い',text:'鱗滝の弟子を何人も食ってきた手鬼が現れる。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'',step:'撃破',title:'頸を斬る',text:'炭治郎は修行で鍛えた技で手鬼の頸を斬った。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'',step:'合格',title:'合格',text:'炭治郎は生き残り、鬼殺隊の剣士となった。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'藤襲山の結果',when:'大正時代（推定）、藤襲山',prev:'—',next:'那田蜘蛛山の戦い',factors:["鱗滝のもとでの修行。", "錆兎・真菰の導き（原作の描写）。"],winner:'A',outcome:'炭治郎の合格',summary:'炭治郎が鬼殺隊に入った試験。鱗滝の弟子たちの仇を討った。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:["炭治郎は日輪刀を受け取り、任務に出る。"],note:'展開は原作漫画1巻・アニメ第1期第4〜5話にもとづく（話数は推定）。数値は作中に示されない。'};
"""
