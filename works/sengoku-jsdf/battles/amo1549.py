from common import land_env, specials, labels
UC=1549.06
ARC='1549'
OUT='amo1549.html'
TITLE='天母城の戦い 3D俯瞰'
HEAD='天母城'
ERA='1549年（推定）'
SE='的場の部隊'; SA='救出部隊'; PALE='zeon'; PAL='efsf'
NOTE='2005年映画『戦国自衛隊1549』の概略。配置は推定'
ENV=land_env('0x4f5a3a','0x8a8a6a',amp=6,seed=11)+specials(labels([('天母城','','E',(0,14,-30),3)]))
DATA=r"""
const U=[
{name:'的場の部隊',cmd:'的場毅一佐',side:'E',n:30,k:{0:{p:[0,7,-30],s:'ready',l:'城に拠る'},1:{p:[0,7,-28],s:'fight'},2:{p:[0,7,-26],s:'fight',b:1},3:{p:[0,7,-30],s:'broken'}}},
{name:'救出部隊',cmd:'森三佐／鹿島',side:'A',n:16,k:{0:{p:[0,7,30],s:'ready',l:'時代を越えて救出へ'},1:{p:[0,7,10],s:'move'},2:{p:[0,7,-6],s:'fight'},3:{p:[0,7,-20],s:'charge'}}}
];
const PH=[
{time:'1549年',clock:'',step:'到着',title:'救出部隊の転移',text:'先に戦国時代へ消えた部隊を救うため、別の部隊が1549年へ送られる。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
{time:'接近',clock:'',step:'接近',title:'天母城へ',text:'先遣隊を率いた的場は城を築き、歴史を変えようとしていた。',cam:{fit:1,th:.7,ph:.9},arrows:[{p:[[0,7,30],[0,7,10]],c:'A'}]},
{time:'攻防',clock:'',step:'攻防',title:'城での戦い',text:'救出部隊は城に入り、的場の部隊と戦う。',cam:{fit:1,th:.3,ph:.85},arrows:[]},
{time:'終局',clock:'',step:'決着',title:'計画の阻止',text:'的場の計画は阻まれる。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'天母城の戦いの結果',when:'1549年（推定）、天母城',prev:'先遣隊の転移',next:'—',
 factors:['救出部隊が的場の計画を阻んだ。'],winner:'A',outcome:'救出部隊の勝利（推定）',
 summary:'リメイク映画の山場。歴史を書き換えようとする自衛官を、後から来た部隊が止める。',
 sides:[{name:'的場の部隊',side:'E',cmdr:'的場毅',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'救出部隊',side:'A',cmdr:'森三佐',flag:'—',others:'鹿島',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['戦国時代と現代のつながりが断たれる。'],
 note:'人名・城名・展開は記憶にもとづく推定で、出典確認が不十分。'};
"""
