import t3

def get_tuple_from_string(coords: str):
    keys = coords.split()
    if len(keys) != 2:
        raise ValueError(f"input takes 2 arguments but {len(keys)} were given")
    
    try:
        board_x = int(keys[0])
        board_y = int(keys[1])
    except ValueError:
        raise ValueError(f"input must be convertible to integers")
    
    return board_x, board_y

if __name__ == "__main__":
    board = t3.Board()
    turn = t3.Cell.X

    while True:
        print(f"\n{board}")

        winner = board.get_winner()
        if winner in [t3.Cell.X, t3.Cell.O]:
            print(f"\n{winner.value} wins")
            break

        position = input(f"{turn.value} > ")
        if position == "end":
            break

        try:
            board.place(turn, get_tuple_from_string(position))
        except ValueError as e:
            print(f"Invalid syntax: {e}")
            continue

        turn = t3.Cell.X if turn == t3.Cell.O else t3.Cell.O