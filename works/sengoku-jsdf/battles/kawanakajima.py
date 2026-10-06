from common import land_env, specials, labels, shot
UC=1561.09
ARC='川中島と上洛'
OUT='kawanakajima.html'
TITLE='川中島の戦い 3D俯瞰'
HEAD='川中島'
ERA='1561年9月（推定。史実の第四次川中島）'
SE='武田軍'; SA='自衛隊・長尾軍'; PALE='zeon'; PAL='efsf'
NOTE='1979年映画の流れにもとづく概略。部隊の大きさは目安'
ENV=land_env('0x5a6a3a','0x9a9a6a',water='0x4a6a8a',amp=4,seed=3)+specials(labels([('八幡原','','A',(0,10,0),3),('千曲川','','A',(-40,8,20),2.4)]),shot([0,9,30],'武田本陣',2))
DATA=r"""
const U=[
{name:'武田本陣',cmd:'武田信玄',side:'E',n:40,k:{0:{p:[0,7,-40],s:'ready',f:'concave',l:'武田軍'},1:{p:[0,7,-34],s:'fight'},2:{p:[0,7,-30],s:'fight',l:'車両・ヘリを狙う'},3:{p:[0,7,-34],s:'broken',l:'信玄討たれる'}}},
{name:'武田騎馬隊',cmd:'武田軍',side:'E',n:30,k:{0:{p:[-30,7,-30],s:'ready'},1:{p:[-20,7,-6],s:'charge',l:'突撃'},2:{p:[-10,7,10],s:'fight',l:'接近戦'},3:{p:[-30,7,-40],s:'withdraw'}}},
{name:'自衛隊',cmd:'伊庭義明三尉',side:'A',n:14,k:{0:{p:[0,7,30],s:'ready',l:'戦車・ヘリ・装甲車'},1:{p:[0,7,26],s:'fight',b:1},2:{p:[0,7,20],s:'fight',l:'車両と重火器を失う'},3:{p:[0,7,-20],s:'charge',l:'伊庭が本陣へ'}}},
{name:'長尾軍',cmd:'長尾景虎',side:'A',n:40,k:{0:{p:[30,7,30],s:'ready',f:'line'},1:{p:[26,7,10],s:'move'},2:{p:[20,7,-4],s:'fight'},3:{p:[16,7,-18],s:'charge'}}}
];
const PH=[
{time:'開戦前',clock:'',step:'布陣',title:'川中島の対陣',text:'長尾景虎と組んだ自衛隊が、川中島で武田信玄の軍と向き合う。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'開戦',clock:'',step:'突撃',title:'騎馬隊の突撃',text:'武田の騎馬隊が押し寄せ、自衛隊は火力で迎え撃つ。',cam:{fit:1,th:.7,ph:.9},arrows:[{p:[[-30,7,-30],[-10,7,10]],c:'E'}]},
{time:'激戦',clock:'',step:'消耗',title:'近代兵器の喪失',text:'接近戦に持ち込まれ、自衛隊は車両や重火器を失い、5人が戦死した。',cam:{fit:1,th:.3,ph:.85},arrows:[]},
{time:'終局',clock:'',step:'決着',title:'信玄の最期',text:'伊庭は武田本陣に迫り、自ら信玄を討ち取った。',cam:{fit:1,th:.5,ph:1.0},arrows:[{p:[[0,7,20],[0,7,-20]],c:'A'}]}
];
const RESULT={title:'川中島の戦いの結果',when:'1561年（推定）、川中島',prev:'矢野隊の離反',next:'京での最期',
 factors:['自衛隊の火力が武田軍の陣を崩した。','ただし接近戦で車両・重火器を失った。','伊庭自身が本陣に切り込んだ。'],winner:'A',outcome:'自衛隊・長尾軍の勝利（信玄戦死）',
 summary:'作品の山場。史実と違い信玄が討たれるが、自衛隊は近代兵器の多くを失った。',
 sides:[{name:'武田軍',side:'E',cmdr:'武田信玄',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['武田信玄']},
        {name:'自衛隊・長尾軍',side:'A',cmdr:'伊庭義明三尉／長尾景虎',flag:'—',others:'—',before:'不明',loss:'自衛隊員5名戦死、車両・重火器を喪失',rate:null,deaths:'自衛隊員5名',dead:[]}],
 after:['伊庭は天下取りを目指し、京へ向かう。'],
 note:'信玄を伊庭が討つこと、5名戦死と車両・重火器の喪失は英語版Wikipedia「G.I. Samurai」に拠る。年月は史実の第四次川中島（1561年9月）に合わせた推定。'};
"""
