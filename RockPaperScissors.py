import random        

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    print(f"Your score: {user_wins}\nComputer score: {computer_wins}")
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid input.")
        continue
    
    computer_pick = options[random.randint(0, 2)]   #Rock: 1, Paper: 2, Scissors: 3
    if user_input == "rock" and computer_pick == "scissors":
        print (f"You chose {user_input} and the computer picked {computer_pick}.\nYou win!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print (f"You chose {user_input} and the computer picked {computer_pick}.\nYou win!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print (f"You chose {user_input} and the computer picked {computer_pick}.\nYou win!")
        user_wins += 1
        continue
    else:
        print (f"You chose {user_input} and the computer picked {computer_pick}.\nYou lose!")
        computer_wins += 1
        continue

raise SystemExit