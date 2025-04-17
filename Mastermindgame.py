# A Mastermind Computer Game

# Function for main menu
def menu():
    # Welcome message to player
    print('+-------------------------------------+')
    print('| Welcome to Mastermind Computer Game |')
    print('+-------------------------------------+\n')
    print('[1] Start game')
    print('[2] How to play')
    print('[3] Exit game ')


# Function for [1] Start game
def start_game():
    # Brief instruction for player
    print('+-------------------------------------+')
    print('| Welcome to Mastermind Computer Game |')
    print('+-------------------------------------+\n')
    print("Guess the fruit code in as few tries as possible with complete word.\n")
    print("Use the fruits given below:\napple, orange, mango and grape\n")

    # List for fruit choices
    fruits = ['apple', 'orange', 'mango', 'grape']

    # Computer chooses four fruits randomly
    def random():
        import random
        fruit_code = []
        fruit_code = random.choices(fruits, k=4)
        return fruit_code

    # Player inputs the guess of fruit
    def guess(fruits):
        guessed_fruits = []
        count = 0

        # Ensure player to enter four guesses
        while count < 4:
            player_guess = input('Enter your guess: ').lower()
            if player_guess in fruits:
                guessed_fruits.append(player_guess)
                count += 1
            # Other input will not be counted
            else:
                print('Try again')
        # Show player their guesses
        print('Your guesses are:', guessed_fruits, '\n')
        return guessed_fruits

    # Check if player's guess is correct
    def check(guessed_fruits, answer_code):
        copy_answer_code = answer_code.copy()
        correct = 0
        wrong = 0

        # Check correct fruits in correct position
        for i in range(4):
            if guessed_fruits[i] in copy_answer_code[i]:
                if guessed_fruits[i] == answer_code[i]:
                    correct += 1

        # Check correct fruits in incorrect position
        for i in range(4):
            if guessed_fruits[i] in copy_answer_code:
                if guessed_fruits[i] != answer_code[i]:
                    wrong += 1

        # Show player the result
        print('Correct fruits in correct position  : ', correct)
        print('Correct fruits in incorrect position: ', wrong, '\n')
        return correct

    # Loop for the game and play again
    again = 'Y'
    while again == 'Y' or 'y' == again:
        answer_code = random()
        attempt = 0
        while True:
            guess_fruits = guess(fruits)
            attempt += 1
            # When player guesses the code correctly
            if check(guess_fruits, answer_code) == 4:
                print('Congratulations! You took ' + str(attempt), 'attempts to guessed it right.\n')
                break

        # Ask player if they want to play again
        while True:
            again = input('Do you want to play again? [Y/N]: ')
            print()
            # When player enter Y or y
            if again == 'Y' or 'y' == again:
                print('New Game')
                print('+-------------------------------------+')
                print('| Welcome to Mastermind Computer Game |')
                print('+-------------------------------------+\n')
                print("Guess the fruit code in as few tries as possible.\n")
                print("Use the fruits given below:\napple, orange, mango and grape\n")
                break
            # When player enter N or n
            elif again == 'N' or 'n' == again:
                print('Thank you for playing!')
                quit()
                break
            # Try again when other input is being entered
            else:
                print('ERROR! Invalid option')
                continue


# Function for [2] How to play
def instruction():
    print('+-------------------------------------+')
    print('|            How to play              |')
    print('+-------------------------------------+\n')
    print('Objective: ')
    print('Guess a code consisting of four fruits in the right sequence\n')
    print('Instructions: ')
    print('1. The computer will automatically generate four fruit code (may duplicate)')
    print('2. The four different fruits to pick are: Apple, Orange, Mango and Pear')
    print('3. Enter your fruit code one by one according to given fruits with complete word')
    print('4. After four fruit code are entered, the guess code will be checked')
    print('5. The game will display the number of fruits in correct position and')
    print('   number of correct fruits but in wrong position')
    print('6. Good luck, you can do it!\n')

    instruction_option = int(input('Enter 1 to return main menu or 2 to start game: '))
    # Go back to menu if player enter 1
    while instruction_option != 1:
        # Start game when player enter 2
        if instruction_option == 2:
            start_game()
        # Try again when other input is being entered
        else:
            print('ERROR! Invalid option\n')
            instruction_option = int(input('Enter 1 to return main menu or 2 to start game: '))
    menu()


# User menu
menu()
option = int(input('Enter your option [1,2,3]: '))
# Exit program when player enter 3
while option != 3:
    # Start game when player enter 1
    if option == 1:
        start_game()
    # Show instruction when player enter 2
    elif option == 2:
        instruction()
    # Try again when other input is being entered
    else:
        print('ERROR! Invalid option\n')
        menu()

    print()
    option = int(input('Enter your option [1,2,3]: '))

print('Thank you, bye!')

