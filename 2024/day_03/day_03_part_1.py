import os
import sys
import re

def parse_input(file_path):
    # Parse the input file
    try:
        with open(file_path, 'r') as file:
            # Read the entire file
            data = file.read().strip()
            # Choose one of these parsing methods based on input format
            # 1. Read as a single string
            # return data
            # 2. Read as a list of lines
            # return data.split('\n')
            # 3. Read as a list of integers
            # return [int(line) for line in data.split('\n')]
            # 4. Read as a list of lists (e.g., for grid-like inputs)
            # return [list(line) for line in data.split('\n')]
            #
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def solve(input_data):
    result = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, input_data)
    print(matches)
    for match in matches:
        result += int(match[0]) * int(match[1])
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
    print(f"Solution for Day 03, Part One: {result}")

if __name__ == '__main__':
    main()
