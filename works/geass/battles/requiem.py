from common import *
UC=2018.12
ARC="レクイエム"
OUT='requiem.html'
TITLE="ゼロ・レクイエム 3D俯瞰"
HEAD="レクイエム"
ERA="皇暦2018年"
SE="皇帝ルルーシュ"; SA="ゼロ"; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置はTV版にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x3a3a3e','0x6a6a6a',amp=2,seed=3,sky='0x8a9aaa')+specials(labels([("パレード", "処刑台へ向かう列", 'A', (0, 24, 0), 3)]))
DATA=r"""
const U=[
 {name:"パレード",cmd:"皇帝ルルーシュ",side:'E',n:20,k:{0:{p: [0, 7, -10], s: "move", l: "捕虜を引き連れる"},1:{p: [0, 7, -6], s: "move"},2:{p: [0, 7, -6], s: "broken", l: "皇帝が倒れる"},3:{p: [0, 7, -6], s: "gone"}}},
 {name:"ゼロ",cmd:"正体を隠す",side:'A',n:2,k:{0:{p: [0, 7, 30], s: "hidden"},1:{p: [0, 7, 14], s: "charge", l: "単身で現れる"},2:{p: [0, 7, -4], s: "charge", l: "皇帝を討つ"},3:{p: [0, 7, 10], s: "ready", l: "人々の英雄に"}}}
];
const PH=[
 {time:"皇暦2018年",clock:"R2 第25話",step:"行進",title:"処刑への行進",text:"ルルーシュは捕らえた黒の騎士団の幹部らの処刑に向けてパレードを行った。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:"",clock:"",step:"出現",title:"ゼロの出現",text:"そこへゼロの仮面をかぶった者が一人で現れ、警備をすり抜けた。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
 {time:"",clock:"",step:"刺殺",title:"計画の完成",text:"ゼロは皇帝ルルーシュを刺した。ルルーシュ自身が仕組んだ計画だった。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:"",clock:"",step:"解放",title:"その後",text:"捕虜は解放され、世界は対話に向かった。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "ゼロ・レクイエムの結果", "when": "皇暦2018年", "prev": "ダモクレス攻防戦", "next": "—", "factors": ["ルルーシュとスザクがあらかじめ仕組んだ計画だった。"], "winner": "A", "outcome": "皇帝ルルーシュの死（計画どおり）", "summary": "世界の憎しみを一身に集めたルルーシュが討たれ、戦争の連鎖が止まった。", "sides": [{"name": "皇帝ルルーシュ", "side": "E", "cmdr": "ルルーシュ・ヴィ・ブリタニア", "flag": "—", "others": "—", "before": "不明", "loss": "—", "rate": null, "deaths": "不明", "dead": ["ルルーシュ・ヴィ・ブリタニア"]}, {"name": "ゼロ", "side": "A", "cmdr": "（仮面の人物）", "flag": "—", "others": "—", "before": "1人", "loss": "なし", "rate": null, "deaths": "不明", "dead": []}], "after": ["ナナリーらのもとで和平が進む。", "ゼロは英雄として残る。"], "note": "展開はTVアニメ『コードギアス 反逆のルルーシュ』R1・R2にもとづく概略（配置は抽象化）。兵数・日付は作中で確認できたものが少なく、不明は「不明」とした。月は確認できず、並び順用の小数は放送順にもとづく推定。話数は英語版Wikipedia「List of Code Geass episodes」で確認。"};
"""
