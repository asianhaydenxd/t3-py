import t3, os

def get_coords_as_ints(coords: str):
    if len(keys := coords.split()) != 2:
        raise ValueError(f"input takes 2 arguments but {len(keys)} were given")
    
    try:
        board_x = int(keys[0])
        board_y = int(keys[1])
    except ValueError:
        raise ValueError(f"input must be convertible to integers")
    
    return board_x, board_y

def main():
    board = t3.Board()

    while True:
        os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        print(f"\n{board}")

        if winner := board.get_winner():
            print(f"\n{winner} wins")
            break
        
        position = input(f"{board.get_turn()} > ")

        if position == "q": break

        try:
            x, y = get_coords_as_ints(position)
            board.place(x, y)
        except (ValueError, IndexError) as e:
            print(f"Invalid syntax: {e}")
            continue

        board.iterate_turn()

if __name__ == "__main__": main()
