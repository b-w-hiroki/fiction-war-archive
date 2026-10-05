from common import *
UC=2009.04
ARC='帰還の旅'
OUT='saturn.html'
TITLE='土星リングの戦い（ダイダロス・アタック） 3D俯瞰'
HEAD='土星'
ERA='2009年（月日不明・推定）'
SE='ゼントラーディ軍'; SA='統合軍'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-40,-260),120,color='0xc9a86a',land='0xe0c890',label=('土星','リングを盾に','A'))+specials(labels([('土星の環','氷塊の帯','A',(0,6,-60),3)]))
DATA=r"""
const U=[
 {name:'ゼントラーディ艦隊',cmd:'ブリタイ艦隊（推定）',side:'E',n:40,k:{0:{p:[0,0,-60],s:'ready',l:''},1:{p:[0,0,-40],s:'fight',l:''},2:{p:[0,0,-30],s:'fight',l:''},3:{p:[0,0,-30],s:'broken',l:'艦を貫かれる'},4:{p:[0,0,-60],s:'withdraw',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,0,40],s:'ready',l:'環に隠れる'},1:{p:[0,0,20],s:'move',l:''},2:{p:[0,0,0],s:'charge',l:'ダイダロスで突撃'},3:{p:[0,0,-24],s:'fight',l:'零距離で一斉射撃',b:1},4:{p:[0,0,30],s:'ready',l:''}}},
 {name:'VF隊',cmd:'ロイ・フォッカー',side:'A',n:16,k:{0:{p:[14,0,30],s:'ready',l:''},1:{p:[12,0,0],s:'fight',l:''},2:{p:[8,0,-20],s:'fight',l:''},3:{p:[6,0,-28],s:'fight',l:''},4:{p:[14,0,30],s:'ready',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第6話',step:'環',title:'土星の環に入る',text:'マクロスは土星の環の中を進み、氷塊を盾にした。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第6話',step:'交戦',title:'ゼントラーディの追撃',text:'ゼントラーディ艦隊が追いつき、環の中で戦闘になる。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第6話',step:'突撃',title:'ダイダロス・アタック',text:'右腕の空母ダイダロスを敵艦に突き刺した。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第6話',step:'撃沈',title:'艦内から一斉射撃',text:'ダイダロスの艦首から兵器を撃ち込み、敵艦を内側から破壊した。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'土星リングの戦い（ダイダロス・アタック）の戦果',when:'2009年（月日不明・推定）',prev:'—',next:'—',
 factors:["強攻型の腕が空母になっている構造を生かした"],winner:'A',outcome:'統合軍の勝利',summary:'強攻型の腕の空母で敵艦に突っ込み、内側から壊す戦法が生まれた。',
 sides:[{name:'ゼントラーディ軍',side:'E',cmdr:'ブリタイ艦隊（推定）',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍',side:'A',cmdr:'グローバル艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["ダイダロス・アタックが以後の切り札になる"],note:'第6話で土星の環を使う作戦が描かれる（英語版Wikipedia）。細部は記憶にもとづく推定。'};
"""
