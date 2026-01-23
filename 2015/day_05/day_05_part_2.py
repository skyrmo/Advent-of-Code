import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    result = 0
    for line in input_data:
        n = len(line)

        start_ss = line[0] + line[1]
        substrings = {start_ss: 0}
        repeated_pair = False
        trio = False

        for i in range(2, n):
            ss = line[i - 1] + line[i]
            if ss in substrings and i - 1 - substrings[ss] >= 2:
                repeated_pair = True
            else:
                substrings[ss] = i - 1

            if line[i] == line[i - 2]:
                trio = True

            if repeated_pair and trio:
                result += 1
                break

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
    print(f"Solution for Day 05, Part Two: {result}")


if __name__ == "__main__":
    main()
