import math
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def check_nbrs(pos, grid) -> int:
    r, c = pos
    dirs = [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c - 1),
        (r, c + 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    ]
    return sum(grid.get((nr, nc), 0) for nr, nc in dirs)


def solve(input_data):
    grid = {(0, 0): 1}

    dir = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    r, c = 0, 0

    while grid[(r, c)] <= int(input_data):
        r = r + dirs[dir][0]
        c = c + dirs[dir][1]

        grid[(r, c)] = check_nbrs((r, c), grid)

        directions = [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]
        total_nbrs = sum(1 if (nr, nc) in grid else 0 for nr, nc in directions)
        if total_nbrs == 1:
            dir = (dir + 1) % 4

    return grid[(r, c)]


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, 'sample_input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 03, Part Two: {result}")


if __name__ == "__main__":
    main()
