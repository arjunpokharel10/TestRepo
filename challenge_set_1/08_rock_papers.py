import random

game_art = {
    'rock':  '''
    ________
---'     ____)
        (_____)
        (_____)
        (_____)
---.___(____)
''',

    'paper': '''
    _______
---'   _____)______
        ____________)
        _____________)
        ___________)
---.___________)
''',

    'scissors': '''
    _______
---'   _____)______
        ____________)
        _____________)
        (_____)
---.___(____)
'''

}


game = ['rock', 'paper', 'scissors']


while True:

    computers_choice = random.choice(game)

    while True:
        players_choice = input("what do you choose: R for rock, P for paper, S for scissors\n").lower()

        if players_choice.startswith('r'):
            players_choice = 'rock'
            break
        elif players_choice.startswith('s'):
            players_choice = 'scissors'
            break
        elif players_choice.startswith('p'):
            players_choice = 'paper'
            break
        else:
            print("Enter a valid choice: R for rock, P for paper, or S for scissors\n")
    
    print(f'You chose: {players_choice}\n {game_art[players_choice]} \n\nComputer chose: {computers_choice}\n {game_art[computers_choice]}\n\n')

    if computers_choice == players_choice:
        print("It's a TIE!")
    elif computers_choice == 'rock' and players_choice == 'paper':
        print("YOU WIN!!")
    elif computers_choice == 'paper' and players_choice == 'scissors':
        print("YOU WIN!!")
    elif computers_choice == 'scissors' and players_choice == 'rock':
        print("YOU WIN!")
    else:
        print('YOU LOSE! BETTER LUCK NEXT TIME!\n\n')

    play_again = input('Do you want to play again? [Y or press any key to quit]\n').lower()
    if not play_again.startswith('y'):
        print('Thank you for playing!')
        break
    



        