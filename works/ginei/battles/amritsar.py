import sys
UC=796.1
ARC='黎明'
OUT='amritsar.html'
TITLE='アムリッツァ会戦 3D俯瞰'
HEAD='アムリッツァ'
ERA='宇宙暦796年／帝国暦487年'
NOTE='交戦中／健在の艦隊数。艦艇は抽象表現、展開は原作小説にもとづく概略'
ENV=r'''// 恒星アムリッツァ
const STAR=new THREE.Vector3(20,-14,125);
const sunM=new THREE.Mesh(new THREE.SphereGeometry(24,48,32),new THREE.MeshBasicMaterial({color:0xffb35c}));sunM.position.copy(STAR);scene.add(sunM);
[[150,0xff8a30,.75],[260,0xff6a20,.35]].forEach(([s,c,o])=>{const g=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex,color:c,transparent:true,opacity:o,blending:THREE.AdditiveBlending,depthWrite:false}));g.scale.set(s,s,1);g.position.copy(STAR);scene.add(g)});
const pl=new THREE.PointLight(0xffc690,1.25,0);pl.position.copy(STAR);scene.add(pl);
scene.add(new THREE.AmbientLight(0x4a5a78,.55));
const fill=new THREE.DirectionalLight(0x9fb6ff,.35);fill.position.set(-60,80,-80);scene.add(fill);

// 機雷原
const MN=5200,mPos=new Float32Array(MN*3),mCol=new Float32Array(MN*3),mBase=new Float32Array(MN*3),mInfo=[];
for(let i=0;i<MN;i++){const x=(hs(i,3)-.5)*130,y=(hs(4,i)-.5)*80,z=27+(x*x+y*y)/900+hs(i,8)*7;mPos.set([x,y,z],i*3);
 const b=.25+hs(i,6)*.35;mBase.set([b*1.0,b*.55,b*.5],i*3);mInfo.push({c:Math.hypot(x-2,y-6)<10,z})}
mCol.set(mBase);
const mGeo=new THREE.BufferGeometry();mGeo.setAttribute('position',new THREE.BufferAttribute(mPos,3));mGeo.setAttribute('color',new THREE.BufferAttribute(mCol,3));
scene.add(new THREE.Points(mGeo,new THREE.PointsMaterial({size:.55,vertexColors:true,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false})));


const SPECIAL={update(now,dt){
// 機雷原の焼却
 const burn=phase>=4?(phase>4?9:(now-phaseStart)):-1,colA=mGeo.attributes.color;
 for(let i=0;i<MN;i++){const m=mInfo[i];if(!m.c)continue;let r=mBase[i*3],g=mBase[i*3+1],b=mBase[i*3+2];
  if(burn>=0){const t=burn-(40-m.z)*.08-.2;if(t>0){const h=Math.max(0,1-t*1.4);r=1.6*h;g=.8*h;b=.2*h;if(t<.05&&Math.random()<.004)boom([mPos[i*3],mPos[i*3+1],mPos[i*3+2]],true,0xff9a40)}}
  colA.array[i*3]=r;colA.array[i*3+1]=g;colA.array[i*3+2]=b}
 colA.needsUpdate=true;
 

}};
'''
DATA=r'''/* ---------- 艦隊データ（位置は演出上の概略） ---------- */
const U=[
 {name:'第13艦隊',cmd:'ヤン',side:'A',n:90,k:{0:{p:[-18,0,10],s:'ready'},1:{p:[-18,0,4],s:'fight',l:'先制攻撃',f:'concave'},2:{l:''},5:{p:[-46,28,2],s:'withdraw',l:'殿'}}},
 {name:'第10艦隊残存',cmd:'ヤン指揮下',side:'A',n:30,k:{0:{p:[-32,-5,15],s:'ready'},4:{s:'fight'},5:{p:[-62,30,12],s:'withdraw'}}},
 {name:'第8艦隊',cmd:'アップルトン',side:'A',n:85,k:{0:{p:[5,0,12],s:'ready'},1:{s:'fight'},2:{p:[12,-8,24],s:'broken',l:'瓦解'},4:{s:'gone'}}},
 {name:'第5艦隊',cmd:'ビュコック',side:'A',n:85,k:{0:{p:[26,0,10],s:'ready'},1:{s:'fight'},5:{p:[-26,42,14],s:'withdraw'}}},
 {name:'本隊',cmd:'ラインハルト',side:'E',n:120,k:{0:{p:[0,0,-60],s:'wait'},5:{p:[-6,6,-32],l:'追撃指揮'}}},
 {name:'ミッターマイヤー艦隊',cmd:'ミッターマイヤー',side:'E',n:80,k:{0:{p:[-20,2,-28],s:'ready'},1:{s:'fight',l:'先制を受ける'},2:{l:''},5:{p:[-30,18,-8],s:'charge',l:'追撃'}}},
 {name:'ロイエンタール艦隊',cmd:'ロイエンタール',side:'E',n:80,k:{0:{p:[24,-2,-28],s:'ready'},1:{s:'fight'},5:{p:[2,24,-4],s:'charge',l:'追撃'}}},
 {name:'黒色槍騎兵艦隊',cmd:'ビッテンフェルト',side:'E',n:95,k:{0:{p:[-3,-2,-32],s:'ready'},1:{s:'fight'},2:{p:[-7,0,6],s:'charge',l:'突出',f:'spindle'},3:{p:[-12,-6,-14],s:'broken',l:'大損害',nf:1},5:{p:[-10,-12,-44],l:'後退'}}},
 {name:'ケンプ艦隊',cmd:'ケンプ',side:'E',n:60,k:{0:{p:[-40,6,-36],s:'wait'},4:{s:'fight'}}},
 {name:'メックリンガー艦隊',cmd:'メックリンガー',side:'E',n:60,k:{0:{p:[42,6,-38],s:'wait'},4:{s:'fight'}}},
 {name:'キルヒアイス艦隊',cmd:'ワーレン・ルッツを含む',side:'E',n:110,k:{0:{p:[70,10,-50],s:'move',l:'別動隊'},1:{p:[92,14,5],l:'迂回中'},2:{p:[76,12,52]},3:{p:[20,8,54],l:'機雷原の外'},4:{p:[2,6,19],s:'charge',l:'背後から突入',dl:2.4,f:'spindle'},5:{p:[-12,10,6],s:'charge',l:''}}}
];
const PH=[
 {time:'第1幕',clock:'両軍集結',step:'布陣',title:'機雷原を背に',text:'帝国領から後退した同盟軍は、アムリッツァ恒星系に残存艦隊を集めた。後背には分厚い機雷原。帝国軍は本隊が正面から迫り、キルヒアイスが全軍の約3割を率いて別行動に出る。',cam:{t:[4,0,0],r:244,th:.75,ph:1.12},arrows:[{p:[[70,10,-50],[92,14,5],[76,12,52]],c:'E',dash:1}]},
 {time:'第2幕',clock:'戦端',step:'先制',title:'ヤンの先手',text:'戦端を開いたのはヤンの第13艦隊。ミッターマイヤー艦隊に先制の一撃を加える。その間もキルヒアイス艦隊は戦場を大きく迂回していく。',cam:{t:[-18,0,-10],r:109,th:-.65,ph:1.05},arrows:[{p:[[-18,0,4],[-19,1,-12],[-20,2,-24]],c:'A'}]},
 {time:'第3幕',clock:'中盤',step:'突出',title:'黒色槍騎兵、割り込む',text:'ビッテンフェルトの黒色槍騎兵艦隊が突出し、第13艦隊と第8艦隊の間に割り込む。速度に対応しきれなかった第8艦隊は側面を突かれ、瓦解する。',cam:{t:[-4,0,6],r:100,th:.55,ph:.95},arrows:[{p:[[-3,-2,-32],[-6,-1,-12],[-7,0,4]],c:'E'}]},
 {time:'第4幕',clock:'中盤',step:'逆撃',title:'途切れた砲火',text:'近接戦で艦載機の発進に切り替えた黒色槍騎兵艦隊は、一時的に砲撃が途切れる。ヤンはその隙に火力を集中させ、同艦隊に甚大な損害を与える。',cam:{t:[-10,-2,-5],r:86,th:-.35,ph:1.18},arrows:[{p:[[-18,0,4],[-15,-3,-5],[-12,-6,-12]],c:'A'}]},
 {time:'第5幕',clock:'終盤',step:'背後',title:'機雷原を焼き払う',text:'キルヒアイス艦隊は指向性ゼッフル粒子で機雷原に通路を焼き開き、同盟軍の背後へ突入する。正面と背後から挟まれ、同盟軍の戦線は崩れ始める。',cam:{t:[4,5,26],r:123,th:1.25,ph:1.02},arrows:[{p:[[20,8,54],[6,7,36],[2,6,21]],c:'E'}]},
 {time:'第6幕',clock:'終局',step:'撤退',title:'殿のヤン',text:'同盟軍は総退却に移る。ヤンが殿を務めて追撃を食い止め、全軍の離脱を支えた。帝国軍は大勝したが、またしても完全な勝利はヤンに阻まれた。',cam:{t:[-14,12,0],r:196,th:.35,ph:1.05},arrows:[{p:[[-18,0,4],[-34,16,4],[-46,28,2]],c:'A'},{p:[[26,0,10],[0,24,14],[-26,42,14]],c:'A'}]}
];


const RESULT={title:'アムリッツァ会戦の戦果',winner:'E',outcome:'帝国軍の大勝（同盟の帝国領侵攻作戦は破綻）',when:'宇宙暦796年／帝国暦487年10月、アムリッツァ星系',
 summary:'帝国領侵攻で消耗しきった同盟軍を、帝国軍が正面と背後から挟撃した。ヤンの殿で全滅は免れたが、同盟は侵攻兵力の大半を失った。',
 prev:'同盟の帝国領侵攻作戦と、帝国軍の焦土作戦による反攻',next:'皇帝フリードリヒ4世の崩御、そして帝国と同盟それぞれの内乱',
 factors:['同盟軍は補給が尽き、反攻ですでに2個艦隊を失った状態で決戦に臨んだ。','キルヒアイスが機雷原を焼き払って背後を取り、挟撃を完成させた。','黒色槍騎兵の突出は帝国側の誤算で、ヤンの逆撃を招いた。','ヤンとビュコックの指揮で同盟軍は秩序を保って撤退できた。'],
 sides:[{name:'帝国軍',side:'E',cmdr:'ラインハルト元帥',flag:'ブリュンヒルト',others:'キルヒアイス、ミッターマイヤー、ロイエンタール、ビッテンフェルト ほか',before:'不明（同盟軍を大きく上回る）',loss:'黒色槍騎兵艦隊の約9割、他は軽微',rate:null,deaths:'不明',dead:[]},
        {name:'同盟軍',side:'A',cmdr:'ロボス元帥（後方のイゼルローンで指揮）',flag:'ヒューベリオン（第13艦隊）',others:'ヤン、ビュコック、アップルトン',before:'不明（第5・第8・第13艦隊と第10艦隊の残存部隊）',loss:'甚大（第8艦隊は瓦解）',rate:null,deaths:'不明',dead:['アップルトン中将（OVAでは戦死、原作では生死不明）']}],
 after:['同盟は帝国領侵攻に動員した8個艦隊の大半を失い、軍事的な均衡が崩れる。','ロボス元帥とシトレ元帥が引責辞任し、ヤンはイゼルローン要塞の司令官となる。','ラインハルトは帝国軍の最高実力者の地位を固める。','敗戦への不満が、翌年の救国軍事会議のクーデターにつながっていく。'],
 note:'帝国領侵攻作戦全体の損害は大きいが、アムリッツァ単独の損害数値は確認できた資料になかったため、数値は記載していない。'};
'''
