import random


def print_header():
    print("Welcome to the HI - LO game!")
    
    ## testing out branch behaviour
    # added after comment in testing_branch, let's see how this goes
    # this is the 3rd comment



def game(ans):
    try:
        guess = int(input("Guess a number between 1 & 100: "))
        ans_checker(guess)
    except (TypeError, ValueError):
        guess = int(input("Invalid input, please try again! \nGuess a number between 1 & 100: "))
        ans_checker(guess)


def ans_checker(guess):
    if guess == ans:
        print(f"Congratulations, you got it! The number is {ans}. :)")
    elif guess > ans:
        print("Too high!")
        game(ans)
    elif guess < ans:
        print("Too low!")
        game(ans)
    else:
        "Something's wrong. Shutting down the game. Please try again later."


if __name__ == '__main__':
    print_header()
    ans = random.randint(1, 100)
    game(ans)
