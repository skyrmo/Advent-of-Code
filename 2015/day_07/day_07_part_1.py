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


cache = {}


def calculate(key, wires) -> int:
    if key in cache:
        return cache[key]

    if key.isdigit():
        return int(key)

    input = wires[key]

    if "NOT " in input:
        cache[key] = ~calculate(input[4:], wires)
        return cache[key]

    elif " OR " in input:
        input1, input2 = input.split(" OR ")
        cache[key] = calculate(input1, wires) | calculate(input2, wires)
        return cache[key]

    elif " AND " in input:
        input1, input2 = input.split(" AND ")
        cache[key] = calculate(input1, wires) & calculate(input2, wires)
        return cache[key]

    elif " RSHIFT " in input:
        input1, input2 = input.split(" RSHIFT ")
        cache[key] = calculate(input1, wires) >> int(input2)
        return cache[key]

    elif " LSHIFT " in input:
        input1, input2 = input.split(" LSHIFT ")
        cache[key] = calculate(input1, wires) << int(input2)
        return cache[key]

    else:
        return calculate(input, wires)


# PLEASE NOTE, INPUT CHANGED TO COMPLETE PART TWO
def solve(input_data):
    wires = {}
    for line in input_data:
        input, assigned_to = line.split(" -> ")
        wires[assigned_to] = input

    return calculate("a", wires)


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
    print(f"Solution for Day 07, Part One: {result}")


if __name__ == "__main__":
    main()
