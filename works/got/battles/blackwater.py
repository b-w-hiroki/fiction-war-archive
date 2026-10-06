from common import *
UC=299.06
ARC='五王の戦争'
OUT='blackwater.html'
TITLE='ブラックウォーターの戦い 3D俯瞰'
HEAD='ブラックウォーター'
ERA='AC299年'
SE='スタニス軍'; SA='王都守備隊'; PALE='misr'; PAL='zeon'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a4a','0x8a8670',water='0x2a3a4a',amp=3,seed=3,sky='0x5a4a40')+specials(labels([('王都キングズ・ランディング', 'ブラックウォーター湾', 'A', (0, 22, 30), 3), ('ブラックウォーター川', '', 'E', (0, 10, 0), 2)]))
DATA=r"""
const U=[
{name:'スタニス艦隊',cmd:'スタニス・バラシオン',side:'E',n:30,k:{0:{p:[0,7,-30],s:'move',f:'line',l:'約200隻（AWOIAF）'},1:{p:[0,7,-6],s:'fight'},2:{p:[0,7,-2],s:'broken',l:'鬼火で炎上'},3:{p:[0,7,-10],s:'broken'},4:{s:'gone'}}},
 {name:'スタニス上陸部隊',cmd:'スタニス・バラシオン',side:'E',n:16,k:{0:{p:[-20,7,-20],s:'move'},1:{p:[-14,7,-4],s:'move'},2:{p:[-10,7,16],s:'charge',l:'城壁に迫る'},3:{p:[-10,7,14],s:'fight'},4:{p:[-14,7,0],s:'withdraw',l:'敗走'}}},
 {name:'王都守備隊',cmd:'ティリオン・ラニスター',side:'A',n:12,k:{0:{p:[0,7,24],s:'ready'},1:{p:[0,7,22],s:'fight',l:'鬼火の罠'},2:{p:[-6,7,20],s:'fight',l:'ティリオン出撃'},3:{p:[-6,7,20],s:'fight'},4:{p:[0,7,22],s:'ready'}}},
 {name:'ラニスター・タイレル援軍',cmd:'タイウィン・ラニスター',side:'A',n:24,k:{0:{s:'hidden',p:[40,7,10]},1:{s:'hidden',p:[40,7,10]},2:{s:'hidden',p:[40,7,10]},3:{p:[14,7,6],s:'charge',l:'側面から到着'},4:{p:[-2,7,4],s:'ready'}}}
];
const PH=[
{time:'AC299年',clock:'原作2部／S2E9',step:'来襲',title:'艦隊の来襲',text:'スタニスが王位を求め、大艦隊で王都に迫った。王都の兵は大幅に少なかった。',cam:{fit:1,th:0.4,ph:0.9},arrows:[{p:[[0,7,-30],[0,7,-6]],c:'E'}]},
 {time:'',clock:'',step:'鬼火',title:'鬼火の罠',text:'ティリオンは湾に鬼火（ワイルドファイア）を仕掛け、敵艦隊を焼き払った。',cam:{fit:1,th:0.6,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'城壁',title:'城壁の攻防',text:'上陸した部隊が城門に迫り、ティリオンが自ら出撃して食い止めた。',cam:{fit:1,th:0.3,ph:0.9},arrows:[]},
 {time:'',clock:'S2E10',step:'援軍',title:'援軍の到着',text:'タイウィンとタイレル家の援軍が側面を突き、スタニス軍は崩れた。',cam:{fit:1,th:0.7,ph:0.9},arrows:[{p:[[40,7,10],[14,7,6]],c:'A'}]},
 {time:'',clock:'',step:'撤退',title:'スタニスの敗走',text:'スタニスは残った船で撤退。ラニスターとタイレルの同盟が固まる。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'ブラックウォーターの戦いの結果',when:'AC299年、王都キングズ・ランディング',prev:'緑の支流の戦い',next:'紅き婚礼',factors:['鬼火で敵艦隊の多くを焼いた。','ティリオンが城門で時間を稼いだ。','タイレル家との同盟で援軍が間に合った。'],winner:'A',outcome:'王都側の勝利',summary:'スタニスの王都攻略が失敗し、ラニスターとタイレルの同盟が成立した。',sides:[{name:'スタニス軍',side:'E',cmdr:'スタニス・バラシオン',flag:'—',others:'サラドール・サーン',before:'艦船 約200隻（AWOIAF）',loss:'130〜140隻が焼失（AWOIAF）',rate:null,deaths:'騎士619人など（AWOIAF）',dead:[]},{name:'王都守備隊・援軍',side:'A',cmdr:'ティリオン・ラニスター',flag:'—',others:'タイウィン・ラニスター、メイス・タイレル',before:'守備隊 7000〜8000（AWOIAF）',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['タイレル家がラニスター家と結ぶ。','スタニスはドラゴンストーンへ退く。'],note:'兵力・損害はA Wiki of Ice and Fire「Battle of the Blackwater」による（小説準拠）。ドラマはS2E9「ブラックウォーター」。'};
"""
