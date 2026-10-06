from common import *
UC=299.02
ARC='五王の戦争'
OUT='whisperingwood.html'
TITLE='囁きの森の戦い 3D俯瞰'
HEAD='囁きの森'
ERA='AC299年'
SE='ラニスター軍'; SA='スターク軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x2e4a2a','0x4d6b3e',amp=3,seed=2,sky='0x7a8a90')+specials(labels([('囁きの森', 'リヴァーランド', 'A', (0, 20, 0), 3)]))
DATA=r"""
const U=[
{name:'ジェイミー軍',cmd:'ジェイミー・ラニスター',side:'E',n:20,k:{0:{p:[0,7,-10],s:'wait',f:'column',l:'リヴァーラン包囲中'},1:{p:[0,7,-4],s:'move',l:'森へ誘い出される'},2:{p:[0,7,0],s:'fight'},3:{p:[0,7,0],s:'broken',l:'ジェイミー捕縛'}}},
 {name:'ロブ本隊',cmd:'ロブ・スターク',side:'A',n:16,k:{0:{p:[0,7,30],s:'hidden'},1:{p:[0,7,24],s:'wait',l:'森に伏せる'},2:{p:[0,7,8],s:'charge'},3:{p:[0,7,4],s:'ready',l:'勝利'}}},
 {name:'ブラックフィッシュ隊',cmd:'ブリンデン・タリー',side:'A',n:8,k:{0:{p:[-26,7,16],s:'hidden'},1:{p:[-26,7,10],s:'wait',l:'囮・側面'},2:{p:[-12,7,0],s:'charge',l:'側面から突入'},3:{p:[-8,7,0],s:'ready'}}},
 {name:'両側の伏兵',cmd:'スターク諸侯',side:'A',n:8,k:{0:{p:[24,7,6],s:'hidden'},1:{p:[24,7,4],s:'wait'},2:{p:[12,7,-2],s:'charge'},3:{p:[8,7,-2],s:'ready'}}}
];
const PH=[
{time:'AC299年',clock:'原作1部／S1E9',step:'包囲',title:'リヴァーラン包囲',text:'ジェイミーはタリー家のリヴァーランを包囲していた。ロブは双子城を渡って南下し、救援に向かう。',cam:{fit:1,th:0.5,ph:0.9},arrows:[{p:[[0,7,30],[0,7,24]],c:'A'}]},
 {time:'',clock:'',step:'誘引',title:'森への誘い出し',text:'ブラックフィッシュの小部隊が襲撃と後退を繰り返し、ジェイミーを夜の森へ誘い込んだ。',cam:{fit:1,th:0.8,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'奇襲',title:'三方からの夜襲',text:'森に伏せていた北部軍が三方から襲いかかり、ラニスター軍は崩れた。',cam:{fit:1,th:0.3,ph:0.9},arrows:[{p:[[0,7,24],[0,7,8]],c:'A'}]},
 {time:'',clock:'S1E10冒頭',step:'捕縛',title:'ジェイミーの捕縛',text:'総大将ジェイミーが捕らえられた。続く野営地の戦いで包囲も解ける。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'囁きの森の戦いの結果',when:'AC299年、リヴァーラン近くの囁きの森',prev:'緑の支流の戦い',next:'野営地の戦い',factors:['ロブが本隊を囮にし、主力を森に伏せた。','ブラックフィッシュがジェイミーを誘い出した。','夜の森で三方から奇襲した。'],winner:'A',outcome:'スターク側の勝利（ジェイミー捕縛）',summary:'ロブ・スタークの名を高めた初勝利。北部はロブを「北の王」に推す。',sides:[{name:'ラニスター軍',side:'E',cmdr:'ジェイミー・ラニスター',flag:'—',others:'—',before:'不明',loss:'不明（総大将が捕虜）',rate:null,deaths:'不明',dead:[]},{name:'スターク軍',side:'A',cmdr:'ロブ・スターク',flag:'—',others:'ブリンデン・タリー',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],after:['ロブが北の王を名乗る。','ジェイミーの身柄が交渉の材料になる。'],note:'展開は小説『七王国の玉座』とドラマS1にもとづく。ドラマでは戦闘自体は描かれず、S1E9の後に結果が語られる。兵力は記憶では示せないため不明とした。年はA Wiki of Ice and Fire の「War of the Five Kings」（298〜300AC）による推定。'};
"""
