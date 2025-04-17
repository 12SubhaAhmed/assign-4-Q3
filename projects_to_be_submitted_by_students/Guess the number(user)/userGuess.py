import random

def user_guessing_game():
    print("\n\t******* WELCOME TO NUMBER GUESSING GAME ******\n")
    print("Try to guess the number I'm thinking of between 1 and 10!")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please guess a number between 1 and 10.")
                continue

            if guess == secret_number:
                print(f"🎉 Correct! You guessed it in {attempts} tries!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == '__main__':
    user_guessing_game()
