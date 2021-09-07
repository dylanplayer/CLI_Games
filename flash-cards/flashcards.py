import json

with open('flash-cards/me-capitals.json', 'r') as f:
    data = json.load(f)

green = '\033[92m'
red = '\033[93m'
blue = '\u001b[34m'

for i in data["Cards"]:
    print(blue,i["q"])
    guess = input(f"{blue}Guess: ")
    if(guess.title() == i["a"].title()):
        print(f"{green}✔ correct!")
    else:
        print(f"{red}x answer: " + i["a"])