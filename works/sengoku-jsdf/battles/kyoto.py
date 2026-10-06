from common import land_env, specials, labels
UC=1561.12
ARC='川中島と上洛'
OUT='kyoto.html'
TITLE='京の寺での最期 3D俯瞰'
HEAD='京の最期'
ERA='1561年（推定）'
SE='長尾軍（裏切り）'; SA='伊庭隊'; PALE='zeon'; PAL='efsf'
NOTE='1979年映画の流れにもとづく概略。時期は推定'
ENV=land_env('0x5a5a4a','0x8a8070',amp=3,seed=9)+specials(labels([('京の寺','','A',(0,12,20),3)]))
DATA=r"""
const U=[
{name:'長尾軍',cmd:'長尾景虎',side:'E',n:40,k:{0:{p:[0,7,-40],s:'hidden'},1:{p:[0,7,-30],s:'move',l:'寺を囲む'},2:{p:[0,7,0],s:'charge',f:'concave'},3:{p:[0,7,10],s:'fight'}}},
{name:'伊庭隊',cmd:'伊庭義明三尉',side:'A',n:8,k:{0:{p:[0,7,20],s:'ready',l:'京に入る'},1:{p:[0,7,20],s:'wait'},2:{p:[0,7,18],s:'fight',l:'寺で応戦'},3:{p:[0,7,20],s:'gone',l:'全滅'}}},
{name:'根元',cmd:'根元茂吉',side:'A',n:2,k:{0:{p:[30,7,30],s:'wait',l:'隊を離れていた'},1:{p:[30,7,30],s:'wait'},2:{p:[34,7,34],s:'wait'},3:{p:[40,7,44],s:'withdraw',l:'ただ一人生き残る'}}}
];
const PH=[
{time:'上洛',clock:'',step:'入京',title:'京へ',text:'川中島のあと、伊庭は残った隊員とともに京に入る。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'寺',clock:'',step:'包囲',title:'景虎の決断',text:'政治の圧力から、景虎は伊庭を除くことを決め、寺を囲む。',cam:{fit:1,th:.7,ph:.9},arrows:[{p:[[0,7,-40],[0,7,-30]],c:'E'}]},
{time:'襲撃',clock:'',step:'襲撃',title:'寺への襲撃',text:'伊庭隊は寺で襲われ、応戦する。',cam:{fit:1,th:.3,ph:.85},arrows:[{p:[[0,7,-30],[0,7,0]],c:'E'}]},
{time:'終局',clock:'',step:'全滅',title:'ただ一人の生還',text:'伊庭隊は全滅し、隊を離れていた根元だけが生き残った。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'京の寺での最期の結果',when:'1561年ごろ（推定）、京',prev:'川中島の戦い',next:'—',
 factors:['自衛隊の力が景虎にとって危うくなった。','近代兵器を失い、少人数で孤立していた。'],winner:'E',outcome:'長尾軍の勝利（伊庭隊全滅）',
 summary:'同盟者に裏切られ、伊庭隊は京の寺で全滅した。映画の結末。',
 sides:[{name:'長尾軍',side:'E',cmdr:'長尾景虎',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'伊庭隊',side:'A',cmdr:'伊庭義明三尉',flag:'—',others:'—',before:'不明（11名以下）',loss:'根元を除き全員',rate:null,deaths:'不明',dead:['伊庭義明']}],
 after:['根元茂吉だけが生き残る。'],
 note:'結末は英語版Wikipedia「G.I. Samurai」の映画あらすじに拠る。小説は結末が異なる（伊庭が織田信長の役割を担う流れとされるが未確認）。'};
"""
