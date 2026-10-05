from common import *
UC=2009.09
ARC='帰還の旅'
OUT='blockade.html'
TITLE='包囲突破と地球帰還 3D俯瞰'
HEAD='地球帰還'
ERA='2009年（月日不明・推定）'
SE='ゼントラーディ軍'; SA='統合軍'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-260,40),200,label=('地球','帰還','A'))+specials(labels([('包囲網','ゼントラーディ艦隊','E',(0,20,-40),3)]))
DATA=r"""
const U=[
 {name:'ゼントラーディ包囲艦隊',cmd:'ブリタイ艦隊',side:'E',n:50,k:{0:{p:[0,0,-40],s:'ready',l:'包囲'},1:{p:[0,0,-30],s:'fight',l:''},2:{p:[0,0,-20],s:'fight',l:''},3:{p:[0,0,-30],s:'broken',l:'突破される'},4:{p:[0,0,-60],s:'withdraw',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,0,40],s:'ready',l:''},1:{p:[0,0,20],s:'charge',l:'強行突破'},2:{p:[0,0,-10],s:'charge',l:''},3:{p:[0,0,-40],s:'move',l:''},4:{p:[0,-20,-50],s:'ready',l:'地球へ'}}},
 {name:'VF隊',cmd:'ロイ・フォッカー',side:'A',n:16,k:{0:{p:[12,0,36],s:'ready',l:''},1:{p:[10,0,14],s:'fight',l:''},2:{p:[8,0,-12],s:'fight',l:''},3:{p:[6,0,-36],s:'move',l:''},4:{p:[6,-20,-46],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第13話',step:'包囲',title:'地球を前に包囲される',text:'捕虜から逃れた後、マクロスの前に敵の包囲網があった（推定）。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第13話',step:'突破',title:'包囲網へ突入',text:'マクロスは包囲の中を強行突破した。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第13話',step:'交戦',title:'VF隊の援護',text:'VF隊が艦を援護する。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第13話',step:'帰還',title:'地球へ',text:'マクロスは地球に帰り着いた。しかし統合政府は民間人の下船を認めなかった。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'包囲突破と地球帰還の戦果',when:'2009年（月日不明・推定）',prev:'—',next:'—',
 factors:["強攻型の火力で正面を開いた（推定）"],winner:'A',outcome:'統合軍の突破成功',summary:'マクロスは包囲を破って地球に帰り着いたが、政府は艦を秘密にしようとした。',
 sides:[{name:'ゼントラーディ軍',side:'E',cmdr:'ブリタイ艦隊',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍',side:'A',cmdr:'グローバル艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["統合政府はマクロスに地球からの退去を命じる（第19話）"],note:'第13話の「包囲を突破して地球へ」は英語版Wikipediaの話数一覧による。時期は推定。'};
"""
