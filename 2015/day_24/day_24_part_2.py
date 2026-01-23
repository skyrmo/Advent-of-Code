import collections
import math
import os
from itertools import combinations


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        return [int(line) for line in data.split("\n")]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(nums):
    n = len(nums)
    tgt = sum(nums) // 4
    valid_combos = []
    found = False

    for i in range(n):
        valid_combos = []

        for combo in combinations(nums, i):
            if sum(combo) == tgt:
                valid_combos.append((combo, math.prod(combo)))
                found = True

        if found:
            break

    valid_combos.sort(key=lambda x: x[1])

    return valid_combos[0][1]


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
    print(f"Solution for Day 24, Part Two: {result}")


if __name__ == "__main__":
    main()
