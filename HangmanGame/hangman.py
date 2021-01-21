#!/usr/bin/env python3
import sys, os

from absl import app
from string import ascii_lowercase
from words import get_random_word


minWordLen = 3
maxWordLen = 5


# setting number of attempts until loss
def getNumAttempts(wordLen):
    x = -1
    while True:
        try:
            x = int(input("How many attempts? (1-20): "))
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
            msg = "What length of word would you like to attempt? ({}-{}): "
            msg.format(minWordLen, maxWordLen)
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
    
    output = "\nWord: "
    for letter in wordArr:
        output = output + str(letter) + " "
    output = output + "\n"
    msg = "You have {} attempts left\n".format(attemptsLeft) 
    
    output = output + msg
    
    print(output)
    
def winMessage(turns, answer):
    pass
    print("\nYou Win!\n")


def isGameOver():
    # ask if you would like to play again
    isValidInput = False
    exitPrompt = ""

    while isValidInput == False:
        exitPrompt = input('Would you like to play again? (y/n): ')
        exitPrompt = exitPrompt.lower()
        exitPrompt = exitPrompt.strip()

        if exitPrompt == 'y':
            # isValidInput = True
            print("Let's Play Again!\n")
            return False
        elif exitPrompt == 'n':
            # isValidInput = True
            print("Ok No Problem!\n")
            return True
        else:
            # isValidInput = False
            print("\nInvalid Input!\n")
            return True


def requestGuess(word):
    validInput = False
    guess = ""
    while True:
        guess = input("Guess a letter: -> ")
        guess = guess.strip()
        
        if len(guess) == 1:
            validInput = True
        elif len(guess) == len(word):
            validInput = True
        
        if validInput == True:
            break
    return guess


def checkLetterGuess(word, guessStr, lettersCorrect, answer):
    correct = False
    for i in range(0, len(word)):
        letter = answer[i]
        
        if letter == '*':
            if word[i] == guessStr:
                correct = True
                lettersCorrect += 1
                answer[i] = guessStr
    return correct, lettersCorrect, answer


def playHangman(word, turns):
    # setup answer string and printable answer state
    answer = ['*'] * len(word)
    lettersCorrect = 0
    for i in range(0, turns):
        correctAns = False
        #loop to not count correct answers
        while True:
            printGameState(turns - i, answer)
            
            guess = requestGuess(word)

            # check each location in answer string and reflect correct letters
            if len(guess) == len(word):
                if guess == word:
                    lettersCorrect = len(word)
            else:
                correctAns, lettersCorrect, answer = checkLetterGuess(
                    word, 
                    guess, 
                    lettersCorrect, 
                    answer
                )
            
            # check win condition
            if lettersCorrect >= len(word):
                winMessage(turns, answer)
                return
            
            # if correct add extra turn
            if correctAns == True:
                pass
            else:
                break
        

    outcome = "You Lose! The word was -> " + word + "\n"
    print(outcome)
    return


def main(argv):
    # get word
    gameOver = False
    
    while gameOver == False:
        # setup
        # wordLen = getMinWordLen()
        word = get_random_word(-1)
        # word = "example"
        turns = getNumAttempts(len(word))
        
        # main game loop
        playHangman(word, turns)
    
        gameOver = isGameOver()


if __name__ == '__main__':
    # print(sys.path)
    app.run(main)
    print("Thank you for playing!")
