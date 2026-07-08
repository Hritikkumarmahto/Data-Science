import random

game_items = ["rock", "paper", "scissors"]

def play_game(user_choice, countUser, computerCount):
    computer_choice = random.choice(game_items)
    
    print("=========================================")
    print("     Computer: " + computer_choice.upper())
    print("     You:      " + user_choice.upper())
    print("-----------------------------------------")

    if computer_choice == user_choice:
        print("              IT'S A TIE!        ")
        countUser += 1
        computerCount += 1
    elif computer_choice == "scissors" and user_choice == "rock":
        print("          YOU WON!  ")
        countUser += 1
    elif computer_choice == "scissors" and user_choice == "paper":
        print("          BETTER LUCK NEXT TIME.  ")
        computerCount += 1
    elif computer_choice == "rock" and user_choice == "paper":
        print("          YOU WON!  ")
        countUser += 1
    elif computer_choice == "rock" and user_choice == "scissors":
        print("          BETTER LUCK NEXT TIME.  ")
        computerCount += 1
    elif computer_choice == "paper" and user_choice == "rock":
        print("          BETTER LUCK NEXT TIME.  ")
        computerCount += 1
    elif computer_choice == "paper" and user_choice == "scissors":
        print("          YOU WON! EXTRAORDINARY!  ")
        countUser += 1
    else:
        print("       INVALID CHOICE! GO PLAY CRICKET.  ")

    print("=========================================\n")
    return countUser, computerCount

i = 0
print("""
Enter your selection
      1. rock
      2. paper
      3. scissors
      """)

countUser = 0
computerCount = 0

while i < 3:
    user_choice = input(f"Round {i+1} started choose (rock/paper/scissors): ").lower()
    countUser, computerCount = play_game(user_choice, countUser, computerCount)
    i += 1

user_final_score = countUser
computer_final_score = computerCount

print("=========================================")
print("               FINAL RESULT         ")
print("=========================================")
if user_final_score > computer_final_score:
    print(f"         You Won hurrah!!!! Score: {user_final_score}")
    print(f"         Computer score: {computer_final_score}")
elif user_final_score == computer_final_score:  
    print(f"         Tie !!! Score: {computer_final_score}")
else:
    print(f"         Computer won. Score: {computer_final_score}")
    print(f"         Your Score: {user_final_score}")
print("=========================================")


