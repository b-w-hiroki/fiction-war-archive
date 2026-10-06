from common import land_env, specials, labels
UC=1561.01
ARC='戦国転移'
OUT='arrival.html'
TITLE='越後での遭遇戦 3D俯瞰'
HEAD='越後遭遇戦'
ERA='1561年（推定）'
SE='土地の武士団'; SA='自衛隊・長尾軍'; PALE='zeon'; PAL='efsf'
NOTE='配置は1979年映画の流れにもとづく概略。時期・場所は推定'
ENV=land_env('0x4f6a3a','0x8a9a6a',water='0x4a6a8a',amp=5,seed=4)+specials(labels([('海岸（推定）','','A',(0,10,36),3)]))
DATA=r"""
const U=[
{name:'土地の武士団',cmd:'不明',side:'E',n:30,k:{0:{p:[0,7,-40],s:'ready',f:'line',l:'騎馬と足軽'},1:{p:[0,7,-20],s:'charge'},2:{p:[0,7,-24],s:'broken',l:'火器に驚き崩れる'},3:{p:[0,7,-50],s:'withdraw'}}},
{name:'伊庭小隊',cmd:'伊庭義明三尉',side:'A',n:14,k:{0:{p:[0,7,24],s:'ready',l:'隊員21名・戦車など'},1:{p:[0,7,20],s:'fight',f:'line'},2:{p:[0,7,16],s:'fight',b:1},3:{p:[0,7,12],s:'wait'}}},
{name:'長尾景虎',cmd:'長尾景虎',side:'A',n:8,k:{0:{p:[30,7,0],s:'hidden'},1:{p:[34,7,-4],s:'wait',l:'戦いを見る'},2:{p:[26,7,-6],s:'move'},3:{p:[12,7,4],s:'move',l:'伊庭と手を結ぶ'}}}
];
const PH=[
{time:'転移直後',clock:'',step:'転移',title:'戦国時代への転移',text:'演習中の自衛隊員21名が、車両や武器ごと約400年前の戦国時代へ飛ばされた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'遭遇',clock:'',step:'衝突',title:'武士との衝突',text:'土地の武士団と出くわし、戦いになる。',cam:{fit:1,th:.7,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-20]],c:'E'}]},
{time:'交戦',clock:'',step:'火力',title:'現代火器の威力',text:'自衛隊の火器の前に武士団は崩れる。その様子を長尾景虎が見ていた。',cam:{fit:1,th:.3,ph:.85},arrows:[]},
{time:'その後',clock:'',step:'合流',title:'景虎との手組み',text:'伊庭三尉は景虎と手を結び、この時代で生き抜く道を選ぶ。',cam:{fit:1,th:.5,ph:1.0},arrows:[{p:[[26,7,-6],[12,7,4]],c:'A'}]}
];
const RESULT={title:'越後での遭遇戦の結果',when:'1561年ごろ（推定）、越後',prev:'自衛隊の時代転移',next:'矢野の離反',
 factors:['現代火器の火力差。','長尾景虎が自衛隊の力に目をつけた。'],winner:'A',outcome:'自衛隊の勝利（推定）',
 summary:'転移直後の自衛隊が武士団を退け、長尾景虎と手を結ぶきっかけになった。',
 sides:[{name:'土地の武士団',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'自衛隊',side:'A',cmdr:'伊庭義明三尉',flag:'—',others:'長尾景虎',before:'隊員21名',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['伊庭と景虎が同盟する。','隊員の一部は帰れない現実に動揺する。'],
 note:'隊員21名は英語版Wikipedia「G.I. Samurai」の映画あらすじに拠る。遭遇戦の細部・場所・年は推定。'};
"""
