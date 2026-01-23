import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    final_strings = set()
    keys, string = input_data
    n = len(string)
    swaps = collections.defaultdict(list)
    for line in keys.split("\n"):
        k, v = line.split(" => ")
        swaps[k].append(v)

    for i in range(n):
        for k, v in swaps.items():
            key_len = len(k)
            if n - i - key_len < 0:
                continue

            if string[i : i + key_len] == k:
                for replacement in v:
                    final_strings.add(string[:i] + replacement + string[i + key_len :])

    return len(final_strings)


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
    print(f"Solution for Day 19, Part One: {result}")


if __name__ == "__main__":
    main()
