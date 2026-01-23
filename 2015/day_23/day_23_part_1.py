import os
import re


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
    instructions = []
    for line in input_data:
        m = re.search(r"\b([ab])\b", line)
        n = re.search(r"([+-]\d+)", line)

        instruction = line[:3]
        register = m.group(1) if m else None
        jump = n.group(0) if n else None

        # print(line)
        # print(instruction, register, jump)
        instructions.append((instruction, register, jump))

    idx = 0
    n = len(instructions)
    registers = {"a": 0, "b": 0}

    while idx < n:
        instruction, reg, jump = instructions[idx]
        # print(idx, instruction, register, jump)

        if instruction == "hlf":
            registers[reg] //= 2
        elif instruction == "tpl":
            registers[reg] *= 3
        elif instruction == "inc":
            registers[reg] += 1
        elif instruction == "jmp":
            idx += int(jump)
            continue
        elif instruction == "jie":
            if registers[reg] % 2 == 0:
                idx += int(jump)
                continue
        elif instruction == "jio":
            if registers[reg] == 1:
                idx += int(jump)
                continue
        else:
            print("Invalid instruction")

        idx += 1

    return registers["b"]


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
    print(f"Solution for Day 23, Part One: {result}")


if __name__ == "__main__":
    main()
