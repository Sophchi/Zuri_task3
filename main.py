import random

'''
The outcome of this game depend on the choices made by the two player involved (i.e CPU : USER).
RULES:
    ROck crushes/bends Scissors
    Paper covers Rock
    SCissors cuts Paper
...............................The above are the conditions for a win, to lose is otherwise.

'''


R_for = 'Rock'
P_for = 'Paper'
S_for = 'Scissors'

while True:
    choice_list = [R_for, P_for, S_for]

    computer_choice = random.choice(choice_list) #Enable the computer take a pick from the choice_list
    User_input = None

    while User_input not in choice_list: 
        User_input = input('Rock, Paper, or Scissors?:  ').title()
        if User_input not in choice_list:
            print('{} is an invalid input, TRY AGAIN\n'.format(User_input)) 
        else:
            break
        
    
    if User_input == computer_choice:
        print('computer_choice: {1}, User_input: {0}'.format( User_input, computer_choice))
        print("It\'s a tie......\n")

    elif User_input == 'Rock':
        if computer_choice == 'Paper':
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You LOse!')
        if computer_choice == 'scissors':   
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You Win!') 
 

    elif User_input == 'Paper':
        if computer_choice == 'Scissors':
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You LOse!')
        if computer_choice == 'Rock':
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You Win!')


    elif User_input == 'Scissors':
        if computer_choice == 'Rock':
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You LOse!')
        if computer_choice == 'Paper':
            print('computer_choice: {}, User_input: {}'.format(computer_choice, User_input))
            print('You Win!')
            
    play_again = input('LIke to play again, YES/No?: ').title()
    if play_again != 'Yes':
        break