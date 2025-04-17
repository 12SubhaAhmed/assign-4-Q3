import random

########### HANGMAN GAME #########

stages = ['''
    -------
    |     | 
    |     
    |
    |
    -------   
    ''', '''
    -------
    |     |
    |     O
    |     |
    |
    |
    --------
    ''', '''
    --------
    |      |
    |      O
    |     /|
    |
    |
    --------
    ''','''
    --------
    |      |
    |      O
    |     /|\\
    |
    |
    --------
    ''','''
    --------
    |      |
    |      O
    |     /|\\
    |     / 
    |
    --------
    ''','''
    --------
    |      |
    |      O
    |     /|\\
    |     / \\
    |
    --------
''']

words = ["red", "yellow", "orange", "purple", "blue", "pink", "white", "black", "grey", "green"]
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
guess_letter = []
lives = len(stages) - 1

print("\n\t ****** WELCOME TO HANGMAN GAME ****** \n")
print("Guess the color name:")

while True:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a valid single letter!\n")
        continue

    if guess in guess_letter:
        print("You already guessed that letter. Try again!\n")
        continue

    guess_letter.append(guess)

    if guess in chosen_word:
        print(f"✅ Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print(f"❌ Sorry, '{guess}' is not in the word.")
        print(stages[len(stages) - lives - 1])
        lives -= 1
        print(f"You have {lives} lives left.\n")

    if '_' not in word_display:
        print("\n🎉 Congratulations! You guessed the word:", chosen_word)
        break

    if lives == 0:
        print(stages[-1])
        print(f"\n💀 You lose! The word was \"{chosen_word}\".")
        break
