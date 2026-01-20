import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split(",")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


dirs = {
    "n": (-1, 0),
    "s": (1, 0),
    "ne": (-1, 1),
    "nw": (0, -1),
    "se": (0, 1),
    "sw": (1, -1),
}


def solve(input_data):
    r, c = 0, 0

    for dir in input_data:
        r = r + dirs[dir][0]
        c = c + dirs[dir][1]

    return (abs(r) + abs(c) + abs(c + r)) // 2


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
    print(f"Solution for Day 11, Part One: {result}")


if __name__ == "__main__":
    main()
