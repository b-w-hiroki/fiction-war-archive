import sys
UC=799.04
ARC='神々の黄昏'
OUT='vermilion.html'
TITLE='バーミリオン会戦 3D俯瞰'
HEAD='バーミリオン'
ERA='宇宙暦799年／帝国暦490年'
NOTE='交戦中／健在の部隊数。帝国18,860隻（後にミュラー8,080隻）、同盟16,420隻。展開は原作小説にもとづく概略'
ENV=r'''
const STAR=new THREE.Vector3(-90,30,160);
const sunM=new THREE.Mesh(new THREE.SphereGeometry(26,48,32),new THREE.MeshBasicMaterial({color:0xff5a3c}));sunM.position.copy(STAR);scene.add(sunM);
[[160,0xff4a28,.7],[280,0xc8301c,.35]].forEach(([s,c,o])=>{const g=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex,color:c,transparent:true,opacity:o,blending:THREE.AdditiveBlending,depthWrite:false}));g.scale.set(s,s,1);g.position.copy(STAR);scene.add(g)});
const pl=new THREE.PointLight(0xffa080,1.2,0);pl.position.copy(STAR);scene.add(pl);
scene.add(new THREE.AmbientLight(0x4a5a78,.6));
const fill=new THREE.DirectionalLight(0x9fb6ff,.35);fill.position.set(60,80,-80);scene.add(fill);
// 曳航される隕石
const AN=70,ast=new THREE.InstancedMesh(new THREE.DodecahedronGeometry(1,0),new THREE.MeshLambertMaterial({color:0x8d7b68}),AN);ast.frustumCulled=false;ast.visible=false;scene.add(ast);
const AO=[];for(let i=0;i<AN;i++)AO.push({o:[(hs(i,21)-.5)*22,(hs(22,i)-.5)*10,(hs(i,23)-.5)*18],s:.7+hs(i,24)*1.8,d:hs(i,25)*1.2,hit:false});


const SPECIAL={asteroidWave:false,finalBarrage:false,reset(){AO.forEach(a=>a.hit=false);this.asteroidWave=false;this.finalBarrage=false},update(now,dt){
// 隕石
 const mu=units.find(u=>u.name==='マリノ囮艦隊');
 ast.visible=(phase===2||phase===3)&&mu.mat.opacity>.05;
 if(ast.visible){for(let i=0;i<AN;i++){const a=AO[i];let X=mu.x+a.o[0],Y=mu.y+a.o[1],Z=mu.z+a.o[2]+6,sc=a.s*Math.min(1,mu.mat.opacity*1.2);
   if(phase===3){const t=Math.max(0,Math.min(1,(now-phaseStart-1-a.d)/2.6)),tx=25+a.o[0]*.3,ty=a.o[1]*.3,tz=-33+a.o[2]*.3;
    X+=(tx-X)*t;Y+=(ty-Y)*t;Z+=(tz-Z)*t;if(t>=1){sc=0;if(!a.hit){a.hit=true;boom([tx,ty,tz],true,0xffa060)}}}
   dummy.position.set(X,Y,Z);dummy.rotation.set(now*.3+i,now*.2+i*2,0);dummy.scale.set(sc,sc,sc);dummy.updateMatrix();ast.setMatrixAt(i,dummy.matrix)}
  dummy.scale.set(1,1,1);ast.instanceMatrix.needsUpdate=true}
 

}};
'''
DATA=r'''/* ---------- 部隊データ（位置は演出上の概略） ---------- */
const U=[
 {name:'ブリュンヒルト本営',cmd:'ラインハルト',side:'E',n:40,k:{0:{p:[0,0,-62],s:'ready'},3:{l:'孤立'},5:{l:'射程内に'},6:{s:'wait',l:'停戦'}}},
 {name:'縦深陣・前衛',cmd:'直属部隊',side:'E',n:60,k:{0:{p:[0,0,-28],s:'ready',l:'24段の防御陣',f:'line'},1:{s:'fight',l:''},2:{s:'broken',l:'突破される'}}},
 {name:'縦深陣・中衛',cmd:'直属部隊',side:'E',n:60,k:{0:{p:[0,0,-38],s:'ready',f:'line'},1:{s:'fight'},2:{p:[26,3,-30],s:'charge',l:'囮へ攻撃'},3:{p:[28,2,-28],s:'broken',l:'包囲される'},6:{s:'wait',l:''}}},
 {name:'縦深陣・後衛',cmd:'直属部隊',side:'E',n:60,k:{0:{p:[0,0,-48],s:'ready',f:'line'},2:{p:[20,-3,-42],s:'charge',l:'囮へ攻撃'},3:{p:[22,-2,-38],s:'broken',l:'包囲される'},6:{s:'wait',l:''}}},
 {name:'ミュラー艦隊',cmd:'ミュラー',side:'E',n:55,k:{0:{p:[-110,12,-120],s:'hidden'},4:{p:[-4,2,-52],s:'fight',l:'救援到着',f:'convex',h:0},5:{p:[-2,1,-50],l:'防戦'},6:{s:'wait',l:''}}},
 {name:'ヤン本隊',cmd:'ヤン',side:'A',n:70,k:{0:{p:[0,0,22],s:'ready'},1:{p:[0,0,-12],s:'fight',l:'陣を一段ずつ突破'},2:{p:[0,0,-14],l:''},3:{p:[8,0,-20],l:'右へ90度回頭',f:'concave',h:90},4:{l:''},5:{p:[0,0,-40],s:'charge',l:'ブリュンヒルトへ',b:1,f:'wedge'},6:{p:[0,0,-30],s:'wait',l:'停戦受諾'}}},
 {name:'アッテンボロー分艦隊',cmd:'アッテンボロー',side:'A',n:40,k:{0:{p:[-16,4,26],s:'ready'},1:{p:[-12,3,-8],s:'fight'},3:{p:[14,8,-14],l:'包囲に加わる'},4:{l:''},5:{p:[-10,4,-38],s:'charge'},6:{s:'wait'}}},
 {name:'フィッシャー分艦隊',cmd:'フィッシャー',side:'A',n:40,k:{0:{p:[16,-4,26],s:'ready'},1:{p:[12,-3,-6],s:'fight'},3:{p:[36,-2,-14],l:'包囲に加わる'},4:{l:''},5:{p:[10,-4,-36],s:'charge'},6:{s:'wait'}}},
 {name:'マリノ囮艦隊',cmd:'マリノ　2,000隻',side:'A',n:22,k:{0:{p:[70,10,-50],s:'hidden'},2:{p:[44,6,-34],s:'charge',l:'隕石で1万隻に偽装',nf:1},3:{p:[42,4,-34],s:'fight',l:'隕石を撃ち込む'},4:{l:''},6:{s:'wait'}}}
];
const PH=[
 {time:'4月24日',clock:'開戦前',step:'布陣',title:'囮となった本陣',text:'ラインハルトは麾下の艦隊を同盟領各地へ分散させ、手薄な本陣を餌にヤンを誘い出した。直属部隊は艦艇18,860隻、ヤン艦隊は16,420隻。ラインハルトは24段に重ねた縦深の防御陣で待ち受ける。',cam:{t:[0,0,-20],r:150,th:.7,ph:1.1},arrows:[]},
 {time:'4月24日〜',clock:'序盤',step:'突破',title:'縦深陣を削る',text:'ヤンは艦隊を小集団に分けて攻勢をかけ、防御陣を一段ずつ突き破っていく。だが一段破るたびに次の段が現れ、本営には届かない。',cam:{t:[0,0,-20],r:115,th:-.6,ph:1.05},arrows:[{p:[[0,0,22],[0,0,4],[0,0,-14]],c:'A'}]},
 {time:'4月末',clock:'中盤',step:'偽装',title:'1万隻に見えた囮',text:'帝国軍の側面に大兵力の攻勢部隊が現れる。オーベルシュタインに促されたラインハルトは、これを敵の主力と見て防御陣を解き、攻撃を命じた。実体はマリノの2,000隻が隕石を曳いて1万隻規模に見せかけた偽装艦隊だった。',cam:{t:[24,3,-34],r:125,th:.9,ph:1.0},arrows:[{p:[[70,10,-50],[56,8,-42],[44,6,-34]],c:'A'},{p:[[0,0,-38],[14,2,-34],[26,3,-30]],c:'E'}]},
 {time:'4月末',clock:'中盤',step:'包囲',title:'旗艦からの分断',text:'読み通りの動きに、ヤンは本隊を右へ90度転じて凹形の陣に組み直す。囮艦隊が隕石を撃ち込み、本隊と挟んで帝国の分艦隊を包囲。分艦隊は旗艦ブリュンヒルトから切り離された。',cam:{t:[22,2,-28],r:115,th:1.3,ph:.95},arrows:[{p:[[0,0,-14],[5,0,-17],[8,0,-20]],c:'A'},{p:[[42,4,-34],[34,3,-31],[28,2,-29]],c:'A'}]},
 {time:'5月2日',clock:'終盤',step:'救援',title:'ミュラー到着',text:'同盟軍が砲撃に移る寸前、ミュラー艦隊8,080隻が戦場に駆けつけ、ブリュンヒルトの盾となる。強行軍の末の到着で、艦列は大きく減っていた。',cam:{t:[-20,4,-60],r:140,th:-.9,ph:1.0},arrows:[{p:[[-110,12,-120],[-40,8,-80],[-4,2,-52]],c:'E'}]},
 {time:'5月5日',clock:'最終局面',step:'目前',title:'ブリュンヒルト、射程に',text:'幾度も戦況が入れ替わる激戦の末、ヤン艦隊はミュラーの防衛線を押し破り、ブリュンヒルトを撃沈する寸前まで迫った。',cam:{t:[0,0,-48],r:100,th:-.35,ph:1.15},arrows:[{p:[[8,0,-20],[3,0,-32],[0,0,-40]],c:'A'}]},
 {time:'5月5日 22:40',clock:'終結',step:'停戦',title:'停戦命令',text:'ヒルダの進言でミッターマイヤーとロイエンタールが首都ハイネセンへ進攻し、同盟政府は無条件停戦を受諾した。命令は22時40分にヤンへ届き、ヤンはこれに従う。戦術的優位のまま、会戦は終わった。',cam:{t:[0,0,-35],r:150,th:.4,ph:1.05},arrows:[]}
];


const RESULT={title:'バーミリオン会戦の戦果',winner:'',outcome:'戦術的にはヤン優勢、政治的には帝国の勝利',when:'宇宙暦799年／帝国暦490年 4月24日〜5月5日、バーミリオン星域（ラグナロック作戦の最終決戦）',
 summary:'ヤンはラインハルトの旗艦を射程に収めるところまで追い詰めたが、首都を押さえられた同盟政府の停戦命令に従った。戦場での優勢は、政治の決着で覆された。',
 prev:'ランテマリオ会戦の敗北と、ヤンの遊撃戦による帝国軍の各個撃破',next:'バーラトの和約と同盟の帝国への従属、ヤンの退役',
 factors:['ヤンは隕石を曳いた囮で敵の判断を誤らせ、縦深陣を崩して分艦隊を旗艦から切り離した。','ミュラーの強行軍による救援が、ブリュンヒルトを最後の一線で守った。','ヒルダの進言で帝国の別働隊がハイネセンへ向かい、同盟政府に停戦を受け入れさせた。','ヤンは文民統制に従うことを選び、戦場での勝ちを手放した。'],
 sides:[{name:'帝国軍',side:'E',cmdr:'ラインハルト',flag:'ブリュンヒルト',others:'ミュラー（救援）、オーベルシュタイン（総参謀長）',before:'18,860隻（のちミュラー8,080隻が合流、計26,940隻）',loss:'不明（直属部隊の大半が損傷）',rate:null,deaths:'不明',dead:[]},
        {name:'同盟軍',side:'A',cmdr:'ヤン・ウェンリー',flag:'ヒューベリオン',others:'アッテンボロー、フィッシャー、マリノ、メルカッツ',before:'16,420隻（将兵190万7,600名）',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['同盟はバーラトの和約を結び、帝国の保護国に近い立場となる。','ヤンは退役して年金生活に入るが、メルカッツに艦隊の一部を預けて姿を隠させた。','ラインハルトは戴冠して皇帝となり、ローエングラム王朝を開く。','ラインハルトはヤンに帝国軍への参加を勧めたが、ヤンは断った。'],
 note:'兵力は原作小説の記述にもとづく。損害の数値は確認できた資料になかったため「不明」とした。'};
'''
