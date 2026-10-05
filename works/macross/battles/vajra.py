from common import *
UC=2059.1
ARC='マクロスF'
OUT='vajra.html'
TITLE='バジュラ本星決戦 3D俯瞰'
HEAD='バジュラ'
ERA='2059年（月日不明・推定）'
SE='バジュラ／ギャラクシー残党'; SA='マクロス・フロンティア船団'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-240,-40),190,color='0x3a6a8a',land='0x6a9a5a',label=('バジュラ本星','銀河中心近く','E'))+specials(labels([('クイーン','バジュラの中枢','E',(0,10,-50),3.2)]))
DATA=r"""
const U=[
 {name:'バジュラ群',cmd:'クイーン',side:'E',n:60,k:{0:{p:[0,0,-50],s:'ready',l:''},1:{p:[0,0,-34],s:'fight',l:''},2:{p:[0,0,-30],s:'fight',l:''},3:{p:[0,0,-34],s:'wait',l:'歌で敵意を解く'},4:{p:[0,0,-40],s:'ready',l:''}}},
 {name:'ギャラクシー残党',cmd:'グレイスほか',side:'E',n:10,k:{0:{p:[20,0,-40],s:'ready',l:'クイーンを支配'},1:{p:[20,0,-30],s:'fight',l:''},2:{p:[16,0,-24],s:'fight',l:''},3:{p:[12,0,-20],s:'broken',l:''},4:{s:'gone'}}},
 {name:'フロンティア船団',cmd:'ワイルダー艦長',side:'A',n:30,k:{0:{p:[0,0,40],s:'ready',l:'本星へ'},1:{p:[0,0,20],s:'fight',l:''},2:{p:[0,0,10],s:'charge',l:'',b:1},3:{p:[0,0,6],s:'fight',l:''},4:{p:[0,0,10],s:'ready',l:''}}},
 {name:'SMS VF隊',cmd:'早乙女アルト',side:'A',n:12,k:{0:{p:[12,0,30],s:'ready',l:''},1:{p:[10,0,0],s:'fight',l:''},2:{p:[10,0,-14],s:'charge',l:'シェリルとランカの歌'},3:{p:[12,0,-20],s:'charge',l:''},4:{p:[10,0,0],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第24話（推定）',step:'到着',title:'本星へ',text:'住む星を失いかけた船団は、バジュラの本星へ向かった。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第25話',step:'交戦',title:'本星での決戦',text:'バジュラとの総力戦になる。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第25話',step:'歌',title:'二人の歌',text:'シェリルとランカの歌がバジュラに届く。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第25話',step:'黒幕',title:'ギャラクシー残党の敗北',text:'バジュラを操っていたグレイスたちが倒された。',cam:{fit:1,th:0.75,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第25話',step:'共存',title:'共存へ',text:'バジュラとの戦いは終わり、船団は本星に降りる。',cam:{fit:1,th:0.90,ph:.9},arrows:[]}
];
const RESULT={title:'バジュラ本星決戦の戦果',when:'2059年（月日不明・推定）',prev:'—',next:'—',
 factors:["歌がバジュラとの意思疎通を可能にした"],winner:'A',outcome:'フロンティア船団の勝利・バジュラとの和解',summary:'黒幕を倒し、歌でバジュラとの戦いを終わらせた。',
 sides:[{name:'バジュラ／ギャラクシー残党',side:'E',cmdr:'クイーン',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'マクロス・フロンティア船団',side:'A',cmdr:'ワイルダー艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["船団は本星に移り住む（推定）"],note:'全25話（英語版Wikipedia）。年代と細部は記憶にもとづく推定。'};
"""
