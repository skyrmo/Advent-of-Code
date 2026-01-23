
import os

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

        return data

def solve(input_data):
    # print(input_data)

    keys = []
    locks = []
    for section in input_data:
        grid = [list(line) for line in section.split('\n')]
        if all([x =='#' for x in grid[6]]):
            key = [0] * 5
            for r in range(7 -1, -1, -1):
                for c in range(5):
                    if grid[r][c] == '#':
                        key[c] = 7 - r - 1

            keys.append(key)
        else:
            lock = [0] * 5
            for r in range(7):
                for c in range(5):
                    if grid[r][c] == '#':
                        lock[c] = r

            locks.append(lock)

    #     for row in grid:
    #         print(row)
    #     print("_____________")
    # print(locks)
    # print(keys)
    result = 0
    for lock in locks:
        for key in keys:
            for i in range(5):
                if key[i] +  lock[i] >= 6:
                    result += 1
                    break
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
    print(f"Solution for Day 25, Part One: {result}")

if __name__ == '__main__':
    main()
