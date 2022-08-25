import random as r


def game():
    num = r.randint(1, 100)
    print(f"Number chosen --- {num}")
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff == "easy":
        attempts = 10
        print(f"You have a total of {attempts} attempts for {diff} level.")
    elif diff == "hard":
        attempts = 5
        print(f"You have a total of {attempts} attempts for {diff} level.")
    else:
        print("Please enter correct input. ")
        exit(0)

    def wrong_guess():
        print("Guess again.")
        print(f"You have {attempts} attempts remaining to guess the number.")

    while(attempts > 0):
        guess = int(input("Make a guess: "))
        if guess < num:
            attempts -= 1
            print("Too Low.")
            wrong_guess()
        elif guess > num:
            attempts -= 1
            print("Too High.")
            wrong_guess()
        elif guess == num:
            print("CORRECT GUESS (: CONGRATS :) ")
            break

    else:
        print("You have run out of guesses, ): You lose :( ")


game()
