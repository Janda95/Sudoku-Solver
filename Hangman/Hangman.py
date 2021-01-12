from string import ascii_lowercase
from words import get_random_word


def get_num_attempts():
    pass
    # get input for number between 1 - 20?


def get_min_word_length(minLength):
    pass
    # get input and check for valid len between 1-5


def printGameState():
    # 
    print("GameState Goes Here")    


def play():
    # get word
    gameOver = False
    
    while gameOver == False:
        # main game loop
        playHangman(word, turns)
    
        # ask if you would like to play again
        isValidInput = False
        exitPrompt = ""
        while isValidInput == False
            exitPrompt = input('Would you like to play again? (y/n)')
            exitPrompt.lower()
            exitPrompt.trim()
            
            if exitPrompt == 'y':
                pass
            elif exitPrompt == 'n':
                gameOver = True
                # return
            else:
                print(Invalid Input!)


if __name__ == '__main__':
    play()
    print("Thank you for playing!")

