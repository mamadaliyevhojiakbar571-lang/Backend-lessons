-- vazifalar jadvalini yaratish
CREATE TABLE vazifalar (
    id    INTEGER PRIMARY KEY,
    nomi  TEXT NOT NULL,
    fan   TEXT
);

-- namunaviy vazifalar
INSERT INTO vazifalar (nomi, fan) VALUES ('Misol yechish', 'Matematika');
INSERT INTO vazifalar (nomi, fan) VALUES ('Kitob o''qish', 'Adabiyot');
INSERT INTO vazifalar (nomi, fan) VALUES ('Yugurish', 'Jismoniy tarbiya');
