import queen


def all_possible_knight_moves(position):
    file, rank = position[0].upper(), int(position[1])

    # Generate all possible moves
    all_moves = []

    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (-1, 2), (1, -2), (-1, -2)
    ]

    for move in knight_moves:
        queen.add_move(all_moves, chr(ord(file) + move[0]), rank + move[1])

    return all_moves


# Example usage:
# knight_position = "C3"
# possible_moves = all_possible_knight_moves(knight_position)
# print(f"Possible moves for Knight at {knight_position}: {possible_moves}")
