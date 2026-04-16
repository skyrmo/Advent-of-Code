import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split(",")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):

    data = [chr(i) for i in range(ord("a"), ord("p") + 1)]

    for instruction in input_data:
        inst = instruction[0]

        if inst == "s":
            steps = int(instruction[1:])
            data = data[-steps:] + data[:-steps]

        elif inst == "p":
            a, b = instruction[1:].split("/")
            # print(instruction, a, b)
            for i in range(len(data)):
                if data[i] == a:
                    data[i] = b
                elif data[i] == b:
                    data[i] = a

        elif inst == "x":
            a, b = [int(x) for x in instruction[1:].split("/")]
            data[a], data[b] = data[b], data[a]

    print("".join(data))


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
    print(f"Solution for Day 16, Part One: {result}")


if __name__ == "__main__":
    main()
