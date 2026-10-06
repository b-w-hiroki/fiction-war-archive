from common import *
UC=299.09
ARC='五王の戦争'
OUT='redwedding.html'
TITLE='紅き婚礼（双子城） 3D俯瞰'
HEAD='紅き婚礼'
ERA='AC299年'
SE='フレイ家・ボルトン家'; SA='スターク軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は原作・ドラマにもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x4a5a44','0x6a7a5a',water='0x30485a',amp=3,seed=4,sky='0x5a6070')+specials(labels([('双子城', '緑の支流の渡し', 'E', (0, 24, -10), 3)]))
DATA=r"""
const U=[
{name:'フレイ兵',cmd:'ウォルダー・フレイ',side:'E',n:14,k:{0:{p:[0,7,-14],s:'ready'},1:{p:[0,7,-10],s:'ready',l:'宴を開く'},2:{p:[0,7,-4],s:'charge',nf:1},3:{p:[0,7,0],s:'fight'}}},
 {name:'ボルトン兵',cmd:'ルース・ボルトン',side:'E',n:10,k:{0:{p:[16,7,-8],s:'ready'},1:{p:[16,7,-6],s:'ready'},2:{p:[10,7,-2],s:'charge',l:'裏切り'},3:{p:[8,7,2],s:'fight'}}},
 {name:'ロブ一行',cmd:'ロブ・スターク',side:'A',n:6,k:{0:{p:[0,7,20],s:'move'},1:{p:[0,7,-2],s:'ready',l:'婚礼に出席'},2:{p:[0,7,0],s:'broken',l:'ロブ死亡'},3:{s:'gone'}}},
 {name:'北部軍野営地',cmd:'スターク諸侯',side:'A',n:14,k:{0:{p:[-20,7,24],s:'ready'},1:{p:[-20,7,20],s:'wait'},2:{p:[-20,7,18],s:'fight',l:'野営地も襲撃'},3:{p:[-20,7,24],s:'broken'}}}
];
const PH=[
{time:'AC299年',clock:'原作3部／S3E9',step:'到着',title:'双子城へ',text:'ロブは約束を破った婚姻の償いに、叔父とフレイ家の娘の婚礼に出向いた。',cam:{fit:1,th:0.5,ph:0.9},arrows:[{p:[[0,7,20],[0,7,-2]],c:'A'}]},
 {time:'',clock:'',step:'宴',title:'宴の席',text:'客人の権利を約束されて宴が開かれた。',cam:{fit:1,th:0.8,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'裏切り',title:'裏切り',text:'フレイ家とボルトン家が宴の場でロブ一行を襲い、外の北部軍も攻撃された。',cam:{fit:1,th:0.3,ph:0.9},arrows:[]},
 {time:'',clock:'',step:'終幕',title:'北部の王の終わり',text:'ロブと母キャトリンが殺され、北部の王国は崩れた。',cam:{fit:1,th:0.5,ph:1.0},arrows:[]}
];
const RESULT={title:'紅き婚礼の結果',when:'AC299年、双子城',prev:'ブラックウォーターの戦い',next:'黒の城の戦い',factors:['フレイ家がロブの婚約破棄を恨んでいた。','ボルトン家がタイウィンと通じていた。','客人の権利を破る不意打ちだった。'],winner:'E',outcome:'フレイ・ボルトン側の勝利（ロブ死亡）',summary:'戦場ではなく宴で決着した虐殺。五王の戦争でスターク家が敗れる。',sides:[{name:'フレイ家・ボルトン家',side:'E',cmdr:'ウォルダー・フレイ',flag:'—',others:'ルース・ボルトン',before:'不明',loss:'—',rate:null,deaths:'—',dead:[]},{name:'スターク軍',side:'A',cmdr:'ロブ・スターク',flag:'—',others:'—',before:'不明',loss:'不明（多数）',rate:null,deaths:'不明',dead:['ロブ・スターク','キャトリン・スターク']}],after:['ボルトン家が北部総督になる。','フレイ家はリヴァーランの領主となる。'],note:'展開は小説『剣嵐の大地』とドラマS3E9「キャスタミアの雨」による。数は確認できなかった。'};
"""
