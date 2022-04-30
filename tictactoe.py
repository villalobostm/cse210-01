# CSE 210 | Programming With Classes
# Tic-Tac-Toe game
# Author: Thomas Villalobos


def main():

    number_squares_chosen = 0
    grid = ["1","2","3","4","5","6","7","8","9"]
    mark = ["x", "o", "x", "o", "x", "o", "x", "o", "x"]
    
    while (number_squares_chosen < 9):
        print_grid(grid)
        position_square_choose = int(input(f"{mark[number_squares_chosen]}'s turn to choose a square (1-9): "))
        fill_grid(grid, position_square_choose, mark[number_squares_chosen])
        if is_a_winner(grid):
            break
        number_squares_chosen += 1

    print_grid(grid)
    print("Good game. Thanks for playing!")


def print_grid(grid):
    print("")
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-+-+-")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-+-+-")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print("")


def fill_grid(grid, position_square_choose, mark):
    for i in range(9):
        if i == (position_square_choose - 1):
            grid[i] = mark


def is_a_winner(grid):
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])


if __name__ == "__main__":
    main()

