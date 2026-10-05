from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=71.0615
ARC='地球の攻防'
OUT='orb71.html'
TITLE='オーブ解放作戦 3D俯瞰'
HEAD='オーブ解放作戦'
ERA='C.E.71年6月15日'
SE='オーブ・AA'; SA='地球連合軍'; PALE='scout'; PAL='efsf'
NOTE='交戦中／健在の部隊。概略。この戦いはオーブ側をE枠で表示'
ENV=land_env('0x3a6a3a','0x9a9a70',amp=5,seed=9,water='0x2a6a90',sky='0x7aa0c0')+specials(labels([('オノゴロ島','カグヤ・マスドライバー','E',(0,14,30),3.2)]))
DATA=r"""
const U=[
 {name:'連合侵攻軍',cmd:'地球連合軍',side:'A',n:40,k:{0:{"p": [0, 7, -50], "s": "move", "f": "line"},1:{"p": [0, 7, -20], "s": "charge", "b": 1},2:{"p": [0, 7, 0], "s": "fight"},3:{"p": [0, 7, 10], "s": "charge", "l": "島に迫る"},4:{"p": [0, 7, 20], "s": "ready", "l": "島を占領"}}},
 {name:'連合新型G',cmd:'オルガ／クロト／シャニ',side:'A',n:3,k:{0:{"p": [10, 7, -40], "s": "move"},1:{"p": [10, 7, -10], "s": "charge"},2:{"p": [12, 7, 4], "s": "fight", "l": "フリーダムらと交戦"},3:{"p": [10, 7, -6], "s": "fight"},4:{"p": [10, 7, -20], "s": "withdraw"}}},
 {name:'オーブ軍',cmd:'ウズミ・ナラ・アスハ',side:'E',n:24,k:{0:{"p": [0, 7, 24], "s": "ready", "f": "concave"},1:{"p": [0, 7, 16], "s": "fight"},2:{"p": [0, 7, 20], "s": "fight"},3:{"p": [0, 7, 28], "s": "broken", "l": "押される"},4:{"p": [0, 7, 30], "s": "gone", "l": "施設と共に自爆"}}},
 {name:'アークエンジェル隊',cmd:'キラ／アスラン',side:'E',n:6,k:{0:{"p": [16, 7, 20], "s": "ready"},1:{"p": [14, 7, 8], "s": "fight"},2:{"p": [14, 7, 6], "s": "fight", "l": "アスランが加わる"},3:{"p": [16, 7, 20], "s": "fight"},4:{"p": [20, 40, 40], "s": "withdraw", "l": "宇宙へ脱出"}}}
];
const PH=[
 {"time": "C.E.71年6月15日", "clock": "TV版第38話", "step": "侵攻", "title": "連合の侵攻", "text": "中立を守るオーブに、マスドライバーを求める連合が攻め込んだ。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 7, -50], [0, 7, -20]], "c": "A"}]},
 {"time": "同日", "clock": "", "step": "防戦", "title": "オーブの防戦", "text": "オーブ軍とアークエンジェルが迎え撃つ。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "TV版第39話", "step": "合流", "title": "アスランの参戦", "text": "アスランのジャスティスが加わり、キラと共に戦った。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同日", "clock": "", "step": "劣勢", "title": "押されるオーブ", "text": "数で劣るオーブは押し込まれた。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": []},
 {"time": "翌日", "clock": "TV版第40話", "step": "自爆", "title": "カグヤの自爆", "text": "ウズミら首脳は施設と共に自爆し、残った者はクサナギとアークエンジェルで宇宙へ出た。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[16, 7, 20], [20, 40, 40]], "c": "E"}]}
];
const RESULT={"title": "オーブ解放作戦の結果", "when": "C.E.71年6月15日、オーブ連合首長国", "prev": "パナマ攻略戦", "next": "ボアズ攻略戦（9月23日）", "factors": ["連合の数の優位。", "オーブは施設を渡さないことを選んだ。"], "winner": "A", "outcome": "連合の勝利（オーブ占領）", "summary": "中立国オーブが連合に攻め落とされた戦い。三隻同盟の出発点になった。", "sides": [{"name": "オーブ軍・アークエンジェル", "side": "E", "cmdr": "ウズミ・ナラ・アスハ", "flag": "不明", "others": "キラ・ヤマト、アスラン・ザラ", "before": "不明", "loss": "国土とマスドライバー", "rate": null, "deaths": "不明", "dead": ["ウズミ・ナラ・アスハ"]}, {"name": "地球連合軍", "side": "A", "cmdr": "不明", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}], "after": ["オーブ勢力とアークエンジェルが宇宙へ逃れる。", "キラ、アスラン、カガリが同じ側に立つ。"], "note": "日付はfandom年表による。この戦いでは便宜上オーブ側を左側（E枠）に置いた。話数はPHASE-38「決意の砲火」〜PHASE-40「暁の宇宙へ」（https://en.wikipedia.org/wiki/List_of_Mobile_Suit_Gundam_SEED_episodes ）。"};
"""
