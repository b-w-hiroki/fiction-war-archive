from common import space_env, specials, labels
UC=79.12241
ARC='宇宙決戦'
OUT='thunderbolt.html'
TITLE='サンダーボルト宙域の戦い 3D俯瞰'
HEAD='サンダーボルト'
ERA='U.C.0079年12月（推定・ソロモン攻略と同時期）'
SE='ジオン軍'; SA='連邦軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。旧サイド4の残骸が漂う宙域。配置は『機動戦士ガンダム サンダーボルト』にもとづく概略で、時期と経過は推定を含む'
EXTRA=r"""
(function(){const n=900,p=new Float32Array(n*3),c=new Float32Array(n*3);for(let i=0;i<n;i++){p.set([(hs(i,41)-.5)*200,(hs(42,i)-.5)*50,(hs(i,43)-.5)*160],i*3);const b=.35+hs(i,44)*.35;c.set([b,b*.95,b*.9],i*3)}
 const g=new THREE.BufferGeometry();g.setAttribute('position',new THREE.BufferAttribute(p,3));g.setAttribute('color',new THREE.BufferAttribute(c,3));scene.add(new THREE.Points(g,new THREE.PointsMaterial({size:2.4,sizeAttenuation:false,vertexColors:true})))})();
"""
ENV=space_env()+EXTRA+specials(labels([('サンダーボルト宙域','旧サイド4（ムーア）の残骸','A',(0,24,0),3.4)]))
DATA=r"""
const U=[
 {name:'リビング・デッド師団',cmd:'ジオン守備部隊',side:'E',n:30,k:{0:{p:[0,0,-36],s:'ready',l:'宙域を封鎖'},1:{p:[0,0,-26],s:'fight',l:'狙撃で迎え撃つ'},2:{p:[0,0,-20],s:'fight'},3:{p:[0,0,-30],s:'broken',l:'防衛線が崩れる'},4:{p:[-10,0,-50],s:'withdraw',l:'撤退'}}},
 {name:'ダリル・ローレンツ',cmd:'ジオン軍エース',side:'E',n:3,k:{0:{p:[10,0,-30],s:'ready'},1:{p:[8,0,-16],s:'fight',l:'スナイパー'},2:{p:[4,0,-4],s:'charge',l:'ガンダムと交戦'},3:{p:[0,0,-14],s:'fight'},4:{p:[-6,0,-46],s:'withdraw'}}},
 {name:'ムーア同胞団',cmd:'連邦軍 第5艦隊所属',side:'A',n:40,k:{0:{p:[0,0,40],s:'ready',l:'故郷ムーアの奪回を誓う'},1:{p:[0,0,30],s:'fight',l:'損害が重なる'},2:{p:[0,0,20],s:'fight'},3:{p:[0,0,-4],s:'charge',l:'宙域を突破'},4:{p:[0,0,-20],s:'ready'}}},
 {name:'イオ・フレミング',cmd:'フルアーマー・ガンダム',side:'A',n:3,k:{0:{p:[-10,0,30],s:'ready'},1:{p:[-8,0,16],s:'fight'},2:{p:[-2,0,4],s:'charge',l:'ダリルと交戦'},3:{p:[-4,0,-6],s:'fight'},4:{p:[-6,0,-16],s:'ready'}}}
];
const PH=[
 {time:'12月',clock:'',step:'封鎖',title:'雷の宙域',text:'崩れたコロニーの残骸がぶつかり合い、放電が絶えない宙域を、ジオンの守備部隊が押さえていた。手足を失った兵士を集めた部隊で、遠距離からの狙撃を得意とした。',cam:{fit:1,th:.4,ph:.9},arrows:[]},
 {time:'攻勢',clock:'',step:'攻勢',title:'ムーア同胞団の攻勢',text:'この宙域にあったコロニー群の出身者で作られた連邦部隊「ムーア同胞団」が、奪回を目指して攻め込む。残骸に隠れた狙撃で、損害が重なった。',cam:{fit:1,th:.8,ph:.95},arrows:[{p:[[0,0,40],[0,0,24]],c:'A'}]},
 {time:'激戦',clock:'',step:'一騎打ち',title:'イオとダリル',text:'連邦のイオ・フレミングと、ジオンのダリル・ローレンツが何度も戦場で向き合う。二人の戦いは宙域全体の行方と重なっていく。',cam:{fit:1,th:.3,ph:.8},arrows:[{p:[[-8,0,16],[-2,0,4]],c:'A'},{p:[[8,0,-16],[4,0,-4]],c:'E'}]},
 {time:'終盤',clock:'',step:'突破',title:'防衛線の崩壊',text:'ソロモン攻略と同じころ、宙域のジオン防衛線は崩れた。連邦はこの宙域を押さえ、ジオンの守備部隊は撤退した。',cam:{fit:1,th:.5,ph:.95},arrows:[{p:[[0,0,20],[0,0,-4]],c:'A'}]},
 {time:'その後',clock:'',step:'その後',title:'戦いの後',text:'双方に大きな犠牲が出た。イオとダリルの因縁は一年戦争後も続いていく。',cam:{fit:1,th:.4,ph:1.1},arrows:[]}
];
const RESULT={title:'サンダーボルト宙域の戦いの結果',when:'U.C.0079年12月（推定）、旧サイド4周辺の暗礁宙域',prev:'ルウム戦役後の宙域封鎖',next:'ア・バオア・クー攻略戦',
 factors:['残骸と放電で視界も通信も効かず、狙撃と待ち伏せが有利だった。','ムーア同胞団は故郷を取り戻す意志で、損害を出しながら攻め続けた。','ソロモンの陥落でジオン側は増援を受けられなかった（推定）。'],winner:'A',outcome:'連邦軍の勝利（宙域を確保・推定）',
 summary:'旧サイド4の暗礁宙域で、連邦のムーア同胞団とジオンの守備部隊が戦った。勝敗の大筋は連邦側だが、経過には推定を含む。',
 sides:[{name:'ジオン軍',side:'E',cmdr:'不明',flag:'不明',others:'ダリル・ローレンツ',before:'不明',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'地球連邦軍',side:'A',cmdr:'不明',flag:'不明',others:'イオ・フレミング',before:'不明',loss:'不明（大きな損害）',rate:null,deaths:'不明',dead:[]}],
 after:['連邦はサイド4周辺の宙域を押さえる（推定）。','イオとダリルの物語は、一年戦争後の地球（南洋）へ続く。'],
 note:'作品の描写は一年戦争の大筋と細部が異なる部分がある。時期・勝敗・経過は推定を含み、数値はすべて不明とした。'};
"""
