import numpy

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = numpy.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for row in range(ROW_COUNT):
        if(board[row][col] == 0):
            return row
        
def drop_piece(board, row, col, piece):
    board[row][col] = piece
    
def print_board(board):
    print(numpy.flip(board, 0))
    
def winning_move(board, piece):
    # Horizontal Check
    for col in range(COLUMN_COUNT - 3):
        for row in range(ROW_COUNT):
            if(board[row][col] == piece and board[row][col + 1] == piece and board[row][col + 2] == piece and
               board[row][col + 3] == piece):
                return True
            
    # Vertical Check
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT):
            if(board[row][col] == piece and board[row + 1][col] == piece and board[row + 2][col] == piece and 
               board[row + 3][col] == piece):
                return True
            
    # Positive Diagonal Check
    for row in range(ROW_COUNT - 3):
        for col in range(COLUMN_COUNT - 3):
            if(board[row][col] == piece and board[row + 1][col + 1] == piece and board[row + 2][col + 2] == piece and 
               board[row + 3][col + 3] == piece):
                return True
            
    # Negative Diagonal Check
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT - 3):
            if(board[row][col] == piece and board[row - 1][col + 1] == piece and board[row - 2][col + 2] == piece and 
               board[row - 3][col + 3] == piece):
                return True

board = create_board()
print_board(board)
game_over = False
turn = 0

while game_over != True:
        
    # Player 1 Input
    if turn == 0:
        col = int(input("Player 1 - Make your selection "))
        if is_valid_location:
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            
            if winning_move(board, 1):
                print_board(board)
                print("Player 1 Wins..!!!")
                game_over = True
                break
    
    # Player 2 Input
    if turn == 1:
        col = int(input("Player 2 - Make your selection "))
        if is_valid_location:
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            
            if winning_move(board, 2):
                print_board(board)
                print("Player 2 Wins..!!!")
                game_over = True
                break
                
    print_board(board)
    
    turn = turn + 1
    turn = turn % 2
    