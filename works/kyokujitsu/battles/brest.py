from common import land_env, specials, labels
UC=1948.05
ARC='反攻'
OUT='brest.html'
TITLE='ブレスト殴り込み 3D俯瞰'
HEAD='ブレスト殴り込み'
ERA='1948年（推定）'
SE='ドイツ第三帝国軍'; SA='旭日艦隊・英国軍'; PALE='zeon'; PAL='scout'
NOTE='交戦中／健在の部隊。配置はOVA・小説の描写にもとづく概略で、位置関係は推定。部隊の大きさは規模の目安'
ENV=land_env('0x24506e','0x2e6688',water='0x1f4a68',amp=0.6,seed=7,sky='0x7d8fa3')+specials(labels([('ブレスト', '独占領下の仏軍港', 'E', (0, 12, -40), 3)]))
DATA=r"""
const U=[
 {name:'アドミラル・ヒッパー',cmd:'独海軍',side:'E',n:10,k:{0:{p:[0,4,-36],s:'ready',l:'港内'},1:{p:[0,4,-30],s:'fight'},2:{p:[0,4,-30],s:'gone',l:'撃沈'},3:{p:[0,4,-30],s:'gone'}}},
 {name:'ブレスト守備隊',cmd:'独軍',side:'E',n:10,k:{0:{p:[16,4,-42],s:'ready'},1:{p:[16,4,-42],s:'fight'},2:{p:[16,4,-42],s:'fight'},3:{p:[16,4,-42],s:'ready'}}},
 {name:'日本武尊',cmd:'大石蔵良',side:'A',n:16,k:{0:{p:[0,4,40],s:'move',l:'半潜状態で接近',f:'column'},1:{p:[0,4,0],s:'charge',l:'殴り込み'},2:{p:[0,4,-6],s:'fight'},3:{p:[0,4,30],s:'withdraw'}}},
 {name:'装甲空母 信長',cmd:'旭日艦隊',side:'A',n:10,k:{0:{p:[-20,4,46],s:'move'},1:{p:[-20,4,24],s:'fight'},2:{p:[-20,4,24],s:'broken'},3:{p:[-20,4,24],s:'gone',l:'沈没'}}}
];
const PH=[
 {time:'推定',clock:'',step:'接近',title:'半潜状態の接近',text:'日本武尊は船体を沈めた半潜状態で、独の軍港ブレストへ近づいた。',cam:{fit:1,th:0.4,ph:.9},arrows:[{p:[[0,4,40],[0,4,0]],c:'A'}]},
 {time:'',clock:'',step:'突入',title:'殴り込み',text:'港に突入し、独艦と砲戦を交えた。',cam:{fit:1,th:0.6,ph:.9},arrows:[]},
 {time:'',clock:'',step:'戦果',title:'ヒッパー撃沈',text:'重巡アドミラル・ヒッパーを撃沈した。',cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:'その後',clock:'',step:'損害',title:'信長の喪失',text:'この戦いの中で装甲空母・信長が沈んだ。',cam:{fit:1,th:0.5,ph:.9},arrows:[]}
];
const RESULT={title:'ブレスト殴り込みの結果',when:'時期は推定、ブレスト',prev:'トド作戦迎撃',next:'アイスランド沖海戦',factors:["半潜状態で接近し、港を奇襲した。"],winner:'A',outcome:'旭日艦隊の勝利（損害あり）',summary:'日本武尊が半潜状態で港に突入し、アドミラル・ヒッパーを沈めた。旭日艦隊も装甲空母・信長を失った。',sides:[{name:'独ブレスト部隊',side:'E',cmdr:'不明',flag:'—',others:'アドミラル・ヒッパー',before:'不明',loss:'アドミラル・ヒッパー撃沈',rate:null,deaths:'不明',dead:[]},{name:'旭日艦隊',side:'A',cmdr:'大石蔵良',flag:'日本武尊',others:'装甲空母 信長',before:'不明',loss:'信長沈没',rate:null,deaths:'不明',dead:[]}],after:["旭日艦隊は北大西洋の独機動部隊と向き合う。"],note:'戦果は日本語版Wikipedia「旭日の艦隊」の要約による。信長の沈没がこの戦いかは同記事の並びからの推定。時期・兵力・巻は確認できなかった。'};
"""
