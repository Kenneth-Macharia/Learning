def is_valid_chess_board(moves_dict):
    ''' Checks if chess moves passed in as a dictionary are legal chess moves
    '''

    valid = False

    # Create valid chess board layout
    chess_board = {}
    for col in range(ord('a'), ord('i')):  # The column letter a - h
        for row in range(1, 9):  # The row numbers 1 - 8
            chess_board[str(row)+chr(col)] = ''

    # Create the valid pieces
    piece_types = ['Rook', 'Knight', 'Bishop', 'King', 'Queen', 'Pawn']
    piece_colors = ['w', 'b']

    all_chess_piece_types = []

    for color in piece_colors:
        for piece in piece_types:
            all_chess_piece_types.append(f'{color}-{piece}')

    # Check if moves parameter dict is valid
    move_sequence = []
    for move, piece in moves_dict.items():
        if move in chess_board:
            if piece in all_chess_piece_types:
                move_sequence.append(piece[0])
            else:
                break
        else:
            break

    if len(move_sequence) == len(moves_dict):
        for i in range(len(move_sequence) - 1):
            if move_sequence[i] != move_sequence[i + 1]:
                valid = True
            else:
                valid = False
                break

    return valid

is_valid_chess_board({'1h': 'w-King', '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'w-Queen', '3e': 'w-King'})