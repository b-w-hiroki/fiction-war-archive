from common import land_env, specials, labels
UC=1945.06
ARC='大西洋派遣'
OUT='canary.html'
TITLE='カナリア諸島沖海戦 3D俯瞰'
HEAD='カナリア諸島沖海戦'
ERA='1945年（照和20年・月は不明）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=2,sky='0x7d8fa3')+specials(labels([('カナリア諸島沖', '大西洋', 'A', (0, 12, 0), 3)]))
DATA=r"""
const U=[
 {name:'ビスマルクII世',cmd:'ドイツ海軍',side:'E',n:14,k:{0:{p:[0,4,-50],s:'move',l:'高速戦艦が出港',f:'column'},1:{p:[-6,4,-25],s:'fight'},2:{p:[-6,4,-20],s:'broken',l:'戦闘不能'},3:{p:[-20,4,-50],s:'withdraw'}}},
 {name:'シャルンホルスト',cmd:'ドイツ海軍',side:'E',n:10,k:{0:{p:[14,4,-46],s:'move',l:'巡洋戦艦',f:'column'},1:{p:[10,4,-18],s:'fight',l:'先に砲戦'},2:{p:[8,4,-12],s:'gone',l:'撃沈'},3:{p:[8,4,-12],s:'gone'}}},
 {name:'日本武尊',cmd:'大石蔵良',side:'A',n:16,k:{0:{p:[0,4,40],s:'move',l:'旭日艦隊旗艦',f:'column'},1:{p:[4,4,20],s:'fight',l:'51cm砲'},2:{p:[0,4,14],s:'fight'},3:{p:[0,4,20],s:'ready',l:'損傷なし'}}},
 {name:'旭日艦隊',cmd:'大石蔵良',side:'A',n:10,k:{0:{p:[-20,4,48],s:'ready',f:'line'},1:{p:[-20,4,34],s:'ready'},2:{p:[-16,4,28],s:'fight'},3:{p:[-16,4,30],s:'ready'}}}
];
const PH=[
 {time:'照和20年',clock:'',step:'接近',title:'独戦艦の出撃',text:'喜望峰沖で独潜水艦隊を破り、ジブラルタル基地の装甲空母を沈めた旭日艦隊に対し、独の高速戦艦ビスマルクII世と巡洋戦艦シャルンホルストが出てきた。',cam:{fit:1,th:0.4,ph:.9},arrows:[{p:[[0,4,-50],[-6,4,-25]],c:'E'},{p:[[0,4,40],[4,4,20]],c:'A'}]},
 {time:'',clock:'',step:'砲戦',title:'日本武尊の砲撃',text:'日本武尊は51cm主砲で独艦と撃ち合った。',cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:'',clock:'',step:'決着',title:'シャルンホルスト撃沈',text:'シャルンホルストは撃沈され、ビスマルクII世も戦闘不能となった。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:'その後',clock:'',step:'戦後',title:'大西洋の制海',text:'旭日艦隊は大西洋での足場を固め、次のジブラルタル攻略へ向かう。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'カナリア諸島沖海戦の結果',when:'1945年（照和20年）、カナリア諸島沖',prev:'喜望峰沖の対潜戦・ジブラルタル基地奇襲',next:'ジブラルタル要塞攻略',factors:["日本武尊の51cm主砲が独艦の砲を上回った。"],winner:'A',outcome:'旭日艦隊の勝利',summary:'日本武尊がシャルンホルストを沈め、ビスマルクII世を戦闘不能にした。旭日艦隊の大西洋での初の艦隊決戦。',sides:[{name:'独水上部隊',side:'E',cmdr:'不明',flag:'ビスマルクII世',others:'シャルンホルスト',before:'不明',loss:'シャルンホルスト撃沈、ビスマルクII世戦闘不能',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊',side:'A',cmdr:'大石蔵良',flag:'日本武尊',others:'—',before:'不明（艦隊全体は約40隻）',loss:'日本武尊は損傷なし',rate:null,deaths:'不明',dead:[]}],after:["旭日艦隊がジブラルタル攻略に向かう。"],note:'戦果は日本語版Wikipedia「日本武尊 (旭日の艦隊)」「旭日の艦隊」の記述による。年は同記事の照和20年。月と兵力は確認できなかった。'};
"""
