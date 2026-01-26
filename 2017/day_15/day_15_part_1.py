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


def compare_lower_16(a, b):
    mask = 0xFFFF  # 16 bits set to 1 (65535)
    return (a & mask) == (b & mask)


def solve(input_data):
    a = 512
    b = 191

    result = 0

    a_factor = 16807
    b_factor = 48271

    modulo = 2147483647

    for i in range(40000000):
        a = (a * a_factor) % modulo
        b = (b * b_factor) % modulo

        if (a & 0xFFFF) == (b & 0xFFFF):
            result += 1

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
    print(f"Solution for Day 15, Part One: {result}")


if __name__ == "__main__":
    main()
