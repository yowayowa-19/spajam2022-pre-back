CREATE TABLE IF NOT EXISTS user_table (
    id serial PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    region int,
    has_car boolean,
    has_bike boolean,
    has_aircon boolean,
    has_tv boolean,
    total_points int
);

CREATE TABLE IF NOT EXISTS daily_mission_table (
    id serial PRIMARY KEY,
    name varchar(255),
    content varchar(255),
    tag_id int,
    point int
);

CREATE TABLE IF NOT EXISTS weekly_mission_table (
    id serial PRIMARY KEY,
    name varchar(255),
    content varchar(255),
    tag_id int,
    point int
);

CREATE TABLE IF NOT EXISTS daily_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp ,
    user_id int,
    mission_id int
);

CREATE TABLE IF NOT EXISTS weekly_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp ,
    user_id int,
    mission_id int
);

CREATE TABLE IF NOT EXISTS all_history_table (
    id serial PRIMARY KEY,
    completed_at timestamp ,
    user_id int,
    mission_category str,
    mission_id int
);

CREATE TABLE IF NOT EXISTS region_table (id serial PRIMARY KEY, name varchar(255));

CREATE TABLE IF NOT EXISTS tag_table (id serial PRIMARY KEY, name varchar(255));