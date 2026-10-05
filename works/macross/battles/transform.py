from common import *
UC=2009.03
ARC='帰還の旅'
OUT='transform.html'
TITLE='マクロス強攻型の初戦 3D俯瞰'
HEAD='強攻型'
ERA='2009年（月日不明・推定）'
SE='ゼントラーディ軍'; SA='統合軍'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+specials(labels([('冥王星軌道付近','フォールド後の宙域','A',(0,24,0),3)]))
DATA=r"""
const U=[
 {name:'ゼントラーディ部隊',cmd:'ブリタイ艦隊（カムジン隊の参加は記憶にもとづく）',side:'E',n:30,k:{0:{p:[0,0,-50],s:'ready',l:''},1:{p:[0,0,-30],s:'fight',l:'攻撃'},2:{p:[0,0,-20],s:'fight',l:''},3:{p:[0,0,-26],s:'broken',l:''},4:{p:[0,0,-50],s:'withdraw',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,0,30],s:'ready',l:''},1:{p:[0,0,30],s:'wait',l:'主砲が撃てない'},2:{p:[0,0,26],s:'move',l:'強攻型へ変形'},3:{p:[0,0,24],s:'fight',l:'主砲発射',b:1},4:{p:[0,0,30],s:'ready',l:''}}},
 {name:'VF隊',cmd:'ロイ・フォッカー',side:'A',n:16,k:{0:{p:[10,0,20],s:'ready',l:''},1:{p:[8,0,0],s:'fight',l:''},2:{p:[6,0,-6],s:'fight',l:''},3:{p:[4,0,-10],s:'fight',l:''},4:{p:[10,0,20],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第4話',step:'漂流',title:'帰還の旅の始まり',text:'フォールド後、マクロスは民間人を乗せて地球への長い旅を始めた。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第5話',step:'接敵',title:'主砲が撃てない',text:'フォールド装置を失った影響で主砲への動力系が使えなくなっていた（推定）。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第5話',step:'変形',title:'強攻型への変形',text:'艦を人型に組み替えて主砲を撃てるようにした。艦内の市街地にも被害が出た。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第5話',step:'撃退',title:'敵を撃退',text:'強攻型の主砲で敵を退けた。以後の基本形態になる。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'マクロス強攻型の初戦の戦果',when:'2009年（月日不明・推定）',prev:'—',next:'—',
 factors:["変形で主砲の砲身をつなぎ直した（推定）"],winner:'A',outcome:'統合軍の勝利（撃退）',summary:'マクロスが初めて強攻型に変形して戦った。主砲は使えるようになったが、艦内市街に被害が出た。',
 sides:[{name:'ゼントラーディ軍',side:'E',cmdr:'ブリタイ艦隊（カムジン隊の参加は記憶にもとづく）',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍',side:'A',cmdr:'グローバル艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["以後、強攻型が戦闘時の形態になる"],note:'話数は英語版Wikipediaの話数一覧（https://en.wikipedia.org/wiki/List_of_The_Super_Dimension_Fortress_Macross_episodes 、第5話でブリタイとエキセドルが登場）による。変形の理由は記憶にもとづく推定。'};
"""
