

# converts a line of text to integer array
# return: int[]
def line_to_integer_array(line):

    line_ = line.rstrip("\n") # remove trailing newline
    array = [int(num) for num in line_.split()]

    return array

# read drawn numbers and all boards from input file 
# return: 2-element tuple
def read_boards():
    input_file = '../input/input4.txt' # relative path to input file 
    boards = []
    row_index = 0

    with open(input_file) as input_file:
        for i,line in enumerate(input_file):
            if i == 0:
                drawn = line.split(",") # convert to integer
                drawn = [int(num) for num in drawn]
            else:
                if line == '\n' or line == '': # prepare to read a new board
                    board = [0,0,0,0,0]
                else: # read row
                    row = line_to_integer_array(line)
                    board[row_index] = row
                    row_index += 1

                    if row_index == 5: # entire board has been read
                        boards.append(board)
                        row_index = 0

    return (drawn, boards)

# checks if array elements are included in drawn array
# return: boolean
def all_drawn(array, drawn):
    for el in array:
        contained = True

        if el not in drawn:
            return False
    
    # all elements are in drawn
    return True

# checks if given board is a winning board, based on numbers drawn
# return: boolean
def winning(board, drawn):
    # check rows
    for i in range(len(board)):
        row = board[i]

        if all_drawn(row, drawn):
            return True
    
    # check columns
    for i in range(len(board[0])):
        col = [board[j][i] for j in range(len(board))]
        
        if all_drawn(col, drawn):
            return True

    # neither row/col contained in drawn
    return False


# calculates boards score
# return: int
def calculate_score(board, drawn):
    sum = 0 # of all unmarked elements

    for row in board:
        for el in row:
            if el not in drawn:
                sum += el 
    
    last_called = drawn[len(drawn) - 1]

    return sum * last_called

# prints board as a matrix
# return: void
def print_as_matrix(board):
    print('\n'.join([''.join(['{:5}'.format(item) for item in row]) for row in board]))

drawn, boards = read_boards()

# increment drawn elements and find first winning board
for i in range(1,len(drawn)+1):
    drawn_ = drawn[:i]

    winner_exists = False
    for board in boards:
        if winning(board, drawn_):
            winner_exists = True
            print("First winner:")
            print("drawn: ", drawn_)
            print("winning board: ")
            print_as_matrix(board)
            print("score: ", calculate_score(board, drawn_))
            break

    if winner_exists:
        break

# --- Part Two: figure out which board will win last ---


# - construct an ordered list of winners
# - only add board (and its score) if it is not already included
# - last winner is last one added

ordered_winners = []
scores = []

for i in range(1,len(drawn)+1):
    drawn_ = drawn[:i] 

    for board in boards:
        if winning(board, drawn_) and (board not in ordered_winners):
            ordered_winners.append(board)
            scores.append(calculate_score(board, drawn_))

print(len(ordered_winners))
print(len(scores))
last_winner = ordered_winners[len(ordered_winners)-1]
print_as_matrix(last_winner)
print("score: ", scores[len(scores)-1])