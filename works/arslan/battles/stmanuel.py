from common import land_env, specials, labels
UC=321.05
ARC='王都奪還'
OUT='stmanuel.html'
TITLE='聖マヌエル城の攻防 3D俯瞰'
HEAD='聖マヌエル城'
ERA='パルス暦321年5月'
SE='ルシタニア軍'; SA='パルス軍'; PALE='lusi'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作小説にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x6a6a48','0xa89a70',amp=5,seed=12)+specials(labels([('聖マヌエル城', 'ルシタニアの拠点', 'E', (0, 14, -34), 3)]))
DATA=r"""
const U=[
{name:'ルシタニア守備隊',cmd:'バルカシオン伯',side:'E',n:30,k:{0:{p:[0,7,-30],s:'ready',f:'line',l:'城を守る'},1:{p:[0,7,-24],s:'fight'},2:{p:[0,7,-28],s:'broken',l:'城が落ちる'},3:{s:'gone'}}},
 {name:'パルス軍',cmd:'アルスラーン',side:'A',n:70,k:{0:{p:[0,7,40],s:'move',f:'line',l:'王都へ出撃（約9万5千）'},1:{p:[0,7,4],s:'fight',f:'concave',b:1},2:{p:[0,7,-14],s:'charge',l:'城を攻め落とす'},3:{p:[0,7,-20],s:'ready'}}}
];
const PH=[
{time:'321年5月',clock:'',step:'出撃',title:'王都への出撃',text:'兵を集めたアルスラーンは、約9万5千で王都エクバターナへ向けて出撃した。途中のルシタニアの拠点が聖マヌエル城である。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,7,40],[0,7,10]],c:'A'}]},
 {time:'',clock:'',step:'攻城',title:'城への攻撃',text:'パルス軍は城を囲んで攻めた。守将バルカシオン伯は老齢ながら最後まで城を守ろうとする。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'陥落',title:'聖マヌエル城の陥落',text:'城は落ち、バルカシオン伯は死んだ。アルスラーンは、かつて出会ったルシタニアの少女エトワールと再会する。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'その後',clock:'',step:'その後',title:'王都への道',text:'王都への道が開けたが、東からトゥラーンの侵攻の知らせが届く。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'聖マヌエル城の攻防の結果',when:'パルス暦321年5月、聖マヌエル城',prev:'ザーブル城の攻略／解放王の布告',next:'トゥラーン侵攻（ペシャワール攻防戦）',
 factors:['パルス軍は兵力で大きく上回っていた。','城は孤立しており、ルシタニア本隊からの救援がなかった。'],winner:'A',outcome:'パルス軍の勝利（城を攻略）',
 summary:'王都への進軍の途中、ルシタニアの拠点を落とした戦い。アルスラーンにとって、敵国の人々と向き合う場面ともなった。',
 sides:[{name:'ルシタニア守備隊',side:'E',cmdr:'バルカシオン伯',flag:'—',others:'エトワール',before:'不明',loss:'城を失う',rate:null,deaths:'不明',dead:['バルカシオン伯']},
        {name:'パルス軍',side:'A',cmdr:'アルスラーン',flag:'—',others:'ダリューン、ナルサス',before:'全軍約95,000（騎兵3万8千・歩兵5万・輜重7千）',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['パルス軍は王都に近づく。','トゥラーンの侵攻で、軍はペシャワールへ引き返すことになる。'],
 note:'全軍の兵力は原作4巻の要約による。城の守備兵力は不明。'};
"""
