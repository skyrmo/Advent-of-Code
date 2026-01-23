import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        return [int(line) for line in data.split(",")]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


#                   |
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 6, 7, 8, 9, 0, 1, 2, 3, 4, 5
# 2, 1, 0, 9, 8, 7, 6, 3, 4, 5
# 8, 7, 6, 3, 4, 5, 2, 1, 0, 9
# change = 6
# i = 6
# n = 10


def solve(input_data):
    i = 0
    skip = 0
    n = 256
    data = list(range(256))

    for change in input_data:
        data = data[i:] + data[:i]

        data = data[:change][::-1] + data[change:]
        p = (n - i) % n
        data = data[p:] + data[:p]

        i = (i + change + skip) % n
        skip += 1

    return data[0] * data[1]


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
    print(f"Solution for Day 10, Part One: {result}")


if __name__ == "__main__":
    main()
