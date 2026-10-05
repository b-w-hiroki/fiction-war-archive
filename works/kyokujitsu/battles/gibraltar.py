from common import land_env, specials, labels
UC=1945.09
ARC='大西洋派遣'
OUT='gibraltar.html'
TITLE='ジブラルタル要塞攻略戦 3D俯瞰'
HEAD='ジブラルタル要塞攻略戦'
ERA='1945年（照和20年・推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=3,sky='0x7d8fa3')+specials(labels([('ジブラルタル要塞', '独軍の要塞', 'E', (0, 14, -30), 3)]))
DATA=r"""
const U=[
 {name:'ジブラルタル要塞',cmd:'要塞司令官',side:'E',n:16,k:{0:{p:[0,4,-34],s:'ready',l:'巨砲ヘラクレス'},1:{p:[0,4,-34],s:'fight',l:'囮を狙う'},2:{p:[0,4,-34],s:'broken',l:'攻撃を受ける'},3:{p:[0,4,-34],s:'gone',l:'陥落'}}},
 {name:'八咫烏',cmd:'旭日艦隊',side:'A',n:8,k:{0:{p:[20,4,30],s:'move',l:'木造の囮艦',f:'column'},1:{p:[10,4,0],s:'move',l:'目立つ動き'},2:{p:[10,4,0],s:'broken',l:'巨砲の標的に'},3:{p:[10,4,0],s:'gone'}}},
 {name:'前衛遊撃艦隊',cmd:'旭日艦隊',side:'A',n:12,k:{0:{p:[-24,4,40],s:'wait',f:'line'},1:{p:[-20,4,20],s:'move'},2:{p:[-10,4,-10],s:'charge',l:'要塞を攻撃'},3:{p:[-6,4,-16],s:'ready',l:'制圧'}}}
];
const PH=[
 {time:'照和20年',clock:'',step:'準備',title:'囮の木造艦',text:'日本武尊の試験用に造られた木造の同型艦・八咫烏を、前衛遊撃艦隊とともに要塞攻撃に出した。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'囮',title:'巨砲の照準',text:'八咫烏はわざと目立つ動きをし、要塞の巨砲ヘラクレスはこれに照準を合わせた。',cam:{fit:1,th:0.6,ph:.9},arrows:[{p:[[20,4,30],[10,4,0]],c:'A'}]},
 {time:'',clock:'',step:'攻撃',title:'要塞を突く',text:'巨砲が囮に向いたすきに、本命の部隊が要塞を攻めた。',cam:{fit:1,th:0.3,ph:.9},arrows:[{p:[[-20,4,20],[-10,4,-10]],c:'A'}]},
 {time:'その後',clock:'',step:'陥落',title:'要塞の制圧',text:'奇計によって要塞は制圧され、要塞司令官は戦死した。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'ジブラルタル要塞攻略戦の結果',when:'1945年（照和20年・推定）、ジブラルタル',prev:'カナリア諸島沖海戦',next:'北海の戦い（ドイツ本土空襲へ）',factors:["木造の囮艦で要塞の巨砲を引きつけた。"],winner:'A',outcome:'旭日艦隊の勝利（要塞を制圧）',summary:'囮の八咫烏で巨砲を引きつけ、前衛遊撃艦隊が要塞を落とした。地中海の出入口が独軍から奪われた。',sides:[{name:'ジブラルタル要塞守備隊',side:'E',cmdr:'要塞司令官（名は未確認）',flag:'—',others:'—',before:'不明',loss:'要塞陥落、司令官戦死',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊前衛遊撃艦隊',side:'A',cmdr:'大石蔵良（全体指揮）',flag:'八咫烏（囮）',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:["旭日艦隊本隊はドイツ本土空襲を目指す。"],note:'経過はOVA第3話のあらすじ（バンダイチャンネル）と日本語版Wikipediaの記述による。年は前後関係からの推定。兵力は確認できなかった。'};
"""
