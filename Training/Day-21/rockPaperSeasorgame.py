import random

game_items = ["rock", "paper", "scissors"]

def play_game():
    print("""
Enter your selection
      1. rock
      2. paper
      3. scissors
      """)
    
    user_choice = input("Enter your choice by typing (rock/paper/scissors): ").lower()
    
    computer_choice = random.choice(game_items)
    print(f"Computer chose: {computer_choice}")

    if computer_choice == user_choice:
        print("Tie!")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Better luck next time.")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Better luck next time.")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Better luck next time.")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
    else:
        print("Invalid choice! Go play cricket.")

while True:
    play_game()
    retry = input("\nDo you want to play again? (y/n): ").lower()
    if retry != 'y':
        print("Thank you for playing!")
        break
