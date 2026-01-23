
import collections
import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):
    bytes = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in input_data]
    h, w = 71, 71

    for k in range(len(bytes)):
        grid = [[float('inf')] * w for _ in range(h)]
        for i in range(k):
            c, r = bytes[i]
            grid[r][c] = 0

        found_route = False

        q = collections.deque([(0, 0, 0)])
        grid[0][0] = 0

        while q:
            r, c, steps = q.popleft()

            if r == h - 1 and c == w - 1:
                found_route = True
                print(k, "Completed", steps)
                # continue

            for nr, nc in ((r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)):
                if 0 <= nr < h and 0 <= nc < w and steps + 1 < grid[nr][nc]:
                    q.append((nr, nc, steps + 1))
                    grid[nr][nc] = steps + 1

        if not found_route:
            print("the maze is bloacked on", k)
            return bytes[k-1][0], bytes[k-1][1]
        # for row in grid:
        #     print(*row, sep=' ')




def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 18, Part One: {result}")

if __name__ == '__main__':
    main()
