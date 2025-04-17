import random
print("\n\t ****** WELCOME TO ROCK, PAPER, SCISSORS GAME ******")

choices = ["rock", "paper", "scissor" ]
user_score = computer_score = 0
print("Let's play!")

while True:
    user_input = input("Type Rock, Paper, Scissor or Q to quit: ").lower()
    if user_input == 'q':
        print(f'Final score - you: {user_score}, computer: {computer_score}')
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid input!")
        continue
    computer_choice = random.choice(choices)
    print(f'Computer choose {computer_choice}.')
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_choice == 'scissor') or \
           (user_input == 'paper' and computer_choice == 'rock') or \
           (user_input == 'scissor' and computer_choice == 'paper'):
        print("You win!")
        user_score +=1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f'Current score - You: {user_score}, Computer: {computer_score}.')



