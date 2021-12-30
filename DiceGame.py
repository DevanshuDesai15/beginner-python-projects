import random

while True:
    # GIVING OPTIONS
    print(''' 1. Yay!!! Enjoying then roll the dice...                 
    2. Awww... If bored you can.....Quit''')
    user= int(input("Through which option do you want to go??"))
    # USED TO GET A RANDOM NUMBER ON THE DICE
    if user==1:
        number = random.randint(1,6)
        print(number)
    # THE GAME WILL STOP
    else:
        break