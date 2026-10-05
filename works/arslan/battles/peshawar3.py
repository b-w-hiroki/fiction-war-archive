from common import land_env, specials, labels
UC=325.6
ARC='第二部'
OUT='peshawar3.html'
TITLE='ペシャワールの三つ巴 3D俯瞰'
HEAD='三つ巴'
ERA='パルス暦325年（推定）'
SE='チュルク軍'; SA='シンドゥラ軍'; PALE='turan'; PAL='sind'
NOTE='交戦中／健在の部隊。配置は原作小説の要約にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a5a48','0x9a8a68',amp=6,seed=32)+specials(labels([('ペシャワール', '', 'A', (0, 10, 0), 3)]))
DATA=r"""
const U=[
{name:'チュルク軍',cmd:'チュルク軍',side:'E',n:30,k:{0:{p:[-20,7,-25],s:'move'},1:{p:[-6,7,-8],s:'fight'},2:{p:[-6,7,-8],s:'broken',l:'ほぼ全滅'}}},
 {name:'シンドゥラ軍',cmd:'ラジェンドラ二世',side:'A',n:30,k:{0:{p:[20,7,25],s:'move'},1:{p:[6,7,8],s:'fight'},2:{p:[10,7,20],s:'withdraw',l:'象400頭・兵1万近く喪失'}}}
];
const PH=[
{time:'325年',clock:'',step:'進軍',title:'三勢力の接近',text:'ペシャワール周辺に、シンドゥラ軍、チュルク軍、魔軍が入り乱れた。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'交戦',title:'三つ巴',text:'三つの勢力が互いにぶつかり合った。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'地震',title:'大地震',text:'大地震が起き、シンドゥラ軍は象約400頭と兵1万近くを失い、チュルク軍はほぼ全滅した。',cam:{fit:1,th:.3,ph:.9},arrows:[]}
];
const RESULT={title:'ペシャワールの三つ巴の結果',when:'パルス暦325年（推定）、ペシャワール',prev:'ペシャワール城の攻防（対魔軍）',next:'ナルサスの戦死',
 factors:['大地震が戦場を襲った。'],winner:'none',outcome:'決着つかず（大地震で両軍壊滅的損害）',
 summary:'シンドゥラ・チュルク・魔軍の三つ巴が、大地震によって終わった戦い。',
 sides:[{name:'チュルク軍',side:'E',cmdr:'—',flag:'—',others:'—',before:'不明',loss:'ほぼ全滅',rate:null,deaths:'不明',dead:[]},
        {name:'シンドゥラ軍',side:'A',cmdr:'ラジェンドラ二世',flag:'—',others:'—',before:'不明',loss:'象約400頭・兵1万近く',rate:null,deaths:'不明',dead:[]}],
 after:['東方の諸国が大きく消耗する。'],
 note:'14巻。経過は原作小説の要約（本の窓口ほんシェルジュ「小説『アルスラーン戦記』全16巻分の魅力をネタバレ紹介」、chichibu.moo.jp「アルスラーン戦記第二部」）による。損害は同要約による。年と配置は推定。陣営色はチュルクをトゥラーン系、シンドゥラをシンドゥラ色で示した。'};
"""
