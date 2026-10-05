from common import *
UC=2199.11
ARC='決戦'
OUT='desler.html'
TITLE='デスラー艦との最終戦 3D俯瞰'
HEAD='デスラー艦'
ERA='2199年'
SE='デスラー艦'; SA='ヤマト'; PALE='gamilas'; PAL='earth'
NOTE='交戦中／健在の部隊。展開は1974年版TVシリーズにもとづく概略。部隊の大きさは兵力の目安'
ENV=space_env()+specials(labels([]))
DATA=r"""
const U=[
{name:'デスラー艦',cmd:'デスラー',side:'E',n:6,k:{0:{p:[0,0,-30],s:'move',l:'帰路を追う'},1:{p:[0,0,-6],s:'charge',l:'ヤマトに接舷'},2:{p:[0,0,-4],s:'broken',l:'デスラー砲が跳ね返る'},3:{s:'gone'}}},
 {name:'ヤマト',cmd:'沖田十三',side:'A',n:8,k:{0:{p:[0,0,20],s:'move',l:'地球へ帰る'},1:{p:[0,0,4],s:'fight',l:'白兵戦'},2:{p:[0,0,6],s:'fight',l:'空間磁力メッキ'},3:{p:[0,0,30],s:'ready',l:'地球へ'}}}
];
const PH=[
{time:'2199年',clock:'第26話ごろ（推定）',step:'追撃',title:'デスラーの追撃',text:'放射能除去装置を積んで帰るヤマトを、生き延びたデスラーが追った。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,0,-30],[0,0,-6]],c:'E'}]},
 {time:'',clock:'',step:'接舷',title:'接舷と白兵戦',text:'デスラー艦はヤマトに接舷し、兵が艦内に乗り込んだ。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'反射',title:'デスラー砲の反射',text:'デスラーはデスラー砲を撃つが、ヤマトの空間磁力メッキに跳ね返され、自らの艦が爆発した。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'帰還',title:'地球へ',text:'ヤマトは地球へ戻り、沖田は地球を目にして息を引き取る。',cam:{fit:1,th:.5,ph:1.0},arrows:[{p:[[0,0,6],[0,0,30]],c:'A'}]}
];
const RESULT={title:'デスラー艦との最終戦の結果',when:'2199年、ヤマトの帰路',prev:'ガミラス本星の決戦／イスカンダル',next:'地球帰還',
 factors:['イスカンダルで施した空間磁力メッキがデスラー砲を跳ね返した。'],winner:'A',outcome:'ヤマトの勝利（デスラー艦爆沈）',
 summary:'帰路で追ってきたデスラーをヤマトが退けた旅の最後の戦い。ヤマトは放射能除去装置を地球へ持ち帰る。',
 sides:[{name:'デスラー艦',side:'E',cmdr:'デスラー総統',flag:'デスラー艦',others:'—',before:'デスラー艦1隻',loss:'爆沈',rate:100,deaths:'不明',dead:[]},
        {name:'ヤマト',side:'A',cmdr:'沖田十三',flag:'ヤマト',others:'古代進、森雪',before:'ヤマト1隻',loss:'損傷',rate:null,deaths:'不明',dead:[]}],
 after:['ヤマトは地球に帰り、地球は再生へ向かう。','沖田十三は地球を目にして亡くなる。','デスラーは続編で再び現れる。'],
 note:'展開は1974年版TV最終話にもとづく。話数は推定。'};
"""
