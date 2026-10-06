from common import land_env, specials, labels
UC=1561.04
ARC='戦国転移'
OUT='yano.html'
TITLE='矢野隊の離反 3D俯瞰'
HEAD='矢野離反'
ERA='1561年（推定）'
SE='矢野隊（離反組）'; SA='伊庭隊'; PALE='zeon'; PAL='efsf'
NOTE='1979年映画の流れにもとづく概略。時期・規模は推定'
ENV=land_env('0x4f6a3a','0x8a9a6a',water='0x3d5f80',amp=4,seed=7)+specials(labels([('海辺の村（推定）','','E',(0,10,-36),3)]))
DATA=r"""
const U=[
{name:'矢野隊',cmd:'矢野',side:'E',n:10,k:{0:{p:[0,7,-30],s:'ready',l:'巡視艇で離脱'},1:{p:[0,7,-26],s:'fight',l:'村を荒らす'},2:{p:[0,7,-20],s:'fight'},3:{p:[0,7,-22],s:'broken',l:'矢野が討たれる'}}},
{name:'伊庭隊',cmd:'伊庭義明三尉',side:'A',n:12,k:{0:{p:[0,7,30],s:'ready'},1:{p:[0,7,14],s:'move'},2:{p:[0,7,0],s:'fight',f:'line'},3:{p:[0,7,-8],s:'fight'}}}
];
const PH=[
{time:'転移後',clock:'',step:'離反',title:'部隊の分裂',text:'帰れない不安から、矢野らが隊を離れて勝手に動き出す。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'略奪',clock:'',step:'暴走',title:'離反組の暴走',text:'離反組は武器を頼みに村を荒らした。',cam:{fit:1,th:.7,ph:.9},arrows:[]},
{time:'追撃',clock:'',step:'対決',title:'伊庭隊の追撃',text:'伊庭は隊の規律を守るため、離反組を追う。',cam:{fit:1,th:.3,ph:.85},arrows:[{p:[[0,7,30],[0,7,0]],c:'A'}]},
{time:'決着',clock:'',step:'決着',title:'矢野の最期',text:'伊庭は矢野を討ち、隊は再びひとつにまとまる。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'矢野隊の離反の結果',when:'1561年ごろ（推定）',prev:'越後での遭遇戦',next:'川中島の戦い',
 factors:['帰還の見込みがなく、隊の規律が崩れた。','伊庭が指揮官として離反を許さなかった。'],winner:'A',outcome:'伊庭隊の勝利',
 summary:'自衛隊の内部分裂。伊庭が離反組を討ち、隊は景虎のもとで戦う道に進む。',
 sides:[{name:'矢野隊',side:'E',cmdr:'矢野',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['矢野']},
        {name:'伊庭隊',side:'A',cmdr:'伊庭義明三尉',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['隊員は21名から11名まで減っていく（脱走・戦死を含む）。'],
 note:'21名から11名への減少は英語版Wikipedia「G.I. Samurai」に拠る。矢野の離反の細部と人数は記憶にもとづく推定。'};
"""
