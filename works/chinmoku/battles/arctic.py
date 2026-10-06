from common import *
UC=1.04
ARC='北上'
OUT='arctic.html'
TITLE='北極海海戦 3D俯瞰'
HEAD='北極海'
ERA='作中年不明'
SE='米海軍'; SA='やまと'; PALE='efsf'; PAL='scout'
NOTE='配置は原作漫画にもとづく概略（推定）。部隊の大きさは戦力の目安。海面下の位置関係は抽象化'
ENV=land_env('0x0e2438','0x1e3c58',water='0x1f4f78',amp=2,seed=6,sky='0x5a7088')+specials(labels([('ベーリング海峡〜北極海', '', 'A', (0, 22, 0), 3)]))
DATA=r"""
const U=[
{name:'米原潜部隊',cmd:'米海軍',side:'E',n:20,k:{0:{p:[0,7,-40],s:'ready',f:'line',l:'包囲'},1:{p:[0,7,-20],s:'fight',f:'concave'},2:{p:[0,7,-14],s:'fight',b:1},3:{p:[0,7,-30],s:'broken'},4:{p:[0,7,-40],s:'withdraw'}}},
{name:'やまと',cmd:'海江田四郎艦長',side:'A',n:3,k:{0:{p:[0,7,40],s:'move',l:'潜航'},1:{p:[0,7,10],s:'wait',nf:1,l:'沈黙'},2:{p:[6,7,-4],s:'charge',l:'反撃'},3:{p:[0,7,-10],s:'fight'},4:{p:[0,7,-60],s:'move',l:'離脱'}}}
];
const PH=[
{time:'作中年不明',clock:'',step:'接近',title:'ベーリング海峡〜北極海へ',text:'独立国やまとがベーリング海峡〜北極海に向かう。米原潜部隊がこれを待ち受けた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'',clock:'',step:'包囲',title:'阻止線',text:'米原潜部隊は氷の下でやまとを待ち伏せた。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-20]],c:'E'}]},
{time:'',clock:'',step:'沈黙',title:'音を消す',text:'やまとは音を消して相手の探知をかわし、隙を待った。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
{time:'',clock:'',step:'反撃',title:'反撃',text:'やまとは相手の陣の弱い所を突いた。',cam:{fit:1,th:.5,ph:1.0},arrows:[{p:[[6,7,-4],[0,7,-10]],c:'A'}]},
{time:'',clock:'',step:'結果',title:'結果',text:'やまとは氷海を抜けて大西洋へ出た。',cam:{fit:1,th:.6,ph:1.0},arrows:[]}
];
const RESULT={title:'北極海海戦の結果',when:'作中年不明、ベーリング海峡〜北極海',prev:'東京湾海戦',next:'大西洋の戦い',
 factors:['やまとは高い静粛性で探知を避けた。','海江田は相手の判断を読んで動いた（作中描写の要約）。'],winner:'A',outcome:'やまと（突破）',
 summary:'やまとは氷海を抜けて大西洋へ出た。',
 sides:[{name:'米原潜部隊',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'やまと',side:'A',cmdr:'海江田四郎',flag:'やまと（旧シーバット）',others:'—',before:'原潜1隻',loss:'なし（推定）',rate:null,deaths:'不明',dead:[]}],
 after:['やまとは航海を続ける。'],
 note:'作中で年は明示されないため「作中年不明」。艦名・戦力は確認できず不明。展開の細部と巻の区切りは記憶にもとづく推定（英語版Wikipedia「The Silent Service」で大筋のみ確認）。'};
"""
