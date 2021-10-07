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
    #Resets the terminal
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
    #Ask for input if the player wants to play
    answer = input("Carpet?(y/n)")
    #Return Values
    if answer == 'y':
        return True
    elif answer == 'n':
        return False
    else:
        print('Invalid answer')
        return False
#This function returns a boolean value depending if it wins
def win(hidden, guess):
    #check if same then return corresponding values
    if hidden == guess:
        return True
    else:
        return False
#This function creates the random 4 colors to be guessed
def encodePass():
    #Place holder for the the random colors
    rand_colors = []
    #iterate 4 times for the random 4 colors
    for x in range(4):
        #get random number from 1 to 6
        rand = random.randint(1, 6)
        #the the corresponding color from the converter
        rand_colors.append(color_num.get(rand))
    #return the values    
    return rand_colors
#This funtion checks and gets the input of the user
def playerGuess():
    #Place holder for the correct places in the player's guess
    correct = []
    #Place holder for the corresponding color from the player's guess
    guess_color = []
    #Check until the player's guess in correct and valid
    while True:
        #Ask for the player's guess
        guess = input("Guess: ")
        #check every number of the player's guess
        for char in guess:
            if int(char)> 0 and int(char) < 7:
                correct.append(char)
        #If the player's guess has 4 numbers and each number is valid then break out of the lopp
        if len(guess) == 4 and len(correct) == 4:
            break
        #Else the process repeats and prints out Wrong Input
        else:
            print('Wrong input')
            correct = []
            continue
    #Convert the numbers to corresponding colors
    for char in guess:
        guess_color.append(color_num.get(int(char)))
    #return the player's guess
    return guess_color
#This function gets the response of the input of the user
def compareGuess(hidden, guess, r):
    #Creates a copy of the hidden since the list is mutable and the the thing that is passed is a pointer
    temp_hidden = hidden.copy()
    #Placeholder for the color that are in guess and hidden
    R = []
    #Checks for a color in guess and in hidded
    for x in guess:
        if x in temp_hidden:
            #removes the already checked color so it wil not repeat
            temp_hidden.remove(x)
            #Append the color that has is in guess and hidden
            R.append(x)
    #Placeholder for the guess's colors in right position and same color as hidden         
    W = []
    #checks for guess's color and hidden's color in the same position
    for x in range(len(hidden)):
        #Check is the colors are the same
        if guess[x] == hidden[x]:
            #Append the color that is in the same position and same color
            W.append(x)
    #The r variabel is just for returning the right value in in the function call in main loop
    #if r is True that means that the main loop need the R varible
    if r:
        #Since R is a set of all colors in from guess that is in hidden the W is a subset of that set Therefore I need to subtract it
        return len(R)-len(W)
    #If r is False then the main loop calls for the W variable
    else:
        return len(W)
#this function draws the game board 
def drawBoard(game_over, hidden, tries, left, R , W):
    #creates a copy of tries so that of the lists so that it wont affect the global variables
    tries_temp = tries.copy()
    R_temp = R.copy()
    W_temp = W.copy()
    #I need to reverse the list so that the order of the input of the guess is stacking upwards to the header
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
    #Checks if the game is over. If true then reveals the answer if False then just prints X otherwise
    if game_over:
        #This iterates to the whole colors in hidded in 1 line. The end parameter makes the next interation next to each other
        for g in hidden:
            #To get a Uniform spaces between guess I limit the displayed color to 3 characters
            print("\t"+ f"{g[:3]}", end='')
        #Prints the header for the response    
        print("\t|R\tW")
    else:
        #same process but inputs X characters instead of the color
        for g in hidden:
            print("\t"+ 'XXX' , end='')
        print("\t|R\tW")
    print("---------------------------------------------------")
    #This prints the number of tries left So the blank spaces to be filled
    #This process is the same above but inputs blacks spaces (-)
    for i in range(left):
        for g in hidden:
            print("\t"+ '---' , end='')
        print("\t|-\t-")
    #This process is fundamentally the same as above. Enumerate just adds a counter variable in the decleration of
    #the for loop
    #This process loops over all the tries commited so far
    for x, guess in enumerate(tries_temp):
        #Prints the color of each tries
        for color in guess:
            print("\t"+ color[:3] , end='')
        #and prints the responses of each tries
        print(f"\t|{R_temp[x]}\t{W_temp[x]}")
#This serves as the converter from number to Color
color_num = {1:"RED", 2:"ORANGE", 3:"YELLOW", 4:"GREEN", 5:"BLUE", 6:"VIOLET"}
#This is the number of chance
chance = 10
#This list contains the list of the guesses of the player
tries = []
#Setting the random 4 colors
hidden = encodePass()
#This list contains the responses of the guess by the player
R = []
W = []
#Setting some variables for starting the game
#wins is for the ending the game if true
wins = False
#show is for the showing the correct answer by the end of the game
show = False
#initiating the menu for the overview of the Game
start = menu()
#This is the game loop
while True:
    #The menu returns a true or false if the player wants to play
    if start:
        #this draws the board 
        drawBoard(show, hidden, tries, chance, R, W)
        #this calls the input of the player
        guess = playerGuess()
        #Checks if the player wins
        wins = win(hidden, guess)
        #Append the response of the player's guess
        R.append(compareGuess(hidden,guess, True))
        W.append(compareGuess(hidden,guess, False))
        #Record the guess of the player 
        tries.append(guess)
        #Reduce the number of chance per turn
        chance -= 1
        #Check if the already wins or lose (run out of chance)
        if chance == 0 or wins:
            #Show the correct answer
            show = True
            #Display the last board with correct answer
            drawBoard(show, hidden, tries, chance, R, W)
            #Prints the corresponding message upon finfishing
            if wins:
                print('YOU WINN, CONGRATULATIONS')
            else:
                print('Too Bad, You Lose')
            #Asks if the player wants to play again
            response = input('Want to play again? (Type y to play)')
            #if the player wants to play then reset tha values
            if response == 'y':
                wins = False
                show = False
                chance = 10
                tries = []
                hidden = encodePass()
                R = []
                W = []
            #If not y then stop the game
            else:
                break
    #End the game otherwise
    else:
        break

    