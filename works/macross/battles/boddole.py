from common import *
UC=2010.02
ARC='最終決戦'
OUT='boddole.html'
TITLE='ボドル基幹艦隊決戦 3D俯瞰'
HEAD='ボドル'
ERA='2010年（月日不明・推定）'
SE='ボドル基幹艦隊'; SA='統合軍・ブリタイ艦隊'; PALE='titan'; PAL='efsf'
NOTE='交戦中／健在の部隊。展開は作中描写にもとづく概略（位置は抽象化）'
ENV=space_env()+planet((0,-260,40),200,color='0x5a4a40',land='0x7a6050',label=('地球','砲撃で焦土に','A'))+specials(labels([('ボドル基幹艦隊','400万隻以上','E',(0,24,-60),3.4)]),shot((0,0,20),'ボドル基幹艦隊',3,delay=1.5,beam='0xfff2b0',w=6,booms=16))
DATA=r"""
const U=[
 {name:'ボドル基幹艦隊',cmd:'ボドルザー',side:'E',n:90,k:{0:{p:[0,0,-60],s:'ready',l:'地球圏にフォールド'},1:{p:[0,-10,-40],s:'fight',l:'地球を一斉砲撃',b:1},2:{p:[0,0,-40],s:'fight',l:''},3:{p:[0,0,-40],s:'broken',l:'歌で混乱'},4:{p:[0,0,-50],s:'broken',l:'旗艦撃沈'}}},
 {name:'ブリタイ艦隊',cmd:'ブリタイ（統合軍と同盟）',side:'A',n:30,k:{0:{p:[30,0,30],s:'ready',l:''},1:{p:[30,0,20],s:'wait',l:''},2:{p:[26,0,0],s:'fight',l:''},3:{p:[20,0,-20],s:'charge',l:''},4:{p:[20,0,-30],s:'ready',l:''}}},
 {name:'SDF-1マクロス',cmd:'グローバル艦長',side:'A',n:10,k:{0:{p:[0,0,30],s:'ready',l:''},1:{p:[0,-10,20],s:'fight',l:'グランド・キャノンの後'},2:{p:[0,0,20],s:'fight',l:'歌を全艦に流す'},3:{p:[0,0,0],s:'charge',l:''},4:{p:[0,0,-40],s:'charge',l:'旗艦に突入'}}},
 {name:'VF隊',cmd:'一条輝ほか',side:'A',n:16,k:{0:{p:[-14,0,30],s:'ready',l:''},1:{p:[-12,0,20],s:'fight',l:''},2:{p:[-10,0,0],s:'fight',l:''},3:{p:[-8,0,-20],s:'charge',l:''},4:{p:[-4,0,-40],s:'charge',l:''}}}
];
const PH=[
 {time:'不明',clock:'TV第27話',step:'出現',title:'基幹艦隊の地球圏到着',text:'ゼントラーディの本隊ボドル基幹艦隊が地球圏に現れた。',cam:{fit:1,th:0.30,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第27話',step:'砲撃',title:'地球への一斉砲撃',text:'基幹艦隊は地球を砲撃し、地上の生命の大半が失われた。',cam:{fit:1,th:0.45,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第27話',step:'反撃',title:'歌による反撃',text:'マクロスはリン・ミンメイの歌を流し、文化に触れていない敵兵を混乱させた。ブリタイ艦隊も味方として戦う。',cam:{fit:1,th:0.60,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第27話',step:'突入',title:'旗艦への突入',text:'混乱した艦隊の中を進み、マクロスは基幹艦隊の旗艦に突入した。',cam:{fit:1,th:0.75,ph:.9},arrows:[]},
 {time:'不明',clock:'TV第27話',step:'終戦',title:'ボドルザー戦死',text:'旗艦は内部から破壊され、ボドルザーは死んだ。第一次星間大戦は終わる。',cam:{fit:1,th:0.90,ph:.9},arrows:[]}
];
const RESULT={title:'ボドル基幹艦隊決戦の戦果',when:'2010年（月日不明・推定）',prev:'—',next:'—',
 factors:["文化に触れたことのないゼントラーディ兵が歌で混乱した", "ブリタイ艦隊が人類側についた"],winner:'A',outcome:'統合軍・ブリタイ艦隊の勝利',summary:'地球は焦土となったが、歌で敵を混乱させて基幹艦隊を破った。第一次星間大戦の終わり。',
 sides:[{name:'ボドル基幹艦隊',side:'E',cmdr:'ボドルザー',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'統合軍・ブリタイ艦隊',side:'A',cmdr:'ブリタイ（統合軍と同盟）',flag:'不明',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:["生き残った人類とゼントラーディの共存と復興が始まる（第28話以降、約2年後）"],note:'「400万隻以上」は英語版Wikipediaの話数要約（over 4,000,000 warships）による。地球の生命の大半が失われたことは日本語Wikipediaによる。日付は不明、年は推定。'};
"""
