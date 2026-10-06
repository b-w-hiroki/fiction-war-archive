from common import *
UC=305.03
ARC='ドラマ独自'
OUT='bells.html'
TITLE='王都の戦い（ドラマS8） 3D俯瞰'
HEAD='王都'
ERA='AC305年'
SE='ラニスター軍'; SA='ターガリエン軍'; PALE='zeon'; PAL='lusi'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x7a705a','0x9a9078',water='0x2a4a5a',amp=3,seed=9,sky='0x8a8070')+specials(labels([('王都キングズ・ランディング', '', 'E', (0, 24, -10), 3)]))
DATA=r"""
const U=[
{name:'ラニスター軍',cmd:'サーセイ・ラニスター',side:'E',n:24,k:{0:{p:[0,7,-6],s:'ready',f:'line'},1:{p:[0,7,-6],s:'fight'},2:{p:[0,7,-6],s:'broken',l:'降伏の鐘'},3:{p:[0,7,-10],s:'broken'}}},
 {name:'鉄の艦隊',cmd:'ユーロン・グレイジョイ',side:'E',n:10,k:{0:{p:[-24,7,-10],s:'ready'},1:{p:[-24,7,-10],s:'broken',l:'ドラゴンが焼く'},2:{s:'gone'},3:{s:'gone'}}},
 {name:'ドロゴン',cmd:'デナーリス・ターガリエン',side:'A',n:4,k:{0:{p:[20,20,30],s:'move'},1:{p:[0,20,0],s:'fight',b:1},2:{p:[0,20,-10],s:'fight',b:1,l:'鐘の後も街を焼く'},3:{p:[0,20,-10],s:'ready'}}},
 {name:'ターガリエン地上軍',cmd:'ジョン・スノウ',side:'A',n:20,k:{0:{p:[0,7,30],s:'ready'},1:{p:[0,7,12],s:'charge'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,0],s:'ready'}}}
];
const PH=[
{time:'AC305年（推定）',clock:'S8E5',step:'布陣',title:'王都へ',text:'デナーリスの軍が王都に迫った。',cam:{fit:1,th:0.5,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'攻撃',title:'ドラゴンの攻撃',text:'ドロゴンが艦隊と城壁の兵器を焼き払い、門が破られた。',cam:{fit:1,th:0.4,ph:0.9},arrows:[{p:[[0,7,30],[0,7,12]],c:'A'}]},
 {time:'',clock:'',step:'鐘',title:'降伏の鐘の後',text:'降伏の鐘が鳴ったあとも、デナーリスは街を焼いた。',cam:{fit:1,th:0.7,ph:0.9},arrows:[]},
 {time:'',clock:'S8E6',step:'終幕',title:'終幕',text:'サーセイは死に、王都は廃墟となった。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'王都の戦いの結果',when:'ドラマS8、王都キングズ・ランディング',prev:'長い夜',next:'—',factors:['ドラゴンが艦隊と防御兵器を破った。','ラニスター軍は戦意を失い降伏した。'],winner:'A',outcome:'ターガリエン側の勝利（王都陥落）',summary:'ドラマ独自の結末。勝利の後の虐殺が、デナーリスの最期につながる。',sides:[{name:'ラニスター軍',side:'E',cmdr:'サーセイ・ラニスター',flag:'—',others:'ユーロン・グレイジョイ',before:'不明',loss:'壊滅',rate:null,deaths:'不明',dead:['サーセイ・ラニスター','ジェイミー・ラニスター']},{name:'ターガリエン軍',side:'A',cmdr:'デナーリス・ターガリエン',flag:'—',others:'ジョン・スノウ',before:'不明',loss:'不明',rate:null,deaths:'—',dead:[]}],after:['ジョンがデナーリスを討つ。','ブランが王に選ばれる。'],note:'ドラマS8E5「鐘」による。AC年はドラマで明示されず、305年は推定。民間人の死者数は示されない。'};
"""
