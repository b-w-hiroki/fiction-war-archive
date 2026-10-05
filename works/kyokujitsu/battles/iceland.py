from common import land_env, specials, labels
UC=1949.12
ARC='反攻'
OUT='iceland.html'
TITLE='アイスランド沖海戦 3D俯瞰'
HEAD='アイスランド沖海戦'
ERA='1949年12月（照和24年12月）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=8,sky='0x8a99a8')+specials(labels([('アイスランド沖', '北大西洋', 'A', (0, 12, 0), 3)]))
DATA=r"""
const U=[
 {name:'独第一機動艦隊',cmd:'独海軍',side:'E',n:16,k:{0:{p:[0,4,-50],s:'move',l:'旗艦ロートリンゲン',f:'concave'},1:{p:[0,4,-30],s:'fight',l:'航空攻撃'},2:{p:[0,4,-24],s:'broken'},3:{p:[0,4,-24],s:'gone',l:'旗艦撃沈'}}},
 {name:'旭日艦隊機動部隊',cmd:'旭日艦隊',side:'A',n:12,k:{0:{p:[-20,4,44],s:'ready',f:'line'},1:{p:[-20,4,36],s:'fight',l:'航空戦'},2:{p:[-18,4,30],s:'fight'},3:{p:[-18,4,32],s:'ready'}}},
 {name:'日本武尊',cmd:'大石蔵良',side:'A',n:16,k:{0:{p:[14,4,40],s:'ready',f:'column'},1:{p:[14,4,20],s:'move'},2:{p:[8,4,-10],s:'charge',l:'とどめ'},3:{p:[8,4,0],s:'ready',l:'損傷なし'}}}
];
const PH=[
 {time:'照和24年12月',clock:'',step:'接近',title:'独機動艦隊',text:'北大西洋のアイスランド沖で、独の第一機動艦隊と旭日艦隊が向き合った。',cam:{fit:1,th:0.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'航空戦',title:'空母どうしの戦い',text:'双方の航空戦力がぶつかった。',cam:{fit:1,th:0.6,ph:.9},arrows:[{p:[[0,4,-50],[0,4,-30]],c:'E'}]},
 {time:'',clock:'',step:'決着',title:'日本武尊のとどめ',text:'弱った独艦隊に日本武尊がとどめを刺し、旗艦ロートリンゲンを沈めた。',cam:{fit:1,th:0.3,ph:.9},arrows:[{p:[[14,4,20],[8,4,-10]],c:'A'}]},
 {time:'その後',clock:'',step:'結果',title:'独海軍の主力喪失',text:'独は機動艦隊の主力を失った。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'アイスランド沖海戦の結果',when:'1949年12月（照和24年12月）、アイスランド沖',prev:'ブレスト殴り込み',next:'総統要塞襲撃',factors:["航空戦で弱らせた敵に日本武尊がとどめを刺した。"],winner:'A',outcome:'旭日艦隊の勝利',summary:'旭日艦隊が独第一機動艦隊を破り、旗艦ロートリンゲンを沈めた。',sides:[{name:'独第一機動艦隊',side:'E',cmdr:'不明',flag:'ロートリンゲン',others:'—',before:'不明',loss:'ロートリンゲン撃沈',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊',side:'A',cmdr:'大石蔵良',flag:'日本武尊',others:'—',before:'不明',loss:'日本武尊は損傷なし',rate:null,deaths:'不明',dead:[]}],after:["北大西洋の制海権が旭日艦隊側に移る（推定）。"],note:'年月と日本武尊の戦果は日本語版Wikipedia「日本武尊 (旭日の艦隊)」、旗艦撃沈は「旭日の艦隊」による。兵力・損害の数値は確認できなかった。'};
"""
