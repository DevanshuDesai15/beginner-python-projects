import random

# ASKING USER FOR LENGTH
passwordLength=int(input("Enter how much length of password do you want? "))
# THE CHARACTERS USED FOR CREATING THE PASSWORD
passwordCharacters="abcdefghijklmnopqrstuvwxyz0123456789ABCDWFGHIJKLMNOPQRSTUVWXYZ!@#$%&?_"
# FOR GENERATING A RANDOM PASSWORD
generator="".join(random.sample(passwordCharacters, passwordLength))
# PRINTING THE PASSWORD
print(generator)