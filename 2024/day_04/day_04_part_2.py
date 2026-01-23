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

        return data

def solve(input_data):
    grid = input_data
    h, w = len(grid), len(grid[0])
    result = 0

    for r in range(1, h - 1):
        for c in range(1, w - 1):
            if grid[r][c] == 'A':
                group_one = [grid[r-1][c-1], grid[r+1][c+1]]
                group_two = [grid[r+1][c-1], grid[r-1][c+1]]

                if 'M' in group_one and 'S' in group_one and 'M' in group_two and 'S' in group_two:
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
    print(f"Solution for Day 04, Part Two: {result}")

if __name__ == '__main__':
    main()
