import random

def play_game():
    # take input from user about range of numbers
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    # define number of guesses allowed
    num_guesses = 7
    print("You have only 7 chances to guess the integer!")
    # generate random number within range
    secret_num = random.randint(min_num, max_num)
    
    while num_guesses > 0:
        # prompt user to input guess and validate input
        guess = input(f"Guess a number between {min_num} and {max_num}: ")
        if guess.isnumeric() and min_num <= int(guess) <= max_num:
            guess = int(guess)
            num_guesses -= 1
            # compare guess with secret number and provide feedback
            if guess == secret_num:
                print("Congratulations, you guessed the number!")
                break
            elif guess > secret_num:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
            # provide feedback on number of guesses remaining
            print(f"You have {num_guesses} guesses left.")
        else:
            print("Invalid input. Please enter a valid integer within the range.")
    else:
        # if user has used up all guesses
        print(f"Sorry, you ran out of guesses. The secret number was {secret_num}.")
    
    # ask user if they want to play again
    play_again = input("Do you want to play again? (Y/N) ")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")
play_game()