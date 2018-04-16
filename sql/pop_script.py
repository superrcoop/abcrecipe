from pathlib import Path
from random import randint, choice
from future import print_function
ingredients_count = 4 #This is the number of ingredients in each recipe
instructions_count = 4 #This is the number of instructions in each recipe
num_users = 3 #This is the number of users. I used this in meal_plan and contructs
num_meal_plans = 4 * num_users #This is the number of meal plans for each user

def generate_db():
    create_db()
    create_user()
    create_profile()
    create_recipe()
    create_nutrition()
    create_ingredients()
    create_kitchen()
    create_meal()
    create_meal_plan()
    create_measurements()
    create_instructions()
    create_address()
    create_uploads()
    create_contains()
    create_stores()
    create_creates()
    create_constructs()
    create_requests()
    create_located_at()
    create_outlines()
    create_consists()
    create_provide()
    insert_user()
    insert_profile()
    insert_recipe()
    insert_nutrition()
    insert_ingredients()
    insert_kitchen()
    insert_meals()
    insert_meal_plan()
    insert_measurements()
    insert_instructions()
    insert_address()
    insert_uploads()
    insert_contains()
    insert_stores()
    insert_creates()
    insert_constructs()
    insert_requests()
    insert_located_at()
    insert_outlines()
    insert_consists()
    insert_provide()

def get_data(file_name):
    file = open(file_name,"r")
    data = []
    for line in file:
        data.append(line[:-1])
    file.close()
    return data

def insert_ingredients():
    ingredients = get_data("ingredients.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(ingredients)):
            sql_line = 'insert into Ingredients(name) values('+'"'+ingredients[index]+'"'+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(ingredients)):
            sql_line = "insert into Ingredients(name) values("+'"'+ingredients[index]+'"'+");\n"
            file.write(sql_line)
        file.close()

def insert_nutrition():
    nutritions = get_data("nutrition.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(nutritions)):
            sql_line = "insert into Nutrition(name) values("+'"'+nutritions[index]+'"'+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(nutritions)):
            sql_line = "insert into Nutrition(name) values("+'"'+nutritions[index]+'"'+");\n"
            file.write(sql_line)
        file.close()

def insert_provide():
    ingredients_num = num_records("ingredients.txt")
    nutritions_num = num_records("nutrition.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,ingredients_num):
            sql_line = "insert into Provide(ingredient_id, nutrition_id) values("+str((index+1))+", "+str(randint(1,nutritions_num))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,ingredients_num):
            sql_line = "insert into Provide(ingredient_id, nutrition_id) values("+str((index+1))+", "+str(randint(1,nutritions_num))+");\n"
            file.write(sql_line)
        file.close()

def insert_recipe():
    recipes = get_data("recipe.txt")
    file_path = Path("schema.sql")
    diets = get_data("diet.txt")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(recipes)):
            sql_line = "insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) "
            sql_line+="values("+'"'+recipes[index]+'"'+","+str(randint(0,100))+","+str(randint(0,100))+","+str(randint(0,60))+","+str(randint(0,60))+","+'"'+choice(diets)+'"'+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(recipes)):
            sql_line = "insert into Recipe(name, calorie, servings, cook_time, prep_time, diet_type) "
            sql_line+="values("+'"'+recipes[index]+'"'+","+str(randint(0,1000))+","+str(randint(0,100))+","+str(randint(0,60))+","+str(randint(0,60))+","+'"'+choice(diets)+'"'+");\n"
            file.write(sql_line)
        file.close()

def insert_contains():
    recipe_num = num_records("recipe.txt")
    file_path = Path("schema.sql")
    ingredients_num = num_records("ingredients.txt")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,recipe_num):
            seen = {}
            for counter in range(0,ingredients_count):
                sql_line = "insert into Contains(recipe_id, ingredients_id) "
                value_id = randint(1,ingredients_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,ingredients_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,recipe_num):
            seen = {}
            for counter in range(0,ingredients_count):
                sql_line = "insert into Contains(recipe_id, ingredients_id) "
                value_id = randint(1,ingredients_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,ingredients_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()

def insert_meals():
    meals = get_data("meal.txt")
    diets = get_data("diet.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(meals)):
            sql_line = "insert into Meal(meal_name, meal_type, img_src) "
            sql_line+="values("+'"'+meals[index]+'"'+","+'"'+choice(diets)+'"'+","+'"'+"None"+'"'+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(meals)):
            sql_line = "insert into Meal(meal_name, meal_type, img_src) "
            sql_line+="values("+'"'+meals[index]+'"'+","+'"'+choice(diets)+'"'+","+'"'+"None"+'"'+");\n"
            file.write(sql_line)
        file.close()

def insert_creates():
    meal_num = num_records("meal.txt")
    recipe_num = num_records("recipe.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,recipe_num):
            sql_line = "insert into Creates(recipe_id, meal_id) values("+str((index+1))+", "+str(randint(1,meal_num))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,recipe_num):
            sql_line = "insert into Creates(recipe_id, meal_id) values("+str((index+1))+", "+str(randint(1,meal_num))+");\n"
            file.write(sql_line)
        file.close()

def insert_outlines():
    recipe_num = num_records("recipe.txt")
    instruction_num = num_records("instructions.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,recipe_num):
            seen = {}
            for counter in range(0,instructions_count):
                sql_line = "insert into Outlines(recipe_id, instruction_id) "
                value_id = randint(1,instruction_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,instruction_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,recipe_num):
            seen = {}
            for counter in range(0,instructions_count):
                sql_line = "insert into Outlines(recipe_id, instruction_id) "
                value_id = randint(1,instruction_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,instruction_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()

def insert_measurements():
    measurements = get_data("measurement.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(measurements)):
            sql_line = "insert into Measurements(unit) "
            sql_line+="values("+'"'+measurements[index]+'"'+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(measurements)):
            sql_line = "insert into Measurements(unit) "
            sql_line+="values("+'"'+measurements[index]+'"'+");\n"
            file.write(sql_line)
        file.close()

def insert_instructions(): 
    instructions = get_data("instructions.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,len(instructions)):
            sql_line = "insert into Instructions(task, instruction_order) "
            sql_line += "values("+'"'+instructions[index]+'"'+str(randint(1,ingredients_count))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,len(instructions)):
            sql_line = "insert into Instructions(task) "
            sql_line += "values("+'"'+instructions[index]+'"'+str(randint(1,ingredients_count))+");\n"
            file.write(sql_line)
        file.close()

def num_records(filename):
    file = open(filename,"r")
    counter = 0
    for line in file:
        counter+=1
    return counter

def insert_consists():
    ingredients_num = num_records("ingredients.txt")
    measurement_num = num_records("measurement.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,ingredients_num):
            sql_line = "insert into Consists(ingredients_id, measure_id) "
            sql_line += "values("+str((index+1))+", "+str(randint(1,measurement_num))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,ingredients_num):
            sql_line = "insert into Consists(ingredients_id, measure_id) "
            sql_line += "values("+str((index+1))+", "+str(randint(1,measurement_num))+");\n"
            file.write(sql_line)
        file.close()
        
def insert_meal_plan():
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,num_meal_plans):
            sql_line = "insert into Meal_plan(week_num, calorie) "
            sql_line +="values("+str(randint(1,52))+", "+str(randint(1,10000))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,num_meal_plans):
            sql_line = "insert into Meal_plan(week_num, calorie) "
            sql_line +="values("+str(randint(1,52))+", "+str(randint(1,10000))+");\n"
            file.write(sql_line)
        file.close()
        
def insert_constructs():
    meal_num = num_records("meal.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql", "w")
        for index in range(0,num_meal_plans):
            seen = {}
            for counter in range(0,21):
                sql_line = "insert into Constructs(plan_id, meal_id) "
                value_id = randint(1,meal_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,meal_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql", "a")
        for index in range(0,num_meal_plans):
            seen = {}
            for counter in range(0,21):
                sql_line = "insert into Constructs(plan_id, meal_id) "
                value_id = randint(1,meal_num)
                found = seen.get(value_id,False)
                if not found:
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                    seen[value_id] = (index+1)
                else:
                    while found and seen[value_id] == (index+1):
                        value_id = randint(1,meal_num)
                        found = seen.get(value_id,False)
                    sql_line+="values("+str((index+1))+", "+str(value_id)+");\n"
                file.write(sql_line)
        file.close()

def insert_user():
    user_path = Path("user.txt")
    if user_path.is_file():
        user_file = open("user.txt","r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into User(user_name, hash_password) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+", "+'"'+"None"+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
        else:
            file = open("schema.sql","a")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into User(user_name, hash_password) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+", "+'"'+"None"+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
    else:
        print("File could not be found")

def insert_profile():
    user_path = Path("user.txt")
    if user_path.is_file():
        user_file = open("user.txt","r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            diets = get_data("diet.txt")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) "
                sql_line +="values("+'"'+name[0]+'"'+", "+'"'+name[0]+"."+name[1]+'"'+", "+'"'+name[1]+'"'+", "+'"'+"None"+'"'+", "+'"'+"None"+'"'
                sql_line +=", "+'"'+choice(diets)+'"'+", "+'"'+"None"+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
        else:
            file = open("schema.sql","a")
            diets = get_data("diet.txt")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Profile(first_name, user_name, last_name, email, phone, diet, health_info) "
                sql_line +="values("+'"'+name[0]+'"'+", "+'"'+name[0]+"."+name[1]+'"'+", "+'"'+name[1]+'"'+", "+'"'+"None"+'"'+", "+'"'+"None"+'"'
                sql_line +=", "+'"'+choice(diets)+'"'+", "+'"'+"None"+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
    else:
        print("File could not be found")

def insert_kitchen():
    user_path = Path("user.txt")
    if user_path.is_file():
        user_file = open("user.txt","r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Kitchen(user_name) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
        else:
            file = open("schema.sql","a")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Kitchen(user_name) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
    else:
        print("File could not be found")

def insert_stores():
    ingredients_num = num_records("ingredients.txt")
    file_path = Path("schema.sql")
    if not file_path.is_file():
        file = open("schema.sql","w")
        for index in range(0,num_users):
            sql_line = "insert into Stores(kitchen_id, ingredients_id, quantity) "
            sql_line += "values("+str((index+1))+", "+str(randint(1,ingredients_num))+", "+str(randint(1,50))+");\n"
            file.write(sql_line)
        file.close()
    else:
        file = open("schema.sql","a")
        for index in range(0,num_users):
            sql_line = "insert into Stores(kitchen_id, ingredients_id, quantity) "
            sql_line += "values("+str((index+1))+", "+str(randint(1,ingredients_num))+", "+str(randint(1,50))+");\n"
            file.write(sql_line)
        file.close()

def generate_date():
    #This generates a random date
    year = ""
    month = ""
    day = ""
    for count in range(0,4):
        year+=str(randint(1,9))
    day_value = randint(1,28)
    month_value = randint(1,12)
    if day_value < 10 :
        day = str("0")+str(day_value)
    else:
        day = str(day_value)
    if month_value < 10:
        month = str("0")+str(month_value)
    else:
        month = str(month_value)
    return year+"-"+month+"-"+day

def gen_ran_text(num):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for count in range(0,num):
        result+=alphabet[randint(0,25)]
    return result

def gen_ran_code(num):
    result = ""
    for count in range(num):
        result+=str(randint(1,9))
    return result

def random_address(num):
    file_path = Path("address.txt")
    file = open(file_path,"w")
    for count in range(0,num):
        line = gen_ran_text(25)+","+gen_ran_text(10)+","+gen_ran_code(4)+","+gen_ran_text(7)+"\n"
        file.write(line)
    file.close()

def insert_address():
    file_path = Path("schema.sql")
    address_path = Path("address.txt")
    if address_path.is_file():
        if not file_path.is_file():
            file = open("schema.sql","w")
            address_file = open(address_path,"r")
            for line in address_file:
                data = line.split(",")
                data[-1] = data[-1][:-1]
                sql_line = "insert into Address(street_address, city, zip_code, country) values("
                for count in range(0,len(data)):
                    if count == len(data)-1:
                        sql_line +='"'+data[count]+'"'+");\n"
                    else:
                        sql_line +='"'+data[count]+'"'+", "
                file.write(sql_line)
            file.close()
        else:
            file = open("schema.sql","a")
            address_file = open(address_path,"r")
            for line in address_file:
                data = line.split(",")
                data[-1] = data[-1][:-1]
                sql_line = "insert into Address(street_address, city, zip_code, country) values("
                for count in range(0,len(data)):
                    if count == len(data)-1:
                        sql_line +='"'+data[count]+'"'+");\n"
                    else:
                        sql_line +='"'+data[count]+'"'+", "
                file.write(sql_line)
            file.close()

def insert_located_at():
    user_path = Path("user.txt")
    if user_path.is_file():
        user_file = open("user.txt","r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Located_at(user_name, street_address) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+", "+'"'+gen_ran_text(25)+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
        else:
            file = open("schema.sql","a")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Located_at(user_name, street_address) "
                sql_line += "values("+'"'+name[0]+"."+name[1]+'"'+", "+'"'+gen_ran_text(25)+'"'+");\n"
                file.write(sql_line)
            file.close()
            user_file.close()
def insert_uploads():
    user_path = Path("user.txt")
    counter = 1
    if user_path.is_file():
        user_file = open("user.txt", "r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            recipe_num = num_records("recipe.txt")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Uploads(user_name, recipe_id) "
                if counter < recipe_num:
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(counter)+","+'"'+generate_date()+'"'+");\n"
                    counter += 1
                else:
                    counter = 1
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(counter)+","+'"'+generate_date()+'"'+");\n"
                    counter += 1
                file.write(sql_line)
            file.close()
        else:
            file = open("schema.sql","a")
            recipe_num = num_records("recipe.txt")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Uploads(user_name, recipe_id) "
                if counter < recipe_num:
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(counter)+","+'"'+generate_date()+'"'+");\n"
                    counter += 1
                else:
                    counter = 1
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(counter)+","+'"'+generate_date()+'"'+");\n"
                    counter += 1
                file.write(sql_line)
            file.close()
    else:
        print("File could not be found")

def insert_requests():
    user_path = Path("user.txt")
    counter = 1
    if user_path.is_file():
        user_file = open("user.txt", "r")
        file_path = Path("schema.sql")
        if not file_path.is_file():
            file = open("schema.sql","w")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Requests(user_name, plan_id) "
                if counter < num_meal_plans:
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(randint(counter*4,counter*4+4))+");\n"
                    counter += 1
                else:
                    counter = 1
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(randint(counter*4,counter*4+4))+");\n"
                    counter += 1
                file.write(sql_line)
            file.close()
        else:
            file = open("schema.sql","a")
            for line in user_file:
                name = line.split(" ")
                name[1] = name[1][:-1]
                sql_line = "insert into Requests(user_name, plan_id) "
                if counter < num_meal_plans:
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(randint(counter*4,counter*4+4))+");\n"
                    counter += 1
                else:
                    counter = 1
                    sql_line +="values("+'"'+name[0]+"."+name[1]+'"'+","+str(randint(counter*4,counter*4+4))+");\n"
                    counter += 1
                file.write(sql_line)
            file.close()
    else:
        print("File could not be found")

def create_db():
    file = open("schema.sql","w")
    file.write("drop database if exists abcrecipe;\n")
    file.write("create database abcrecipe;\n")
    file.write("use abcrecipe;\n")
    file.close()

def create_user():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists User;\n")
        file.write("create table IF NOT EXISTS User(\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("hash_password varchar(100) not null,\n\t")
        file.write("primary key(user_name)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_profile():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Profile;\n")
        file.write("create table IF NOT EXISTS Profile(\n\t")
        file.write("profile_id int auto_increment not null,\n\t")
        file.write("first_name varchar(100) not null,\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("last_name varchar(100) not null,\n\t")
        file.write("email varchar(100) not null UNIQUE,\n\t")
        file.write("phone varchar (255) not null,\n\t")
        file.write("diet varchar(20) not null,\n\t")
        file.write("health_info varchar(50) not null,\n\t")
        file.write("foreign key(user_name) references User(user_name) on delete cascade on update cascade,\n\t")
        file.write("primary key(profile_id)\n;\n")
        file.close()
    else:
        print("File was not found")
def create_recipe():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Recipe;\n")
        file.write("create table IF NOT EXISTS Recipe(\n\t")
        file.write("recipe_id int auto_increment not null,\n\t")
        file.write("name varchar(100) not null,\n\t")
        file.write("calorie decimal(7,2),\n\t")
        file.write("servings decimal(4,2),\n\t")
        file.write("cook_time varchar(100) not null,\n\t")
        file.write("prep_time varchar(100) not null,\n\t")
        file.write("diet_type varchar(100) not null,\n\t")
        file.write("primary key(recipe_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_nutrition():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Nutrition;\n")
        file.write("create table IF NOT EXISTS Nutrition(\n\t")
        file.write("nutrition_id int auto_increment not null,\n\t")
        file.write("name varchar(100) not null,\n\t")
        file.write("primary key(nutrition_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_ingredients():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Ingredients;\n")
        file.write("create table IF NOT EXISTS Ingredients(\n\t")
        file.write("ingredients_id int auto_increment not null,\n\t")
        file.write("name varchar(100) not null,\n\t")
        file.write("primary key(ingredients_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_kitchen():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Kitchen;\n")
        file.write("create table IF NOT EXISTS Kitchen(\n\t")
        file.write("kitchen_id int auto_increment not null,\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("foreign key(user_name) references User(user_name) on delete cascade on update cascade,\n\t")
        file.write("primary key(kitchen_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_meal():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Meal;\n")
        file.write("create table IF NOT EXISTS Meal(\n\t")
        file.write("meal_id int auto_increment not null,\n\t")
        file.write("name varchar(100) not null,\n\t")
        file.write("meal_type varchar(100) not null,\n\t")
        file.write("img_src varchar(255) not null,\n\t")
        file.write("primary key(meal_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_meal_plan():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Meal_plan;\n")
        file.write("create table IF NOT EXISTS Meal_plan(\n\t")
        file.write("plan_id int auto_increment not null,\n\t")
        file.write("week_num int not null,\n\t")
        file.write("calorie decimal(7,2) not null,\n\t")
        file.write("primary key(plan_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_measurements():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Measurements;\n")
        file.write("create table IF NOT EXISTS Measurements(\n\t")
        file.write("measure_id int auto_increment not null,\n\t")
        file.write("unit varchar(50) not null,\n\t")
        file.write("primary key(measure_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_instructions():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Instructions;\n")
        file.write("create table IF NOT EXISTS Instructions(\n\t")
        file.write("instruction_id int auto_increment not null,\n\t")
        file.write("task varchar(255) not null,\n\t")
        file.write("instruction_order int not null,\n\t")
        file.write("primary key(instruction_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_address():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Address;\n")
        file.write("create table IF NOT EXISTS Address(\n\t")
        file.write("street_address varchar(255) not null,\n\t")
        file.write("city varchar(50),\n\t")
        file.write("zip_code varchar(20),\n\t")
        file.write("country varchar(50),\n\t")
        file.write("primary key(street_address)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_uploads():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Uploads;\n")
        file.write("create table IF NOT EXISTS Uploads(\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("recipe_id int not null,\n\t")
        file.write("upload_date date not null,\n\t")
        file.write("foreign key(user_name) references User(user_name) on delete cascade on update cascade,\n\t")
        file.write("foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(user_name,recipe_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_contains():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Contains;\n")
        file.write("create table IF NOT EXISTS Contains(\n\t")
        file.write("recipe_id int not null,\n\t")
        file.write("ingredients_id int not null,\n\t")
        file.write("foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(recipe_id, ingredients_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_stores():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Stores;\n")
        file.write("create table IF NOT EXISTS Stores(\n\t")
        file.write("kitchen_id int not null,\n\t")
        file.write("ingredients_id int not null,\n\t")
        file.write("quantity int,\n\t")
        file.write("foreign key(kitchen_id) references Kitchen(kitchen_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(kitchen_id, ingredients_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_creates():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Creates;\n")
        file.write("create table IF NOT EXISTS Creates(\n\t")
        file.write("recipe_id int not null,\n\t")
        file.write("meal_id int not null,\n\t")
        file.write("foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(recipe_id, meal_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_constructs():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Constructs;\n")
        file.write("create table IF NOT EXISTS Constructs(\n\t")
        file.write("plan_id int not null,\n\t")
        file.write("meal_id int not null,\n\t")
        file.write("foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(meal_id) references Meal(meal_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(plan_id, meal_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_requests():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Requests;\n")
        file.write("create table IF NOT EXISTS Requests(\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("plan_id int not null,\n\t")
        file.write("foreign key(plan_id) references Meal_plan(plan_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(user_name) references User(user_name) on delete cascade on update cascade,\n\t")
        file.write("primary key(user_name, meal_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_located_at():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Located_at;\n")
        file.write("create table IF NOT EXISTS Located_at(\n\t")
        file.write("user_name varchar(100) not null,\n\t")
        file.write("street_address varchar(255) not null,\n\t")
        file.write("foreign key(street_address) references Address(street_address) on delete cascade on update cascade,\n\t")
        file.write("foreign key(user_name) references User(user_name) on delete cascade on update cascade,\n\t")
        file.write("primary key(user_name, street_address)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_outlines():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Outlines;\n")
        file.write("create table IF NOT EXISTS Outlines(\n\t")
        file.write("recipe_id int not null,\n\t")
        file.write("instruction_id int not null,\n\t")
        file.write("foreign key(recipe_id) references Recipe(recipe_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(instruction_id) references Instructions(instruction_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(recipe_id, instruction_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_consists():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Consists;\n")
        file.write("create table IF NOT EXISTS Consists(\n\t")
        file.write("ingredients_id int not null,\n\t")
        file.write("measure_id int not null,\n\t")
        file.write("foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(measure_id) references Measurements(measure_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(ingredients_id, measure_id)\n);\n")
        file.close()
    else:
        print("File was not found")
def create_provide():
    file_path = Path("schema.sql")
    if file_path.is_file():
        file = open(file_path,"a")
        file.write("drop table if exists Provide;\n")
        file.write("create table IF NOT EXISTS Provide(\n\t")
        file.write("ingredients_id int not null,\n\t")
        file.write("nutrition_id int not null,\n\t")
        file.write("foreign key(ingredients_id) references Ingredients(ingredients_id) on delete cascade on update cascade,\n\t")
        file.write("foreign key(nutrition_id) references Nutrition(nutrition_id) on delete cascade on update cascade,\n\t")
        file.write("primary key(ingredients_id, nutrition_id)\n);\n")
        file.close()
    else:
        print("File was not found")
