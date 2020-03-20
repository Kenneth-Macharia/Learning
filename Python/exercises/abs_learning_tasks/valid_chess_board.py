def is_valid_chess_board(moves_dict=None):
    ''' Checks if chess moves passed in as a dictionary are legal chess moves
    '''

    valid = False

    # Create valid chess board layout
    chess_board = {}
    for col in range(ord('a'), ord('i')):  # The column letter a - h
        for row in range(1, 9):  # The row numbers 1 - 8
            chess_board[str(row)+chr(col)] = ''

    # print(chess_board)

    # Create the valid pieces
    piece_types = ['Rook', 'Knight', 'Bishop', 'King', 'Queen', 'Pawn']
    piece_colors = ['w', 'b']

    all_chess_piece_types = []

    for color in piece_colors:
        for piece in piece_types:
            all_chess_piece_types.append(f'{color}-{piece}')

    print(all_chess_piece_types)

    {'1h': 'w-King', '6c': 'b-Queen', '2j': 'w-Bishop', '5h': 'b-Queen', '3e': 'w-King'}

    # Check if moves parameter dict is valid
    for key, value in moves_dict.items():
        pass


    return valid

if __name__ == "__main__":
    is_valid_chess_board()
