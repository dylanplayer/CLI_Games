# Import random
from random import *

# Initialize colors
green = '\033[92m'
red = '\033[93m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
game_state = True
user_wins = 0
user_losses = 0

# Loop the game unitl user tells it to end
while(game_state):

    # Get computer choice
    choices = ["Bear", "Ninja", "Cowboy"]
    computer_choice = choices[randint(0, len(choices) - 1)]

    # Get user choice
    user_choice = input(f"{blue}Bear, Ninja, or Cowboy: {magenta}")

    # Win and Loss strings
    lose_str = f"{red}You lost {computer_choice.title()} beats {user_choice.title()}"
    win_str = f"{green}You won {user_choice.title()} beats {computer_choice.title()}"

    # Game logic
    if(user_choice.lower() == computer_choice.lower()):
        print("Draw")
    elif(computer_choice.lower() == "cowboy"):
        if(user_choice.lower() == "bear"):
            user_losses += 1
            print(lose_str)
        elif(user_choice.lower() == "ninja"):
            user_wins += 1
            print(win_str)
    elif(computer_choice.lower() == "bear"):
        if(user_choice.lower() == "ninja"):
            user_losses += 1
            print(lose_str)
        elif(user_choice.lower() == "cowboy"):
            user_wins += 1
            print(win_str)
    elif(computer_choice.lower() == "ninja"):
        if(user_choice.lower() == "cowboy"):
            user_losses += 1
            print(lose_str)
        elif(user_choice.lower() == "bear"):
            user_wins += 1
            print(win_str)
    else:
        print(f"{red}Invalid Entry")
    
    if(input(f"{magenta}Do you want to quit (yes/no): ").lower() == "yes"):
        break


win_loss_ratio = user_wins / user_losses
print(f"Your win loss ratio is: {win_loss_ratio}")
