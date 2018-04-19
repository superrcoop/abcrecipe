drop database if exists abcrecipe;
create database abcrecipe;
use abcrecipe;

drop table if exists User;
create table IF NOT EXISTS User(
    user_name varchar(100) not null,
    hash_password varchar(100) not null,
    primary key(user_name)
);

Insert into User Values ("jodi","jodi"),("jordan","jordan");

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
);

drop table if exists Recipe;
create table Recipe(
    recipe_id int auto_increment not null,
    name varchar(100) not null,
    calorie int,
    servings int,
    cook_time varchar(100) not null,
    prep_time varchar(100) not null,
    diet_type varchar(100) not null,
    primary key(recipe_id)
);



drop table if exists Ingredients;
create table Ingredients(
    ingredients_id int auto_increment not null,
    name varchar(100),
    primary key(ingredients_id)
);

insert into Ingredients(name) values("rice");
insert into Ingredients(name) values("lime-juice");
insert into Ingredients(name) values("coffee-powder");
insert into Ingredients(name) values("bananas");
insert into Ingredients(name) values("mushroom");
insert into Ingredients(name) values("vinegar");
insert into Ingredients(name) values("flour");
insert into Ingredients(name) values("eggs");
insert into Ingredients(name) values("salmon");
insert into Ingredients(name) values("pepper");
insert into Ingredients(name) values("chocolate");
insert into Ingredients(name) values("onions");
insert into Ingredients(name) values("cheese");
insert into Ingredients(name) values("chicken");
insert into Ingredients(name) values("fish");
insert into Ingredients(name) values("water");
insert into Ingredients(name) values("salt");
insert into Ingredients(name) values("sugar");
insert into Ingredients(name) values("butter");
insert into Ingredients(name) values("pork");
insert into Ingredients(name) values("oxtail");
insert into Ingredients(name) values("turkey neck");
insert into Ingredients(name) values("liver");
insert into Ingredients(name) values("spinach");
insert into Ingredients(name) values("carrot");
insert into Ingredients(name) values("lettuce");
insert into Ingredients(name) values("tomato");
insert into Ingredients(name) values("beef");
insert into Ingredients(name) values("pea");

drop table if exists Kitchen;
create table Kitchen(
    kitchen_id int auto_increment not null,
    user_name varchar(100) not null,
    foreign key(user_name) references User(user_name) on delete cascade on update cascade,
    primary key(kitchen_id)
);

drop table if exists Meal;
create table Meal(
    meal_id int auto_increment not null,
    name varchar(100) not null,
    meal_type varchar(100) not null,
    img_src varchar(255) not null,
    primary key(meal_id)
);

drop table if exists Meal_plan;
create table Meal_plan(
    plan_id int auto_increment not null,
    week_num int not null,
    calorie decimal(7,2) not null,
    primary key(plan_id)
);

drop table if exists Measurements;
create table Measurements(
    measure_id int auto_increment not null,
    unit varchar(50) not null,
    primary key(measure_id)
);

drop table if exists Instructions;
create table Instructions(
    instruction_id int auto_increment not null,
    recipe_id int not null,
    task varchar(255) not null,
    instruction_order int not null,
    foreign key (recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    primary key(instruction_id,recipe_id)
);

drop table if exists Uploads;
create table Uploads(
    user_name varchar(100) not null,
    recipe_id int not null,
    upload_date date not null,
    foreign key(user_name) references User(user_name) on delete cascade on update cascade,
    foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    primary key(user_name,recipe_id)
);

drop table if exists Contains;
create table Contains(
    recipe_id int not null,
    ingredients_id int not null,
    foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
    primary key(recipe_id, ingredients_id)
);

drop table if exists Stores;
create table Stores(
    kitchen_id int not null,
    ingredients_id int not null,
    quantity int,
    foreign key(kitchen_id) references Kitchen(kitchen_id) on delete cascade on update cascade,
    foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
    primary key(kitchen_id,ingredients_id)
);

drop table if exists Creates;
create table Creates(
    recipe_id int not null,
    meal_id int not null,
    foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,
    primary key(recipe_id,meal_id)
);

drop table if exists Constructs;
create table Constructs(
    meal_id int not null,
    plan_id int not null,
    foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,
    foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,
    primary key(meal_id,plan_id)
);

drop table if exists Requests;
create table Requests(
    user_name varchar(100) not null,
    plan_id int not null,
    foreign key(user_name) references User(user_name) on delete cascade on update cascade,
    foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,
    primary key(user_name,plan_id)
);

drop table if exists Consists;
create table Consists(
    ingredients_id int not null,
    measure_id int not null,
    foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
    foreign key(measure_id) references Measurements(measure_id) on delete cascade on update cascade,
    primary key(ingredients_id,measure_id)
);

Drop procedure if exists GetRecipes;
DELIMITER //
CREATE PROCEDURE GetRecipes(IN name VARCHAR(120))
BEGIN (
    SELECT * from Recipe WHERE Recipe.name LIKE name
);
END //
DELIMITER ;

Drop procedure if exists GetRecipeId;
DELIMITER //
CREATE PROCEDURE GetRecipeId(IN name VARCHAR(120))
BEGIN (
    SELECT recipe_id from Recipe WHERE Recipe.name LIKE name
);
END //
DELIMITER ;

Drop procedure if exists GetInstructionsId;
DELIMITER //
CREATE PROCEDURE GetInstructionsId(IN task VARCHAR(120))
BEGIN (
    SELECT Instructions.instruction_id from Instructions WHERE Instructions.task LIKE task
);
END //
DELIMITER ;

Drop procedure if exists GetIngredientsId;
DELIMITER //
CREATE PROCEDURE GetIngredientsId(IN name VARCHAR(120))
BEGIN (
    SELECT Ingredients.ingredients_id from Ingredients WHERE Ingredients.name LIKE name
);
END //
DELIMITER ;

Drop procedure if exists GetRecipeInfo;
DELIMITER //
CREATE PROCEDURE GetRecipeInfo(IN id int)
BEGIN (
    SELECT * from Recipe WHERE Recipe.recipe_id=id
);
END //
DELIMITER ;

Drop procedure if exists GetIngredients;
DELIMITER //
CREATE PROCEDURE GetIngredients(IN id int)
BEGIN (
    SELECT ingredients_id from Contains WHERE Contains.recipe_id=id
);
END //
DELIMITER ;

Drop procedure if exists GetIngredientsInfo;
DELIMITER //
CREATE PROCEDURE GetIngredientsInfo(IN id int)
BEGIN (
    SELECT * from Ingredients WHERE Ingredients.ingredients_id=id
);
END //
DELIMITER ;

Drop procedure if exists GetInstructionsInfo;
DELIMITER //
CREATE PROCEDURE GetInstructionsInfo(IN id int)
BEGIN (
    SELECT * from Instructions WHERE Instructions.recipe_id=id
);
END //
DELIMITER ;


Drop procedure if exists GetDate;
DELIMITER //
CREATE PROCEDURE GetDate(IN id int)
BEGIN (
    SELECT upload_date from Uploads WHERE Uploads.recipe_id=id
);
END //
DELIMITER ;

Drop procedure if exists GetMealPlan;
DELIMITER //
CREATE PROCEDURE GetMealPlan()
BEGIN (
    SELECT * from Meal_plan
);
END //
DELIMITER ;

/*
drop table if exists Address;
create table Address(
    street_address varchar(255) not null,
    city varchar(50),
    zip_code varchar(20),
    country varchar(50),
    primary key(street_address)
);

drop table if exists Located_at;
create table Located_at(
    user_name varchar(100) not null,
    street_address varchar(255) not null,
    foreign key(user_name) references User(user_name) on delete cascade on update cascade,
    foreign key(street_address) references Address(street_address) on delete cascade on update cascade,
    primary key(user_name, street_address)
);

drop table if exists Nutrition;
create table Nutrition(
    nutrition_id int auto_increment not null,
    name varchar(100) not null,
    primary key(nutrition_id)
);


drop table if exists Provide;
create table Provide(
    ingredients_id int,
    nutrition_id int,
    foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,
    foreign key(nutrition_id) references Nutrition(nutrition_id) on delete cascade on update cascade,
    primary key(ingredients_id,nutrition_id)
);python

drop table if exists Outlines;
create table Outlines(
    recipe_id int not null,
    instruction_id int not null,
    foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,
    foreign key(instruction_id) references Instructions(instruction_id) on delete cascade on update cascade,
      primary key(recipe_id,instruction_id)
);
*/

insert into User(user_name, hash_password) values("Qlpavcniun.Nhuzuogg", "None");
insert into User(user_name, hash_password) values("Fuipmwqkwv.Neqecedpo", "None");
insert into User(user_name, hash_password) values("Dvmckm.Qjnfqcvm", "None");
insert into User(user_name, hash_password) values("Fzeklobgur.Tyich", "None");
insert into User(user_name, hash_password) values("Hinlhic.Hrgpt", "None");
insert into User(user_name, hash_password) values("Scill.Qlebqyinh", "None");
insert into User(user_name, hash_password) values("Uzphs.Ssxjk", "None");
insert into User(user_name, hash_password) values("Knpbhf.Erwiixfb", "None");
insert into User(user_name, hash_password) values("Psycfk.Muupmez", "None");
insert into User(user_name, hash_password) values("Tiosdou.Qkelfyqtir", "None");
insert into Measurements(unit) values("teaspoon");
insert into Measurements(unit) values("tablespoon");
insert into Measurements(unit) values("cup");
insert into Measurements(unit) values("pint");
insert into Measurements(unit) values("quart");
insert into Measurements(unit) values("gallon");
insert into Measurements(unit) values("pound");
insert into Measurements(unit) values("pinch");
insert into Measurements(unit) values("dash");
insert into Measurements(unit) values("ounces");
insert into Measurements(unit) values("scoop");
insert into Measurements(unit) values("ml");
insert into Measurements(unit) values("liter");
insert into Measurements(unit) values("gram");
insert into Measurements(unit) values("kilogram");
insert into Measurements(unit) values("inch");
insert into Measurements(unit) values("centimeter");
insert into Measurements(unit) values("F");
insert into Measurements(unit) values("C");
insert into Measurements(unit) values("stick");
insert into Measurements(unit) values("lemon");
insert into Measurements(unit) values("light cream");
insert into Measurements(unit) values("heavy cream");
insert into Measurements(unit) values("double cream");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Qlpavcniun", "Qlpavcniun.Nhuzuogg", "Nhuzuogg", "Qlpavcniun.Nhuzuogg@yahoo.com", "671-1483", "Zone", "Hypertension");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Fuipmwqkwv", "Fuipmwqkwv.Neqecedpo", "Neqecedpo", "Fuipmwqkwv.Neqecedpo@gmail.com", "227-5712", "Ketogenic", "Hypertension");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Dvmckm", "Dvmckm.Qjnfqcvm", "Qjnfqcvm", "Dvmckm.Qjnfqcvm@hotmail.com", "586-4413", "Weight Watchers", "Cancer");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Fzeklobgur", "Fzeklobgur.Tyich", "Tyich", "Fzeklobgur.Tyich@gmail.com", "516-1671", "Weight Watchers", "Diabetes");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Hinlhic", "Hinlhic.Hrgpt", "Hrgpt", "Hinlhic.Hrgpt@gmail.com", "155-6644", "Ketogenic", "Sickle Cell");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Scill", "Scill.Qlebqyinh", "Qlebqyinh", "Scill.Qlebqyinh@gmail.com", "431-4261", "Mediterranea", "Cancer");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Uzphs", "Uzphs.Ssxjk", "Ssxjk", "Uzphs.Ssxjk@outlook.com", "171-3194", "Mediterranea", "Sickle Cell");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Knpbhf", "Knpbhf.Erwiixfb", "Erwiixfb", "Knpbhf.Erwiixfb@yahoo.com", "859-7596", "Vegetarian", "Sickle Cell");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Psycfk", "Psycfk.Muupmez", "Muupmez", "Psycfk.Muupmez@gmail.com", "838-9315", "Atkins", "Sickle Cell");
insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) values("Tiosdou", "Tiosdou.Qkelfyqtir", "Qkelfyqtir", "Tiosdou.Qkelfyqtir@hotmail.com", "212-2324", "Raw food ", "Sickle Cell");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Uqtvpohlufnfwln",19,1,14,20,"Vegetarian");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Ukglqnud",33,74,48,11,"Vegetarian");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Wqtjrysesxj",42,86,22,53,"Mediterranea");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Gelmthqgxh",23,94,47,24,"Atkins");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Dvgmbsnqdyib",36,16,42,25,"Ketogenic");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Ltruihvievpgzr",82,74,16,18,"Ketogenic");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Xtaxurdbdalw",73,24,8,57,"South Beach");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Qululrugtqljsrk",8,25,16,43,"Weight Watchers");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Aopjlacteppr",92,3,4,30,"Atkins");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Ggpowuruxlm",19,22,53,31,"South Beach");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Sswghakvyofajnqh",39,46,0,55,"Mediterranea");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Wrnlpnluvrvjaaxz",59,53,35,47,"Vegetarian");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Ehmugcup",45,80,47,60,"Ketogenic");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Hmkwfpebehiajw",9,51,44,10,"South Beach");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Tdyniqjcksdp",49,97,19,13,"Mediterranea");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Ztunlhdaesta",34,18,42,22,"Vegan");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Bjztjqsew",14,84,29,32,"Vegan");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Qfwehkhuxsjmt",11,59,13,46,"Vegan");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Jjvshftgjbumizg",43,31,36,57,"Atkins");
insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) values("Wiwaeweerd",22,31,26,60,"South Beach");
insert into Uploads(user_name, recipe_id,upload_date) values("Qlpavcniun.Nhuzuogg",1,"7514-08-14");
insert into Uploads(user_name, recipe_id,upload_date) values("Qlpavcniun.Nhuzuogg",2,"3212-05-05");
insert into Uploads(user_name, recipe_id,upload_date) values("Fuipmwqkwv.Neqecedpo",3,"6662-06-04");
insert into Uploads(user_name, recipe_id,upload_date) values("Fuipmwqkwv.Neqecedpo",4,"9875-01-25");
insert into Uploads(user_name, recipe_id,upload_date) values("Dvmckm.Qjnfqcvm",5,"9157-04-16");
insert into Uploads(user_name, recipe_id,upload_date) values("Dvmckm.Qjnfqcvm",6,"5754-12-12");
insert into Uploads(user_name, recipe_id,upload_date) values("Fzeklobgur.Tyich",7,"4667-12-11");
insert into Uploads(user_name, recipe_id,upload_date) values("Fzeklobgur.Tyich",8,"6593-06-25");
insert into Uploads(user_name, recipe_id,upload_date) values("Hinlhic.Hrgpt",9,"7169-04-11");
insert into Uploads(user_name, recipe_id,upload_date) values("Hinlhic.Hrgpt",10,"7437-05-21");
insert into Uploads(user_name, recipe_id,upload_date) values("Scill.Qlebqyinh",11,"1558-05-25");
insert into Uploads(user_name, recipe_id,upload_date) values("Scill.Qlebqyinh",12,"6151-03-15");
insert into Uploads(user_name, recipe_id,upload_date) values("Uzphs.Ssxjk",13,"7362-11-25");
insert into Uploads(user_name, recipe_id,upload_date) values("Uzphs.Ssxjk",14,"1748-07-15");
insert into Uploads(user_name, recipe_id,upload_date) values("Knpbhf.Erwiixfb",15,"8346-02-14");
insert into Uploads(user_name, recipe_id,upload_date) values("Knpbhf.Erwiixfb",16,"4998-06-22");
insert into Uploads(user_name, recipe_id,upload_date) values("Psycfk.Muupmez",17,"3667-04-26");
insert into Uploads(user_name, recipe_id,upload_date) values("Psycfk.Muupmez",18,"3536-10-05");
insert into Uploads(user_name, recipe_id,upload_date) values("Tiosdou.Qkelfyqtir",19,"6949-12-26");
insert into Uploads(user_name, recipe_id,upload_date) values("Tiosdou.Qkelfyqtir",20,"5545-11-15");
insert into Kitchen(user_name) values("Qlpavcniun.Nhuzuogg");
insert into Kitchen(user_name) values("Fuipmwqkwv.Neqecedpo");
insert into Kitchen(user_name) values("Dvmckm.Qjnfqcvm");
insert into Kitchen(user_name) values("Fzeklobgur.Tyich");
insert into Kitchen(user_name) values("Hinlhic.Hrgpt");
insert into Kitchen(user_name) values("Scill.Qlebqyinh");
insert into Kitchen(user_name) values("Uzphs.Ssxjk");
insert into Kitchen(user_name) values("Knpbhf.Erwiixfb");
insert into Kitchen(user_name) values("Psycfk.Muupmez");
insert into Kitchen(user_name) values("Tiosdou.Qkelfyqtir");
insert into Meal(meal_name, meal_type, img_src) values("Krxvhpi","Weight Watchers","None");
insert into Meal(meal_name, meal_type, img_src) values("Dugzvjqrq","Atkins","None");
insert into Meal(meal_name, meal_type, img_src) values("Csrahfosvx","Weight Watchers","None");
insert into Meal(meal_name, meal_type, img_src) values("Uakc","Mediterranea","None");
insert into Meal(meal_name, meal_type, img_src) values("Gzpwli","South Beach","None");
insert into Meal(meal_name, meal_type, img_src) values("Carme","Atkins","None");
insert into Meal(meal_name, meal_type, img_src) values("Jpnsspagq","Mediterranea","None");
insert into Meal(meal_name, meal_type, img_src) values("Ydchztwln","Atkins","None");
insert into Meal(meal_name, meal_type, img_src) values("Dxgc","Vegetarian","None");
insert into Meal(meal_name, meal_type, img_src) values("Snxfnn","Zone","None");
insert into Meal_plan(week_num, calorie) values(25, 4053);
insert into Meal_plan(week_num, calorie) values(2, 983);
insert into Meal_plan(week_num, calorie) values(13, 4694);
insert into Meal_plan(week_num, calorie) values(24, 7580);
insert into Meal_plan(week_num, calorie) values(35, 1999);
insert into Instructions(recipe_id, task, instruction_order) values(1, "roll", 3),
(1, "prepare", 1),
(1, "bake", 3),
(1, "store", 1),
(2, "whisk", 2),
(2, "start", 4),
(2, "microwave", 3),
(3, "get", 3),
(3, "mix", 2),
(4, "blend", 1),
(4, "microwave", 1),
(4, "keep", 1),
(5, "roll out", 3),
(5, "roll", 1),
(5, "drain", 2),
(5, "grate", 1),
(6, "keep", 2),
(6, "blend", 3),
(7, "use", 2),
(7, "blend", 1),
(7, "barbeque", 4),
(7, "get", 3),
(8, "cut", 3),
(8, "fire up", 2),
(9, "stir-fry", 4),
(9, "stir", 1),
(10, "keep", 2),
(10, "strain", 2),
(10, "boil over", 2),
(11, "get", 4),
(11, "bake", 2),
(11, "bake", 4),
(11, "fry", 2),
(12, "grab", 3),
(12, "barbeque", 4),
(12, "roll out", 2),
(13, "whisk", 1),
(13, "start", 3),
(13, "whisk", 2),
(14, "grab", 1),
(14, "store", 3),
(14, "fry", 1),
(15, "stir", 1),
(15, "get", 2),
(15, "microwave", 3),
(15, "roll", 2),
(16, "use", 4),
(16, "microwave", 2),
(16, "fry", 2),
(16, "mix", 2),
(17, "fire up", 4),
(17, "drain", 2),
(17, "roast", 3),
(18, "hit", 3),
(18, "grate", 1),
(18, "drain", 1),
(19, "prepare", 2),
(19, "blend", 4),
(19, "strain", 3),
(20, "fry", 4);
insert into Contains(recipe_id, ingredients_id) values(1, 26);
insert into Contains(recipe_id, ingredients_id) values(1, 15);
insert into Contains(recipe_id, ingredients_id) values(1, 1);
insert into Contains(recipe_id, ingredients_id) values(1, 4);
insert into Contains(recipe_id, ingredients_id) values(2, 19);
insert into Contains(recipe_id, ingredients_id) values(2, 13);
insert into Contains(recipe_id, ingredients_id) values(2, 20);
insert into Contains(recipe_id, ingredients_id) values(2, 25);
insert into Contains(recipe_id, ingredients_id) values(3, 24);
insert into Contains(recipe_id, ingredients_id) values(3, 14);
insert into Contains(recipe_id, ingredients_id) values(3, 1);
insert into Contains(recipe_id, ingredients_id) values(3, 19);
insert into Contains(recipe_id, ingredients_id) values(4, 1);
insert into Contains(recipe_id, ingredients_id) values(4, 21);
insert into Contains(recipe_id, ingredients_id) values(4, 10);
insert into Contains(recipe_id, ingredients_id) values(4, 19);
insert into Contains(recipe_id, ingredients_id) values(5, 20);
insert into Contains(recipe_id, ingredients_id) values(5, 3);
insert into Contains(recipe_id, ingredients_id) values(5, 4);
insert into Contains(recipe_id, ingredients_id) values(5, 26);
insert into Contains(recipe_id, ingredients_id) values(6, 5);
insert into Contains(recipe_id, ingredients_id) values(6, 25);
insert into Contains(recipe_id, ingredients_id) values(6, 3);
insert into Contains(recipe_id, ingredients_id) values(6, 2);
insert into Contains(recipe_id, ingredients_id) values(7, 27);
insert into Contains(recipe_id, ingredients_id) values(7, 13);
insert into Contains(recipe_id, ingredients_id) values(7, 8);
insert into Contains(recipe_id, ingredients_id) values(7, 7);
insert into Contains(recipe_id, ingredients_id) values(8, 21);
insert into Contains(recipe_id, ingredients_id) values(8, 5);
insert into Contains(recipe_id, ingredients_id) values(8, 14);
insert into Contains(recipe_id, ingredients_id) values(8, 8);
insert into Contains(recipe_id, ingredients_id) values(9, 19);
insert into Contains(recipe_id, ingredients_id) values(9, 16);
insert into Contains(recipe_id, ingredients_id) values(9, 14);
insert into Contains(recipe_id, ingredients_id) values(9, 24);
insert into Contains(recipe_id, ingredients_id) values(10, 2);
insert into Contains(recipe_id, ingredients_id) values(10, 25);
insert into Contains(recipe_id, ingredients_id) values(10, 17);
insert into Contains(recipe_id, ingredients_id) values(10, 23);
insert into Contains(recipe_id, ingredients_id) values(11, 21);
insert into Contains(recipe_id, ingredients_id) values(11, 22);
insert into Contains(recipe_id, ingredients_id) values(11, 19);
insert into Contains(recipe_id, ingredients_id) values(11, 3);
insert into Contains(recipe_id, ingredients_id) values(12, 12);
insert into Contains(recipe_id, ingredients_id) values(12, 9);
insert into Contains(recipe_id, ingredients_id) values(12, 20);
insert into Contains(recipe_id, ingredients_id) values(12, 15);
insert into Contains(recipe_id, ingredients_id) values(13, 2);
insert into Contains(recipe_id, ingredients_id) values(13, 7);
insert into Contains(recipe_id, ingredients_id) values(13, 23);
insert into Contains(recipe_id, ingredients_id) values(13, 26);
insert into Contains(recipe_id, ingredients_id) values(14, 11);
insert into Contains(recipe_id, ingredients_id) values(14, 28);
insert into Contains(recipe_id, ingredients_id) values(14, 18);
insert into Contains(recipe_id, ingredients_id) values(14, 8);
insert into Contains(recipe_id, ingredients_id) values(15, 4);
insert into Contains(recipe_id, ingredients_id) values(15, 20);
insert into Contains(recipe_id, ingredients_id) values(15, 28);
insert into Contains(recipe_id, ingredients_id) values(15, 5);
insert into Contains(recipe_id, ingredients_id) values(16, 5);
insert into Contains(recipe_id, ingredients_id) values(16, 9);
insert into Contains(recipe_id, ingredients_id) values(16, 10);
insert into Contains(recipe_id, ingredients_id) values(16, 13);
insert into Contains(recipe_id, ingredients_id) values(17, 17);
insert into Contains(recipe_id, ingredients_id) values(17, 29);
insert into Contains(recipe_id, ingredients_id) values(17, 1);
insert into Contains(recipe_id, ingredients_id) values(17, 11);
insert into Contains(recipe_id, ingredients_id) values(18, 16);
insert into Contains(recipe_id, ingredients_id) values(18, 3);
insert into Contains(recipe_id, ingredients_id) values(18, 23);
insert into Contains(recipe_id, ingredients_id) values(18, 2);
insert into Contains(recipe_id, ingredients_id) values(19, 2);
insert into Contains(recipe_id, ingredients_id) values(19, 6);
insert into Contains(recipe_id, ingredients_id) values(19, 26);
insert into Contains(recipe_id, ingredients_id) values(19, 18);
insert into Contains(recipe_id, ingredients_id) values(20, 12);
insert into Contains(recipe_id, ingredients_id) values(20, 21);
insert into Contains(recipe_id, ingredients_id) values(20, 11);
insert into Contains(recipe_id, ingredients_id) values(20, 22);

insert into Creates(recipe_id, meal_id) values(1, 4);
insert into Creates(recipe_id, meal_id) values(2, 7);
insert into Creates(recipe_id, meal_id) values(3, 9);
insert into Creates(recipe_id, meal_id) values(4, 3);
insert into Creates(recipe_id, meal_id) values(5, 8);
insert into Creates(recipe_id, meal_id) values(6, 5);
insert into Creates(recipe_id, meal_id) values(7, 5);
insert into Creates(recipe_id, meal_id) values(8, 8);
insert into Creates(recipe_id, meal_id) values(9, 8);
insert into Creates(recipe_id, meal_id) values(10, 2);
insert into Creates(recipe_id, meal_id) values(11, 9);
insert into Creates(recipe_id, meal_id) values(12, 9);
insert into Creates(recipe_id, meal_id) values(13, 10);
insert into Creates(recipe_id, meal_id) values(14, 8);
insert into Creates(recipe_id, meal_id) values(15, 7);
insert into Creates(recipe_id, meal_id) values(16, 3);
insert into Creates(recipe_id, meal_id) values(17, 9);
insert into Creates(recipe_id, meal_id) values(18, 1);
insert into Creates(recipe_id, meal_id) values(19, 6);
insert into Creates(recipe_id, meal_id) values(20, 7);
insert into Stores(kitchen_id, ingredients_id, quantity) values(1, 2, 33);
insert into Stores(kitchen_id, ingredients_id, quantity) values(2, 2, 17);
insert into Stores(kitchen_id, ingredients_id, quantity) values(3, 26, 24);
insert into Stores(kitchen_id, ingredients_id, quantity) values(4, 8, 8);
insert into Stores(kitchen_id, ingredients_id, quantity) values(5, 11, 20);
insert into Stores(kitchen_id, ingredients_id, quantity) values(6, 3, 6);
insert into Stores(kitchen_id, ingredients_id, quantity) values(7, 7, 29);
insert into Stores(kitchen_id, ingredients_id, quantity) values(8, 10, 42);
insert into Stores(kitchen_id, ingredients_id, quantity) values(9, 9, 25);
insert into Stores(kitchen_id, ingredients_id, quantity) values(10, 9, 4);
