from common import *
UC=300.01
ARC='北の脅威'
OUT='castleblack.html'
TITLE='黒の城の戦い 3D俯瞰'
HEAD='黒の城'
ERA='AC300年'
SE='野人'; SA='冥夜の守人'; PALE='titan'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xdfe6ea','0xf4f8fa',amp=2,seed=5,sky='0x9aa6b0')+wall(200,30,0,40,arc=1.2,start=2.55,color='0xd8eef8')+specials(labels([('黒の城', '壁の南', 'A', (0, 24, 40), 3), ('壁', '', 'A', (0, 40, -14), 2.4)]))
DATA=r"""
const U=[
{name:'野人の大軍',cmd:'マンス・レイダー',side:'E',n:40,k:{0:{p:[0,7,-40],s:'move'},1:{p:[0,7,-24],s:'charge',l:'壁の門へ'},2:{p:[0,7,-20],s:'fight'},3:{p:[0,7,-30],s:'withdraw'}}},
 {name:'南からの襲撃隊',cmd:'野人の一隊',side:'E',n:8,k:{0:{p:[-20,7,50],s:'move'},1:{p:[-10,7,40],s:'charge',l:'黒の城を背後から'},2:{p:[-4,7,38],s:'broken'},3:{s:'gone'}}},
 {name:'冥夜の守人',cmd:'ジョン・スノウ',side:'A',n:8,k:{0:{p:[0,7,30],s:'ready'},1:{p:[0,7,34],s:'fight'},2:{p:[0,7,10],s:'fight',l:'門を守る'},3:{p:[0,7,10],s:'ready'}}},
 {name:'スタニス軍',cmd:'スタニス・バラシオン',side:'A',n:20,k:{0:{s:'hidden',p:[30,7,-50]},1:{s:'hidden',p:[30,7,-50]},2:{s:'hidden',p:[30,7,-50]},3:{p:[20,7,-34],s:'charge',l:'野人を蹴散らす'}}}
];
const PH=[
{time:'AC300年',clock:'原作3部／S4E9',step:'来襲',title:'野人の来襲',text:'マンス・レイダーの野人の大軍が壁に迫った。守り手はわずかだった。',cam:{fit:1,th:0.5,ph:0.9},arrows:[{p:[[0,7,-40],[0,7,-24]],c:'E'}]},
 {time:'',clock:'',step:'両面',title:'南北からの攻撃',text:'南へ回った野人の一隊が黒の城を背後から襲った。',cam:{fit:1,th:0.8,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'門',title:'門の守り',text:'ジョンらが壁の門を守り抜いた。',cam:{fit:1,th:0.3,ph:0.9},arrows:[]},
 {time:'',clock:'S4E10',step:'援軍',title:'スタニスの到着',text:'スタニスの軍が北から野人を突き、マンスを捕らえた。',cam:{fit:1,th:0.6,ph:1.0},arrows:[{p:[[30,7,-50],[20,7,-34]],c:'A'}]}
];
const RESULT={title:'黒の城の戦いの結果',when:'AC300年、壁と黒の城',prev:'紅き婚礼',next:'堅牢な家（ドラマ）',factors:['壁が攻め手を阻んだ。','守人が門を守り抜いた。','スタニスの軍が間に合った。'],winner:'A',outcome:'冥夜の守人・スタニス側の勝利',summary:'壁が守られ、ジョンが指揮官として頭角を現す。',sides:[{name:'野人',side:'E',cmdr:'マンス・レイダー',flag:'—',others:'巨人ら',before:'不明（大軍）',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'冥夜の守人',side:'A',cmdr:'ジョン・スノウ',flag:'—',others:'スタニス・バラシオン',before:'不明（少数）',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['ジョンが総帥に選ばれる。','スタニスが壁に拠点を置く。'],note:'展開は小説『剣嵐の大地』とドラマS4E9「壁を守る者たち」による。小説では戦いは数日に分かれる。兵数は確認できなかった。'};
"""
