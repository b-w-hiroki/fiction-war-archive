from common import *
UC=2199.03
ARC='旅立ち'
OUT='plutobase.html'
TITLE='冥王星前線基地攻略 3D俯瞰'
HEAD='冥王星基地'
ERA='2199年'
SE='冥王星前線基地'; SA='ヤマト'; PALE='gamilas'; PAL='earth'
NOTE='交戦中／健在の部隊。展開は1974年版TVシリーズにもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+planet(pos=(0,-120,-40),r=60,color='0x8a8a9a',land='0x6a6a7a',label=('冥王星','ガミラス前線基地','E'))+specials(labels([]))
DATA=r"""
const U=[
{name:'冥王星前線基地',cmd:'シュルツ司令',side:'E',n:30,k:{0:{p:[0,0,-30],s:'ready',l:'遊星爆弾の発射基地'},1:{p:[0,0,-26],s:'fight',l:'反射衛星砲',b:1},2:{p:[0,0,-28],s:'broken',l:'基地壊滅'},3:{p:[0,0,-60],s:'withdraw',l:'シュルツ脱出'}}},
 {name:'ヤマト',cmd:'沖田十三',side:'A',n:8,k:{0:{p:[0,0,30],s:'move'},1:{p:[0,0,14],s:'broken',l:'被弾し海中へ'},2:{p:[0,0,-8],s:'charge',l:'基地を攻撃'},3:{p:[0,0,0],s:'ready',l:'太陽系を出る'}}},
 {name:'艦載機隊',cmd:'古代進ほか',side:'A',n:8,k:{0:{p:[10,0,24],s:'hidden'},1:{p:[10,0,24],s:'move',l:'反射衛星を探す'},2:{p:[8,0,-20],s:'charge',l:'基地を叩く'},3:{p:[6,0,10],s:'ready'}}}
];
const PH=[
{time:'2199年',clock:'第7〜8話',step:'接近',title:'冥王星へ',text:'イスカンダルへ旅立ったヤマトは、地球を焼く遊星爆弾の発射基地がある冥王星に向かった。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,0,30],[0,0,14]],c:'A'}]},
 {time:'',clock:'',step:'反射衛星砲',title:'見えない砲撃',text:'ガミラスは衛星で光線を反射させ、死角からヤマトを撃った。ヤマトは被弾して冥王星の海に沈む。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'反撃',title:'基地への反撃',text:'艦載機隊が反射衛星の仕組みを突き止め、浮上したヤマトとともに基地を叩いた。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[0,0,-8],[0,0,-26]],c:'A'}]},
 {time:'',clock:'',step:'壊滅',title:'前線基地の壊滅',text:'冥王星前線基地は壊滅し、遊星爆弾の攻撃は止まった。ヤマトは太陽系の外へ向かう。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'冥王星前線基地攻略の結果',when:'2199年、冥王星',prev:'冥王星沖海戦／ヤマト発進',next:'バラン星〜七色星団',
 factors:['艦載機隊が反射衛星砲の仕組みを見抜いた。','ヤマトの耐久力が、死角からの砲撃に耐えた。'],winner:'A',outcome:'ヤマトの勝利（前線基地壊滅）',
 summary:'遊星爆弾を撃ち込んでいたガミラスの冥王星基地を、ヤマトが壊滅させた。地球への直接攻撃がここで止まる。',
 sides:[{name:'冥王星前線基地',side:'E',cmdr:'シュルツ',flag:'—',others:'ガンツ',before:'不明',loss:'基地壊滅',rate:null,deaths:'不明',dead:[]},
        {name:'ヤマト',side:'A',cmdr:'沖田十三',flag:'ヤマト',others:'古代進、島大介',before:'ヤマト1隻と艦載機',loss:'損傷',rate:null,deaths:'不明',dead:[]}],
 after:['遊星爆弾の攻撃が止まる。','ヤマトは太陽系を出て、イスカンダルへの旅を続ける。'],
 note:'展開は1974年版TVにもとづく。話数は英語版Wikipedia「List of Space Battleship Yamato episodes」の各話題名（第7話「運命の要塞攻略戦」・第8話「反射衛星砲撃破」）で確認。'};
"""
