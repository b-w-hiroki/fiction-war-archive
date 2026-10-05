from common import *
UC=2009.0207
ARC='開戦'
OUT='misfire.html'
TITLE='主砲誤射（南アタリア島） 3D俯瞰'
HEAD='主砲誤射'
ERA='2009年2月7日'
SE='ゼントラーディ軍'; SA='統合軍'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-260,0),200,label=('地球','南アタリア島上空','A'))+specials(labels([('SDF-1','進宙式の当日','A',(0,14,30),3)]),shot((0,10,30),'ゼントラーディ偵察艦隊',1,delay=1.2,beam='0xffe0a0',w=5,booms=14))
DATA=r"""
const U=[
 {name:'ゼントラーディ偵察艦隊',cmd:'ブリタイ艦隊（推定）',side:'E',n:40,k:{0:{p:[0,10,-50],s:'ready',l:'地球圏に出現'},1:{p:[0,10,-40],s:'ready',l:''},2:{p:[0,10,-36],s:'fight',l:'反撃'},3:{p:[0,10,-40],s:'fight',l:''},4:{p:[0,10,-55],s:'withdraw',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,4,30],s:'ready',l:'進宙式'},1:{p:[0,4,30],s:'fight',l:'主砲が自動発射',b:1},2:{p:[0,4,30],s:'fight',l:''},3:{p:[0,10,30],s:'move',l:'フォールド'},4:{s:'gone'}}},
 {name:'統合軍VF隊',cmd:'ロイ・フォッカー',side:'A',n:20,k:{0:{p:[10,4,20],s:'ready',l:''},1:{p:[10,6,10],s:'fight',l:''},2:{p:[8,6,0],s:'fight',l:'迎撃'},3:{p:[6,6,10],s:'fight',l:''},4:{s:'gone'}}}
];
const PH=[
 {time:'2月7日',clock:'TV第1話',step:'誤射',title:'主砲の自動発射',text:'進宙式の日、ゼントラーディ艦隊が地球圏に現れた。マクロスの主砲が自動で発射され、敵艦を撃った。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'同日',clock:'TV第1話',step:'開戦',title:'第一次星間大戦の始まり',text:'この誤射で戦争が始まった。ゼントラーディは南アタリア島を攻撃する。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'同日',clock:'TV第2話',step:'防空戦',title:'島の防空戦',text:'統合軍のVF隊が迎え撃つ。民間人の一条輝も戦闘に巻き込まれる。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'同日',clock:'TV第3話',step:'フォールド',title:'月軌道へのフォールド失敗',text:'マクロスは月の裏へ逃れようとフォールドしたが、島ごと冥王星軌道付近へ飛ばされた。',cam:{fit:1,th:0.75,ph:.9},arrows:[]}
];
const RESULT={title:'主砲誤射（南アタリア島）の戦果',when:'2009年2月7日',prev:'—',next:'—',
 factors:["主砲は異星人の艦に反応する自動の仕掛けだった（推定）", "フォールド装置の制御が不十分だった"],winner:'none',outcome:'決着なし（マクロスが離脱）',summary:'主砲の誤射で第一次星間大戦が始まった。マクロスは島ごと太陽系の外縁へ飛ばされる。',
 sides:[{name:'ゼントラーディ軍',side:'E',cmdr:'ブリタイ艦隊（推定）',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍',side:'A',cmdr:'グローバル艦長',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["南アタリア島の住民約5万8千人がマクロスに収容される", "フォールド装置は消失する（推定）"],note:'日付は日本語Wikipediaの作品解説（2009年2月7日進宙式）による。兵力は不明。'};
"""
