import os
from collections import deque


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
    line = input_data
    n = len(input_data)
    result = 0

    DIGITS = [
        "-",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    cur_num = deque()
    for i in range(n - 1, -1, -1):
        c = line[i]
        if c in DIGITS:
            cur_num.appendleft(c)
        elif cur_num:
            num = int("".join(list(cur_num)))
            # print(list(cur_num), num)
            result += num
            cur_num.clear()

    if cur_num:
        num = int("".join(list(cur_num)))
        result += num

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 12, Part One: {result}")


if __name__ == "__main__":
    main()
