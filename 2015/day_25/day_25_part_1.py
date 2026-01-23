import collections
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
    tgt_row = 2978 + 3083 - 1
    tgt_col = 3083

    row_len = 1
    row = [20151125]

    while row_len < tgt_row:
        next_row_len = row_len + 1
        next_row = [0] * next_row_len
        next_row[0] = row[-1] * 252533 % 33554393

        for i in range(1, next_row_len):
            next_row[i] = next_row[i - 1] * 252533 % 33554393

        # print(next_row)
        row = next_row
        row_len = next_row_len

    return row[tgt_col - 1]


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    # input_path = os.path.join(script_dir, 'input.txt')
    input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 25, Part One: {result}")


if __name__ == "__main__":
    main()
