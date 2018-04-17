/*==============================================================*/
/* Database: abcrecipe                                          */
/*==============================================================*/

/*==============================================================*/
/* Table: person.                                               */
/*==============================================================*/
CREATE TABLE person (
    profile_id int NOT NULL,
    first_name varchar(80) NOT NULL,
    last_name varchar(80) NOT NULL,
    primary key(profile_id)
);


/*==============================================================*/
/* Table: account                                              */
/*==============================================================*/
CREATE TABLE account(
    profile_id int NOT NULL,
    user_name varchar(80) NOT NULL,
    email varchar(80) NOT NULL,
    addr varchar(80) NOT NULL,
    gender varchar(20) NOT NULL,
    _password varchar(255) NOT NULL,
    diet_type varchar(40) NOT NULL,
    allergies varchar(80) NOT NULL,
    foreign key(profile_id) references person(profile_id) on delete cascade on update cascade
);

