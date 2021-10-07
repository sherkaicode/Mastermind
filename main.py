#Importing random for the random colors
import random
from os import system, name

#This function is for clearing the terminal for cleaner UI [To add it is like a game frame]
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
#This function contains the instruction of the game and some Rules
def menu():
    clear()
    print("---------------------------------------------------")
    print("\t\t    MASTERMIND")
    print("---------------------------------------------------")
    print("The [R] Column means right color but wrong place")
    print("The [W] Column means right color and right place")
    print("---------------------------------------------------")
    print("The Colors of this game is ROYGBV (Rainbow without Indigo)")
    print("Each corresponds to a number from 1 to 6")
    print("You have to guess the hidden 4 colors using these ")
    print("corresponding numbers and you have 10 tries to do it")
    print("---------------------------------------------------")
    answer = input("Carpet?(y/n)")
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print('Invalid answer')
        return False
#This function returns a boolean value depending if it wins
def win(hidden, guess):
    if hidden == guess:
        return True
    else:
        return False
def encodePass():
    rand_colors = []
    for x in range(4):
        rand = random.randint(1, 6)
        rand_colors.append(color_num.get(rand))
    return rand_colors
def playerGuess():
    correct = []
    while True:
        guess = input("Guess: ")
        for char in guess:
            if int(char)> 0 and int(char) < 7:
                correct.append(char)
        if len(guess) == 4 and len(correct) == 4:
            break
        else:
            print('Wrong input')
            correct = []
            continue
    guess_color = []
    for char in guess:
        guess_color.append(color_num.get(int(char)))
    return guess_color
def compareGuess(hidden, guess, r):
    #print(hidden)
    temp_hidden = hidden.copy()
    temp_guess = guess.copy()
    R = []
    for x in temp_guess:
        if x in temp_hidden:
            temp_hidden.remove(x)
            R.append(x)
            #print(x)  
    W = []
    for x in range(len(hidden)):
        if guess[x] == hidden[x]:
            W.append(x)
    if r:
        return len(R)-len(W)
    else:
        return len(W)
def drawBoard(game_over, hidden, tries, left, R = [0], W = [0]):
    tries_temp = tries.copy()
    R_temp = R.copy()
    W_temp = W.copy()
    R_temp.reverse()
    W_temp.reverse()
    tries_temp.reverse()
    clear()
    print("---------------------------------------------------")
    print("\t\t    MASTERMIND")
    print("---------------------------------------------------")
    print("\t\t       Menu")
    print("---------------------------------------------------")
    print("Enter code using numbers.")
    print("1 - RED, 2 - ORANGE, 3 - YELLOW, 4 - GREEN, 5 - BLUE\n, 6 - VIOLET")
    print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
    print("---------------------------------------------------")
    #print("||",hidden, tries, left, R, W, "||" )
    if game_over:
        for g in hidden:
            print("\t"+ f"{g[:3]}", end='')
        print("\t|R\tW")
    else:
        for g in hidden:
            print("\t"+ 'X' , end='')
        print("\t|R\tW")
    print("---------------------------------------------------")
    for i in range(left):
        for g in hidden:
            print("\t"+ '---' , end='')
        print("\t|-\t-")

    for x, guess in enumerate(tries_temp):
        for color in guess:
            print("\t"+ color[:3] , end='')
        print(f"\t|{R_temp[x]}\t{W_temp[x]}")

color_num = {1:"RED", 2:"ORANGE", 3:"YELLOW", 4:"GREEN", 5:"BLUE", 6:"VIOLET"}
chance = 10
tries = []
hidden = encodePass()
R = []
W = []
wins = False
show = False
start = menu()
while True:
    if start:
        drawBoard(show, hidden, tries, chance, R, W)
        guess = playerGuess()
        wins = win(hidden, guess)
        R.append(compareGuess(hidden,guess, True))
        W.append(compareGuess(hidden,guess, False))
        tries.append(guess)
        chance -= 1
        if chance == 0 or wins:
            show = True
            drawBoard(show, hidden, tries, chance, R, W)
            if wins:
                print('YOU WINN, CONGRATULATIONS')
            else:
                print('Too Bad, You Lose')
            response = input('Want to play again? (y/n)')
            if response == 'y':
                wins = False
                chance = 10
                tries = []
                hidden = encodePass()
                R = []
                W = []
            else:
                break
    else:
        break

    