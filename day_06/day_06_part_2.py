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


def redist(memory, max_idx, n):
    prev_value = memory[max_idx]
    memory[max_idx] = 0

    increase_amount = max(1, prev_value // n)
    cur_idx = (max_idx + 1) % n

    while prev_value > 0:
        memory[cur_idx] += increase_amount
        prev_value -= increase_amount
        cur_idx = (cur_idx + 1) % n

    return memory


def find_max(memory):
    max_idx = 0
    max_val = 0
    for i, value in enumerate(memory):
        if value > max_val:
            max_val = value
            max_idx = i

    return max_idx


def solve(input_data):
    memory = [int(x) for x in input_data.split("\t")]
    n = len(memory)

    seen_states = set()
    while str(memory) not in seen_states:
        seen_states.add(str(memory))

        max_idx = find_max(memory)

        redist(memory, max_idx, n)

    seen_states = set()
    steps = 0

    while str(memory) not in seen_states:
        seen_states.add(str(memory))

        max_idx = find_max(memory)

        redist(memory, max_idx, n)

        steps += 1

    return steps


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
    print(f"Solution for Day 06, Part Two: {result}")


if __name__ == "__main__":
    main()
