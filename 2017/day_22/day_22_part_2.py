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
        return [list(line) for line in data.split("\n")]

        return data


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solve(input_data):
    h = len(input_data)
    w = len(input_data[0])

    state = {}

    for r in range(h):
        for c in range(w):
            if input_data[r][c] == "#":
                state[(r - (h // 2), c - (w // 2))] = "infected"

    node = ((0, 0), 0)
    result = 0

    def take_turn(node):
        pos, dir = node

        nonlocal result

        cell_state = state.get(pos, "clean")

        if cell_state == "clean":
            dir = (dir + 3) % 4
            state[pos] = "weakened"

        elif cell_state == "infected":
            dir = (dir + 1) % 4
            state[pos] = "flagged"

        elif cell_state == "flagged":
            dir = (dir + 2) % 4
            state[pos] = "clean"

        elif cell_state == "weakened":
            state[pos] = "infected"
            result += 1

        new_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        return (new_pos, dir)

    for _ in range(10000000):
        node = take_turn(node)

    return result


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
    print(f"Solution for Day 22, Part One: {result}")


if __name__ == "__main__":
    main()
