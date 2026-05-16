import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")


def solve(input_data):
    registers = {}
    played = []

    instructions = []
    for line in input_data:
        line = [int(x) if x.lstrip("-").isdigit() else x for x in line.split()]
        instructions.append(line)

    n = len(instructions)
    i = 0

    while 0 <= i < n:
        inst = instructions[i]

        if inst[0] == "snd":
            x = inst[1]
            played.append((x, registers[x]))

        elif inst[0] == "set":
            x = inst[1]
            y = inst[2]
            registers[x] = y if isinstance(y, int) else registers[y]

        elif inst[0] == "add":
            x = inst[1]
            y = inst[2]
            registers[x] = registers.get(x, 0) + (
                y if isinstance(y, int) else registers[y]
            )

        elif inst[0] == "mul":
            x = inst[1]
            y = inst[2]
            registers[x] = registers.get(x, 0) * (
                y if isinstance(y, int) else registers[y]
            )

        elif inst[0] == "mod":
            x = inst[1]
            y = inst[2]
            k = y if isinstance(y, int) else registers[y]
            if k != 0:
                registers[x] = registers.get(x, 0) % k

        elif inst[0] == "rcv":
            x = inst[1]
            if registers.get(x, 0) != 0 and played:
                return played[-1][1]

        elif inst[0] == "jgz":
            x = inst[1]
            y = inst[2]
            if registers.get(x, 0) != 0:
                i += y
                continue

        i += 1


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
    print(f"Solution for Day 18, Part One: {result}")


if __name__ == "__main__":
    main()
