from common import *
UC=1943.07
ARC='北と南'
OUT='kiska.html'
TITLE='キスカ撤退 3D俯瞰'
HEAD='キスカ撤退'
ERA='1943年7月（推定）'
SE='米海軍'; SA='みらい・キスカ守備隊'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略で、位置関係・兵力は推定'
ENV=land_env('0x4a5a50','0x9aa098',water='0x2a4a5e',amp=4,seed=9,sky='0xa4acb4')+specials(labels([('キスカ島','アリューシャン列島','A',(0,18,-10),3)]))
DATA=r"""
const U=[
{name:'米艦隊',cmd:'不明',side:'E',n:20,k:{0:{p:[0,7,-60],s:'move',l:'島を封鎖'},1:{p:[0,7,-50],s:'wait',nf:1},2:{p:[0,7,-45],s:'fight',l:'みらいと交戦'},3:{p:[0,7,-55],s:'wait',nf:1}}},
{name:'キスカ守備隊',cmd:'不明',side:'A',n:20,k:{0:{p:[-10,7,0],s:'ready',nf:1},1:{p:[-10,7,10],s:'move',l:'濃霧の中で乗船',nf:1},2:{p:[-20,7,30],s:'move',nf:1},3:{p:[-30,7,60],s:'withdraw',l:'撤退成功',nf:1}}},
{name:'みらい',cmd:'梅津三郎',side:'A',n:6,k:{0:{p:[20,7,20],s:'move'},1:{p:[10,7,-10],s:'wait',nf:1},2:{p:[10,7,-20],s:'fight',l:'米艦隊を引き付ける'},3:{p:[20,7,40],s:'withdraw'}}}
];
const PH=[
{time:'1943年7月（推定）',clock:'',step:'封鎖',title:'孤立した守備隊',text:'アリューシャンのキスカ島に日本軍守備隊が取り残され、米艦隊が周囲を固めていた。',cam:{fit:1,th:.5,ph:.9},arrows:[]},
{time:'',clock:'',step:'濃霧',title:'濃霧の中の収容',text:'濃霧にまぎれて守備隊の収容が進んだ。',cam:{fit:1,th:.8,ph:.9},arrows:[{p:[[-10,7,0],[-20,7,30]],c:'A'}]},
{time:'',clock:'',step:'交戦',title:'米艦隊との交戦',text:'みらいは米艦隊と向き合い、撤退の時間を稼いだ。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[10,7,-20],[0,7,-45]],c:'A'}]},
{time:'',clock:'',step:'撤退',title:'撤退成功',text:'守備隊は島を離れた。',cam:{fit:1,th:.6,ph:1.0},arrows:[]}
];
const RESULT={title:'キスカ撤退の結果',when:'1943年（月は推定）、キスカ島沖',prev:'ダンピール海峡',next:'タラワ撤収',
 factors:['濃霧が撤退を隠した。','みらいのレーダーと火力が米艦隊を牽制した。'],winner:'A',outcome:'撤退成功',
 summary:'みらいの支援で、キスカ島の守備隊が濃霧の中で撤退した。',
 sides:[{name:'米海軍',side:'E',cmdr:'不明',flag:'ノースカロライナ（資料による）',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'みらい・キスカ守備隊',side:'A',cmdr:'不明',flag:'みらい',others:'—',before:'守備隊 約4000人（資料による・未確認）',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['草加の計画と角松らの考えの違いが深まっていく。'],
 note:'撤退成功・濃霧・約4000人・ノースカロライナ隊はネタバレ解説サイト（k-diary24.com）に拠り、原作本文とは照合していない。年月は史実のキスカ撤退（1943年7月）からの推定。アニメ化されていない。'};
"""
