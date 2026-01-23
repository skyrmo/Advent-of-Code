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
    result = []
    new_string = list(input_data)

    for _ in range(50):
        input = new_string
        new_string = []
        cur_count = 1
        prev_char = input[0]
        for char in input[1:]:
            if char == prev_char:
                cur_count += 1
            else:
                new_string.append(str(cur_count))
                new_string.append(prev_char)
                prev_char = char
                cur_count = 1

        new_string.append(str(cur_count))
        new_string.append(prev_char)
        cur_count = 1
        result = new_string

    return len(result)


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    # input_path = os.path.join(script_dir, 'input.txt')
    input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 10, Part Two: {result}")


if __name__ == "__main__":
    main()
