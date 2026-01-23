from collections import defaultdict
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):
    values = defaultdict(bool)
    for line in input_data[0].split("\n"):
        k, v = line.split(":")
        values[k] = bool(int(v))

    print(*values.items(), sep="\n")

    inst = {}
    zeds = []
    for instruction in input_data[1].split("\n"):
        a, op, b, _ , res = instruction.split(" ")
        inst[res] = (op, a, b)
        if res[0] == 'z':
            zeds.append(res)
        if a[0] == 'z':
            zeds.append(a)
        if b[0] == 'z':
            zeds.append(b)

    def process(val):
        if val in values:
            return values[val]

        (op, a, b) = inst[val]

        if op == 'AND':
            values[val] = process(a) and process(b)
        elif op == 'OR':
            values[val] = process(a) or process(b)
        elif op == 'XOR':
            values[val] = process(a) != process(b)

        return values[val]

    print(int("".join(['1' if process(z) else '0' for z in sorted(set(zeds), reverse=True)]), 2))



def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 24, Part One: {result}")

if __name__ == '__main__':
    main()
