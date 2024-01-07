import queen


def all_possible_bishop_moves(position):
    file, rank = position[0].upper(), int(position[1])

    # Generate all possible moves
    all_moves = []

    # Diagonal moves
    for i in range(1, 8):
        queen.add_move(all_moves, chr(ord(file) + i), rank + i)
        queen.add_move(all_moves, chr(ord(file) + i), rank - i)
        queen.add_move(all_moves, chr(ord(file) - i), rank + i)
        queen.add_move(all_moves, chr(ord(file) - i), rank - i)

    return all_moves


