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
        return [[int(x) for x in list(line)] for line in data.split('\n')]

        return data

def solve(grid):
        h, w = len(grid), len(grid[0])
        result = 0

        def search_trail(start_pos):
            q = collections.deque()
            q.append(start_pos)
            count = 0

            while q:
                r, c = q.popleft()

                if grid[r][c] == 9:
                    count += 1
                    continue

                for nr, nc in ((r - 1, c), (r, c + 1),(r + 1, c),(r, c - 1)):
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == grid[r][c] + 1:
                        q.append((nr, nc))

            return count

        # print(search_trail((0, 2)))

        for r in range(h):
            for c in range(w):
                if grid[r][c] == 0:
                    result += search_trail((r, c))

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
    print(f"Solution for Day 10, Part Two: {result}")

if __name__ == '__main__':
    main()
