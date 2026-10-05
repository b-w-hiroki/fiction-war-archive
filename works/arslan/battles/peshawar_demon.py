from common import land_env, specials, labels
UC=325.3
ARC='第二部'
OUT='peshawar_demon.html'
TITLE='ペシャワール城の攻防（対魔軍） 3D俯瞰'
HEAD='魔軍襲来'
ERA='パルス暦325年（推定）'
SE='魔軍'; SA='パルス軍'; PALE='serpent'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作小説の要約にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a48','0x9a8a68',amp=6,seed=31)+specials(labels([('ペシャワール城', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'魔軍',cmd:'イルテリシュ',side:'E',n:30,k:{0:{p:[0,7,-30],s:'move'},1:{p:[0,7,-4],s:'fight'},2:{p:[0,7,-20],s:'withdraw'}}},
 {name:'ペシャワール守備隊',cmd:'パルス軍',side:'A',n:30,k:{0:{p:[0,7,10],s:'ready',f:'line'},1:{p:[0,7,4],s:'fight',f:'line'},2:{p:[0,7,0],s:'charge'}}}
];
const PH=[
{time:'325年',clock:'',step:'襲来',title:'魔軍の襲来',text:'蛇王の眷属である魔物の群れが、東の拠点ペシャワール城を襲った。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,7,-30],[0,7,-4]],c:'E'}]},
 {time:'',clock:'',step:'籠城',title:'地上と空から',text:'魔軍は地上と空の両方から攻め、城内への侵入を許した。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'救援',title:'援軍の到着',text:'援軍が到着し、パルス軍は魔軍を退けた。',cam:{fit:1,th:.3,ph:.9},arrows:[]}
];
const RESULT={title:'ペシャワール城の攻防（対魔軍）の結果',when:'パルス暦325年（推定）、ペシャワール城',prev:'カーヴェリー河の戦い（対チュルク）',next:'ペシャワールの三つ巴',
 factors:['援軍の到着が間に合った。'],winner:'A',outcome:'パルス軍の勝利（城を守る）',
 summary:'第二部で蛇王の勢力が初めて正面からパルスの城を攻めた戦い。',
 sides:[{name:'魔軍',side:'E',cmdr:'イルテリシュ',flag:'—',others:'—',before:'不明',loss:'撃退',rate:null,deaths:'不明',dead:[]},
        {name:'パルス軍',side:'A',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['蛇王の勢力との戦いが本格化する。'],
 note:'11〜12巻。経過は原作小説の要約（本の窓口ほんシェルジュ「小説『アルスラーン戦記』全16巻分の魅力をネタバレ紹介」、chichibu.moo.jp「アルスラーン戦記第二部」）による。年は推定。兵力・指揮官名の詳細は確認できなかった。'};
"""
