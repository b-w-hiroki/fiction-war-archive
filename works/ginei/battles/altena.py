from common import env
UC=797.04;ARC='内乱'
OUT='altena.html'
TITLE='アルテナ会戦 3D俯瞰';HEAD='アルテナ';ERA='宇宙暦797年／帝国暦488年'
NOTE='リップシュタット戦役の初戦。ミッターマイヤー14,500隻、シュターデン16,000隻'
SE='ローエングラム陣営';SA='貴族連合軍';PAL='noble'
EXTRA=r"""
(function(){const n=1800,p=new Float32Array(n*3),c=new Float32Array(n*3);for(let i=0;i<n;i++){p.set([(hs(i,41)-.5)*70,(hs(42,i)-.5)*24,-6+(hs(i,43)-.5)*10],i*3);const b=.4+hs(i,44)*.4;c.set([b,b*.7,b*.3],i*3)}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));g.setAttribute('color',new THREE.BufferAttribute(c,3));
 scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:.7,vertexColors:true,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false})))})();
"""
SP="const SPECIAL={lab:null,reset(){if(!this.lab){this.lab=sprite('機雷原','ミッターマイヤーが敷設',CSS.E,2.4);this.lab.position.set(0,14,-6);scene.add(this.lab)}},update(){}};"
ENV=env(color='0xfff0d8',glow='0xffc070',pos=(-150,40,-150),extra=EXTRA,special=SP)
DATA=r"""
const U=[
 {name:'ミッターマイヤー艦隊',cmd:'ミッターマイヤー',side:'E',n:60,k:{0:{p:[0,0,-34],s:'wait',l:'機雷原の奥で動かず',f:'line'},2:{p:[-46,0,-14],s:'move',l:'機雷原を迂回',f:'column'},3:{p:[-30,0,30],s:'charge',l:'敵の背後へ',f:'wedge',h:90},4:{p:[-10,0,32],s:'fight',l:''},5:{s:'wait'}}},
 {name:'シュターデン本隊',cmd:'シュターデン',side:'A',n:55,k:{0:{p:[0,0,34],s:'ready',f:'line',h:180},1:{l:'動かない敵に苛立つ'},2:{p:[6,0,22],s:'move',l:'機雷原の前で止まる'},3:{s:'fight',l:'背後を突かれる'},4:{s:'broken',l:'崩れる'},5:{p:[10,0,80],s:'withdraw',l:'敗走'}}},
 {name:'ヒルデスハイム隊',cmd:'ヒルデスハイム伯',side:'A',n:40,k:{0:{p:[26,0,40],s:'ready',f:'line',h:180},1:{p:[24,0,26],l:'出撃を迫る'},2:{p:[24,0,12],s:'charge',l:'功を焦って前進'},3:{p:[16,0,20],s:'fight'},4:{s:'broken',l:'伯爵戦死'},5:{s:'gone'}}}
];
const PH=[
 {time:'4月19日',clock:'',step:'対峙',title:'最初の衝突',text:'リップシュタット戦役の最初の艦隊戦。貴族連合軍のシュターデン艦隊16,000隻に、ミッターマイヤー艦隊14,500隻が向かい合う。',cam:{fit:1,th:.5,ph:.95},arrows:[]},
 {time:'4月',clock:'',step:'静止',title:'動かない艦隊',text:'ミッターマイヤーは前面に機雷原を敷き、その奥でじっと動かなかった。功を焦る貴族たちは、攻めてこない敵に苛立ちを募らせる。',cam:{fit:1,th:.0,ph:.6},arrows:[]},
 {time:'4月',clock:'',step:'迂回',title:'機雷原の陰で',text:'貴族連合軍が機雷原の前で足を止めている間に、ミッターマイヤーは艦隊を動かし、機雷原を大きく回り込んだ。',cam:{fit:1,th:-.8,ph:.9},arrows:[{p:[[0,0,-34],[-40,0,-30],[-46,0,-14]],c:'E'}]},
 {time:'4月',clock:'',step:'背後',title:'疾風の一撃',text:'「疾風ウォルフ」の艦隊が貴族連合軍の背後に躍り出る。正面の機雷原と背後の敵に挟まれ、連合軍は混乱に陥った。',cam:{fit:1,th:-1.2,ph:1.0},arrows:[{p:[[-46,0,-14],[-44,0,10],[-30,0,30]],c:'E'}]},
 {time:'4月',clock:'',step:'崩壊',title:'ヒルデスハイムの最期',text:'ヒルデスハイム伯は戦死し、連合軍は総崩れとなる。貴族の中から初めての戦死者が出た。',cam:{fit:1,th:-.4,ph:1.0},arrows:[]},
 {time:'戦後',clock:'',step:'敗走',title:'シュターデンの敗走',text:'シュターデンは残存艦を率いて敗走した。連合軍の兵力の大半はなお健在だったが、初戦の敗北は貴族たちを動揺させた。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[6,0,22],[8,0,50],[10,0,80]],c:'A'}]}
];
const RESULT={title:'アルテナ会戦の結果',winner:'E',outcome:'ローエングラム陣営の勝利',when:'宇宙暦797年／帝国暦488年 4月19日〜、アルテナ星域',
 summary:'機雷原で敵を足止めし、その間に迂回して背後を突いたミッターマイヤーが、数で勝るシュターデン艦隊を破った。',
 prev:'リップシュタット貴族連合の結成と戦役の勃発',next:'レンテンベルク要塞攻略戦',
 factors:['機雷原で敵の前進を止め、自軍の機動の自由を確保した。','動かないことで功名心の強い貴族たちの焦りを誘った。','迂回による背後からの攻撃で、数の不利を打ち消した。'],
 sides:[{name:'ローエングラム陣営',side:'E',cmdr:'ミッターマイヤー大将',flag:'ベイオウルフ',others:'—',before:'14,500隻',loss:'不明（軽微）',rate:null,deaths:'不明',dead:[]},
        {name:'貴族連合軍',side:'A',cmdr:'シュターデン大将',flag:'不明',others:'ヒルデスハイム伯 ほか',before:'16,000隻',loss:'参加艦艇の多く',rate:null,deaths:'不明',dead:['ヒルデスハイム伯']}],
 after:['貴族連合軍は初めての戦死者を出したが、兵力2,560万人の大半はなお健在だった。','連合軍は要塞の守りを固め、ラインハルト本隊はレンテンベルクへ向かう。','ミッターマイヤーの名声がさらに高まる。'],
 note:'機雷原の規模、損害の数値は確認できた資料になかった。'};
"""
