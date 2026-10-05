from common import *
UC=2017.08
ARC="反逆"
OUT='kyushu.html'
TITLE="九州戦役 3D俯瞰"
HEAD="九州"
ERA="皇暦2017年"
SE="澤崎・中華連邦"; SA="ブリタニア軍"; PALE='sind'; PAL='zeon'
NOTE='交戦中／健在の部隊。配置はTV版にもとづく概略。部隊の大きさは兵力の目安'
ENV=land_env('0x2a3a3a','0x5a6a5a',water='0x1a3a5a',amp=5,seed=9,sky='0x5a6a7a')+specials(labels([("福岡", "中華連邦の支援で占拠", 'E', (0, 24, -20), 3)]))
DATA=r"""
const U=[
 {name:"占拠軍",cmd:"澤崎敦",side:'E',n:30,k:{0:{p: [0, 7, -20], s: "ready", l: "福岡を占拠"},1:{p: [0, 7, -16], s: "fight", l: "防衛"},2:{p: [0, 7, -14], s: "broken", l: "司令部を突かれる"},3:{p: [0, 7, -40], s: "withdraw", l: "逃走"}}},
 {name:"ランスロット",cmd:"枢木スザク",side:'A',n:4,k:{0:{p: [10, 7, 30], s: "move", l: "単機で出撃"},1:{p: [6, 7, 0], s: "charge", l: "敵陣へ"},2:{p: [0, 7, -10], s: "charge", l: "司令部を叩く"},3:{p: [0, 7, -14], s: "ready"}}},
 {name:"ゼロ（援護）",cmd:"ゼロ",side:'A',n:3,k:{0:{p: [20, 7, 40], s: "hidden"},1:{p: [16, 7, 6], s: "fight", l: "ガウェインで援護"},2:{p: [8, 7, -6], s: "fight"},3:{p: [10, 7, 0], s: "ready"}}}
];
const PH=[
 {time:"皇暦2017年",clock:"R1 第20話",step:"占拠",title:"独立の宣言",text:"元日本政府の澤崎が中華連邦の支援で九州に上陸し、日本の独立を名乗った。",cam:{fit:1,th:0.3,ph:.9},arrows:[]},
 {time:"",clock:"",step:"出撃",title:"騎士の突入",text:"ユーフェミアの騎士となったスザクが、ランスロットで単機突入した。",cam:{fit:1,th:0.5,ph:.9},arrows:[]},
 {time:"",clock:"",step:"共闘",title:"思わぬ援護",text:"ゼロもガウェインで現れ、スザクと並んで敵の司令部を崩した。",cam:{fit:1,th:0.7,ph:.9},arrows:[]},
 {time:"",clock:"",step:"鎮圧",title:"澤崎の敗走",text:"司令部を失った占拠軍は崩れ、澤崎は捕らえられた。",cam:{fit:1,th:0.9,ph:.9},arrows:[]}
];
const RESULT={"title": "九州戦役の結果", "when": "皇暦2017年", "prev": "ナリタ攻防戦", "next": "ブラック・リベリオン", "factors": ["ランスロットの突破力が司令部への近道を開いた。", "ゼロも中華連邦の介入を嫌い、敵の敵として援護した。"], "winner": "A", "outcome": "ブリタニア軍の勝利", "summary": "中華連邦の後押しした独立宣言は短期で潰えた。", "sides": [{"name": "中華連邦の支援を受けた占拠軍", "side": "E", "cmdr": "澤崎敦", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "ブリタニア軍", "side": "A", "cmdr": "コーネリア・リ・ブリタニア総督", "flag": "—", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["スザクの評価が高まる。", "ユーフェミアの行政特区日本構想へつながる（推定）。"], "note": "展開はTVアニメ『コードギアス 反逆のルルーシュ』R1・R2にもとづく概略（配置は抽象化）。兵数・日付は作中で確認できたものが少なく、不明は「不明」とした。月は確認できず、並び順用の小数は放送順にもとづく推定。話数は英語版Wikipedia「List of Code Geass episodes」で確認。"};
"""
