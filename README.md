from game_data import data
from art import logo, vs
import random
import os
print(logo)
length = len(data)
rand_num_A = random.randint(0,length - 1)
name = data[rand_num_A]["name"]
follower_a = data[rand_num_A]["follower_count"]
descrip = data[rand_num_A]["description"]
count = data[rand_num_A]["country"]
comp_a = f"Compare A: {name}, a {descrip}, from {count} {follower_a}"
print(comp_a)
print(vs)
rand_num_B = random.randint(0,length - 1)
name = data[rand_num_B]["name"]
follower_b = data[rand_num_B]["follower_count"]
descrip = data[rand_num_B]["description"]
count = data[rand_num_B]["country"]
comp_b =f"Compare B: {name}, a {descrip}, from {count} {follower_b}"
print(comp_b)
answer = input("Who has more follower? Type 'A' or 'B': ").lower()
if answer == "a" and follower_a > follower_b:
    os.system('cls')
    print(logo) 
    comp_a = f"Compare A: {name}, a {descrip}, from {count} {follower_a}"
    print(comp_a)
    rand_num_A = random.randint(0,length - 1)
    name = data[rand_num_A]["name"]
    follower_a = data[rand_num_A]["follower_count"]
    descrip = data[rand_num_A]["description"]
    count = data[rand_num_A]["country"]
    print(vs)
elif answer == "b" and follower_b > follower_a:
    os.system('cls')
    print(logo)
    comp_b =f"Compare A: {name}, a {descrip}, from {count} {follower_b}"
    print(comp_b)
    rand_num_B = random.randint(0,length - 1)
    name = data[rand_num_B]["name"]
    follower_b = data[rand_num_B]["follower_count"]
    descrip = data[rand_num_B]["description"]
    count = data[rand_num_B]["country"]
   
    print(vs)
else:
    print("You lost")
    
