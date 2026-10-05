from common import land_env, specials, labels
UC=1946.05
ARC='英本土防衛'
OUT='northsea.html'
TITLE='北海の戦い（ホルス16） 3D俯瞰'
HEAD='北海の戦い（ホルス16）'
ERA='1946年（照和21年・推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=4,sky='0x6c7a88')+specials(labels([('北海', '英本土の東', 'A', (0, 12, 0), 3)]))
DATA=r"""
const U=[
 {name:'ホルス16',cmd:'ドイツ空軍',side:'E',n:8,k:{0:{p:[0,4,-50],s:'move',l:'円盤型の秘密兵器'},1:{p:[0,4,-10],s:'charge',l:'艦隊を襲う'},2:{p:[0,4,4],s:'fight'},3:{p:[0,4,-40],s:'withdraw'}}},
 {name:'日本武尊',cmd:'大石蔵良',side:'A',n:16,k:{0:{p:[0,4,30],s:'move',l:'ドイツ本土へ',f:'column'},1:{p:[0,4,24],s:'fight',l:'対空戦'},2:{p:[0,4,22],s:'broken',l:'左舷に被雷'},3:{p:[0,4,26],s:'ready',l:'作戦継続'}}},
 {name:'旭日艦隊本隊',cmd:'大石蔵良',side:'A',n:10,k:{0:{p:[-18,4,36],s:'move',f:'line'},1:{p:[-16,4,30],s:'fight'},2:{p:[-14,4,26],s:'fight'},3:{p:[-16,4,30],s:'ready'}}}
];
const PH=[
 {time:'照和21年（推定）',clock:'',step:'進出',title:'ドイツ本土を目指す',text:'ジブラルタル陥落後、旭日艦隊本隊はドイツ本土空襲を目指して北の海へ進んだ。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'襲撃',title:'ホルス16の出現',text:'独の秘密兵器、円盤型のホルス16が艦隊を襲った。',cam:{fit:1,th:0.6,ph:.9},arrows:[{p:[[0,4,-50],[0,4,-10]],c:'E'}]},
 {time:'',clock:'',step:'被害',title:'日本武尊の被雷',text:'日本武尊は左舷の喫水線の上に被雷したが、戦い続けた。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:'その後',clock:'',step:'継続',title:'作戦続行',text:'艦隊は損傷を負いながら作戦を続けた。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'北海の戦いの結果',when:'1946年（照和21年・推定）、北海',prev:'ジブラルタル要塞攻略戦',next:'ベルリン空襲とゲルマン砲',factors:["日本武尊の防御力で損傷に耐えた。"],winner:'A',outcome:'旭日艦隊が作戦を継続（決着は限定的）',summary:'新兵器ホルス16の攻撃で日本武尊が損傷したが、艦隊は作戦を続けた。',sides:[{name:'独軍（ホルス16）',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊本隊',side:'A',cmdr:'大石蔵良',flag:'日本武尊',others:'—',before:'不明',loss:'日本武尊が左舷に被雷',rate:null,deaths:'不明',dead:[]}],after:["旭日艦隊と英空軍がベルリン空襲へ。"],note:'OVA第4話のあらすじ（バンダイチャンネル）と、Wikipedia「日本武尊 (旭日の艦隊)」の照和21年・心臓作戦でのホルス16被雷の記述を合わせた。両者が同じ戦いかは推定。'};
"""
