from common import *
UC=153.05
ARC='ザンスカール戦争'
OUT='kaileth.html'
TITLE='カイラスギリー攻略 3D俯瞰'
HEAD='カイラスギリー'
ERA='U.C.0153年5月（推定）'
SE='ザンスカール帝国'; SA='リガ・ミリティア・連邦軍'; PALE='serpent'; PAL='scout'
NOTE='交戦中／健在の部隊。TV版『Vガンダム』第27〜28話にもとづく概略'
ENV=space_env()+planet(pos=(0,-80,220),r=70,label=('地球','','A'))+rock_fortress((0,0,-40),12,'solomon','KG')+specials(labels([('カイラスギリー','ザンスカールの巨大ビーム砲','E',(0,20,-40),3.2)]))
DATA=r"""
const U=[
 {"name": "カイラスギリー守備隊", "cmd": "タシロ・ヴァゴ", "side": "E", "n": 12, "k": {"0": {"p": [0, 0, -40], "s": "ready", "f": "convex"}, "1": {"p": [0, 0, -28], "s": "fight", "b": 1}, "2": {"p": [0, 0, -24], "s": "fight"}, "3": {"p": [0, 0, -30], "s": "broken"}, "4": {"s": "gone"}}},
 {"name": "リガ・ミリティア", "cmd": "Vガンダム（ウッソ・エヴィン）", "side": "A", "n": 6, "k": {"0": {"p": [-10, 0, 40], "s": "move"}, "1": {"p": [-8, 0, 10], "s": "charge"}, "2": {"p": [-4, 0, -20], "s": "fight", "l": "砲台に取りつく"}, "3": {"p": [-2, 0, -30], "s": "fight"}, "4": {"p": [-4, 0, 0], "s": "ready"}}},
 {"name": "連邦艦隊", "cmd": "地球連邦軍", "side": "A", "n": 10, "k": {"0": {"p": [14, 0, 50], "s": "ready"}, "1": {"p": [12, 0, 30], "s": "fight"}, "2": {"p": [10, 0, 20], "s": "fight"}, "3": {"p": [10, 0, 10], "s": "fight"}, "4": {"p": [10, 0, 10], "s": "ready"}}}
];
const PH=[
 {"time": "5月（推定）", "clock": "TV版第27話", "step": "開戦", "title": "巨大砲の攻略へ", "text": "ザンスカールは巨大ビーム砲カイラスギリーで地球圏をおびやかした。", "cam": {"fit": 1, "th": 0.4, "ph": 0.9}, "arrows": []},
 {"time": "同日", "clock": "", "step": "突撃", "title": "艦隊の攻撃", "text": "リガ・ミリティアと連邦艦隊が攻撃をかけた。", "cam": {"fit": 1, "th": 0.4, "ph": 0.9}, "arrows": [{"p": [[-8, 0, 10], [-4, 0, -20]], "c": "A"}]},
 {"time": "同日", "clock": "", "step": "肉薄", "title": "砲台への取りつき", "text": "Vガンダムが砲台へ取りついた。", "cam": {"fit": 1, "th": 0.6, "ph": 0.9}, "arrows": []},
 {"time": "同日", "clock": "", "step": "陥落", "title": "カイラスギリー奪取", "text": "タシロらは退き、リガ・ミリティアが巨大砲を奪った。のちに仕掛けられた爆弾で内部から爆発した。", "cam": {"fit": 1, "th": 0.2, "ph": 1.0}, "arrows": []}
];
const RESULT={"title": "カイラスギリー攻略の結果", "when": "U.C.0153年、地球軌道", "prev": "フロンティアIV・ラフレシア（0123）", "next": "エンジェル・ハイロゥの決戦", "factors": ["リガ・ミリティアのMSが砲台に肉薄した。"], "winner": "A", "outcome": "リガ・ミリティア側の勝利（奪取）", "summary": "ザンスカールの地球圏攻撃の拠点が失われた。", "sides": [{"name": "ザンスカール帝国", "side": "E", "cmdr": "タシロ・ヴァゴ", "flag": "不明", "others": "—", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "リガ・ミリティア・連邦軍", "side": "A", "cmdr": "ロベルト・ゴメス", "flag": "不明", "others": "ウッソ・エヴィン", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": ["ジュンコ・ジェンコ"]}], "after": ["戦いはエンジェル・ハイロゥへ移る。"], "note": "話数（第27〜28話）はhttps://en.wikipedia.org/wiki/List_of_Mobile_Suit_Victory_Gundam_episodes 、経緯・指揮官・ジュンコの戦死は https://dic.pixiv.net/a/%E3%82%AB%E3%82%A4%E3%83%A9%E3%82%B9%E3%82%AE%E3%83%AA%E3%83%BC による。月は記憶にもとづく推定。"};
"""
