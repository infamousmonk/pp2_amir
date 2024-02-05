import random

def guess_the_number():
    print("Hello! What is your name?")
    player_name = input()
    
    print(f"Well, {player_name}, I am thinking of a number between 1 and 20.")
    
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        player_guess = int(input())
        attempts += 1

        if player_guess < secret_number:
            print("Your guess is too low.")
        elif player_guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {player_name}! You guessed my number in {attempts} guesses!")
            break
        
guess_the_number()
