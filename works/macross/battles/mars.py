from common import *
UC=2009.05
ARC='帰還の旅'
OUT='mars.html'
TITLE='火星サラ基地の戦い 3D俯瞰'
HEAD='火星'
ERA='2009年（月日不明・推定）'
SE='ゼントラーディ軍'; SA='統合軍'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-220,0),180,color='0xa8543a',land='0xc87850',label=('火星','サラ基地','A'))+specials(labels([('サラ基地','放棄された基地','A',(0,-30,20),3)]))
DATA=r"""
const U=[
 {name:'ゼントラーディ部隊',cmd:'カムジン隊（推定）',side:'E',n:24,k:{0:{p:[0,10,-50],s:'ready',l:''},1:{p:[0,10,-30],s:'fight',l:'奇襲'},2:{p:[0,8,-10],s:'fight',l:''},3:{p:[0,10,-20],s:'broken',l:''},4:{p:[0,10,-50],s:'withdraw',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,0,30],s:'ready',l:'補給のため寄港'},1:{p:[0,0,30],s:'wait',l:''},2:{p:[0,0,30],s:'fight',l:''},3:{p:[0,10,30],s:'move',l:'基地を爆破し離脱'},4:{p:[0,20,40],s:'ready',l:''}}},
 {name:'VF隊',cmd:'一条輝ほか',side:'A',n:12,k:{0:{p:[10,4,20],s:'ready',l:''},1:{p:[10,4,0],s:'fight',l:''},2:{p:[6,6,-4],s:'fight',l:''},3:{p:[6,8,10],s:'fight',l:''},4:{p:[10,10,30],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第7話',step:'寄港',title:'サラ基地へ',text:'マクロスは補給のため火星の放棄された基地に降りた。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第7話',step:'奇襲',title:'ゼントラーディの攻撃',text:'基地の周辺でゼントラーディが攻撃してきた。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第7話',step:'防戦',title:'早瀬未沙の救出',text:'基地に残った早瀬未沙を一条輝が救い出した（推定）。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第7話',step:'離脱',title:'火星を離れる',text:'基地を爆破して敵を巻き込み、火星を離れた（推定）。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'火星サラ基地の戦いの戦果',when:'2009年（月日不明・推定）',prev:'—',next:'—',
 factors:["敵を基地の爆発に巻き込んだ（推定）"],winner:'A',outcome:'統合軍の離脱成功',summary:'火星での補給の途中に襲われたが、マクロスは離脱に成功した。',
 sides:[{name:'ゼントラーディ軍',side:'E',cmdr:'カムジン隊（推定）',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍',side:'A',cmdr:'グローバル艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["マクロスは地球への旅を続ける"],note:'第7話の内容は英語版Wikipediaの話数一覧による。細部は推定。'};
"""
