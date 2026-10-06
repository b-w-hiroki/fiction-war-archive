from common import *
UC=305.01
ARC='ドラマ独自'
OUT='longnight.html'
TITLE='長い夜（ウィンターフェル） 3D俯瞰'
HEAD='長い夜'
ERA='AC305年'
SE='死者の軍'; SA='生者の連合'; PALE='serpent'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0xd8dee4','0xeef2f6',amp=3,seed=8,sky='0x30343c')+specials(labels([('ウィンターフェル', '', 'A', (0, 24, 30), 3)]))
DATA=r"""
const U=[
{name:'死者の軍',cmd:'夜の王',side:'E',n:50,k:{0:{p:[0,7,-40],s:'hidden'},1:{p:[0,7,-16],s:'charge',l:'闇から押し寄せる'},2:{p:[0,7,10],s:'fight'},3:{p:[0,7,22],s:'fight',l:'城内へ'},4:{s:'gone'}}},
 {name:'ドスラク騎兵',cmd:'—',side:'A',n:14,k:{0:{p:[0,7,4],s:'ready'},1:{p:[0,7,-12],s:'broken',l:'火が消える'},2:{s:'gone'},3:{s:'gone'},4:{s:'gone'}}},
 {name:'穢れなき軍団・守備隊',cmd:'グレイ・ワーム',side:'A',n:20,k:{0:{p:[0,7,14],s:'ready',f:'line'},1:{p:[0,7,14],s:'fight'},2:{p:[0,7,22],s:'withdraw',l:'城内へ後退'},3:{p:[0,7,28],s:'fight'},4:{p:[0,7,28],s:'ready'}}},
 {name:'アリア',cmd:'アリア・スターク',side:'A',n:2,k:{0:{s:'hidden',p:[10,7,30]},1:{s:'hidden',p:[10,7,30]},2:{s:'hidden',p:[10,7,30]},3:{s:'hidden',p:[10,7,30]},4:{p:[6,7,32],s:'charge',l:'夜の王を倒す'}}}
];
const PH=[
{time:'AC305年（推定）',clock:'S8E3',step:'布陣',title:'布陣',text:'生者の連合が死者の軍を迎えるため、ウィンターフェルに集まった。',cam:{fit:1,th:0.5,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'突撃',title:'ドスラクの突撃',text:'炎の剣のドスラク騎兵が闇に突っ込み、火は消えた。',cam:{fit:1,th:0.4,ph:0.9},arrows:[{p:[[0,7,4],[0,7,-12]],c:'A'}]},
 {time:'',clock:'',step:'後退',title:'城への後退',text:'守備隊は押されて城内へ後退した。',cam:{fit:1,th:0.7,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'城内',title:'城内の戦い',text:'死者が城壁を越え、城内で戦いが続いた。',cam:{fit:1,th:0.4,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'決着',title:'夜の王の最期',text:'アリアが夜の王を倒し、死者の軍は消えた。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'長い夜の結果',when:'ドラマS8、ウィンターフェル',prev:'落とし子の戦い',next:'王都の戦い',factors:['死者の軍が兵数で圧倒した。','ドラゴンと火が時間を稼いだ。','アリアが夜の王を倒した。'],winner:'A',outcome:'生者の連合の勝利',summary:'ドラマ独自の結末。死者の脅威が終わる。',sides:[{name:'死者の軍',side:'E',cmdr:'夜の王',flag:'—',others:'—',before:'不明',loss:'全滅',rate:null,deaths:'—',dead:[]},{name:'生者の連合',side:'A',cmdr:'ジョン・スノウ、デナーリス',flag:'—',others:'—',before:'不明',loss:'不明（多数）',rate:null,deaths:'不明',dead:['ジョラー・モーモント','シオン・グレイジョイ']}],after:['戦いの焦点は王都に移る。'],note:'ドラマS8E3「長い夜」による。AC年はドラマで明示されず、305年は推定。'};
"""
