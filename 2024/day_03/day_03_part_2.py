import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()
        # Choose one of these parsing methods based on input format
        # 1. Read as a single string
        # return data
        # 2. Read as a list of lines
        # return data.split('\n')
        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]
        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]
        return data


def solve(input_data):
    instructions = []
    include = True
    result = 0

    for i in range(len(input_data)):
        if input_data[i:i + 4] == "do()":
            instructions.append(True)
        elif input_data[i:i + 7] == "don't()":
            instructions.append(False)
        elif input_data[i:i + 4] == "mul(":
            j = i + 4
            nums = ['', '']

            while input_data[j].isdigit():
                nums[0] += input_data[j]
                j += 1

            if input_data[j] != ',':
                continue

            j += 1
            while input_data[j].isdigit():
                nums[1] += input_data[j]
                j += 1

            if input_data[j] != ')':
                continue

            instructions.append([int(x) for x in nums])

    for instruction in instructions:
        if type(instruction) == bool:
            include = instruction
        elif include:
            result += instruction[0] * instruction[1]

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 03, Part Two: {result}")

if __name__ == '__main__':
    main()
