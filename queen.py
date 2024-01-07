def is_valid_position(file, rank):
    return 'A' <= file <= 'H' and 1 <= rank <= 8


def all_possible_queen_moves(position):
    file, rank = position[0].upper(), int(position[1])

    # Generate all possible moves
    all_moves = []

    # Horizontal and vertical moves
    for i in range(1, 8):
        add_move(all_moves, file, rank + i)
        add_move(all_moves, file, rank - i)
        add_move(all_moves, chr(ord(file) + i), rank)
        add_move(all_moves, chr(ord(file) - i), rank)

    # Diagonal moves
    for i in range(1, 8):
        add_move(all_moves, chr(ord(file) + i), rank + i)
        add_move(all_moves, chr(ord(file) + i), rank - i)
        add_move(all_moves, chr(ord(file) - i), rank + i)
        add_move(all_moves, chr(ord(file) - i), rank - i)

    return all_moves


def add_move(moves, new_file, new_rank):
    if is_valid_position(new_file, new_rank):
        moves.append(f"{new_file}{new_rank}")


