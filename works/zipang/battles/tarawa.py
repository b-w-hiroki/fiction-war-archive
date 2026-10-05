from common import *
UC=1943.11
ARC='北と南'
OUT='tarawa.html'
TITLE='タラワ撤収 3D俯瞰'
HEAD='タラワ'
ERA='1943年11月（推定）'
SE='米軍'; SA='日本軍・みらい'; PALE='efsf'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は概略で、位置関係・兵力は推定'
ENV=land_env('0xc8b888','0xd8cca0',water='0x2a6a8e',amp=1.5,seed=13,sky='0x8aa0b8')+specials(labels([('タラワ環礁','ギルバート諸島','A',(0,16,0),3)]))
DATA=r"""
const U=[
{name:'米上陸部隊',cmd:'不明',side:'E',n:30,k:{0:{p:[0,7,-50],s:'move'},1:{p:[0,7,-20],s:'charge',l:'上陸'},2:{p:[0,7,-10],s:'fight'},3:{p:[0,7,-5],s:'fight',l:'島を占領'}}},
{name:'日本軍守備隊',cmd:'不明',side:'A',n:15,k:{0:{p:[0,7,5],s:'ready'},1:{p:[0,7,5],s:'fight'},2:{p:[0,7,15],s:'withdraw',l:'撤収'},3:{p:[-10,7,40],s:'withdraw',nf:1}}},
{name:'みらい',cmd:'梅津三郎',side:'A',n:6,k:{0:{p:[20,7,40],s:'move'},1:{p:[20,7,35],s:'fight'},2:{p:[20,7,35],s:'fight',l:'菊池砲雷長が負傷'},3:{p:[20,7,50],s:'withdraw'}}}
];
const PH=[
{time:'1943年11月（推定）',clock:'',step:'来襲',title:'米軍の来襲',text:'米軍がタラワ環礁に迫った。',cam:{fit:1,th:.5,ph:.9},arrows:[{p:[[0,7,-50],[0,7,-20]],c:'E'}]},
{time:'',clock:'',step:'上陸',title:'上陸と抵抗',text:'米軍が上陸し、守備隊が抵抗した。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
{time:'',clock:'',step:'撤収',title:'撤収作戦',text:'日本側は撤収を進めた。その最中に砲雷長の菊池が負傷した。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[0,7,15],[-10,7,40]],c:'A'}]},
{time:'',clock:'',step:'占領',title:'米軍の占領',text:'島は米軍の手に落ちた（推定）。',cam:{fit:1,th:.6,ph:1.0},arrows:[]}
];
const RESULT={title:'タラワ撤収の結果',when:'1943年11月（推定）、タラワ環礁',prev:'キスカ撤退',next:'サイパン沖の決戦',
 factors:['資料が少なく、戦いの細部は確認できていない。'],winner:'E',outcome:'米軍の占領（推定）・日本側は撤収',
 summary:'日本側の撤収作戦の最中に、みらいの菊池砲雷長が負傷した。展開の細部は確認できていない。',
 sides:[{name:'米軍',side:'E',cmdr:'不明',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'日本軍・みらい',side:'A',cmdr:'不明',flag:'みらい',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['菊池は負傷で戦列を離れ、みらいの中の力関係が変わる（推定）。'],
 note:'「タラワ（1943年11月）の撤収作戦で菊池が負傷」は英語版Wikipedia「Zipang (manga)」に拠る。それ以外の展開・結果は史実をもとにした推定。アニメ化されていない。'};
"""
