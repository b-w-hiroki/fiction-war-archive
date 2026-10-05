from common import *
UC=2199.09
ARC='決戦'
OUT='gamilas.html'
TITLE='ガミラス本星の決戦 3D俯瞰'
HEAD='ガミラス本星'
ERA='2199年'
SE='ガミラス本星'; SA='ヤマト'; PALE='gamilas'; PAL='earth'
NOTE='交戦中／健在の部隊。展開は1974年版TVシリーズにもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet(pos=(0,-140,-30),r=110,color='0x2a5a7a',land='0x4a7a6a',label=('ガミラス本星','','E'))+specials(labels([]))
DATA=r"""
const U=[
{name:'デスラー総統',cmd:'デスラー',side:'E',n:30,k:{0:{p:[0,0,-20],s:'ready',l:'本星で待ち構える'},1:{p:[0,0,-16],s:'fight',l:'硫酸の海・ミサイル',b:1},2:{p:[0,0,-14],s:'broken',l:'火山帯の崩壊'},3:{p:[0,0,-50],s:'withdraw',l:'デスラーは脱出'}}},
 {name:'ヤマト',cmd:'沖田十三',side:'A',n:8,k:{0:{p:[0,0,30],s:'move'},1:{p:[0,0,4],s:'fight',l:'海に誘い込まれる'},2:{p:[0,0,-2],s:'charge',l:'波動砲で火山脈を撃つ'},3:{p:[0,0,10],s:'ready',l:'イスカンダルへ'}}}
];
const PH=[
{time:'2199年',clock:'第24話ごろ（推定）',step:'到着',title:'双子星',text:'イスカンダルの双子星ガミラスにヤマトが到着した。デスラーは本星そのものを使ってヤマトを沈めようとする。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,0,30],[0,0,4]],c:'A'}]},
 {time:'',clock:'',step:'海',title:'硫酸の海',text:'ヤマトは硫酸の海に追い込まれ、艦体が溶け始めた。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'波動砲',title:'火山脈を撃つ',text:'ヤマトは波動砲で本星の火山脈を撃ち、ガミラスの都市は連鎖する噴火で崩壊した。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'崩壊',title:'帝国の崩壊',text:'ガミラス帝国は事実上壊滅し、デスラーは脱出した。ヤマトはイスカンダルに着く。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'ガミラス本星の決戦の結果',when:'2199年、ガミラス本星',prev:'七色星団の決戦',next:'イスカンダル到着／デスラーとの最終戦',
 factors:['ヤマトは本星の地質の弱点を突いた。','デスラーは本星を戦場にし、自らの都市を危険にさらした。'],winner:'A',outcome:'ヤマトの勝利（ガミラス本星壊滅）',
 summary:'ヤマトがガミラス本星で勝ち、ガミラス帝国は壊滅した。勝利の代償として、古代はその破壊の重さに向き合う。',
 sides:[{name:'ガミラス',side:'E',cmdr:'デスラー総統',flag:'デスラー艦',others:'—',before:'不明',loss:'本星の都市が崩壊',rate:null,deaths:'不明（多数）',dead:[]},
        {name:'ヤマト',side:'A',cmdr:'沖田十三',flag:'ヤマト',others:'古代進',before:'ヤマト1隻',loss:'損傷',rate:null,deaths:'不明',dead:[]}],
 after:['ヤマトはイスカンダルで放射能除去装置を受け取る。','デスラーは帰路のヤマトを襲う。'],
 note:'展開は1974年版TVにもとづく。話数は推定。'};
"""
