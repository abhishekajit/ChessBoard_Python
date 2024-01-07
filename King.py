def get_valid_king_moves(position):
    file, rank = position[0], int(position[1])

    horizontal_moves = [file + str(rank - 1), file + str(rank + 1)]
    vertical_moves = [chr(ord(file) - 1) + str(rank),
                      chr(ord(file) + 1) + str(rank)]
    diagonal_moves = [
        chr(ord(file) - 1) + str(rank - 1), chr(ord(file) + 1) + str(rank - 1),
        chr(ord(file) - 1) + str(rank + 1), chr(ord(file) + 1) + str(rank + 1)
    ]
    valid_moves = [move for move in horizontal_moves + vertical_moves + diagonal_moves if
                   'A' <= move[0] <= 'H' and 1 <= int(move[1]) <= 8]
    return valid_moves

