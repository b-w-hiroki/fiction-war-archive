from common import land_env, specials, labels
UC=1950.03
ARC='反攻'
OUT='fuhrer.html'
TITLE='総統要塞襲撃（烏天狗作戦） 3D俯瞰'
HEAD='総統要塞襲撃（烏天狗作戦）'
ERA='1950年（推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=9,sky='0x5f6c7a')+specials(labels([('総統要塞', 'ヒトラーの拠点', 'E', (0, 14, -40), 3)]))
DATA=r"""
const U=[
 {name:'総統要塞',cmd:'ヒトラー',side:'E',n:14,k:{0:{p:[0,4,-40],s:'ready'},1:{p:[0,4,-40],s:'fight'},2:{p:[0,4,-40],s:'broken',l:'司令室に突入される'},3:{p:[0,4,-40],s:'ready',l:'総統は無事'}}},
 {name:'ホズ',cmd:'コルベ艦長',side:'E',n:6,k:{0:{p:[24,4,-20],s:'hidden'},1:{p:[24,4,-10],s:'move',l:'原爆潜水艦'},2:{p:[20,4,10],s:'charge',l:'自爆を決意'},3:{p:[20,4,10],s:'gone'}}},
 {name:'霞部隊',cmd:'烏天狗作戦',side:'A',n:6,k:{0:{p:[-20,4,30],s:'move'},1:{p:[-10,4,-30],s:'charge',l:'破壊工作'},2:{p:[-4,4,-38],s:'charge',l:'司令室へ'},3:{p:[-16,4,10],s:'withdraw'}}},
 {name:'前衛遊撃艦隊',cmd:'旭日艦隊',side:'A',n:12,k:{0:{p:[10,4,40],s:'ready',f:'line'},1:{p:[14,4,30],s:'fight'},2:{p:[16,4,24],s:'fight'},3:{p:[16,4,28],s:'ready'}}}
];
const PH=[
 {time:'推定',clock:'',step:'潜入',title:'烏天狗作戦',text:'霞部隊がヒトラーの総統要塞に潜入し、破壊工作を行った。',cam:{fit:1,th:0.5,ph:.9},arrows:[{p:[[-20,4,30],[-10,4,-30]],c:'A'}]},
 {time:'',clock:'',step:'突入',title:'司令室へ',text:'部隊は司令室に突入したが、ヒトラーの暗殺はマイントイフェルに阻まれた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'海上',title:'原爆潜水艦ホズ',text:'海では原爆を積んだ潜水艦ホズの艦長コルベが、原子炉を暴走させて自爆する道を選び、艦隊との決戦が迫った。',cam:{fit:1,th:0.6,ph:.9},arrows:[{p:[[24,4,-10],[20,4,10]],c:'E'}]},
 {time:'その後',clock:'',step:'結果',title:'次の局面へ',text:'暗殺は果たせず、戦いは最終話へ続く。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'総統要塞襲撃の結果',when:'時期は推定、総統要塞と周辺海域',prev:'アイスランド沖海戦',next:'OVA最終話「暁の遡上」',factors:["特殊部隊で敵の中枢を直接狙った。"],winner:'none',outcome:'決着なし（暗殺は失敗）',summary:'霞部隊が総統要塞に突入したがヒトラーは生き延びた。海上では原爆潜水艦ホズが自爆を図った。',sides:[{name:'独軍',side:'E',cmdr:'ヒトラー',flag:'—',others:'マイントイフェル、ホズ（コルベ）',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊・霞部隊',side:'A',cmdr:'大石蔵良',flag:'—',others:'前衛遊撃艦隊',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:["戦いはOVA第15話へ続く。"],note:'経過はOVA第14話のあらすじ（バンダイチャンネル）による。年と、アイスランド沖海戦との前後関係は推定。'};
"""
