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


def generate_hash(input):
    input_data = [ord(str(x)) for x in input] + [17, 31, 73, 47, 23]
    i = 0
    skip = 0
    n = 256
    data = list(range(256))

    for _ in range(64):
        for change in input_data:
            data = data[i:] + data[:i]

            data = data[:change][::-1] + data[change:]
            p = (n - i) % n
            data = data[p:] + data[:p]

            i = (i + change + skip) % n
            skip += 1

    result = ""
    for i in range(16):
        start, end = 16 * i, 16 * (i + 1)

        val = data[start]
        for num in data[start + 1 : end]:
            val ^= num
        result += str(hex(val)[2:].zfill(2))

    return result


def solve(input_data):
    result = 0
    for i in range(128):
        input = f"oundnydw-{i}"
        generated_hash = generate_hash(input)

        for h in generated_hash:
            binary = bin(int(h, 16))[2:].zfill(4)
            # print(h, binary)
            result += binary.count("1")

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
    print(f"Solution for Day 14, Part One: {result}")


if __name__ == "__main__":
    main()
