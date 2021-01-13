from string import ascii_lowercase
from Words import *

minWordLen = 3
maxWordLen = 5

    # setting number of attempts until loss
def getNumAttempts():
    x = -1
    while True:
        try:
            x = int(input("How many attempts? (1-20)"))
            break
        except ValueError:
            print("Not a valid number. Please try again.\n")
    
    if x > 20:
        x = 20
    elif x < 1:
        x = 1
    
    return x
    
    
def getMinWordLen():
    x = -1
    while True:
        try:
            msg = "What length of word would you like to attempt? (%-%)".format(minWordLen, maxWordLen)
            inputStr = input(msg)
            x = int(inputStr)
            break
        except ValueError:
            print("Not a valid number. Please try again..\n")
    
    if x > maxWordLen:
        x = maxWordLen
    elif x < 1:
        x = minWordLen
    
    return x
    


def printGameState(attemptsLeft, wordArr):
    # 
    print("GameState Goes Here")
    
    output = "Word: "
    for letter in wordArr:
        output = output + str(letter) + " "
    output = output + "\n"
    msg = "You have % attempts left\n" % (attemptsLeft) 
    
    output = output + msg
    
    print(output)


def playAgain():
    # ask if you would like to play again
    isValidInput = False
    exitPrompt = ""

    while isValidInput == False:
        exitPrompt = input('Would you like to play again? (y/n)')
        exitPrompt.lower()
        exitPrompt.trim()
        
        if exitPrompt == 'y':
            # isValidInput = True
            return True
        elif exitPrompt == 'n':
            # isValidInput = True
            return False
        else:
            # isValidInput = False
            print("\nInvalid Input!\n")


def play():
    # get word
    gameOver = False
    
    while gameOver == False:
        # setup
        wordLen = getMinWordLen()
        #word = words.getRandomWord()
        word = "example"
        
        # main game loop
        playHangman(word, turns)
    
        gameOver = playAgain()


def playHangman(word, turns):
    pass    


if __name__ == '__main__':
    play()
    print("Thank you for playing!")

