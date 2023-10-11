-- Create a keyspace
CREATE KEYSPACE IF NOT EXISTS easytally WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : '1' };

-- Create Costs table
CREATE TABLE IF NOT EXISTS easytally.costs (
userid text PRIMARY KEY,
item_count int,
last_update_timestamp timestamp
);


-- Create Income Table --
CREATE TABLE IF NOT EXISTS easytally.income (
    user_id text PRIMARY KEY,
    value float,
    last_update_timestamp timestamp
);

-- Insert some data
INSERT INTO easytally.costs
(userid, item_count, last_update_timestamp)
VALUES ('9876', 2, toTimeStamp(now()));
INSERT INTO store.shopping_cart
(userid, item_count, last_update_timestamp)
VALUES ('1234', 5, toTimeStamp(now()));
