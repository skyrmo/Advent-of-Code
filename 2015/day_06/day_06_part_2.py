import collections
import os
import re


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    grid = [[0] * 1000 for _ in range(1000)]
    result = 0

    for line in input_data:
        regex = r"(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)"
        action, r1, c1, r2, c2 = re.findall(regex, line)[0]

        for r in range(int(r1), int(r2) + 1):
            for c in range(int(c1), int(c2) + 1):
                if action == "toggle":
                    grid[r][c] += 2
                elif action == "turn on":
                    grid[r][c] += 1
                elif action == "turn off":
                    grid[r][c] = max(0, grid[r][c] - 1)

    for r in range(1000):
        for c in range(1000):
            result += grid[r][c]

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, 'sample_input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 06, Part Two: {result}")


if __name__ == "__main__":
    main()
