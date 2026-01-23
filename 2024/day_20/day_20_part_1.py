import collections
import os

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

        # return data

def solve(input):
    start = [-1, -1]
    end = [-1, -1]
    walls = []
    h, w = len(input), len(input[0])

    # find start abd end points and replace with '.'
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if input[r][c] == 'S':
                start = [r, c]
                input[r][c] = '.'
            elif input[r][c] == 'E':
                end = [r, c]
                input[r][c] = '.'

    # find all walls that can be passed through.
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if input[r][c] == '#' and ((input[r - 1][c] == '.' and input[r + 1][c] == '.') or (input[r][c - 1] == '.' and input[r][c + 1] == '.')):
                walls.append((r, c))

    # for row in input:
    #     print(*row, sep="")

    grid = [[float('inf')] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if input[r][c] == '#':
                grid[r][c] = -1


    min_steps = float('inf')
    grid_copy = [list(row) for row in grid]
    q = collections.deque([(start[0], start[1], 0)])
    grid_copy[start[0]][start[1]] = 0
    while q:
        r, c, steps = q.popleft()

        if [r, c] == end:
            min_steps = min(min_steps, steps)
            break

        for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
            if 0 <= nr < h and 0 <= nc < w and steps + 1 < grid_copy[nr][nc]:
                q.append((nr, nc, steps + 1))
                grid_copy[nr][nc] = steps + 1

    print(min_steps)

    counts = collections.defaultdict(int)

    for wr, wc in walls:
        grid_copy = [list(row) for row in grid]
        grid_copy[wr][wc] = float('inf')

        q = collections.deque([(start[0], start[1], 0)])
        grid_copy[start[0]][start[1]] = 0

        while q:
            r, c, steps = q.popleft()

            if steps > min_steps:
                continue

            if [r, c] == end:
                diff = min_steps - steps
                counts[diff] += 1
                break

            for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
                if 0 <= nr < h and 0 <= nc < w and steps + 1 < grid_copy[nr][nc]:
                    q.append((nr, nc, steps + 1))
                    grid_copy[nr][nc] = steps + 1


    result = 0
    for k, v in sorted(counts.items()):
        print(k, v)
        if k >= 100:
            result += v

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
    print(f"Solution for Day 20, Part One: {result}")

if __name__ == '__main__':
    main()
