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

def solve(grid):
    h, w = len(grid), len(grid[0])

    # map to store distances for each cell of the path.
    dists = [[float('inf')] * w for _ in range(h)]

    # mark the walls as -1 so that they are blocked
    start = end = (-1, -1)
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '#':
                dists[r][c] = -1

            elif grid[r][c] == 'S':
                start = (r, c)
                dists[r][c] = 0

            elif grid[r][c] == 'E':
                end = (r, c)

    q = collections.deque([(start, 0)])

    (r, c) =  start

    while (r, c) != end:
        for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
               continue

            if dists[nr][nc] < dists[r][c]:
                continue

            dists[nr][nc] = dists[r][c] + 1
            r, c = nr, nc

    for row in dists:
        print(*row, sep=" ")

    result = 0

    for r in range(h):
        for c in range(w):
            if grid[r][c] == '#':
                continue

            for radius in range(2, 21):
                for dr in range(radius + 1):
                    dc = radius - dr
                    for nr, nc in {(r + dr, c + dc), (r + dr, c - dc), (r - dr, c + dc), (r - dr, c - dc)}:
                        if nr < 0 or nc < 0 or nr >= h or nc >= w:
                            continue

                        if grid[nr][nc] == '#':
                            continue

                        # print(r, c, nr, nc)
                        if dists[r][c] - dists[nr][nc] >= 100 + radius:
                            result += 1
    print(result)
    return result

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the grid file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 20, Part Two: {result}")

if __name__ == '__main__':
    main()
