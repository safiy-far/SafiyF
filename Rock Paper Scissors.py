# Safiy
# Summeer immersion program
# Written in python
# Rock, Paper, Scissors game


from random import randint




# selection options for the game
random_number = randint(0,2)
options = ["Rock", "Paper", "Scissors"]

comp_choice = options[random_number]
print("Computer chooses:", comp_choice)

user_score = 0
comp_score = 0

while user_score < 3 and comp_score < 3:
    
    # asking user for input: rock, paper, scissors
    
    user_input = input("Choose 'Rock', 'Paper', 'Scissors'\n")
    random_number = randint(0,2)
    comp_choice = options[random_number]
    
    
    
    print("Computer chooses:", comp_choice)
    print("User chooses:", user_input)
    
    


    # Exception handling
    
    if user_input != options[0] and user_input != options[1] and user_input != options[2]:
        print("Invalid option")
    elif user_input == options[1] and comp_choice == options[0] or user_input == options[0] and comp_choice == options[2] or user_input == options[2] and comp_choice == options[1]:
        print("You win")
        user_score += 1
    elif user_input == comp_choice:
        print("Tie")
    else:
        print("You Lose")
        comp_score += 1
        
    print ("comp score:", comp_score)
    print ("user_score:", user_score)
    
    # win streak
    
    if user_score == 2 and comp_score == 0:
        print("Win streak! You win!")
        break
    
    
    #play again
    
    if user_score == 3 or comp_score == 3:
         play = input("Play again? (y/n)")
         if play == "y":
            user_score = 0
            comp_score = 0
    
        
