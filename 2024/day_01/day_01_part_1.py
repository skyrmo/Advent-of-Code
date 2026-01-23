import os
import sys


def parse_input(file_path):
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()
        # Choose one of these parsing methods based on input format
        # 1. Read as a single string
        # return data
        # 2. Read as a list of lines
        return data.split('\n')
        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]
        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]
        # return data


def solve(input_data):
    # Implement solution here
    l1, l2 = [], []
    for line in input_data:
        split_line = line.split("   ")
        l1.append(int(split_line[0]))
        l2.append(int(split_line[1]))

    l1.sort()
    l2.sort()
    result = 0
    for i in range(len(l1)):
        result += abs(l2[i] - l1[i])

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
    print(f"Solution for Day 01, Part One: {result}")


if __name__ == '__main__':
    main()
