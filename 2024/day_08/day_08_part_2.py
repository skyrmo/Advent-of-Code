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
    pairs = collections.defaultdict(list)

    for r in range(h):
        for c in range(w):
            char = grid[r][c]
            if char != '.':
                pairs[char].append((r, c))

    for char in pairs:
        for i in range(len(pairs[char])):
            for j in range(len(pairs[char])):
                if i != j:
                    ar, ac = pairs[char][i]
                    br, bc = pairs[char][j]
                    dr, dc = (ar - br), (ac - bc)

                    nr, nc = br - dr, bc - dc
                    while 0 <= nr < h and 0 <= nc < w:
                        if grid[nr][nc] == '.':
                            grid[nr][nc] = '#'
                        nr -= dr
                        nc -= dc
    result = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] != '.':
                result += 1

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
    print(f"Solution for Day 08, Part Two: {result}")

if __name__ == '__main__':
    main()
