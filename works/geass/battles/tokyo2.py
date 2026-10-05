from common import *
UC=2018.08
ARC="復活"
OUT='tokyo2.html'
TITLE="第二次東京決戦 3D俯瞰"
HEAD="トウキョウ"
ERA="皇暦2018年"
SE="ブリタニア軍"; SA="黒の騎士団"; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置はTV版にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x3a3a44','0x6a6a70',water='0x1a2a4a',amp=3,seed=6,sky='0x4a4a5a')+specials(labels([("トウキョウ租界", "フレイヤ着弾点", 'E', (0, 30, -14), 3)]))
DATA=r"""
const U=[
 {name:"ブリタニア守備軍",cmd:"ギルフォードら",side:'E',n:40,k:{0:{p: [0, 7, -20], s: "ready", l: "租界を守る"},1:{p: [0, 7, -16], s: "fight"},2:{p: [0, 7, -16], s: "broken", l: "フレイヤに巻き込まれる"},3:{p: [0, 7, -24], s: "withdraw"}}},
 {name:"黒の騎士団",cmd:"ゼロ",side:'A',n:40,k:{0:{p: [0, 7, 30], s: "move", l: "超合集国の名で進攻"},1:{p: [0, 7, 6], s: "charge", l: "政庁へ"},2:{p: [0, 7, 16], s: "broken", l: "フレイヤに巻き込まれる"},3:{p: [0, 7, 30], s: "withdraw", l: "停戦"}}},
 {name:"ランスロット",cmd:"枢木スザク",side:'E',n:3,k:{0:{p: [20, 7, -10], s: "fight"},1:{p: [14, 7, 0], s: "fight", l: "紅蓮と戦う"},2:{p: [6, 7, -10], s: "fight", l: "フレイヤを撃つ", b: 1},3:{p: [10, 7, -24], s: "ready"}}}
];
const PH=[
 {time:"皇暦2018年",clock:"R2 第17〜18話",step:"進攻",title:"超合集国の進攻",text:"超合集国決議を受け、黒の騎士団がトウキョウ租界へ攻め込んだ。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:"",clock:"R2 第18話",step:"攻防",title:"政庁への接近",text:"騎士団は政庁に迫り、スザクは劣勢に追い込まれた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
 {time:"",clock:"",step:"フレイヤ",title:"大量破壊兵器",text:"スザクはフレイヤを撃ち、租界の中心は大きく消し飛んだ。両軍とも巻き込まれる。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:"",clock:"R2 第19話",step:"停戦",title:"ゼロへの疑念",text:"シュナイゼルが停戦を持ちかけ、ゼロのギアスを明かす。黒の騎士団はゼロを見限った。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "第二次東京決戦の結果", "when": "皇暦2018年", "prev": "天子奪還", "next": "ダモクレス攻防戦", "factors": ["フレイヤの破壊力が戦場そのものを消した。", "シュナイゼルの調略で騎士団の幹部がゼロから離れた。"], "winner": "", "outcome": "停戦（決着なし）", "summary": "フレイヤの一撃で両軍とも戦いを続けられなくなった。", "sides": [{"name": "ブリタニア軍", "side": "E", "cmdr": "ナナリー総督（形式上）", "flag": "—", "others": "—", "before": "不明", "loss": "不明（多数）", "rate": null, "deaths": "不明", "dead": []}, {"name": "黒の騎士団", "side": "A", "cmdr": "ゼロ", "flag": "—", "others": "—", "before": "不明", "loss": "不明（多数）", "rate": null, "deaths": "不明", "dead": []}], "after": ["ナナリーが死んだとされる。", "ゼロは騎士団を追われ、ロロが彼を逃がして死ぬ。"], "note": "展開はTVアニメ『コードギアス 反逆のルルーシュ』R1・R2にもとづく概略（配置は抽象化）。兵数・日付は作中で確認できたものが少なく、不明は「不明」とした。月は確認できず、並び順用の小数は放送順にもとづく推定。話数は英語版Wikipedia「List of Code Geass episodes」で確認。"};
"""
