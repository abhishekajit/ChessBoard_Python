def get_valid_pawn_moves(position, is_white=True):
    file, rank = position[0], int(position[1])

    valid_moves = []

    if is_white:
        valid_moves.append(file + str(rank + 1))
    else:
        valid_moves.append(file + str(rank - 1))
    if (is_white and rank == 2) or (not is_white and rank == 7):
        valid_moves.append(file + str(rank + 2) if is_white else file + str(rank - 2))

    valid_moves.append(chr(ord(file) - 1) + str(rank + 1) if is_white else chr(ord(file) - 1) + str(rank - 1))
    valid_moves.append(chr(ord(file) + 1) + str(rank + 1) if is_white else chr(ord(file) + 1) + str(rank - 1))
    valid_moves = [move for move in valid_moves if 'A' <= move[0] <= 'H' and 1 <= int(move[1]) <= 8]
    return valid_moves

