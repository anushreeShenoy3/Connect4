import numpy

#define fixed board
rowCount = 6
columnCount = 7
board = numpy.empty([rowCount, columnCount], dtype="<U10")

def makeBoard():
    '''
    function to create an empty board
    :return:
    '''
    #create an empty board
    for x in range(0, len(board)):
        for y in range(0, len(board[0])):
            board[x][y] = " "
    print(board)

def board_is_full():
    '''
    Function to check if board is full
    :return: True if top row is full
    '''
    if " " in board[0]:
        return False
    else:
        return True

def check_vertical_downward(player,row,col):
    '''
    Function to check downward cross vertical match
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:

        if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] ==player:
            print("Player {} won".format(player))
            return True
        else:
            return False
    except:
        return False

def check_vertical_upward(player,row,col):
    '''
    Function to check if match is found diagonally upward direction
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:
        if board[row][col] == player and board[row+1][col] == player and board[row+2][col] == player and board[row+3][col] ==player:
            print("Player {} won".format(player))
            return True
        else:
            return False
    except:
        return False

def check_horizontal_right(player,row,col):
    '''
    Function to check horizonatlly right matches
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:
        if col+3 < len(board[row]):
            if board[row][col] == player and board[row][col+1] == player and board[row][col+2] == player and board[row][col+3] ==player:
                print("Player {} won".format(player))
                return True
        else:
            return False
    except:
        return False

def check_horizontal_left(player,row,col):
    '''
    Function to check horizonatlly right matches
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:
        if col-3 > 0 or col-3 == 0:
            if board[row][col] == board[row][col-1] == board[row][col-2] == board[row][col-3] ==player:
                print("Player {} won".format(player))
                return True
    except:
        print("Index out of bound")

def check_diagonal(player,row,col):
    '''
    Function to check matches in diagonal directions
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    if check_upper_right(player,row,col) or check_lower_right(player,row,col) or check_lower_left(player,row,col) or check_upper_left(player,row,col):
        return True
    else:
        return False

def check_lower_right(player,x,y):
    '''
    Function to check diagonal righ match
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:
        if board[(x, y)] == player and board[(x + 1, y + 1)] == player and board[(x + 2, y + 2)] == player and board[
            (x + 3, y + 3)] == player:
            return True
        else:
            return False
    except:
        return False

def check_lower_left(player,x,y):
    try:
        if board[(x, y)] == player and board[(x + 1, y + 1)] == player and board[(x + 2, y + 2)] == player and board[
            (x + 3, y + 3)] == player:
            return True
        else:
            return False
    except:
        return False

def check_upper_left(player,x,y):
    '''
    Function to check diagonal left matches
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match'''
    try:
        if board[(x, y)] == player and board[(x - 1, y - 1)] == player and board[(x - 2, y - 2)] == player and board[
            (x + 3, y + 3)] == player:
            return True
        else:
            return False
    except:
        return False

def check_upper_right(player,x,y):
    '''
    Function to check diagonal right matches
    :param player: Player id for ex: X/O
    :param row: current row
    :param col:current column
    :return: True or False based on match
    '''
    try:
        if board[(x, y)] == player \
                and board[(x - 1, y - 1)] == player \
                and board[(x - 2, y - 2)] == player \
                and board[(x - 3, y - 3)] == player:
            return True
        else:
            return False
    except:
        return False

def is_winner(player,row,col):
    print("checking vertical downward")
    if check_vertical_downward(player,row,col) or check_vertical_upward(player,row,col) \
            or check_horizontal_left(player,row,col) or check_horizontal_right(player,row,col) \
            or check_diagonal(player,row,col):
        print("Player has matched all vertical blocks in row: {} and column {} ".format(player,row,col))
        return True
    else:
        return False


def place_token(player,selection):
    row = 5
    for block in board:
        if board[row][selection] == " ":
            board[row][selection] = player
            break
        elif row > 0:
            row = row - 1
        else:
            print("Block already selected. Player {} lost your turn!".format(player))
    print(board)
    return is_winner(player,row,selection)

if __name__ == "__main__":
    #create board
    makeBoard()
    print(len(board))
    player = 'O'
    while not board_is_full():
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        print("********Player {} **********".format(player))
        print("Please select a column from 0 - 6")
        selection = int(input('Select a column: '))
        if place_token(player,selection):
            print("Player {} won".format(player))
            break
        print(board)
    print("Game Over!")
