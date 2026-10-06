from common import env, labels, shot, specials
UC=794.10;ARC='若き日'
OUT='iser6.html'
TITLE='第6次イゼルローン攻防戦 3D俯瞰';HEAD='第六次イゼルローン';ERA='宇宙暦794年／帝国暦485年'
NOTE='同盟軍51,400隻が要塞を攻める。配置は概略'
EXTRA=r"""
const ISER=new THREE.Mesh(new THREE.SphereGeometry(11,48,32),new THREE.MeshLambertMaterial({color:0xcfd6df,emissive:0x1a2430}));ISER.position.set(0,0,-55);scene.add(ISER);
const RING=new THREE.Mesh(new THREE.TorusGeometry(46,.15,6,120),new THREE.MeshBasicMaterial({color:0xffd080,transparent:true,opacity:.35}));RING.rotation.x=Math.PI/2;RING.position.copy(ISER.position);scene.add(RING);
"""
SPECIAL=specials(
 labels([
  ('イゼルローン要塞','帝国軍','E',(0,13,-55),1.8),
  ('主砲の射程','雷神の鎚','E',(36,2,-20),1.35),
 ]),
 shot((0,0,-55),'同盟軍主力',1,delay=1.2,beam='0xdff5ff',w=2.8,booms=18,wave=True),
)
ENV=env(color='0xfff0d8',glow='0xffd8a0',pos=(150,60,180),extra=EXTRA,special=SPECIAL)
DATA=r"""
const U=[
 {name:'要塞駐留艦隊',cmd:'ミュッケンベルガー',side:'E',n:60,k:{0:{p:[0,0,-38],s:'ready',f:'convex'},1:{s:'fight'},3:{p:[0,0,-30],s:'fight'},4:{s:'wait',l:'要塞を守り切る'}}},
 {name:'ミューゼル少将の部隊',cmd:'ラインハルト',side:'E',n:25,k:{0:{p:[-30,4,-40],s:'wait',l:'約1000隻単位'},3:{p:[-40,4,30],s:'charge',l:'退路を断つそぶり',f:'wedge'},4:{p:[-38,4,26],s:'wait',l:''}}},
 {name:'同盟軍主力',cmd:'ロボス',side:'A',n:90,k:{0:{p:[0,0,40],s:'move',l:'51,400隻',f:'line',h:180},1:{p:[0,0,6],s:'fight',l:'射程の縁で攻撃'},2:{p:[0,0,-2],l:''},3:{p:[0,0,4],l:'後方が気になる'},4:{p:[0,0,60],s:'withdraw',l:'撤退'}}},
 {name:'ホーランド少将の部隊',cmd:'ホーランド',side:'A',n:35,k:{0:{p:[26,0,36],s:'ready',f:'line',h:180},1:{p:[30,0,-8],s:'fight',l:'射程の縁で踊る'},2:{f:{ring:[0,-55,47,-.2,1.1,.06]},l:'D線上のワルツ作戦'},3:{p:[28,0,4],s:'fight',l:''},4:{p:[30,0,64],s:'withdraw'}}}
];
const PH=[
 {time:'10月',clock:'',step:'来攻',title:'5万隻の攻勢',text:'同盟軍はロボス元帥のもと艦艇51,400隻、将兵600万人でイゼルローン要塞に押し寄せた。総参謀長はグリーンヒル、作戦参謀にはヤン大佐の名もあった。',cam:{fit:1,th:.5,ph:.95},arrows:[{p:[[0,0,40],[0,0,20],[0,0,6]],c:'A'}]},
 {time:'11月',clock:'',step:'攻防',title:'主砲の射程',text:'要塞主砲「雷神の鎚」の射程は同盟軍に大きな脅威となった。同盟軍は射程の外縁ぎりぎりで攻撃を続けた。',cam:{fit:1,th:.0,ph:.35},arrows:[]},
 {time:'11月',clock:'',step:'ワルツ',title:'D線上のワルツ作戦',text:'藤崎竜版では、主砲の射程境界を利用して攻防する一連の作戦が「D線上のワルツ作戦」と題されている。',cam:{fit:1,th:.6,ph:.7},arrows:[]},
 {time:'12月',clock:'',step:'牽制',title:'退路を断つそぶり',text:'最終盤、ラインハルトの部隊が同盟軍の後方へ回り込み、退路を断つかのように動いた。心理的な弱点を突かれた同盟軍は浮き足立つ。',cam:{fit:1,th:-.7,ph:1.0},arrows:[{p:[[-30,4,-40],[-48,4,-6],[-40,4,30]],c:'E'}]},
 {time:'12月10日',clock:'終結',step:'撤退',title:'要塞は落ちず',text:'同盟軍は攻略をあきらめて撤退した。イゼルローン要塞はまたも難攻不落を証明した。',cam:{fit:1,th:.4,ph:.9},arrows:[{p:[[0,0,4],[0,0,30],[0,0,60]],c:'A'}]}
];
const RESULT={title:'第6次イゼルローン攻防戦の結果',winner:'E',outcome:'帝国軍の防衛成功',when:'宇宙暦794年／帝国暦485年 10月〜12月10日、イゼルローン回廊',
 summary:'同盟軍の大攻勢は要塞主砲の壁を越えられなかった。ラインハルトの牽制が同盟軍の撤退を早めた。',
 prev:'ヴァンフリート星域会戦',next:'第3次ティアマト会戦',
 factors:['要塞主砲の射程が、大艦隊でも近寄れない壁になっていた。','同盟軍は射程外からの攻撃に終始し、決定打を欠いた。','退路を断たれる不安を突いたラインハルトの機動。'],
 sides:[{name:'帝国軍',side:'E',cmdr:'ミュッケンベルガー元帥',flag:'ヴィルヘルミナ',others:'ラインハルト少将',before:'イゼルローン要塞＋駐留艦隊',loss:'不明',rate:null,deaths:'不明',dead:[]},
        {name:'同盟軍',side:'A',cmdr:'ロボス元帥',flag:'アイアース',others:'グリーンヒル（総参謀長）、ヤン大佐（作戦参謀）、ホーランド少将',before:'51,400隻（将兵600万人）',loss:'不明',rate:null,deaths:'不明',dead:[]}],
 after:['要塞は健在で、回廊の出口は引き続き帝国が押さえる。','ホーランドは名を上げて中将となり、次の第3次ティアマト会戦に臨む。','ラインハルトは戦功を重ね、中将へ進む。'],
 note:'兵力・損害など未照合の数値は今後の監査対象。藤崎竜版の章題「D線上のワルツ作戦」と「雷神の鎚」は集英社公式書誌で確認済み。'};
"""
