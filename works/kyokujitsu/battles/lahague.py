from common import land_env, specials, labels
UC=1947.06
ARC='英本土防衛'
OUT='lahague.html'
TITLE='トド作戦迎撃・ラ・アーグ岬 3D俯瞰'
HEAD='トド作戦迎撃・ラ・アーグ岬'
ERA='1947年（推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=6,sky='0x6c7a88')+specials(labels([('ラ・アーグ岬', '仏コタンタン半島', 'E', (0, 14, -40), 3), ('英本土', '', 'A', (0, 12, 50), 3)]))
DATA=r"""
const U=[
 {name:'独上陸部隊',cmd:'トド作戦',side:'E',n:16,k:{0:{p:[10,4,-30],s:'ready',l:'英本土上陸を準備',f:'line'},1:{p:[10,4,-10],s:'move',l:'上陸開始'},2:{p:[10,4,0],s:'fight'},3:{p:[10,4,-24],s:'withdraw'}}},
 {name:'列車砲',cmd:'ラ・アーグ岬',side:'E',n:8,k:{0:{p:[-12,4,-42],s:'ready'},1:{p:[-12,4,-42],s:'fight'},2:{p:[-12,4,-42],s:'broken',l:'破壊工作'},3:{p:[-12,4,-42],s:'gone'}}},
 {name:'晦天・霞部隊',cmd:'霞部隊',side:'A',n:6,k:{0:{p:[-20,4,30],s:'wait',l:'約2000名'},1:{p:[-16,4,-20],s:'move',l:'半潜水強襲艇'},2:{p:[-14,4,-38],s:'charge',l:'列車砲へ'},3:{p:[-16,4,-30],s:'ready'}}},
 {name:'日本武尊',cmd:'大石蔵良',side:'A',n:14,k:{0:{p:[10,4,40],s:'ready',l:'NC作戦',f:'column'},1:{p:[10,4,20],s:'fight'},2:{p:[10,4,10],s:'fight'},3:{p:[10,4,14],s:'ready'}}}
];
const PH=[
 {time:'推定',clock:'',step:'上陸',title:'トド作戦',text:'独が英本土上陸作戦「トド作戦」を始めた。旭日艦隊は迎撃の「NC作戦」で応じた。',cam:{fit:1,th:0.5,ph:.9},arrows:[{p:[[10,4,-30],[10,4,-10]],c:'E'}]},
 {time:'',clock:'',step:'潜入',title:'晦天の出撃',text:'約2000名の霞部隊を乗せた半潜水強襲艇・晦天が、ラ・アーグ岬の列車砲の破壊へ向かった。',cam:{fit:1,th:0.4,ph:.9},arrows:[{p:[[-20,4,30],[-16,4,-20]],c:'A'}]},
 {time:'',clock:'',step:'激戦',title:'列車砲の破壊',text:'岬と海峡で激しい戦いとなった。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:'その後',clock:'',step:'結果',title:'上陸の阻止',text:'旭日艦隊と英国は英本土を守った（推定）。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'トド作戦迎撃の結果',when:'1947年（推定）、英仏海峡・ラ・アーグ岬',prev:'ベルリン空襲とゲルマン砲',next:'ブレスト殴り込み',factors:["特殊部隊で上陸を支える列車砲を狙った。"],winner:'A',outcome:'旭日艦隊・英国の勝利（推定）',summary:'独の英本土上陸作戦に対し、霞部隊が岬の列車砲を襲い、艦隊が海峡で迎え撃った。',sides:[{name:'独上陸部隊',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊・霞部隊',side:'A',cmdr:'大石蔵良',flag:'日本武尊',others:'晦天・霞部隊',before:'霞部隊 約2,000名',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:["英本土は守られた（推定）。"],note:'経過はOVA第7話「トド作戦発動前夜」・第8話「英本土上陸開始」のあらすじ（バンダイチャンネル）による。霞部隊2000名は第8話あらすじの記載。結果と年は推定。'};
"""
