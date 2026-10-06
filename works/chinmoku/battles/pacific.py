from common import *
UC=1.02
ARC='独立'
OUT='pacific.html'
TITLE='太平洋の対潜戦 3D俯瞰'
HEAD='米原潜'
ERA='作中年不明'
SE='米海軍'; SA='やまと'; PALE='efsf'; PAL='scout'
NOTE='配置は原作漫画にもとづく概略（推定）。部隊の大きさは戦力の目安。海面下の位置関係は抽象化'
ENV=land_env('0x0e2438','0x1e3c58',water='0x1f4f78',amp=2,seed=4,sky='0x5a7088')+specials(labels([('太平洋', '', 'A', (0, 22, 0), 3)]))
DATA=r"""
const U=[
{name:'米攻撃型原潜部隊',cmd:'米海軍',side:'E',n:20,k:{0:{p:[0,7,-40],s:'ready',f:'line',l:'包囲'},1:{p:[0,7,-20],s:'fight',f:'concave'},2:{p:[0,7,-14],s:'fight',b:1},3:{p:[0,7,-30],s:'broken'},4:{p:[0,7,-40],s:'withdraw'}}},
{name:'やまと',cmd:'海江田四郎艦長',side:'A',n:3,k:{0:{p:[0,7,40],s:'move',l:'潜航'},1:{p:[0,7,10],s:'wait',nf:1,l:'沈黙'},2:{p:[6,7,-4],s:'charge',l:'反撃'},3:{p:[0,7,-10],s:'fight'},4:{p:[0,7,-60],s:'move',l:'離脱'}}}
];
const PH=[
{time:'作中年不明',clock:'',step:'接近',title:'太平洋へ',text:'独立国やまとが太平洋に向かう。米攻撃型原潜がこれを待ち受けた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'包囲',title:'阻止線',text:'米攻撃型原潜は深海でやまとを追った。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-20]],c:'E'}]},
{time:'',clock:'',step:'沈黙',title:'音を消す',text:'やまとは音を消して相手の探知をかわし、隙を待った。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'反撃',title:'反撃',text:'やまとは相手の陣の弱い所を突いた。',cam:{fit:1,th:.5,ph:1.0},arrows:[{p:[[6,7,-4],[0,7,-10]],c:'A'}]},
{time:'',clock:'',step:'結果',title:'結果',text:'やまとは音響戦で追撃をかわした（展開は推定）。',cam:{fit:1,th:.6,ph:1.0},arrows:[]}
];
const RESULT={title:'太平洋の対潜戦の結果',when:'作中年不明、太平洋',prev:'沖縄沖海戦',next:'東京湾海戦',
 factors:['やまとは高い静粛性で探知を避けた。','海江田は相手の判断を読んで動いた（作中描写の要約）。'],winner:'A',outcome:'やまと（離脱成功）',
 summary:'やまとは音響戦で追撃をかわした（展開は推定）。',
 sides:[{name:'米攻撃型原潜部隊',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'やまと',side:'A',cmdr:'海江田四郎',flag:'やまと（旧シーバット）',others:'—',before:'原潜1隻',loss:'なし（推定）',rate:null,deaths:'不明',dead:[]}],
 after:['やまとは航海を続ける。'],
 note:'作中で年は明示されないため「作中年不明」。艦名・戦力は確認できず不明。展開の細部と巻の区切りは記憶にもとづく推定（英語版Wikipedia「The Silent Service」で大筋のみ確認）。'};
"""
