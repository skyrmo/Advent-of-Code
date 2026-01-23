import os
import collections


def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        # return data


def solve(input_data):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    lookup = {"^": 0, ">": 1, "v": 2, "<": 3}
    moves = [lookup[x] for x in input_data[1] if x != "\n"]

    small_grid = [list(line) for line in input_data[0].split("\n")]
    small_h, small_w = len(small_grid), len(small_grid[0])

    grid = [['.'] * small_w * 2 for _ in range(small_h)]

    start_pos = [-1, -1]
    for r in range(small_h):
        for c in range(small_w):
            if small_grid[r][c] == '@':
                start_pos = [r, 2 * c]
                grid[r][c * 2] = '@'
            elif small_grid[r][c] == '#':
                grid[r][c * 2] = '#'
                grid[r][c * 2 + 1] = '#'
            elif small_grid[r][c] == 'O':
                grid[r][c * 2] = '['
                grid[r][c * 2 + 1] = ']'

    r, c = start_pos
    for move in moves:
        dr, dc = dirs[move]
        targets = [(r, c)]
        valid_move = True
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in targets:
                continue

            if grid[nr][nc] == '#':
                valid_move = False
                break

            if grid[nr][nc] == ']':
                targets.append((nr, nc))
                targets.append((nr, nc - 1))

            if grid[nr][nc] == '[':
                targets.append((nr, nc))
                targets.append((nr, nc + 1))

        if not valid_move:
            continue

        grid_copy = [list(row) for row in grid]

        for br, bc in targets[1:]:
            grid[br][bc] = '.'
        grid[r][c] = '.'
        grid[r + dr][c + dc] = '@'
        for br, bc in targets[1:]:
            grid[br + dr][bc + dc] = grid_copy[br][bc]
        r += dr
        c += dc

    print(sum(100 * r + c for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == '['))


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 15, Part Two: {result}")


if __name__ == '__main__':
    main()
