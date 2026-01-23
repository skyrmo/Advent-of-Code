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

    result = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '^':
                start_pos = (r, c)
                grid[r][c] = '.'
                break

    def check_grid(start_pos, obsitcle_pos):
        o_r, o_c = obsitcle_pos
        grid[o_r][o_c] = '#'

        visited = set()

        dir_idx = 0

        q = collections.deque([(start_pos[0], start_pos[1], dir_idx)])

        while q:
            r, c, dir_idx = q.popleft()

            if (r, c, dir_idx) in visited:
                grid[o_r][o_c] = '.'
                return 1

            visited.add((r, c, dir_idx))

            nr = r + dirs[dir_idx][0]
            nc = c + dirs[dir_idx][1]

            if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '.':
                q.append((nr, nc, dir_idx))

            elif 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '#':
                dir_idx = (dir_idx + 1) % 4
                q.append((r, c, dir_idx))


        grid[o_r][o_c] = '.'
        return 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '.' and (r, c) != start_pos:
                result += check_grid(start_pos, (r, c))

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 06, Part Two: {result}")

if __name__ == '__main__':
    main()
