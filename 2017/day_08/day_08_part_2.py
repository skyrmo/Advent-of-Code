import os
import re
from collections import defaultdict


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
    registers = defaultdict(int)
    op_lookup = {
        "inc": 1,
        "dec": -1,
    }
    result = float("-inf")

    for line in input_data:
        matches = re.match(
            r"(\w+) (\w+) (-?\d+) if (\w+) (<=|>=|==|!=|<|>) (-?\d+)", line
        )
        if matches:
            (
                reg,
                op,
                val,
                condition_reg,
                condition,
                condition_val,
            ) = matches.groups()

            val, condition_val = int(val), int(condition_val)

            if condition == "<" and registers[condition_reg] < condition_val:
                registers[reg] += val * op_lookup[op]

            elif condition == ">" and registers[condition_reg] > condition_val:
                registers[reg] += val * op_lookup[op]

            elif condition == "<=" and registers[condition_reg] <= condition_val:
                registers[reg] += val * op_lookup[op]
            #
            elif condition == ">=" and registers[condition_reg] >= condition_val:
                registers[reg] += val * op_lookup[op]

            elif condition == "!=" and registers[condition_reg] != condition_val:
                registers[reg] += val * op_lookup[op]

            elif condition == "==" and registers[condition_reg] == condition_val:
                registers[reg] += val * op_lookup[op]

            result = max(result, max([v for v in registers.values()]))

    return result


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
    print(f"Solution for Day 08, Part Two: {result}")


if __name__ == "__main__":
    main()
