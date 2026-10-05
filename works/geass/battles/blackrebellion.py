from common import *
UC=2017.12
ARC="反逆"
OUT='blackrebellion.html'
TITLE="ブラック・リベリオン（第一次東京決戦） 3D俯瞰"
HEAD="トウキョウ"
ERA="皇暦2017年"
SE="ブリタニア軍"; SA="黒の騎士団"; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置はTV版にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x3a3a44','0x6a6a70',water='0x1a2a4a',amp=3,seed=4,sky='0x4a4a5a')+specials(labels([("トウキョウ租界", "政庁", 'E', (0, 30, -20), 3)]))
DATA=r"""
const U=[
 {name:"エリア11総督府軍",cmd:"コーネリア総督",side:'E',n:40,k:{0:{p: [0, 7, -20], s: "ready", l: "政庁を守る"},1:{p: [0, 7, -14], s: "fight"},2:{p: [0, 7, -18], s: "broken", l: "外周を崩される"},3:{p: [0, 7, -16], s: "fight", l: "立て直す"},4:{p: [0, 7, -16], s: "ready", l: "反乱を鎮圧"}}},
 {name:"黒の騎士団",cmd:"ゼロ",side:'A',n:40,k:{0:{p: [0, 7, 30], s: "move", l: "蜂起"},1:{p: [0, 7, 10], s: "charge", l: "租界へ"},2:{p: [0, 7, 0], s: "charge", l: "地盤を崩す", b: 1},3:{p: [0, 7, 4], s: "broken", l: "指揮官不在"},4:{p: [0, 7, 30], s: "broken", l: "崩壊"}}},
 {name:"ランスロット",cmd:"枢木スザク",side:'E',n:3,k:{0:{p: [30, 7, -30], s: "wait"},1:{p: [20, 7, -10], s: "fight"},2:{p: [10, 7, -6], s: "fight"},3:{p: [20, 7, 30], s: "move", l: "ゼロを追う"},4:{p: [24, 7, 40], s: "ready", l: "ゼロを捕らえる"}}}
];
const PH=[
 {time:"皇暦2017年",clock:"R1 第22〜23話",step:"虐殺",title:"行政特区の惨劇",text:"行政特区日本の式典で日本人が殺される事件が起き、ゼロは合衆国日本を宣言して蜂起した。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:"",clock:"R1 第24話",step:"進撃",title:"租界へ",text:"黒の騎士団と各地の日本人がトウキョウ租界へ攻め上がった。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
 {time:"",clock:"",step:"崩落",title:"租界の外周を崩す",text:"ゼロは租界の構造を崩して守備軍に打撃を与えた。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:"",clock:"R1 第25話",step:"離脱",title:"ゼロ不在",text:"ナナリーがさらわれ、ゼロは戦場を離れて神根島へ向かった。指揮官を失った騎士団は崩れ始める。",cam:{fit:1,th:0.9,ph:.9},arrows:[]},
 {time:"",clock:"R2 第1話（回想）",step:"鎮圧",title:"反乱の終わり",text:"蜂起は鎮圧され、神根島でゼロはスザクに捕らえられた。",cam:{fit:1,th:1.1,ph:.9},arrows:[]}
];
const RESULT={"title": "ブラック・リベリオン（第一次東京決戦）の結果", "when": "皇暦2017年", "prev": "九州戦役", "next": "天子奪還", "factors": ["指揮官ゼロが戦場を離れ、騎士団の指揮が崩れた。", "政庁の守備が持ちこたえた。"], "winner": "E", "outcome": "ブリタニア軍の勝利（蜂起失敗）", "summary": "日本独立の蜂起は失敗し、ゼロは捕らえられた。", "sides": [{"name": "ブリタニア軍", "side": "E", "cmdr": "コーネリア・リ・ブリタニア総督", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "黒の騎士団", "side": "A", "cmdr": "ゼロ", "flag": "—", "others": "—", "before": "不明", "loss": "不明（壊滅）", "rate": null, "deaths": "不明", "dead": []}], "after": ["ルルーシュは記憶を書き換えられ、学生として監視下に置かれる。", "騎士団の幹部の多くが捕らわれる。"], "note": "展開はTVアニメ『コードギアス 反逆のルルーシュ』R1・R2にもとづく概略（配置は抽象化）。兵数・日付は作中で確認できたものが少なく、不明は「不明」とした。月は確認できず、並び順用の小数は放送順にもとづく推定。話数は英語版Wikipedia「List of Code Geass episodes」で確認。"};
"""
