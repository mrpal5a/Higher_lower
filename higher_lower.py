from game_data import data
from art import logo, vs
import random
import os
def account_details(account):
    name = account["name"]
    country = account["country"]
    description = account["description"]
    return f"{name} a {description} from {country}"

def higher_score(user_guess,follower_a,follower_b):
    if follower_a > follower_b:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
b = random.choice(data)
is_continue = True
while is_continue:
    print(logo)
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print("Compare A :", account_details(a))
    print(vs)
    print("Against B :", account_details(b))

    account_a_followers = a["follower_count"]
    account_b_followers = b["follower_count"]
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = higher_score(user_guess=user_guess, follower_a= account_a_followers, follower_b= account_b_followers)
    if is_correct:
        score += 1
        os.system("cls")
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_continue = False