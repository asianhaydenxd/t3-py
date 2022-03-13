import t3

def get_tuple_from_string(coords: str):
    if len(keys := coords.split()) != 2:
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

        if (winner := board.get_winner()) in [t3.Cell.X, t3.Cell.O]:
            print(f"\n{winner.value} wins")
            break

        if (position := input(f"{turn.value} > ")) == "end":
            break

        try:
            x, y = get_tuple_from_string(position)
            board.place(turn, x, y)
        except (ValueError, IndexError) as e:
            print(f"Invalid syntax: {e}")
            continue

        turn = t3.Cell.X if turn == t3.Cell.O else t3.Cell.O