from common import *
UC=2018.03
ARC="復活"
OUT='tianzi.html'
TITLE="天子奪還（朱禁城の戦い） 3D俯瞰"
HEAD="朱禁城"
ERA="皇暦2018年"
SE="大宦官・ブリタニア"; SA="黒の騎士団・星刻"; PALE='sind'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置はTV版にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x5a4a30','0x8a7050',amp=3,seed=11,sky='0x8a7a6a')+specials(labels([("朱禁城", "中華連邦の都", 'E', (0, 24, -24), 3)]))
DATA=r"""
const U=[
 {name:"大宦官軍",cmd:"大宦官",side:'E',n:30,k:{0:{p: [0, 7, -24], s: "ready", l: "婚儀を守る"},1:{p: [0, 7, -16], s: "fight"},2:{p: [0, 7, -14], s: "fight"},3:{p: [0, 7, -30], s: "broken", l: "民衆に見放される"}}},
 {name:"ブリタニア派遣軍",cmd:"シュナイゼル",side:'E',n:20,k:{0:{p: [20, 7, -30], s: "wait"},1:{p: [16, 7, -20], s: "wait"},2:{p: [10, 7, -10], s: "fight", l: "介入"},3:{p: [20, 7, -40], s: "withdraw", l: "撤収"}}},
 {name:"黒の騎士団",cmd:"ゼロ",side:'A',n:20,k:{0:{p: [0, 7, 10], s: "charge", l: "天子をさらう"},1:{p: [0, 7, 20], s: "fight", l: "陵墓に籠る"},2:{p: [0, 7, 24], s: "fight", l: "包囲される"},3:{p: [0, 7, 10], s: "ready"}}},
 {name:"星刻派",cmd:"黎星刻",side:'A',n:10,k:{0:{p: [-20, 7, 0], s: "hidden"},1:{p: [-20, 7, -10], s: "fight", l: "騎士団を攻める"},2:{p: [-10, 7, 10], s: "fight", l: "大宦官と決別"},3:{p: [-6, 7, 0], s: "ready"}}}
];
const PH=[
 {time:"皇暦2018年",clock:"R2 第8〜9話",step:"奪取",title:"婚儀の乱入",text:"ゼロは天子とオデュッセウスの婚儀に乱入し、天子を連れ出した。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:"",clock:"R2 第9〜10話",step:"籠城",title:"陵墓の戦い",text:"黒の騎士団は天帝八十八陵に籠り、星刻らに攻められた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
 {time:"",clock:"R2 第10話",step:"世論",title:"大宦官の本音",text:"大宦官が国を売る発言が中継で流れ、民衆と星刻の怒りは大宦官へ向いた。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:"",clock:"",step:"決着",title:"同盟",text:"大宦官は倒れ、星刻は黒の騎士団と手を結んだ。ブリタニアは引いた。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "天子奪還（朱禁城の戦い）の結果", "when": "皇暦2018年", "prev": "ブラック・リベリオン", "next": "第二次東京決戦", "factors": ["戦場の外、中継される言葉で民衆を味方につけた。", "星刻ら国を憂える勢力が大宦官から離れた。"], "winner": "A", "outcome": "黒の騎士団・星刻派の勝利", "summary": "大宦官が倒れ、中華連邦は黒の騎士団と結んだ。", "sides": [{"name": "大宦官とブリタニア派遣軍", "side": "E", "cmdr": "大宦官／シュナイゼル", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "黒の騎士団・星刻派", "side": "A", "cmdr": "ゼロ／黎星刻", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["超合集国の構想が進む。", "天子と星刻が中華連邦を率いる。"], "note": "展開はTVアニメ『コードギアス 反逆のルルーシュ』R1・R2にもとづく概略（配置は抽象化）。兵数・日付は作中で確認できたものが少なく、不明は「不明」とした。月は確認できず、並び順用の小数は放送順にもとづく推定。話数は英語版Wikipedia「List of Code Geass episodes」で確認。"};
"""
