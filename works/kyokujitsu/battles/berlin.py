from common import land_env, specials, labels
UC=1946.08
ARC='英本土防衛'
OUT='berlin.html'
TITLE='ベルリン空襲とゲルマン砲 3D俯瞰'
HEAD='ベルリン空襲とゲルマン砲'
ERA='1946年（推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=5,sky='0x6c7a88')+specials(labels([('ドーバー沖', '英仏海峡', 'A', (0, 12, 10), 3), ('ゲルマン砲', '独の巨砲', 'E', (0, 14, -50), 3)]))
DATA=r"""
const U=[
 {name:'ゲルマン砲',cmd:'ヒトラーの命令',side:'E',n:12,k:{0:{p:[0,4,-50],s:'ready'},1:{p:[0,4,-50],s:'ready'},2:{p:[0,4,-50],s:'fight',l:'報復の砲撃'},3:{p:[0,4,-50],s:'ready'}}},
 {name:'八咫烏',cmd:'旭日艦隊',side:'A',n:8,k:{0:{p:[0,4,14],s:'ready',l:'日本武尊に見せた囮'},1:{p:[0,4,14],s:'ready'},2:{p:[0,4,14],s:'broken',l:'砲撃を受ける'},3:{p:[0,4,14],s:'gone'}}},
 {name:'旭日艦隊・英空軍',cmd:'大石蔵良',side:'A',n:10,k:{0:{p:[-20,4,40],s:'move',l:'ベルリンへ'},1:{p:[-20,4,-30],s:'charge',l:'ベルリン空襲'},2:{p:[-24,4,30],s:'withdraw'},3:{p:[-24,4,36],s:'ready'}}}
];
const PH=[
 {time:'照和21年（推定）',clock:'',step:'空襲',title:'ベルリン空襲',text:'旭日艦隊と英国空軍がベルリンを空襲した。',cam:{fit:1,th:0.5,ph:.9},arrows:[{p:[[-20,4,40],[-20,4,-30]],c:'A'}]},
 {time:'',clock:'',step:'報復',title:'ヒトラーの命令',text:'ヒトラーはドーバー沖の日本戦艦をゲルマン砲で撃てと命じた。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'砲撃',title:'囮への砲撃',text:'砲撃を受けたのは日本武尊ではなく、大石が置いた囮の八咫烏だった。',cam:{fit:1,th:0.3,ph:.9},arrows:[{p:[[0,4,-50],[0,4,14]],c:'E'}]},
 {time:'その後',clock:'',step:'結果',title:'巨砲の位置',text:'独は空襲の報復に失敗し、巨砲の存在が明らかになった。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'ベルリン空襲とゲルマン砲の結果',when:'1946年（推定）、ベルリン・ドーバー沖',prev:'北海の戦い',next:'トド作戦迎撃（NC作戦）',factors:["囮で巨砲の報復を空振りさせた。"],winner:'A',outcome:'旭日艦隊・英国の優勢',summary:'ベルリン空襲の報復にヒトラーが巨砲を撃たせたが、狙われたのは囮艦だった。',sides:[{name:'独軍',side:'E',cmdr:'ヒトラー',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊・英空軍',side:'A',cmdr:'大石蔵良',flag:'—',others:'—',before:'不明',loss:'囮艦八咫烏',rate:null,deaths:'不明',dead:[]}],after:["独は英本土上陸（トド作戦）の準備を進める。"],note:'OVA第5話「ゲルマン砲台殲滅戦」のあらすじ（バンダイチャンネル）による。年は推定。数値は確認できなかった。'};
"""
