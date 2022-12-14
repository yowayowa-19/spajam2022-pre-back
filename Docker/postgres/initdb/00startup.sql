CREATE TABLE IF NOT EXISTS user_table (
    id serial PRIMARY KEY,
    name varchar(255),
    email varchar(255),
		password varchar(255),
    region int DEFAULT 0,
    has_car boolean DEFAULT false,
    has_aircon boolean DEFAULT false,
    has_tv boolean DEFAULT false,
    total_points int DEFAULT 0
);

CREATE TABLE IF NOT EXISTS daily_mission_table (
    id serial PRIMARY KEY,
    title varchar(255),
    describe varchar(255) DEFAULT '',
    tag_id int,
    point int,
    has_slider boolean
);

CREATE TABLE IF NOT EXISTS weekly_mission_table (
    id serial PRIMARY KEY,
    title varchar(255),
    describe varchar(255) DEFAULT '',
    tag_id int,
    point int,
    has_slider boolean
);

CREATE TABLE IF NOT EXISTS daily_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp,
    user_id int,
    mission_id int,
    current_point int DEFAULT 0
);

CREATE TABLE IF NOT EXISTS weekly_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp,
    user_id int,
    mission_id int,
    current_point int DEFAULT 0
);

CREATE TABLE IF NOT EXISTS all_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp,
    user_id int,
    mission_category varchar(255),
    mission_id int
);

CREATE TABLE IF NOT EXISTS region_table (id serial PRIMARY KEY, name varchar(255));

CREATE TABLE IF NOT EXISTS tag_table (id serial PRIMARY KEY, name varchar(255));
