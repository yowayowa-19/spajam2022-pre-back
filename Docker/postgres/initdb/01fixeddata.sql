INSERT INTO
    daily_mission_table (title, tag_id, point, has_slider)
VALUES
    ('100m以内の移動に車を使う', 1, 2, false),
    ('500m以内の移動に車を使う', 1, 3, false),
    ('車のエアコンをつけて窓を全開にする', 1, 5, false),
    ('公共交通機関を使わない', 1, 1, false),
    ('空ぶかしをする', 1, 2, false),
    ('急発進をする', 1, 2, false);

INSERT INTO
    weekly_mission_table (title, tag_id, point, has_slider)
VALUES
    ('1km以内の移動に車を使う', 1, 5, true);
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