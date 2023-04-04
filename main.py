import random

first_names = ["John", "Charlie", "Bob", "Bill", "Mylie", "Sophia", "Isabella", "Ruby"]
last_names = ["Porter", "Hernandez", "Carter", "Brown", "Gonzalez", "Gill"]

road_nums = ["123", "231", "451", "Johnson", "Lincoln", "127"]
road_type = ["Blvd", "Ave", "St", "Rd"]

height = ["5ft", "5'5ft", "6ft", "6'4ft", "5'8", "5'7", "5'11"]
weight = random.randint(100, 215)

print("Building Human...")

first_name_choice = random.choice(first_names)
last_name_choice = random.choice(last_names)

road_num_choice = random.choice(road_nums)
road_type_choice = random.choice(road_type)

height_choice = random.choice(height)

print(first_name_choice + " " + last_name_choice + ", " + road_num_choice + "" + road_type_choice + ", " + height_choice + ", " + str(weight)+ "lbs.")