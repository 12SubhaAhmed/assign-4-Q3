import random

print("\n\t******* WELCOME TO NUMBER GUESSING GAME ******\n\t")

low = 1
high = 10

print("Think of a number between 1 to 10 and the computer will guess it!\n\t")

if low <= high:
    guess = random.randint(low, high)
    print("Computer guesses the number:", guess)

    while True:
        feedback = input("Is the guess too high (H), too low (L), or correct (C): ").strip().upper()

        if feedback == 'C':
            print("Yayy! The computer guessed your number 🎉")
            break
        elif feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
        else:
            print("Invalid input. Please enter H, L, or C.")
            continue

        if low > high:
            print("Hmm... Something doesn't add up! Did you give correct feedback? 🤔")
            break

        guess = random.randint(low, high)
        print("Computer's guess is:", guess)
