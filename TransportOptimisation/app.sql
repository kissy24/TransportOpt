create table app (
 mode TEXT,
 start TEXT,
 end TEXT,
 distance REAL,
 fee REAL,
 time REAL,
 waitingtime REAL,
 eload REAL,
 cost REAL
);

create table cache (
 start TEXT,
 end TEXT,
 amount REAL,
 weight REAL,
 price REAL,
 cost REAL,
 time REAL,
 envload REAL,
 mode TEXT
 );

.separator ,
.import app.csv app