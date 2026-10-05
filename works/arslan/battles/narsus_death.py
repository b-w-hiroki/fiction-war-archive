from common import land_env, specials, labels
UC=325.9
ARC='第二部'
OUT='narsus_death.html'
TITLE='ナルサスの戦死 3D俯瞰'
HEAD='軍師の死'
ERA='パルス暦325年（推定）'
SE='ヒルメス'; SA='パルス軍'; PALE='hilmes'; PAL='parse'
NOTE='交戦中／健在の部隊。配置は原作小説の要約にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a48','0x9a8a68',amp=6,seed=33)+specials(labels([('戦場（場所は未確認）', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'ヒルメス軍',cmd:'ヒルメス',side:'E',n:24,k:{0:{p:[0,7,-25],s:'move'},1:{p:[0,7,-5],s:'charge'},2:{p:[0,7,-15],s:'withdraw'}}},
 {name:'ナルサス',cmd:'ナルサス',side:'A',n:12,k:{0:{p:[0,7,10],s:'ready'},1:{p:[0,7,4],s:'fight'},2:{p:[0,7,4],s:'gone',l:'ナルサス・アルフリード戦死'}}}
];
const PH=[
{time:'325年',clock:'',step:'対峙',title:'ヒルメスとの対決',text:'軍師ナルサスが、ヒルメスと対決した。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'激突',title:'激突',text:'ヒルメスの攻撃を受け、ナルサスと妻アルフリードが倒れた。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'喪失',title:'軍師を失う',text:'パルスは天才軍師を失い、蛇王との最終決戦に向かう。',cam:{fit:1,th:.3,ph:.9},arrows:[]}
];
const RESULT={title:'ナルサスの戦死の結果',when:'パルス暦325年（推定）、戦場（場所は未確認）',prev:'ペシャワールの三つ巴',next:'エクバターナ最終決戦',
 factors:['—'],winner:'E',outcome:'ナルサス・アルフリード戦死',
 summary:'第二部でパルスが軍師ナルサスを失った戦い。',
 sides:[{name:'ヒルメス',side:'E',cmdr:'ヒルメス',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'パルス軍',side:'A',cmdr:'ナルサス',flag:'—',others:'アルフリード',before:'不明',loss:'ナルサス・アルフリード戦死',rate:null,deaths:'不明',dead:['ナルサス','アルフリード']}],
 after:['パルスは軍師を欠いたまま最終決戦を迎える。'],
 note:'15巻『戦旗不倒』。経過は原作小説の要約（本の窓口ほんシェルジュ「小説『アルスラーン戦記』全16巻分の魅力をネタバレ紹介」、chichibu.moo.jp「アルスラーン戦記第二部」）による。場所・兵力・経過の詳細は確認できなかった（ザーブル城とする説は未確認）。年は推定。'};
"""
