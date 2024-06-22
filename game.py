from random import randint
from dataclasses import dataclass


class MineSweeper:
    dim_size: int

    def __init__(self, dim_size: int):
        self.dim_size = dim_size
        self.grid = [[0 for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        self.add_mines()

    def add_mines(self):
        previous_Values = []
        for _ in range(30):
            row = randint(0, self.dim_size - 1)
            col = randint(0, self.dim_size - 1)
            new_values = [row, col]
            if not new_values == previous_Values:
                self.grid[row][col] = 1

            previous_Values = new_values

        self.print_map()

    def reveal(self, user_input: tuple[int, int, int]):
        x, y, z = user_input
        self.grid[x][y] = z
        self.print_map()

    def print_map(self):
        print(" ", " | ".join(str(i) for i in range(self.dim_size)))
        for row_idx, row in enumerate(self.grid):
            print("  " + "-" * (self.dim_size * 4 - 1))
            print(row_idx, " | ".join(str(cell) for cell in row))


@dataclass
class DefineTile:
    dim_size: int

    @staticmethod
    def get_surrounding_coords(x: int, y: int, dim_size: int):
        return [
            (x + i, y + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
            if 0 <= x + i < dim_size
            and 0 <= y + j < dim_size
            and not (i == 0 and j == 0)
        ]

    @staticmethod
    def count_surrounding_bombs(grid: list[list[int]], x: int, y: int) -> int:
        dim_size = len(grid)
        surrounding_bombs = DefineTile.get_surrounding_coords(x, y, dim_size)
        bomb_count = sum(grid[i][j] for i, j in surrounding_bombs if grid[i][j] == 1)
        return bomb_count


def fixInput(x: str, y: str):
    try:
        x_int = int(x)
        y_int = int(y)

        return x_int, y_int

    except ValueError:
        print("Invalid input. Please enter valid integer values.")
        return


def run():
    a = MineSweeper(10)
    while True:
        x_str = input("x: ")
        y_str = input("y: ")
        input_result = fixInput(x_str, y_str)

        if input_result is not None:
            x_int, y_int = input_result
            bomb_count = DefineTile(10).count_surrounding_bombs(a.grid, x_int, y_int)

            a.reveal((x_int, y_int, bomb_count))


if __name__ == "__main__":
    run()
