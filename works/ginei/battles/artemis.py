from common import env,fort
UC=797.08;ARC='内乱'
OUT='artemis.html'
TITLE='アルテミスの首飾り破壊 3D俯瞰';HEAD='アルテミスの首飾り';ERA='宇宙暦797年／帝国暦488年'
NOTE='首都ハイネセンを守る12基の防衛衛星。配置は概略'
SE='ヤン艦隊';SA='救国軍事会議';PALE='ally';PAL='coup'
EX,SP0=fort('首都ハイネセン','救国軍事会議が掌握','A',(0,0,60),'0x5f8ec0',16)
EX+=r"""
const SATS=[];for(let i=0;i<12;i++){const a=i/12*Math.PI*2,m=new THREE.Mesh(new THREE.OctahedronGeometry(1.6),new THREE.MeshLambertMaterial({color:0xd8e2ee,emissive:0x303844}));m.position.set(Math.cos(a)*30,Math.sin(a*2)*6,60+Math.sin(a)*30);scene.add(m);SATS.push({m,a,alive:true})}
const ICE=[];for(let i=0;i<12;i++){const m=new THREE.Mesh(new THREE.IcosahedronGeometry(2.4,0),new THREE.MeshLambertMaterial({color:0xbfe6ff,emissive:0x203040}));m.visible=false;scene.add(m);ICE.push(m)}
"""
SP=r"""const SPECIAL={lab:null,reset(i){if(!this.lab){this.lab=sprite('首都ハイネセン','救国軍事会議が掌握',CSS.A,3);this.lab.position.set(0,20,60);scene.add(this.lab);const l=sprite('アルテミスの首飾り','防衛衛星12基',CSS.A,2.4);l.position.set(32,8,60);scene.add(l)}
 SATS.forEach(s=>{s.alive=i<2;s.m.visible=s.alive});this.hit=false},
 update(now,dt){const t=now-phaseStart;SATS.forEach(s=>{if(s.m.visible){s.m.rotation.y+=dt;s.m.rotation.x+=dt*.6}});
  if(phase===1){ICE.forEach((m,k)=>{const s=SATS[k],p=Math.min(1,Math.max(0,(t-1-k*.15)/3.2));m.visible=p<1;const sx=-10+k*1.5,sy=4,sz=-60;m.position.set(sx+(s.m.position.x-sx)*p,sy+(s.m.position.y-sy)*p,sz+(s.m.position.z-sz)*p);m.rotation.x+=dt*2;
   if(p>=1&&s.alive){s.alive=false;s.m.visible=false;boom([s.m.position.x,s.m.position.y,s.m.position.z],true,0xcfefff);boom([s.m.position.x+1,s.m.position.y,s.m.position.z],true,0xffffff)}})}
  else ICE.forEach(m=>m.visible=false)}};"""
ENV=env(color='0xfff4e0',glow='0xffd090',pos=(-160,60,-120),extra=EX,special=SP)
DATA=r"""
const U=[
 {name:'ヤン艦隊',cmd:'ヤン',side:'E',n:60,k:{0:{p:[0,0,-50],s:'ready',l:'首都へ到着',f:'line'},1:{p:[0,0,-40],s:'wait',l:'氷塊を加速して放つ'},2:{p:[0,0,-10],s:'move',l:'首都へ進む',f:'column'},3:{p:[0,0,10],s:'wait',l:'クーデター終結'}}},
 {name:'救国軍事会議',cmd:'グリーンヒル大将',side:'A',n:12,k:{0:{p:[0,-4,46],s:'ready',l:'首都に籠る'},2:{s:'wait',l:'降伏を決める'},3:{s:'broken',l:'グリーンヒル射殺される'}}}
];
const PH=[
 {time:'8月',clock:'',step:'首都',title:'難攻不落の首飾り',text:'クーデターの最後の砦は、首都ハイネセンを取り巻く12基の無人防衛衛星「アルテミスの首飾り」だった。艦隊で正面から攻めれば大損害は避けられない。',cam:{fit:1,k:1.4,th:.5,ph:.95},arrows:[]},
 {time:'8月',clock:'',step:'氷塊',title:'氷の砲弾',text:'ヤンは艦隊を使わず、巨大な氷の塊を加速させて衛星にぶつけた。人の乗らない質量弾が、12基の衛星を次々に打ち砕く。',cam:{fit:1,k:1.5,th:.9,ph:.85},arrows:[]},
 {time:'8月',clock:'',step:'降伏',title:'無防備になった首都',text:'首飾りを失った首都は丸裸になった。救国軍事会議は抵抗の手段を失う。',cam:{fit:1,k:1.3,th:-.3,ph:.95},arrows:[{p:[[0,0,-40],[0,0,-24],[0,0,-10]],c:'E'}]},
 {time:'8月',clock:'',step:'終結',title:'クーデターの終わり',text:'グリーンヒル大将は、かつての逃亡者リンチに射殺され、リンチもその場で撃たれた。クーデターは終わったが、黒幕がラインハルトであったことを知る者は少なかった。',cam:{fit:1,k:1.3,th:.4,ph:.95},arrows:[]}
];
const RESULT={title:'アルテミスの首飾り破壊の結果',winner:'E',outcome:'ヤン艦隊（政府側）の勝利、クーデター終結',when:'宇宙暦797年8月、首都星ハイネセン',
 summary:'ヤンは氷塊を質量弾として防衛衛星12基を破壊し、艦隊の損害なしに首都を無力化した。救国軍事会議のクーデターはここで終わった。',
 prev:'ドーリア星域会戦',next:'帝国ではリップシュタット戦役の終結、同盟では疲弊した政府の復帰',
 factors:['艦隊で正面から攻めず、無人の質量弾で衛星を破壊した。','救国軍事会議はドーリアで機動戦力を失っており、首飾り以外に頼るものがなかった。'],
 sides:[{name:'ヤン艦隊',side:'E',cmdr:'ヤン・ウェンリー大将',flag:'ヒューベリオン',others:'—',before:'イゼルローン駐留艦隊',loss:'なし',rate:0,deaths:'—',dead:[]},
        {name:'救国軍事会議',side:'A',cmdr:'ドワイト・グリーンヒル大将',flag:'—',others:'アーサー・リンチ',before:'防衛衛星12基',loss:'衛星12基すべて',rate:100,deaths:'不明',dead:['グリーンヒル大将','リンチ']}],
 after:['トリューニヒト政権が復帰し、同盟政治の腐敗はむしろ深まる。','グリーンヒルの娘フレデリカはヤンの副官を続ける。','クーデターの裏にラインハルトの工作があったことは、同盟の多くの人々には知られなかった。'],
 note:'損耗率は衛星の破壊数による。'};
"""
