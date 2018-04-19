#!/usr/bin/python
from __future__ import print_function
from faker import Factory
from random import randint, choice, sample
import pymysql.cursors
import pymysql
import hashlib

fake = Factory.create('en_US')
diets = ["Atkins", "Vegetarian", "Vegan", "Normal"]
health=["Diabetic","Normal","Hypertensive","Hypotensive"]

class Database:
    def __init__(self, host = 'localhost', user = 'root', password = 'mackeba', db = 'project'):
        self.db = pymysql.connect(host = host, user = user, password = password, db = db)

        # I'm just creating random variables 
        self.created_users = list()
        self.people_count = 50

    def destroy(self):
        self.db.close()

    def execute(self, query):
        self.db.cursor().execute(query)
        self.db.commit()


def create_users(db):
    print ("GENERATING THE USERS FOR THE DATABASE!!")

    for i in xrange(db.people_count):
        username = fake.user_name()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = first_name.lower() + "_" + last_name.lower() + str(randint(1, 30)) + "@faker.com"
        phone = "+1 (876) " + fake.numerify('###-####')
        diet_type=choice(diets)
        health_info=choice(health)
        password = hashlib.md5(fake.password()).hexdigest()
        
        if username not in db.created_users:
            db.created_users.append(username)
            db.execute("INSERT INTO Person VALUES('"+username+"', '"+email+"', '"+first_name+"', '"+last_name+"', '"+phone+"','"+diet_type+"','"+health_info+"');")
            db.execute("INSERT INTO User VALUES('"+username+"','"+password+"');")
     
        else:
            i -= 1

    print ("DONE CREATING USERS")
    print ("")

if __name__ == '__main__':
    db = Database()

    # dropping the tables if exist
    db.execute("DROP TABLE IF EXISTS User;")
    db.execute("DROP TABLE IF EXISTS Person;")

    # creating a table called person
    db.execute("CREATE TABLE Person(username VARCHAR(30) NOT NULL PRIMARY KEY, email VARCHAR(60) NOT NULL, first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30) NOT NULL, phone VARCHAR(20) NOT NULL, diet VARCHAR(30) NOT NULL, health_info VARCHAR(30) NOT NULL);")

    # adding an admin user to the database
    db.execute("INSERT INTO Person VALUES('admin',' admin@email.com', 'Administrator', 'Person', '+1 (876) 555-5555', 'Hungry', 'Healthy')")

    db.execute("CREATE TABLE User(user_name VARCHAR(30) NOT NULL PRIMARY KEY, hash_password VARCHAR(90), FOREIGN KEY(user_name) REFERENCES Person(username) ON DELETE CASCADE);")
    #adminpassword hashed to md5
    adminpassword = hashlib.md5("adminpassword").hexdigest()
    db.execute("INSERT INTO User VALUES('admin', '"+adminpassword+"');")


    create_users(db)
    # ending the connection
    # db.destroy()



# 
# 
# 
# PEOPLE_COUNT = 10
# RECIPE_COUNT = 10
# INGREDIENT_COUNT = 10
# 
# lst = []

# health=["Diabetic","Normal","Hypertensive","Hypotensive"]
# ##alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N", "N", "O", "P", "Q",
# ####         "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# ingredient_type = ["Fruits", "Vegetables", "Grains", "Beans", "Wheat", "Meat", "Dairy", "Sauce", "Seasoning"]
# minutes = ["10", "20", "30", "40", "50", "60", "80", "120", "180"]
# directions = "This text was generated as a dummy text for testing purposes only."
# quantity_type = ["pound", "pinch", "tablespoon", "cup", "teaspoon", " "]
# mealType = ["Breakfast", "Lunch", "Dinner", "Snack"]
# image_link = "http://bit.ly/1UTRyAF"
# dates = {1: [3, 10, 17, 24, 31], 2: [7, 14, 21, 28], 3: [6, 13, 20, 27], 4: [3, 10, 17, 24]}

# ing = ['rice', 'lime-juice', 'coffee-powder', 'bananas', 'mushrooms', 'vinegar',
#        'flour', 'eggs', 'salmon', 'pepper', 'chocolate', 'onions',
#        'couscous', 'lemon-grass', 'garlic', 'oregano', 'marinade', 'cheddar', 'peanut',
#        'broccoli', 'lime-leaves', 'lime', 'butter', 'chilli', 'yoghurt', 'clementines', 'falafels',
#        'lettuce', 'asparagus', 'vanilla', 'water', 'prawns', 'sugar', 'basil', 'baking-powder', 'bread','crackers','fish-sauce',
#        'coconut-milk', 'dip', 'pomegranate', 'tomatoes', 'stock','sugar','coconut oil','olive oil','baking soda',
#        'salt','parsley','chicken','beef','shrimp','walnuts','parmesean','bacon','strawberries','oranges','cherries']


# # def generate_diet_types():
# #     diets_ = []
# #     f = open('sql/diet.sql', 'a')
# #     print("Do not shut down!!!")
# #     x = 'CREATE TABLE diet_types(id INT PRIMARY KEY AUTO_INCREMENT, type_name VARCHAR(80) NOT NULL);\n'
# #     f.write(x)
# #     v = 1
# #     for i in diets:
# #         x = 'INSERT INTO diet_types(type_name) VALUES("' + i + '");\n'
# #         f.write(x)
# #         diets_.append(v)
# #         v += 1
# #     f.close()
# #     print("Finished")
# #     return diets_


# def generate_people():
#     account_list = []
#     phone_list = []
#     f = open("sql/people.sql", 'w')
#     print("Do not shut Down!!!!!!!!!")
    
#     x = "CREATE TABLE Person(username VARCHAR(30) NOT NULL PRIMARY KEY, email VARCHAR(60) NOT NULL, first_name VARCHAR(30) NOT NULL, last_name VARCHAR(30) NOT NULL, phone VARCHAR(11) NOT NULL, diet VARCHAR(30) NOT NULL, health_info VARCHAR(30) NOT NULL);\n"
#     f.write(x)
#     for i in range(PEOPLE_COUNT):
#         # account info
        # first_name = fake.first_name()
        # last_name = fake.last_name()
        # email = first_name.lower() + "_" + last_name.lower() + str(randint(1, 30)) + "@faker.com"
        # password = fake.password()
        # username = fake.user_name()
        # phone_num = "+1 (876) " + fake.numerify('###-####')
        # diet_type=choice(diets)
        # health_info=choice(health)
        # if username not in account_list and phone_num not in phone_list:
        #     account_list.append(username)
        #     phone_list.append(phone_num)

        #     x = 'INSERT INTO Profile (first_name,last_name,user_name,email,phone,diet,health_info) VALUES("' + first_name + '","' + username.lower() + '","' + last_name + '","' + email + '","' + diet_type + '","' + health_info + '");\n'

        #     f.write(x)
        #     x = 'INSERT INTO User (user_name,hash_password) VALUES("' + username.lower() + '","' + password + '");\n'
        #     f.write(x)
        #     # phone info        
        # else:
        #     i -= 1

#     f.close()

#     print("Task Finished")
#     return account_list


# # def generate_ingredient_list():
# #     ingredient__list = []
# #     f = open('sql/ingredients.sql', 'a')
# #     c = 372639
# #     x = "CREATE TABLE ingredients_list(rec_id INT PRIMARY KEY, name VARCHAR(80) NOT NULL);\n"
# #     f.write(x)

# #     for i in ing:
# #         x = "INSERT INTO ingredients_list VALUES(" + str(c) + ",'" + i + "');\n"
# #         ingredient__list.append(i)
# #         c += 1
# #         f.write(x)
# #     return ingredient__list


# if __name__ == '__main__':

#     account_lists = generate_people()
#     # diet_list = generate_diet_types()
#     # match_people_to_diet(account_lists, diet_list)
#     # #
#     # ingredient_list = generate_ingredient_list()
#     # # recipe_list = generate_recipe_list()

#     # """
#     # drop database if exists comp3161;
#     # create database comp3161;
#     # use comp3161
#     # """s