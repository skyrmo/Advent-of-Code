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


def dp(containers, idx, eggnog, path):
    if eggnog == 0:
        return len(path)

    if eggnog < 0:
        return float("inf")

    if eggnog > 0 and not containers:
        return float("inf")

    result = float("inf")
    for i in range(idx, len(containers)):
        new_container, id = containers[i]

        new_path = path.copy()
        new_path.add((new_container, id))

        result = min(result, dp(containers, i + 1, eggnog - new_container, new_path))

    return result


def solve(input_data):
    containers = []

    for i, container in enumerate(input_data):
        containers.append((int(container), i))

    return dp(containers, 0, 150, set())


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
    print(f"Solution for Day 17, Part Two: {result}")


if __name__ == "__main__":
    main()
