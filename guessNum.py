import random
# THIS FUNCTION WILL AUTOMATICALLY GIVE A RANDOM NUMBER
number=random.randint(1,10)
print("Player will get 3 chances for guessing the right number... GO FOR IT!!!")

for i in range(0,3):
    # USER INPUT
    user=int(input("Start gussing number between 1-10: "))
    # IF THE NUMBER GUESSED IS CORRECT...
    if user==number:
        print("WOW Great Job!!!")
        print(f"Amazing on gussing the number {number}")
        break
    # HERE ELSE IS NOT USED BECAUSE IT CREATES A LOOP....
    # LIKE THIS WHOLE FOR LOOP RUNS 
    # BUT IF ANOTHER "IF" IS USED OUTSIDE OF FOR LOOP THEN IT WON'T PRINT THE WHOLE FOR LOOP FOR USER
# IF NUMBER GUESSED IS WRONG...
if user!= number:
        print(f"Sorry you guessed the wrong number... it's actually {number}")