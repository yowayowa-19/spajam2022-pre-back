-- tag_id
-- car:    1
-- aircon: 2
-- tv:     3
-- other:  4
INSERT INTO
    daily_mission_table (title, tag_id, point, has_slider)
VALUES
		('100m以内の移動に車を使う', 1, 2, false),
		('500m以内の移動に車を使う', 1, 3, false),
		('車のエアコンをつけて窓を全開にする', 1, 5, false),
		('公共交通機関を使わない', 1, 1, false),
		('空ぶかしをする', 1, 2, false),
		('急発進をする', 1, 2, false),
		('エアコンを1時間つける', 2, 1, false),
		('エアコンの設定温度を20℃に設定する', 2, 5, false),
		('使ってない部屋の電気を3時間つける', 4, 3, false),
		('スーパー/コンビニでレジ袋をもらう', 4, 1, false),
		('歯磨き/手洗いのときに水をだしっぱなしにする', 4, 1, false);


INSERT INTO
    weekly_mission_table (title, tag_id, point, has_slider)
VALUES
		('1km以内の移動に車を使う', 1, 5, false),
		('つかってない電化製品を10個コンセントに繋ぐ',4, 5, false),
		('髪や体を洗っているときにシャワーを出しっぱなしにする', 4, 10, false),
		('わりばしを使う', 4, 5, false),
		('お湯を沸かして冷蔵庫で冷やす', 4, 20, false);
INSERT INTO
    region_table
VALUES
		(0, '未設定'),
		(1, '北海道'),
		(2, '東北'),
		(3, '関東'),
		(4, '中部'),
		(5, '関西'),
		(6, '中国'),
		(7, '四国'),
		(8, '九州'),
		(9, '沖縄') ON CONFLICT DO NOTHING;

-- INSERT INTO
--     tag_table
-- VALUES
--     ();
