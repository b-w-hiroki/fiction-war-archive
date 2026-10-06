from common import env
UC=798.04
ARC='雌伏'
OUT='fortress.html'
TITLE='要塞対要塞 3D俯瞰'
HEAD='要塞対要塞'
ERA='宇宙暦798年／帝国暦489年'
NOTE='交戦中／健在の部隊数。帝国はガイエスブルク要塞＋ケンプ・ミュラー艦隊。展開は概略。主砲名は媒体差を併記'
EXTRA=r"""
// 回廊の壁（航行不能宙域）
(function(){const n=2600,p=new Float32Array(n*3),c=new Float32Array(n*3);for(let i=0;i<n;i++){const sd=i%2?1:-1,x=sd*(62+hs(i,31)*30),y=(hs(32,i)-.5)*70,z=(hs(i,33)-.5)*260;p.set([x,y,z],i*3);const b=.25+hs(i,34)*.3;c.set([b,b*.35,b*.3],i*3)}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));g.setAttribute('color',new THREE.BufferAttribute(c,3));
 scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:1.1,vertexColors:true,transparent:true,blending:THREE.AdditiveBlending,depthWrite:false})))})();
// 要塞
const ISER=new THREE.Mesh(new THREE.SphereGeometry(11,48,32),new THREE.MeshLambertMaterial({color:0xcfd6df,emissive:0x1a2430}));ISER.position.set(0,0,40);scene.add(ISER);
const GAI=new THREE.Group();scene.add(GAI);
GAI.add(new THREE.Mesh(new THREE.SphereGeometry(9.5,40,28),new THREE.MeshLambertMaterial({color:0x8f8b84,emissive:0x1d1810})));
const engM=new THREE.MeshBasicMaterial({color:0x9ad0ff});
for(let i=0;i<16;i++){const a=i/16*Math.PI*2,e=new THREE.Mesh(new THREE.CylinderGeometry(.9,1.3,3.2,10),new THREE.MeshLambertMaterial({color:0x5e5a54}));e.position.set(Math.cos(a)*9.6,0,Math.sin(a)*9.6);e.rotation.z=Math.PI/2;e.rotation.y=-a;GAI.add(e);
 const f=new THREE.Sprite(new THREE.SpriteMaterial({map:glowTex,color:0x9ad0ff,transparent:true,opacity:.0,blending:THREE.AdditiveBlending,depthWrite:false}));f.position.set(Math.cos(a)*11.6,0,Math.sin(a)*11.6);f.scale.set(3,3,1);GAI.add(f)}
GAI.position.set(0,0,-62);
function cannon(a,b,col,w){const d=new THREE.Vector3().subVectors(b,a),L=d.length();const m=new THREE.Mesh(new THREE.CylinderGeometry(w,w,L,12,1,true),new THREE.MeshBasicMaterial({color:col,transparent:true,opacity:1,blending:THREE.AdditiveBlending,depthWrite:false}));
 m.position.copy(a).addScaledVector(d,.5);m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.normalize());scene.add(m);return {m,life:1.1}}
"""
SPECIAL=r"""
const SPECIAL={beams:[],lab:null,shot:0,boom:false,
 reset(i){if(!this.lab){this.lab=[[ISER,'イゼルローン要塞','同盟'],[GAI,'ガイエスブルク要塞','帝国']].map(([o,n,s])=>{const sp=sprite(n,s==='同盟'?'雷神の鎚 / トゥールハンマー':'ガイエスハーケン / ツヴァイヘンダー',s==='同盟'?CSS.A:CSS.E,3.2);scene.add(sp);return {o,sp}})}
  this.shot=0;this.boom=false;GAI.visible=true;GAI.rotation.set(0,0,0);if(i<4)GAI.position.set(0,0,-62);if(i===4)GAI.position.set(0,0,-62)},
 update(now,dt){const t=now-phaseStart;
  if(phase===4){const k=Math.min(1,t/7);GAI.position.z=-62+26*ease(k);GAI.children.forEach(c=>{if(c.isSprite)c.material.opacity=.9})}
  else if(phase===5){GAI.position.z=-36;const spin=Math.min(4,t*.6);GAI.rotation.y+=dt*spin;GAI.rotation.z=Math.sin(now*3)*.2*Math.min(1,t/3);
   if(t>6&&this.shot<1){this.shot=1;this.beams.push(cannon(ISER.position,GAI.position,0xbfe8ff,1.6))}
   if(t>6.5&&!this.boom){this.boom=true;for(let k=0;k<14;k++)boom([GAI.position.x+(Math.random()-.5)*16,(Math.random()-.5)*10,GAI.position.z+(Math.random()-.5)*16],true,0xffb070);GAI.visible=false}}
  else if(phase===6){GAI.visible=false}
  else{GAI.children.forEach(c=>{if(c.isSprite)c.material.opacity=0})}
  if(phase===1&&t>1.2){const n=Math.floor((t-1.2)/3.2);if(n>=this.shot&&n<3){this.shot=n+1;const a=n%2?ISER.position:GAI.position,b=n%2?GAI.position:ISER.position;this.beams.push(cannon(a,b,n%2?0xbfe8ff:0xffd080,1.3));boom([b.x,b.y,b.z],true)}}
  this.beams=this.beams.filter(b=>{b.life-=dt;b.m.material.opacity=Math.max(0,b.life);if(b.life<=0){scene.remove(b.m);b.m.geometry.dispose();return false}return true});
  if(this.lab)this.lab.forEach(l=>{l.sp.position.set(l.o.position.x,l.o.position.y+13,l.o.position.z);l.sp.visible=l.o.visible})}};
"""
ENV=env(color='0xfff0d8',glow='0xffd8a0',pos=(150,60,-200),extra=EXTRA,special=SPECIAL)
DATA=r"""
const U=[
 {name:'ケンプ艦隊',cmd:'ケンプ',side:'E',n:50,k:{0:{p:[-10,0,-48],s:'ready',l:'要塞とともに出現'},1:{p:[-10,0,-26],s:'fight',l:''},4:{p:[-12,0,-24],l:'要塞を護衛'},5:{s:'broken',l:'要塞とともに壊滅'},6:{s:'gone'}}},
 {name:'ミュラー艦隊',cmd:'ミュラー',side:'E',n:45,k:{0:{p:[12,0,-50],s:'ready'},1:{p:[12,0,-30],s:'fight'},2:{p:[18,8,62],s:'charge',l:'要塞の背後へ回り込む'},3:{p:[16,8,60],s:'fight',l:'逆撃を受ける'},4:{p:[14,2,-22],s:'fight',l:''},5:{l:''},6:{p:[0,0,-120],s:'withdraw',l:'残存艦を率い撤退'}}},
 {name:'駐留艦隊',cmd:'メルカッツ',side:'A',n:40,k:{0:{p:[-14,0,28],s:'ready',l:'キャゼルヌが要塞司令官代理'},1:{p:[-12,0,14],s:'fight',l:''},2:{p:[-10,0,30],l:'要塞へ後退'},3:{p:[28,12,50],s:'charge',l:'囮で誘い込み逆撃',f:'wedge'},4:{p:[-8,0,18],s:'fight',l:''},6:{s:'wait'}}},
 {name:'駐留艦隊・分艦隊',cmd:'アッテンボロー',side:'A',n:35,k:{0:{p:[14,0,28],s:'ready'},1:{p:[12,0,14],s:'fight'},2:{p:[10,0,30]},3:{p:[8,2,62],s:'fight',l:'背後で迎え撃つ',f:'concave',h:150},4:{p:[10,0,18],l:''},6:{s:'wait'}}},
 {name:'ヤン救援艦隊',cmd:'ヤン',side:'A',n:45,k:{0:{p:[70,10,-140],s:'hidden'},5:{p:[22,4,-52],s:'fight',l:'推進機1基に集中砲火',b:1,f:'concave',h:-120},6:{p:[24,4,-46],s:'wait',l:''}}}
];
const PH=[
 {time:'4月10日',clock:'出現',step:'出現',title:'要塞がワープしてくる',text:'ヤンが首都で査問会に呼び出されている隙に、帝国軍はワープ機関を取り付けたガイエスブルク要塞をイゼルローン回廊へ送り込んだ。司令官はケンプ、副司令官はミュラー。要塞はキャゼルヌが代理で預かっていた。',cam:{t:[0,0,-10],r:170,th:.6,ph:1.1},arrows:[]},
 {time:'4月',clock:'序盤',step:'主砲',title:'主砲の撃ち合い',text:'ガイエスブルク要塞主砲（原作・旧OVA系「ガイエスハーケン」／DNT「ツヴァイヘンダー」）と、イゼルローン要塞主砲（原作・旧OVA系「雷神の鎚」／DNT「トゥールハンマー」）が撃ち合い、両軍の艦隊が要塞の間でぶつかる。要塞同士の戦いは前例のないものだった。',cam:{t:[0,0,-12],r:170,th:.3,ph:.8},arrows:[]},
 {time:'4月',clock:'中盤',step:'背後',title:'ミュラーの迂回',text:'ミュラーの艦隊が要塞の裏側へ回り込み、防御の隙を突く。正面だけを見ていた守備側は対応に追われた。',cam:{t:[10,4,20],r:150,th:-.5,ph:1.0},arrows:[{p:[[12,0,-30],[38,10,10],[18,8,62]],c:'E'}]},
 {time:'4月',clock:'中盤',step:'逆撃',title:'メルカッツの罠',text:'亡命してきたメルカッツが駐留艦隊を率い、囮で敵を誘い込んで逆撃を加える。ミュラー艦隊は挟まれて大きな損害を受けた。',cam:{t:[12,6,46],r:120,th:.9,ph:1.0},arrows:[{p:[[-10,0,30],[16,14,40],[28,12,50]],c:'A'}]},
 {time:'終盤',clock:'',step:'衝突',title:'要塞をぶつける',text:'攻め手を失ったケンプは、ガイエスブルクそのものをイゼルローンに衝突させる作戦に出る。巨大な要塞がゆっくりと前進を始めた。',cam:{t:[0,0,-8],r:170,th:.45,ph:.85},arrows:[{p:[[0,0,-62],[0,0,-46],[0,0,-30]],c:'E'}]},
 {time:'終盤',clock:'',step:'帰還',title:'ヤン帰還、推進機を撃つ',text:'査問会から解放されたヤンが救援艦隊を率いて到着する。16基ある推進機のうち1基に砲火を集めると、推力の均衡を失った要塞は回転を始めた。そこへイゼルローン要塞の主砲が撃ち込まれ、ガイエスブルクはケンプもろとも爆散した。',cam:{t:[4,2,-24],r:160,th:.9,ph:1.0},arrows:[{p:[[70,10,-140],[45,8,-90],[22,4,-52]],c:'A'}]},
 {time:'戦後',clock:'',step:'撤退',title:'わずかな生還',text:'重傷を負ったミュラーが残存艦をまとめて撤退する。帝国軍は要塞と遠征兵力の大半を失い、回廊からの侵攻は行き詰まった。',cam:{t:[0,0,-40],r:230,th:.4,ph:.9},arrows:[{p:[[14,2,-22],[6,0,-70],[0,0,-120]],c:'E'}]}
];
const RESULT={title:'第8次イゼルローン攻防戦の戦果',when:'宇宙暦798年／帝国暦489年4月、イゼルローン回廊',prev:'ヤンが首都ハイネセンで査問会にかけられ、要塞を離れる',next:'ラグナロック作戦（帝国はフェザーン回廊からの大侵攻へ）',
 factors:['司令官不在でも、キャゼルヌ・メルカッツ・シェーンコップらの留守部隊が持ちこたえた。','メルカッツの逆撃でミュラー艦隊が大損害を受け、帝国は攻め手を失った。','衝突作戦は、推進機1基に砲火を集めて要塞を回転させるというヤンの着想で崩された。'],winner:'A',outcome:'同盟軍の勝利',
 summary:'移動要塞による奇襲は、ヤン不在の要塞を守り切った留守部隊と、帰還したヤンの一撃で失敗した。帝国軍は要塞と遠征部隊の大半を失った。',
 sides:[{name:'帝国軍',side:'E',cmdr:'ケンプ大将',flag:'ヨーツンハイム',others:'ミュラー（副司令官）',before:'移動要塞1基＋艦隊',loss:'要塞1基、艦艇約15,000隻',rate:90,deaths:'約180万名',dead:['ケンプ大将（司令官）']},
        {name:'同盟軍',side:'A',cmdr:'キャゼルヌ（司令官代理）→ヤン（帰還後）',flag:'ヒューベリオン（ヤン帰還後）',others:'メルカッツ、シェーンコップ、アッテンボロー、ユリアン',before:'イゼルローン要塞＋駐留艦隊',loss:'不明（要塞は健在）',rate:null,deaths:'不明',dead:[]}],
 after:['ミュラーは重傷を負いながら生還し、以後の粘り強い戦いぶりにつながる。','回廊からの攻略は割に合わないことがはっきりし、帝国は次の大攻勢でフェザーン回廊を使う方針に傾く。','ヤンは査問会から前線に戻り、同盟の「要塞を守れる唯一の将」という評価がさらに固まる。','同盟政府とヤンの不信は解消されず、政治の足かせは残った。'],
 note:'帝国軍の兵力・損害は資料によって差がある（艦艇約8,000隻とする資料もある）。ここでは損害約15,000隻・将兵約180万名とする資料に拠った。損耗率は「遠征兵力の約9割を喪失」という記述による。'};
"""
