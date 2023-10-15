import random
#Importing modules called random for random output

#2 variables for tracking scores, 1 for user and 1 for computer
user_wins = 0
computer_wins = 0

options = ["Rock","Paper","Scissors"]
#data structures, elements that are stored in the lists. 

#adding a while loop
while True:
    user_input =  input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break #instead of quit, it will 'break' out of the while loop 

    #instead of 'in' we'll use 'not in' to reverse it, so if user types in something that is not in the list, user will then have to type something valid.  
    if user_input not in ["Rock","Paper","Scissors"]:
        continue

    random_number = random.randint(0,2)
    # Rock: 0, paper: 1, scissor: 2
    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")




print("Goodbye")


