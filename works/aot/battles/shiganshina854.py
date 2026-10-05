from common import *
UC=854.06
ARC='地鳴らし'
OUT='shiganshina854.html'
TITLE='シガンシナ区の戦い（854年） 3D俯瞰'
HEAD='シガンシナ854'
ERA='854年'
SE='マーレ軍'; SA='エレン派・兵団'; PALE='marley'; PAL='scout'
NOTE='交戦中／健在の部隊。配置は原作漫画にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x7a7466','0xa49c88',amp=2,seed=19,sky='0x8a96a4')+wall(70,16,0,70)+specials(labels([('シガンシナ区', '', 'A', (0, 22, 0), 3)]))
DATA=r"""
const U=[
{name:'マーレ軍',cmd:'マガト元帥',side:'E',n:50,k:{0:{p:[0,7,-50],s:'move',l:'飛行船で侵攻'},1:{p:[0,7,-10],s:'fight',l:'顎・車力・鎧'},2:{p:[0,7,-6],s:'fight',b:1},3:{p:[0,7,-30],s:'broken',l:'ポルコ戦死'}}},
 {name:'エレン派・兵団',cmd:'イェーガー派',side:'A',n:40,k:{0:{p:[0,7,20],s:'ready'},1:{p:[0,7,10],s:'fight'},2:{p:[0,7,4],s:'fight'},3:{p:[0,7,4],s:'ready'}}},
 {name:'エレン',cmd:'エレン・イェーガー',side:'A',n:3,k:{0:{p:[4,7,6],s:'ready'},1:{p:[4,7,6],s:'fight'},2:{p:[2,7,-4],s:'broken',l:'首を飛ばされる'},3:{p:[0,7,0],s:'ready',l:'始祖と接触。地鳴らしが始まる'}}}
];
const PH=[
{time:'854年',clock:'Final Part2',step:'侵攻',title:'マーレの反撃',text:'レベリオ襲撃への報復として、マーレ軍が飛行船と巨人でシガンシナ区に攻め込んだ。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,7,-50],[0,7,-10]],c:'E'}]},
 {time:'',clock:'',step:'混戦',title:'三つ巴の混戦',text:'エレン派、兵団、マーレの巨人が入り乱れて戦う。',cam:{fit:1,th:.8,ph:.9},arrows:[]},
 {time:'',clock:'',step:'接触',title:'ジークとの接触',text:'エレンはガビの銃撃で首を飛ばされたが、ジークと接触して「道」に入った。',cam:{fit:1,th:.3,ph:.9},arrows:[]},
 {time:'',clock:'',step:'地鳴らし',title:'地鳴らしの始まり',text:'エレンは始祖の力を握り、壁の中の無数の超大型巨人を目覚めさせた。地鳴らしが始まる。',cam:{fit:1,th:.5,ph:1.0},arrows:[]}
];
const RESULT={title:'シガンシナ区の戦い（854年）の結果',when:'854年、シガンシナ区',prev:'レベリオ収容区襲撃',next:'地鳴らし・天と地の戦い',
 factors:['エレンがジークと接触し、始祖の力を使える状態になった。','パラディ側が割れており、統一した防衛ができなかった。'],winner:'none',outcome:'決着前に地鳴らしが始まる',
 summary:'マーレのパラディ島侵攻は、エレンが始祖の力を握ったことで意味を失った。壁の巨人が目覚め、世界を踏み潰す地鳴らしが始まる。',
 sides:[{name:'マーレ軍',side:'E',cmdr:'テオ・マガト元帥',flag:'—',others:'ライナー、ポルコ、ピーク',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:['ポルコ・ガリアード','ジーク・イェーガー（のちに）']},
        {name:'エレン派・兵団',side:'A',cmdr:'エレン・イェーガー',flag:'—',others:'イェーガー派、兵団',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['壁の中の超大型巨人が一斉に動き出す。','兵団の一部はマーレの戦士と手を組み、エレンを止める側に回る。'],
 note:'展開は原作とアニメFinal Season Part2にもとづく。話数は確認できなかった。'};
"""
