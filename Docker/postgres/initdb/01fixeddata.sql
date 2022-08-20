INSERT INTO
    daily_mission_table
VALUES
    ();

INSERT INTO
    weekly_mission_table
VALUES
    ();

INSERT INTO
    region_table
VALUES
    (
        (1, '北海道'),
        (2, '東北'),
        (3, '関東'),
        (4, '中部'),
        (5, '関西'),
        (6, '中国'),
        (7, '四国'),
        (8, '九州'),
        (9, '沖縄')
    ) ON CONFLICT DO NOTHING;

INSERT INTO
    tag_table
VALUES
    ();