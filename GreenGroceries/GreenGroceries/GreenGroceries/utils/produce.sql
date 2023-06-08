DROP TABLE IF EXISTS Produce CASCADE;

CREATE TABLE IF NOT EXISTS Produce(
 pk serial UNIQUE NOT NULL PRIMARY KEY,
    full_name VARCHAR(255),
    goals_scored INT,
    assists INT,
    total_points INT,
    goals_conceded INT,
    creativity DECIMAL(10, 2),
    influence DECIMAL(10, 2),
    threat DECIMAL(10, 2),
    bonus INT,
    bps INT,
    ict_index DECIMAL(10, 2),
    clean_sheets INT,
    red_cards INT,
    yellow_cards INT,
    position VARCHAR(255),
    GW INT,
    total_goals INT,
    all_points INT,
    total_assists INT,
    team VARCHAR(255)
);

DELETE FROM Produce;

CREATE INDEX IF NOT EXISTS produce_index
ON Produce (full_name);

DROP TABLE IF EXISTS Sell;

CREATE TABLE IF NOT EXISTS Sell(
    farmer_pk int not null REFERENCES Farmers(pk) ON DELETE CASCADE,
    produce_pk int not null REFERENCES Produce(pk) ON DELETE CASCADE,
    available boolean default true,
    PRIMARY KEY (farmer_pk, produce_pk)
);

CREATE INDEX IF NOT EXISTS sell_index
ON Sell (farmer_pk, available);

DELETE FROM Sell;

DROP TABLE IF EXISTS ProduceOrder;

CREATE TABLE IF NOT EXISTS ProduceOrder(
    pk serial not null PRIMARY KEY,
    customer_pk int not null REFERENCES Customers(pk) ON DELETE CASCADE,
    farmer_pk int not null REFERENCES Farmers(pk) ON DELETE CASCADE,
    produce_pk int not null REFERENCES Produce(pk) ON DELETE CASCADE,
    created_at timestamp not null default current_timestamp
);

DELETE FROM ProduceOrder;

CREATE OR REPLACE VIEW vw_produce
AS
SELECT p.full_name,p.team,p.position,p.GW, p.total_points, p.goals_scored,
       p.assists
FROM Produce p
ORDER BY p.total_points;

CREATE OR REPLACE VIEW vw_total_produce
AS
SELECT p.full_name,p.team,p.position,p.all_points, p.total_goals, p.total_assists
FROM Produce p
ORDER BY p.total_points;