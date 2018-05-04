drop database if exists abcrecipe;
create database abcrecipe;
use abcrecipe;
drop table if exists User;
create table IF NOT EXISTS User(
	user_name varchar(100) not null,
	hash_password varchar(100) not null,
	primary key(user_name)
);
drop table if exists Profile;
create table IF NOT EXISTS Profile(
	profile_id int auto_increment not null,
	first_name varchar(100) not null,
	user_name varchar(100) not null,
	last_name varchar(100) not null,
	email varchar(100) not null UNIQUE,
	phone varchar (255) not null,
	diet varchar(20) not null,
	health_info varchar(50) not null,
	foreign key(user_name) references User(user_name) on delete cascade on update cascade,
	primary key(profile_id)
;
drop table if exists Ingredients;
create table IF NOT EXISTS Ingredients(
	ingredients_id int auto_increment not null,
	name varchar(100) not null,
	primary key(ingredients_id)
);
drop table if exists Uploads;
create table IF NOT EXISTS Uploads(
	user_name varchar(100) not null,
	recipe_id int not null,
	upload_date date not null,
	foreign key(user_name) references User(user_name) on delete cascade on update cascade,
	foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
	primary key(user_name,recipe_id)
);
drop table if exists Instructions;
create table IF NOT EXISTS Instructions(
	instruction_id int auto_increment not null,
	task varchar(255) not null,
	instruction_order int not null,
	primary key(instruction_id)
);
drop table if exists Recipe;
create table IF NOT EXISTS Recipe(
	recipe_id int auto_increment not null,
	name varchar(100) not null,
	calorie decimal(7,2),
	servings decimal(4,2),
	cook_time varchar(100) not null,
	prep_time varchar(100) not null,
	diet_type varchar(100) not null,
	primary key(recipe_id)
);
drop table if exists Meal;
create table IF NOT EXISTS Meal(
	meal_id int auto_increment not null,
	name varchar(100) not null,
	meal_type varchar(100) not null,
	img_src varchar(255) not null,
	primary key(meal_id)
);
drop table if exists Meal_plan;
create table IF NOT EXISTS Meal_plan(
	plan_id int auto_increment not null,
	week_num int not null,
	calorie decimal(7,2) not null,
	primary key(plan_id)
);
drop table if exists Measurements;
create table IF NOT EXISTS Measurements(
	measure_id int auto_increment not null,
	unit varchar(50) not null,
	primary key(measure_id)
);
drop table if exists Kitchen;
create table IF NOT EXISTS Kitchen(
	kitchen_id int auto_increment not null,
	user_name varchar(100) not null,
	foreign key(user_name) references User(user_name) on delete cascade on update cascade,
	primary key(kitchen_id)
);
drop table if exists Contains;
create table IF NOT EXISTS Contains(
	recipe_id int not null,
	ingredients_id int not null,
	foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
	foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
	primary key(recipe_id, ingredients_id)
);
drop table if exists Stores;
create table IF NOT EXISTS Stores(
	kitchen_id int not null,
	ingredients_id int not null,
	quantity int,
	foreign key(kitchen_id) references Kitchen(kitchen_id) on delete cascade on update cascade,
	foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
	primary key(kitchen_id, ingredients_id)
);
drop table if exists Creates;
create table IF NOT EXISTS Creates(
	recipe_id int not null,
	meal_id int not null,
	foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
	foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,
	primary key(recipe_id, meal_id)
);
drop table if exists Constructs;
create table IF NOT EXISTS Constructs(
	plan_id int not null,
	meal_id int not null,
	foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,
	foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,
	primary key(plan_id, meal_id)
);
drop table if exists Requests;
create table IF NOT EXISTS Requests(
	user_name varchar(100) not null,
	plan_id int not null,
	foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,
	foreign key(user_name) references User(user_name) on delete cascade on update cascade,
	primary key(user_name, meal_id)
);
drop table if exists Consists;
create table IF NOT EXISTS Consists(
	ingredients_id int not null,
	measure_id int not null,
	foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
	foreign key(measure_id) references Measurements(measure_id) on delete cascade on update cascade,
	primary key(ingredients_id, measure_id)
);