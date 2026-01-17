import math
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    tgt = int(input_data)
    ring = math.ceil((math.sqrt(tgt) - 1) / 2)
    side_len = (2 * ring) + 1
    ring_max_val = side_len**2
    offset = ring_max_val - tgt

    side_position = offset % (2 * ring)
    offset_from_center = abs(side_position - ring)

    return ring + offset_from_center


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
    print(f"Solution for Day 03, Part One: {result}")


if __name__ == "__main__":
    main()
