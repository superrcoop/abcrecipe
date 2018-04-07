drop table if exists account;
create table account (
    id integer primary key autoincrement,
    username text not null,
    addr text not null,
    birthdate text not null,
    email text not null
);


