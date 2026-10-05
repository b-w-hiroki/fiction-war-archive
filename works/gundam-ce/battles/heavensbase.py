from common import space_env, planet, colony, rock_fortress, land_env, specials, labels
UC=73.11
ARC='第二次大戦'
OUT='heavensbase.html'
TITLE='ヘブンズベース 3D俯瞰'
HEAD='ヘブンズベース'
ERA='C.E.73年（月日不明）'
SE='ザフト'; SA='地球連合軍'; PALE='zeon'; PAL='efsf'
NOTE='交戦中／健在の部隊。配置は概略'
ENV=land_env('0x4a5a5a','0xd0d6da',amp=6,seed=21,water='0x2a4a6a',sky='0x8090a0')+specials(labels([('ヘブンズベース','ロゴスの拠点','A',(0,14,30),3.2)]))
DATA=r"""
const U=[
 {name:'ザフト連合軍',cmd:'ザフト（反ロゴス同盟）',side:'E',n:50,k:{0:{"p": [0, 7, -50], "s": "move", "f": "line"},1:{"p": [0, 7, -20], "s": "charge"},2:{"p": [0, 7, -10], "s": "fight"},3:{"p": [0, 7, 10], "s": "charge", "l": "降下部隊が突入"},4:{"p": [0, 7, 24], "s": "ready", "l": "基地は降伏"}}},
 {name:'デストロイ部隊',cmd:'地球連合軍',side:'A',n:5,k:{0:{"p": [0, 7, 30], "s": "ready"},1:{"p": [0, 7, 14], "s": "fight", "l": "5機で迎撃", "b": 1},2:{"p": [0, 7, 10], "s": "fight"},3:{"p": [0, 7, 14], "s": "broken", "l": "シンらが撃破"},4:{"s": "gone"}}},
 {name:'ミネルバ隊',cmd:'シン・アスカ',side:'E',n:6,k:{0:{"p": [20, 7, -40], "s": "move"},1:{"p": [16, 7, -10], "s": "charge"},2:{"p": [14, 7, 8], "s": "fight", "l": "デストロイに挑む"},3:{"p": [10, 7, 12], "s": "fight"},4:{"p": [10, 7, 20], "s": "ready"}}},
 {name:'ロゴス',cmd:'ロード・ジブリール',side:'A',n:2,k:{0:{"p": [-10, 7, 40], "s": "ready"},1:{"p": [-10, 7, 40], "s": "ready"},2:{"p": [-10, 7, 40], "s": "ready"},3:{"p": [-20, 30, 60], "s": "withdraw", "l": "逃亡"},4:{"s": "gone"}}}
];
const PH=[
 {"time": "C.E.73年", "clock": "DESTINY第38話", "step": "包囲", "title": "ヘブンズベース包囲", "text": "デュランダル議長の呼びかけで、ザフトと反ロゴスの連合軍がロゴスの拠点を囲んだ。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": [{"p": [[0, 7, -50], [0, 7, -20]], "c": "E"}]},
 {"time": "同", "clock": "", "step": "反撃", "title": "デストロイの反撃", "text": "基地側は巨大MAデストロイ5機で応戦した。", "cam": {"fit": 1, "th": 0.8, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "交戦", "title": "デストロイとの戦い", "text": "シンらミネルバ隊がデストロイと戦った。", "cam": {"fit": 1, "th": 0.3, "ph": 0.95}, "arrows": []},
 {"time": "同", "clock": "", "step": "突入", "title": "降下部隊突入", "text": "ザフトの降下部隊が基地に入った。", "cam": {"fit": 1, "th": 0.5, "ph": 0.95}, "arrows": [{"p": [[0, 7, -10], [0, 7, 10]], "c": "E"}]},
 {"time": "同", "clock": "", "step": "降伏", "title": "基地の降伏", "text": "基地は降伏したが、ジブリールは逃れてオーブへ向かった。", "cam": {"fit": 1, "th": 0.4, "ph": 0.95}, "arrows": []}
];
const RESULT={"title": "ヘブンズベース攻防戦の結果", "when": "C.E.73年、アイスランド・ヘブンズベース", "prev": "ベルリン戦", "next": "オーブ攻防（ジブリール追撃）", "factors": ["デュランダルが反ロゴスの世論をまとめた。", "デストロイが撃破された。"], "winner": "E", "outcome": "ザフト側の勝利", "summary": "ロゴスの拠点がザフト中心の軍に落とされた戦い。", "sides": [{"name": "ザフト・反ロゴス同盟", "side": "E", "cmdr": "不明（デュランダル議長の指示）", "flag": "不明", "others": "シン・アスカ", "before": "不明", "loss": "不明", "rate": null, "deaths": "不明", "dead": []}, {"name": "地球連合軍（ロゴス派）", "side": "A", "cmdr": "ロード・ジブリール", "flag": "不明", "others": "—", "before": "不明", "loss": "基地", "rate": null, "deaths": "不明", "dead": []}], "after": ["ジブリールはオーブに逃れ、ザフトのオーブ攻撃を招く。"], "note": "月日は確認できず不明（UCは並び順の推定値）。話数第38話は電撃オンラインの記事による。"};
"""
