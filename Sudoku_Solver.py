''' Sudoku Solver

Given a sudoku board, solve for the missing numbers and print out a completed board

If there is no solution then return None

# solve sudoku using backtracking!
# our puzzl is a list of lists, where each inner list is a row in our sudoku puzzle
# return whether a solution exits
# mutates puzzle to be the solution if solution exists

# Step 1: choose somewhere on the puzzle to make a guess

# Step 2: Make a guess

# Step 3: Check Vertical, horizontal, and local square if conflicting

# Step 4: 
    a. If conflicting, try the next number -> if number is 10, set location to -1, 
    pop from the stack, set location and try next number from stack tuple

    b. If successful, add it to the stack with location and guess

# Step 5:
    a. If no more guesses then return the completed puzzle
    b. If no available guesses at and empty stack, return None to represent 
'''


# Template
'''
    puzzle = 
    [
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1 ,-1,  -1, -1, -1,  -1, -1, -1],
        
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
    ]
'''


def pretty_print_puzzle(puzzle):
    print('\nPuzzle:\n')
    for row in puzzle:
        print(row)
    print('\n')


def find_next_empty(puzzle):
    # find next empty square
    # return row, col tuple or (None, None) if there is none

    # Ideas for improvement
    # can use current row and col as a start to reduce checks?
    for i in range(len(puzzle[0])):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == -1:
                return (i, j)

    return (None, None)


def check_valid_number(x, y, puzzle):
    number = puzzle[x][y]
    print(str(number))
    if number > 9:
        return False

    # check row
    for i in range(len(puzzle[0])):
        if i != x:
            if puzzle[i][y] == number:
                return False

    # check column
    for j in range(len(puzzle[0])):
        if j != y:
            if puzzle[x][j] == number:
                return False

    # check box area ignoring location with current guess
    xi = (x // 3) * 3
    yi = (y // 3) * 3

    for i in range(xi, xi + 3):
        for j in range(yi, yi + 3):
            if i != x and j != y:
                if puzzle[i][j] == number:
                    return False

    return True


def solve_sudoku(puzzle):
    guess_stack = list() # tuple ( (x:0-8, y: 0-8), int 1-9)

    still_searching = True
    while still_searching:

        coords = find_next_empty(puzzle)
        pretty_print_puzzle(puzzle)

        if coords == (None, None):
            return puzzle

        # stack interactions - make guess, do a check, fail 1-8 -> +1 fail 9 -> look at stack
        # set location for x and y for new location
        x = coords[0]
        y = coords[1]

        # guess starts at zero to increment at start of loop
        guess = 0
        attempting_numbers = True

        while attempting_numbers:
            # try next number
            guess = guess + 1
            puzzle[x][y] = guess

            # if number valid then find next number
            if check_valid_number(x, y, puzzle):
                attempting_numbers = False
                curr_coords = (x, y)
                guess_stack.append(((curr_coords, guess)))

            else:
                # number is over 9 try next stack location
                if guess > 9:
                    print("\n")
                    msg = "Over 9"
                    print(msg)

                    puzzle[x][y] = -1
                    # if stack is empty then no solution
                    if len(guess_stack) <= 0:
                        return None

                    # pop and set guess and location to iterate next loop
                    backtrack_guess = guess_stack.pop()
                    guess = backtrack_guess[1]
                    x = backtrack_guess[0][0]
                    y = backtrack_guess[0][1]
                    pretty_print_puzzle(puzzle)


def main():
    puzzle = [
        [ 3,  9, -1,  -1,  5, -1,  -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,  -1, -1,  5],
        [-1, -1 ,-1,   7,  1, -1,  -1,  8, -1],
        
        [-1,  5, -1,  -1,  6,  8,  -1, -1, -1],
        [ 2, -1,  6,  -1, -1,  3,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1,  4],

        [ 5, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [ 6,  7, -1,   1, -1,  5,  -1,  4, -1],
        [ 1, -1,  9,  -1, -1, -1,   2, -1, -1],
    ]

    completed_puzzle = solve_sudoku(puzzle)

    if completed_puzzle != None:
        pretty_print_puzzle(puzzle)
    else:
        print("No solution found :(")


if __name__ == '__main__':
    main()
