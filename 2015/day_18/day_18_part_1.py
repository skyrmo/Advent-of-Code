import collections
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
        return [list(line) for line in data.split("\n")]

        return data


def solve(grid):
    h, w = len(grid), len(grid[0])

    for _ in range(100):
        next_grid = [row[:] for row in grid]

        for r in range(h):
            for c in range(w):
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

                nbr_count = 0
                for nr, nc in dirs:
                    if not (0 <= nr < h and 0 <= nc < w):
                        continue

                    if grid[nr][nc] == "#":
                        nbr_count += 1

                if grid[r][c] == "#" and nbr_count not in [2, 3]:
                    next_grid[r][c] = "."

                elif grid[r][c] == "." and nbr_count == 3:
                    next_grid[r][c] = "#"

        grid = next_grid

    return sum([row.count("#") for row in grid])


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 18, Part One: {result}")


if __name__ == "__main__":
    main()
