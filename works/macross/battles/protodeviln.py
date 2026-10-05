from common import *
UC=2046.09
ARC='マクロス7'
OUT='protodeviln.html'
TITLE='プロトデビルン最終決戦 3D俯瞰'
HEAD='プロトデビルン'
ERA='2046年（月日不明・推定）'
SE='プロトデビルン'; SA='マクロス7船団'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+specials(labels([('ゲペルニッチ','スピリチアの渦','E',(0,24,-50),3.4)]))
DATA=r"""
const U=[
 {name:'プロトデビルン',cmd:'ゲペルニッチ',side:'E',n:30,k:{0:{p:[0,0,-50],s:'ready',l:''},1:{p:[0,0,-36],s:'fight',l:'スピリチアを吸う'},2:{p:[0,0,-30],s:'fight',l:'巨大化'},3:{p:[0,0,-34],s:'wait',l:'歌に応える'},4:{p:[0,0,-80],s:'withdraw',l:'銀河を去る'}}},
 {name:'マクロス7',cmd:'マクシミリアン・ジーナス艦長',side:'A',n:20,k:{0:{p:[0,0,30],s:'ready',l:''},1:{p:[0,0,24],s:'fight',l:''},2:{p:[0,0,20],s:'fight',l:''},3:{p:[0,0,16],s:'wait',l:'歌を届ける'},4:{p:[0,0,20],s:'ready',l:''}}},
 {name:'ファイアーボンバー',cmd:'熱気バサラ',side:'A',n:6,k:{0:{p:[10,0,20],s:'ready',l:''},1:{p:[8,0,0],s:'fight',l:'歌で挑む'},2:{p:[6,0,-10],s:'fight',l:''},3:{p:[4,0,-20],s:'fight',l:''},4:{p:[10,0,10],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第47話（推定）',step:'襲来',title:'プロトデビルンの攻勢',text:'プロトデビルンは人の生命エネルギー「スピリチア」を奪っていた。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第48話（推定）',step:'吸収',title:'銀河規模の脅威',text:'ゲペルニッチは巨大化し、宇宙のスピリチアを吸い尽くす存在になりかけた。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第49話',step:'歌',title:'歌で説得',text:'熱気バサラらは武力ではなく歌で向き合い、自分でスピリチアを生めると示した。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第49話',step:'終結',title:'銀河を去る',text:'ゲペルニッチたちは新しい姿で銀河を去り、戦いは終わった。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'プロトデビルン最終決戦の戦果',when:'2046年（月日不明・推定）',prev:'—',next:'—',
 factors:["歌がプロトデビルン自身にスピリチアを生ませた"],winner:'A',outcome:'和解による終結',summary:'敵を倒すのではなく、歌で説得して戦いを終わらせた。',
 sides:[{name:'プロトデビルン',side:'E',cmdr:'ゲペルニッチ',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'マクロス7船団',side:'A',cmdr:'マクシミリアン・ジーナス艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["プロトデビルンは銀河の外へ去る"],note:'2046年と結末は英語版Wikipedia（Macross 7）による。最終決戦が第45〜49話であることはhttps://en.wikipedia.org/wiki/List_of_Macross_7_episodes で確認。第47・48話への場面の割り振りは記憶にもとづく。'};
"""
