from common import *
UC=1912.09
ARC='無限列車編'
OUT='mugen.html'
TITLE='無限列車の戦い 3D俯瞰'
HEAD='無限列車'
ERA='大正時代（推定）'
SE='鬼'; SA='鬼殺隊'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略で、3Dは抽象図形。部隊の大きさは戦力の目安'
ENV=land_env('0x2a3326','0x56603e',amp=2,seed=5,sky='0x23263a')+specials(labels([('無限列車','乗客が消える列車','A',(0,18,0),3)]))
DATA=r"""
const U=[
{name:'魘夢',cmd:'下弦の壱',side:'E',n:16,k:{0:{p:[0,7,-6],s:'ready',l:'列車と融合'},1:{p:[0,7,0],s:'fight',l:'乗客を眠らせる'},2:{p:[0,7,0],s:'broken',l:'頸を斬られる'},3:{p:[0,7,0],s:'gone'}}},
{name:'猗窩座',cmd:'上弦の参',side:'E',n:8,k:{0:{p:[0,7,-30],s:'hidden'},1:{p:[0,7,-30],s:'hidden'},2:{p:[0,7,-30],s:'hidden'},3:{p:[0,7,-12],s:'fight',l:'煉獄と戦う'}}},
{name:'炭治郎たち',cmd:'炭治郎・善逸・伊之助・禰豆子',side:'A',n:8,k:{0:{p:[-8,7,10],s:'ready'},1:{p:[-8,7,6],s:'fight',l:'夢から覚める'},2:{p:[-6,7,2],s:'fight',l:'魘夢を討つ'},3:{p:[-10,7,10],s:'wait'}}},
{name:'煉獄杏寿郎',cmd:'炎柱',side:'A',n:8,k:{0:{p:[8,7,10],s:'ready'},1:{p:[8,7,4],s:'fight',l:'乗客二百人を守る'},2:{p:[8,7,4],s:'fight'},3:{p:[0,7,-4],s:'fight',l:'戦死'}}}
];
const PH=[
{time:'大正時代（推定）',clock:'2期 無限列車編第1話',step:'乗車',title:'乗客が消える列車',text:'炭治郎たちは炎柱・煉獄杏寿郎と列車に乗り込む。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
{time:'',clock:'第2〜4話',step:'夢',title:'眠りの罠',text:'下弦の壱・魘夢が列車と融合し、乗客と隊士を夢に閉じ込めた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]},
{time:'',clock:'第5話',step:'撃破',title:'魘夢を討つ',text:'炭治郎と伊之助が魘夢の頸の骨を斬り、煉獄が乗客を守った。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
{time:'',clock:'第6〜7話',step:'猗窩座',title:'上弦の参',text:'夜明け前に猗窩座が現れる。煉獄は戦い抜き、猗窩座は日の出を前に逃げた。煉獄は死亡した。',cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={title:'無限列車の結果',when:'大正時代（推定）、無限列車',prev:'那田蜘蛛山の戦い',next:'遊郭の戦い',factors:["煉獄が乗客を一人も死なせずに守った。", "夜明けが近づき、猗窩座が退いた。"],winner:'A',outcome:'乗客を守るが、炎柱が戦死',summary:'鬼殺隊が初めて上弦と戦った。煉獄の死が炭治郎たちを強くする。',sides:[{name:'鬼',side:'E',cmdr:'鬼舞辻無惨',flag:'—',others:'—',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'鬼殺隊',side:'A',cmdr:'産屋敷家',flag:'—',others:'—',before:'不明',loss:'煉獄杏寿郎が戦死',rate:null,deaths:'不明',dead:["煉獄杏寿郎"]}],after:["炭治郎たちは修行を重ね、次の任務へ。"],note:'漫画7〜8巻。劇場版（2020年）とテレビ版「無限列車編」全7話。乗客約200人は作中の数字として広く知られるが、出典の確認は記憶にもとづく。'};
"""
