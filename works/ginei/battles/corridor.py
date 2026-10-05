from common import env
SA='ヤン艦隊'
UC=800.05
ARC='新帝国'
PAL='iser'
OUT='corridor.html'
TITLE='回廊の戦い 3D俯瞰'
HEAD='回廊の戦い'
ERA='宇宙暦800年／新帝国暦2年'
NOTE='交戦中／健在の部隊数。帝国軍19万隻超、ヤン艦隊約2万9千隻。展開は原作小説にもとづく概略'
EXTRA=r"""
(function(){const n=3200,p=new Float32Array(n*3),c=new Float32Array(n*3);for(let i=0;i<n;i++){const sd=i%2?1:-1,x=sd*(42+hs(i,31)*34),y=(hs(32,i)-.5)*80,z=(hs(i,33)-.5)*300;p.set([x,y,z],i*3);const b=.25+hs(i,34)*.35;c.set([b,b*.35,b*.3],i*3)}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));g.setAttribute('color',new THREE.BufferAttribute(c,3));
 scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:1.1,vertexColors:true,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false})))})();
const ISER=new THREE.Mesh(new THREE.SphereGeometry(11,48,32),new THREE.MeshLambertMaterial({color:0xcfd6df,emissive:0x1a2430}));ISER.position.set(0,0,95);scene.add(ISER);
"""
SPECIAL=r"""
const SPECIAL={lab:null,reset(){if(!this.lab){this.lab=sprite('イゼルローン要塞','ヤン艦隊の拠点',CSS.A,3);this.lab.position.set(0,13,95);scene.add(this.lab);
 const w=sprite('航行不能宙域','回廊の壁',CSS.E,2.4);w.position.set(-52,10,-10);w.material.opacity=.7;scene.add(w);const w2=sprite('航行不能宙域','回廊の壁',CSS.E,2.4);w2.position.set(52,10,-10);w2.material.opacity=.7;scene.add(w2)}},update(){}};
"""
ENV=env(color='0xfff0d8',glow='0xffd8a0',pos=(180,70,260),extra=EXTRA,special=SPECIAL)
DATA=r"""
const U=[
 {name:'ヤン艦隊本隊',cmd:'ヤン',side:'A',n:70,k:{0:{p:[0,0,42],s:'ready',l:'回廊の狭所に布陣',f:'concave',h:180},1:{s:'fight',l:''},3:{l:'フィッシャー戦死、艦隊運用が乱れる'},4:{l:''},5:{s:'wait',l:'会談を受諾'}}},
 {name:'メルカッツ分艦隊',cmd:'メルカッツ',side:'A',n:35,k:{0:{p:[-24,4,50],s:'ready',f:'line',h:180},1:{s:'fight'},3:{p:[-22,4,40]},5:{s:'wait'}}},
 {name:'アッテンボロー分艦隊',cmd:'アッテンボロー',side:'A',n:35,k:{0:{p:[24,-4,50],s:'ready',f:'line',h:180},1:{s:'fight'},3:{p:[22,-4,40]},5:{s:'wait'}}},
 {name:'黒色槍騎兵艦隊',cmd:'ビッテンフェルト',side:'E',n:55,k:{0:{p:[-8,0,-40],s:'ready'},1:{p:[-6,0,20],s:'charge',l:'正面から突入'},2:{p:[-22,0,-60],s:'withdraw',l:'大損害で後退'},5:{s:'wait',l:''}}},
 {name:'ファーレンハイト艦隊',cmd:'ファーレンハイト',side:'E',n:55,k:{0:{p:[12,0,-46],s:'ready'},1:{p:[10,0,14],s:'charge',l:'突入を支援'},2:{p:[8,0,10],s:'broken',l:'ファーレンハイト戦死'},3:{s:'gone'}}},
 {name:'皇帝本隊',cmd:'ラインハルト',side:'E',n:110,k:{0:{p:[0,0,-120],s:'wait',l:'13万隻'},2:{p:[0,0,-24],s:'fight',l:'波状攻撃で押す',f:'line'},4:{p:[0,0,-40],s:'wait',l:'皇帝が発熱'},5:{l:'講和を申し入れる'}}},
 {name:'シュタインメッツ艦隊',cmd:'シュタインメッツ',side:'E',n:45,k:{0:{p:[-18,0,-95],s:'wait'},2:{p:[-14,0,6],s:'fight',l:''},3:{s:'broken',l:'シュタインメッツ戦死'},4:{s:'gone'}}},
 {name:'ミッターマイヤー艦隊',cmd:'ミッターマイヤー',side:'E',n:55,k:{0:{p:[18,0,-100],s:'wait'},3:{p:[18,0,12],s:'charge',l:'双璧の攻勢',f:'wedge'},4:{s:'fight',l:''},5:{p:[20,0,-10],s:'wait',l:''}}},
 {name:'ロイエンタール艦隊',cmd:'ロイエンタール',side:'E',n:55,k:{0:{p:[0,8,-106],s:'wait'},3:{p:[-4,8,8],s:'charge',l:'双璧の攻勢',f:'wedge'},4:{s:'fight',l:''},5:{p:[-6,8,-12],s:'wait',l:''}}}
];
const PH=[
 {time:'4月29日',clock:'開戦前',step:'布陣',title:'回廊の出口を塞ぐ',text:'同盟滅亡後、ヤンはエル・ファシル独立政府の軍としてイゼルローンを拠点に皇帝ラインハルトを迎え撃つ。兵力は約2万9千隻対19万隻超。大軍が横に広がれない回廊の狭い区間に陣を敷き、数の差を打ち消そうとした。',cam:{t:[0,0,-20],r:200,th:.35,ph:.85},arrows:[{p:[[0,0,-120],[0,0,-70],[0,0,-30]],c:'E'}]},
 {time:'5月初旬',clock:'序盤',step:'突入',title:'黒色槍騎兵の突入',text:'ビッテンフェルトの黒色槍騎兵艦隊が正面から突入し、ファーレンハイト艦隊がこれを支える。狭い回廊では大軍の利が生きず、凹形に構えたヤン艦隊の集中砲火を浴びた。',cam:{t:[0,0,20],r:120,th:-.4,ph:1.0},arrows:[{p:[[-8,0,-40],[-7,0,-10],[-6,0,18]],c:'E'},{p:[[12,0,-46],[11,0,-15],[10,0,12]],c:'E'}]},
 {time:'5月',clock:'中盤',step:'消耗',title:'ファーレンハイト散る',text:'黒色槍騎兵は大損害を受けて後退し、ファーレンハイトは戦死した。皇帝本隊は兵力の厚みで波状攻撃を続け、回廊は消耗戦の場となる。',cam:{t:[0,0,0],r:140,th:.6,ph:1.0},arrows:[{p:[[0,0,-120],[0,0,-70],[0,0,-28]],c:'E'}]},
 {time:'5月',clock:'中盤',step:'双璧',title:'双璧の攻勢',text:'ミッターマイヤーとロイエンタールが前線に出て圧力を強める。シュタインメッツが戦死する一方、ヤン艦隊でも艦隊運用を支えたフィッシャーが戦死し、精緻な機動が難しくなっていった。',cam:{t:[4,4,8],r:155,th:.8,ph:1.0},arrows:[{p:[[18,0,-100],[18,0,-40],[18,0,10]],c:'E'},{p:[[0,8,-106],[-2,8,-40],[-4,8,6]],c:'E'}]},
 {time:'5月中旬',clock:'終盤',step:'発熱',title:'皇帝の発熱',text:'戦いのさなか、皇帝ラインハルトが高熱で倒れる。帝国軍の攻勢は鈍り、ヤン艦隊も消耗の極みにあった。両軍とも決着をつけられないまま、戦線は膠着する。',cam:{t:[0,0,-10],r:150,th:-.5,ph:1.05},arrows:[]},
 {time:'5月17日',clock:'終結',step:'講和',title:'講和の申し入れ',text:'帝国軍から講和の申し入れがあり、ヤンはこれを受けて戦闘は止まった。ヤンは皇帝との会談に向かうことになる。',cam:{t:[0,0,0],r:210,th:.4,ph:.9},arrows:[]}
];
const RESULT={title:'回廊の戦いの戦果',winner:'',outcome:'決着つかず（帝国の申し入れで講和へ）',when:'宇宙暦800年／新帝国暦2年 4月29日〜5月17日、イゼルローン回廊',
 summary:'7倍近い兵力差を、ヤンは回廊の地形で打ち消した。帝国軍は宿将2人と艦艇の約2割を失い、ヤン艦隊も兵力の大半をすり減らした。戦術上の勝敗はつかず、政治的な対話へ移った。',
 prev:'バーミリオン会戦後の同盟滅亡と、エル・ファシル独立政府の成立',next:'会談に向かう途中のヤン暗殺、そしてシヴァ星域会戦',
 factors:['回廊の狭さで帝国軍は大軍を横に展開できず、数の優位が発揮されなかった。','帝国は兵力の厚みに頼って攻め続け、名将を含む大きな損害を出した。','フィッシャーの戦死でヤン艦隊の機動力が落ち、守りの余力も尽きかけていた。','皇帝の発熱が帝国軍の攻勢を止め、講和への転換を促した。'],
 sides:[{name:'帝国軍',side:'E',cmdr:'皇帝ラインハルト',flag:'ブリュンヒルト',others:'ミッターマイヤー、ロイエンタール、ビッテンフェルト、ミュラー ほか',before:'192,410隻',loss:'39,110隻',rate:20,deaths:'約379万名',dead:['ファーレンハイト上級大将','シュタインメッツ上級大将']},
        {name:'ヤン艦隊',side:'A',cmdr:'ヤン・ウェンリー',flag:'ヒューベリオン',others:'メルカッツ、アッテンボロー、フィッシャー、ユリアン ほか',before:'28,840隻',loss:'約18,000隻（推定）',rate:62,deaths:'160万名以上（推定）',dead:['フィッシャー中将']}],
 after:['ヤンは講和会談へ向かう途中、地球教徒に暗殺される（6月1日）。','ユリアンがヤンの軍を引き継ぎ、イゼルローンの勢力は「共和政の火種」として残る。','帝国は上級大将2人を失い、皇帝の体調不安も表に出始める。','武力では屈しなかったイゼルローン勢力が、のちの立憲体制をめぐる交渉相手となっていく。'],
 note:'兵力・損害の数値は資料による。ヤン艦隊の損害は推定値で、資料によって差がある。損耗率は喪失艦艇÷参加艦艇で算出。'};
"""
