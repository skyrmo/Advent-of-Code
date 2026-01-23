import os
import sys

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
            return data.split('\n')
            # 3. Read as a list of integers
            # return [int(line) for line in data.split('\n')]
            # 4. Read as a list of lists (e.g., for grid-like inputs)
            # return [list(line) for line in data.split('\n')]
            return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def solve(input_data):

    def test_line(line):
        is_safe = True
        x, y = int(line[0]), int(line[1])

        for i in range(1, len(line)):
            a, b = int(line[i - 1]) , int(line[i])

            if abs(a - b) < 1 or abs(a - b) > 3:
                is_safe = False
                break

            if x > y:
                    if a <= b:
                        is_safe = False
                        break

            elif x < y:
                    if a >= b:
                        is_safe = False
                        break

            else:
                is_safe = False
                break
        return is_safe

    # Implement solution here
    lines = [line.split(" ") for line in input_data]
    result = 0

    for line in lines:
        if test_line(line):
            result += 1
        else:
            for i in range(len(line)):
                new_line = line[:i] + line[i + 1:]
                if test_line(new_line):
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
    print(f"Solution for Day 02, Part Two: {result}")

if __name__ == '__main__':
    main()
