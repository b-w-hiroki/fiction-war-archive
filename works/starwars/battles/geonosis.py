from common import *
UC=978.0
ARC='クローン戦争'
OUT='geonosis.html'
TITLE='ジオノーシスの戦い 3D俯瞰'
HEAD='ジオノーシス'
ERA='22 BBY（ヤヴィンの戦いの22年前）'
SE='独立星系連合'; SA='銀河共和国'; PALE='serpent'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は映画・アニメの描写にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x8a5a30','0xc8a070',amp=4,seed=7,sky='0xc89060')+specials(labels([('闘技場','ジェダイ救出から開戦','A',(0, 24, -20),3.4)]))
DATA=r"""
const U=[
 {name:'ドロイド軍',cmd:'ドゥークー伯爵',side:'E',n:60,k:{0:{p:[0,7,-20],s:'ready',l:'闘技場を包囲'},1:{p:[0,7,-14],s:'fight',b:1},2:{p:[0,7,-10],s:'fight'},3:{p:[0,7,-40],s:'withdraw',l:'撤退'}}},
 {name:'ジェダイ',cmd:'メイス・ウィンドゥ',side:'A',n:8,k:{0:{p:[0,7,-16],s:'fight',l:'救出に突入'},1:{p:[0,7,-18],s:'broken',l:'包囲される'},2:{p:[0,7,10],s:'move',l:'救出される'},3:{p:[0,7,10],s:'ready'}}},
 {name:'クローン軍',cmd:'ヨーダ',side:'A',n:50,k:{0:{p:[0,7,50],s:'hidden'},1:{p:[10,7,10],s:'charge',l:'ヨーダが到着'},2:{p:[0,7,0],s:'fight',f:'line',b:1},3:{p:[0,7,-20],s:'charge',l:'戦場を制す'}}}
];
const PH=[
 {time:'22 BBY',clock:'エピソード2',step:'処刑',title:'闘技場',text:'捕らえられたオビ＝ワンらの処刑の場に、ジェダイが救出に入った。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'',clock:'',step:'包囲',title:'ジェダイの包囲',text:'ジェダイはドロイド軍に囲まれ、多くが倒れた。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'援軍',title:'クローン軍の到着',text:'ヨーダがクローン軍を率いて到着し、生き残ったジェダイを救った。',cam:{fit:1,th:.3,ph:.9},arrows:[{p:[[0,7,50],[10,7,10]],c:'A'}]},
 {time:'',clock:'',step:'開戦',title:'クローン戦争の始まり',text:'共和国軍はドロイド軍を退けたが、ドゥークーは逃れた。戦争はここから銀河全体に広がる。',cam:{fit:1,th:.5,ph:.9},arrows:[]}
];
const RESULT={title:'ジオノーシスの戦いの戦果',when:'22 BBY、惑星ジオノーシス',prev:'ナブーの戦い',next:'コルサントの戦い',
 factors:['クローン軍が初めて実戦に投入された。'],winner:'A',outcome:'共和国の勝利（ドゥークーは逃亡）',
 summary:'クローン戦争の最初の戦い。共和国が勝ったが、全面戦争の始まりとなった。',
 sides:[{name:'独立星系連合',side:'E',cmdr:'ドゥークー伯爵',flag:'—',others:'—',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},{name:'銀河共和国',side:'A',cmdr:'ヨーダ',flag:'—',others:'メイス・ウィンドゥ',before:'不明',loss:'不明（ジェダイ多数）',rate:null,deaths:'不明',dead:[]}],
 after:['共和国は軍隊を持つ国になった。','アナキンが片腕を失う。'],
 note:'年はWookieepedia（英語版ファンWiki）の正史年表に拠る。兵力・損害の数値は確認できず「不明」とした。'};
"""
