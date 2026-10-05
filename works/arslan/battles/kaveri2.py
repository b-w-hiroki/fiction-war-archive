from common import land_env, specials, labels
UC=324.1
ARC='第二部'
OUT='kaveri2.html'
TITLE='カーヴェリー河の戦い（対チュルク） 3D俯瞰'
HEAD='チュルク'
ERA='パルス暦324年秋（推定）'
SE='チュルク軍'; SA='パルス・シンドゥラ連合'; PALE='turan'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作小説にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6a40','0x9a9468',amp=5,seed=26,water='0x3a5a68')+specials(labels([('カーヴェリー河', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'チュルク軍',cmd:'将軍ゴラーブ',side:'E',n:24,k:{0:{p:[0,7,-30],s:'move',l:'約1万'},1:{p:[0,7,-8],s:'fight'},2:{p:[0,7,-14],s:'broken',l:'ゴラーブ捕らわる'}}},
 {name:'パルス・シンドゥラ連合',cmd:'パルス軍・ラジェンドラ',side:'A',n:50,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'約3万'},1:{p:[0,7,8],s:'fight',f:'concave'},2:{p:[0,7,-6],s:'charge'}}}
];
const PH=[
{time:'324年秋',clock:'',step:'侵攻',title:'チュルクの侵攻',text:'山岳の国チュルクの軍約1万が、シンドゥラとパルスの国境地帯に入った。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,7,-30],[0,7,-8]],c:'E'}]},
 {time:'',clock:'',step:'迎撃',title:'連合軍の迎撃',text:'パルスとシンドゥラの連合軍約3万が迎え撃った。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'捕縛',title:'敵将の捕縛',text:'チュルク軍は敗れ、将軍ゴラーブが捕らえられた。のちに送り返される。',cam:{fit:1,th:.3,ph:.9},arrows:[]}
];
const RESULT={title:'カーヴェリー河の戦い（対チュルク）の結果',when:'パルス暦324年秋（推定）、カーヴェリー河',prev:'ディジレ河の戦い',next:'仮面兵団のシンドゥラ侵攻（325年）',
 factors:['パルスとシンドゥラが同盟して、兵力で3倍になった。'],winner:'A',outcome:'パルス・シンドゥラ連合の勝利',
 summary:'東のチュルクの侵入を、パルスとシンドゥラの同盟が退けた。第一部で結んだ同盟が機能した戦い。',
 sides:[{name:'チュルク軍',side:'E',cmdr:'ゴラーブ',flag:'—',others:'—',before:'約10,000',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'パルス・シンドゥラ連合',side:'A',cmdr:'不明',flag:'—',others:'ラジェンドラ二世',before:'約30,000',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['チュルクはその後、ヒルメスの仮面兵団と組んで再び侵攻する。'],
 note:'時期は推定。兵力は原作8巻の要約による。陣営色はチュルクを便宜上トゥラーンと同系色で示した。'};
"""
