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
    dirs = list(input_data)
    n = len(dirs)

    s_r, s_c = 0, 0
    r_r, r_c = 0, 0

    seen = set([(s_r, s_c)])

    for i in range(0, n, 2):
        s_dir = dirs[i]
        r_dir = dirs[i + 1]

        if s_dir == "^":
            s_r += 1
        elif s_dir == ">":
            s_c += 1
        elif s_dir == "v":
            s_r -= 1
        elif s_dir == "<":
            s_c -= 1

        if r_dir == "^":
            r_r += 1
        elif r_dir == ">":
            r_c += 1
        elif r_dir == "v":
            r_r -= 1
        elif r_dir == "<":
            r_c -= 1

        seen.add((s_r, s_c))
        seen.add((r_r, r_c))

    return len(seen)


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
    print(f"Solution for Day 03, Part Two: {result}")


if __name__ == "__main__":
    main()
