import random

secretNumber = random.randint(1, 20)
guess = None
print("Guess a number between 1 and 20.\nYou have 6 guesses in total.")

for i in range (1, 7):
    while secretNumber != guess:
        try:
            print(f"Guess number {i}: ", end="")
            guess = int(input())

            if guess < secretNumber:
                print("The number is too low.")
                break
            elif guess > secretNumber:
                print("The number is too high.")
                break
            else:
                break
        except:
            print("The input is invalid. Try again.")

try:
    if guess == secretNumber:
        print("Congrats! You guessed the number.")
    else:
        print(f"Better luck next time! The number was {secretNumber}.")
except:
    print(f"Better luck next time! The number was {secretNumber}.")
