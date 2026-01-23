import os
import collections

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        return [list(line) for line in data.split('\n')]

        return data

def solve(grid):
    h, w = len(grid), len(grid[0])
    start_pos = (-1, -1)

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    visited = set()

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '^':
                start_pos = (r, c)
                break

    dir_idx = 0
    q = collections.deque([start_pos])
    grid[start_pos[0]][start_pos[1]] = '.'

    while q:
        r, c = q.popleft()

        visited.add((r, c))

        nr = r + dirs[dir_idx][0]
        nc = c + dirs[dir_idx][1]

        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '.':
            q.append((nr, nc))

        elif 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '#':
            dir_idx = (dir_idx + 1) % 4
            nr = r + dirs[dir_idx][0]
            nc = c + dirs[dir_idx][1]
            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '.':
                q.append((nr, nc))

    return len(visited)


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 06, Part One: {result}")

if __name__ == '__main__':
    main()
