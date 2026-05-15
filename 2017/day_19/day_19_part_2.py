import os
from collections import deque


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        return [list(line) for line in data.split("\n")]

        # return data


def solve(grid):
    h = len(grid)
    w = max(len(line) for line in grid)

    for line in grid:
        line += [" "] * (w - len(line))

    start_pos = (0, grid[0].index("|"))
    moves = deque([(start_pos, (1, 0))])

    visited = set()
    visited.add(start_pos)

    result = 0

    while moves:
        (r, c), (dr, dc) = moves.popleft()

        result += 1

        if grid[r][c] == "+":
            for ndr, ndc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if not (0 <= r + ndr < h and 0 <= c + ndc < w):
                    continue

                if (r + ndr, c + ndc) in visited:
                    continue

                if grid[r + ndr][c + ndc] == " ":
                    continue

                dr, dc = ndr, ndc

        if not (0 <= r + dr < h and 0 <= c + dc < w):
            continue

        if grid[r + dr][c + dc] == " ":
            continue

        moves.append(((r + dr, c + dc), (dr, dc)))
        visited.add((r + dr, c + dc))

    return result


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
    print(f"Solution for Day 19, Part One: {result}")


if __name__ == "__main__":
    main()
