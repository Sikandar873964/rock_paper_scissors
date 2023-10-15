import random
#Importing modules called random for random output

#2 variables for tracking scores, 1 for user and 1 for computer
user_wins = 0
computer_wins = 0

#adding a while loop
while True:
    user_input =  input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        quit()

    if user_input in ["Rock","Paper","Scissors"]:


