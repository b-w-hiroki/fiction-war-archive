from common import land_env, specials, labels
UC=324.09
ARC='第二部'
OUT='dijle.html'
TITLE='ディジレ河の戦い 3D俯瞰'
HEAD='ディジレ河'
ERA='パルス暦324年9月29日'
SE='ミスル軍'; SA='パルス軍'; PALE='misr'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作小説にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a6a40','0x9a9468',amp=5,seed=24,water='0x3a5a68')+specials(labels([('ディジレ河', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'ミスル軍',cmd:'将軍マシニッサ・カラマンデス',side:'E',n:70,k:{0:{p:[0,7,-34],s:'move',f:'line',l:'約8万・戦車2千台'},1:{p:[0,7,-10],s:'charge',l:'河を渡る'},2:{p:[0,7,-4],s:'broken',l:'カラマンデス討たれる'},3:{p:[0,7,-40],s:'withdraw',l:'1万以上を失う'}}},
 {name:'パルス軍',cmd:'ダリューン',side:'A',n:56,k:{0:{p:[0,7,30],s:'ready',f:'concave',l:'約6万5千'},1:{p:[0,7,14],s:'fight',f:'concave',b:1},2:{p:[0,7,4],s:'charge'},3:{p:[0,7,-6],s:'ready'}}}
];
const PH=[
{time:'324年9月29日',clock:'',step:'侵攻',title:'ミスルの侵攻',text:'アルスラーンの即位記念日、西の国ミスルの軍がディジレ河に迫った。駱駝隊と戦車を持つ約8万の軍である。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,7,-34],[0,7,-10]],c:'E'}]},
 {time:'',clock:'',step:'渡河',title:'河を渡る敵を迎え撃つ',text:'ダリューンの率いるパルス軍約6万5千が、河を渡るミスル軍を迎え撃った。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'勝利',title:'ミスル軍の敗退',text:'ダリューンがミスルの将カラマンデスを討ち、ミスル軍は1万以上を失って退いた。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[0,7,14],[0,7,-4]],c:'A'}]}
];
const RESULT={title:'ディジレ河の戦いの結果',when:'パルス暦324年9月29日、ディジレ河',prev:'アルスラーン即位（第一部の終わり）',next:'カーヴェリー河の戦い（対チュルク）',
 factors:['河を渡る途中の敵を迎え撃つ、守る側に有利な形で戦えた。','ダリューンが敵将を討ち取り、指揮を崩した。'],winner:'A',outcome:'パルス軍の勝利',
 summary:'第二部の幕開けの戦い。即位から3年、西のミスルの侵攻をパルスが退けた。',
 sides:[{name:'ミスル軍',side:'E',cmdr:'マシニッサ、カラマンデス',flag:'—',others:'—',before:'約80,000（駱駝隊1万・戦車2千台）',loss:'1万以上',rate:13,deaths:'不明',dead:['カラマンデス']},
        {name:'パルス軍',side:'A',cmdr:'ダリューン',flag:'—',others:'—',before:'約65,000',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['ミスルは西からの圧力を続ける。','ミスルにはのちにヒルメスが現れる。'],
 note:'第二部の数値は原作8巻の要約による。損耗率は「1万以上」を8万で割った概算。'};
"""
