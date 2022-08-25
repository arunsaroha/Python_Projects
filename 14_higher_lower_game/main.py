from art import logo
from art import vs
from game_data import data
import random
# from replit import clear


def game():
    a = len(data)
    A = random.randint(0, a-1)
    game_over = False
    score = 0
    correct = False
    while not game_over:
        # clear()
        print(logo)
        B = random.randint(0, a-1)
        if correct == True:
            print(f"You're right! Current score: {score}")

        print(
            f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}")
        print(vs)
        print(
            f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}")

        followers = input("Who has more followers? Type 'A' or 'B': ").lower()
        if followers == "a":
            if data[A]['follower_count'] > data[B]['follower_count']:
                score += 1
                correct = True
                A = B
            else:
                correct = False
                game_over = True
                print(f"Sorry, that's wrong. Final score = {score}")

        elif followers == "b":
            if data[A]['follower_count'] < data[B]['follower_count']:
                score += 1
                correct = True
                print(f"You're right! Current score: {score}")
                A = B
            else:
                correct = False
                game_over = True
                print(f"Sorry, that's wrong. Final score = {score}")


game()
