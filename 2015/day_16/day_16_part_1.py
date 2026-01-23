import os
import re


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


class Sue:
    def __init__(self, id, props):
        self.id = id
        self.props = props

    def __repr__(self):
        return f"Sue {self.id}: {self.props}"


def solve(input_data):
    sues = []
    real_sue = Sue(
        0,
        {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        },
    )

    for line in input_data:
        match = re.match(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", line)

        if match:
            sue_id = match.group(1)
            props = {
                match.group(2): int(match.group(3)),
                match.group(4): int(match.group(5)),
                match.group(6): int(match.group(7)),
            }
            sue = Sue(sue_id, props)
            sues.append(sue)
        else:
            print(f"Invalid input line: {line}")

    max_matches = 0
    result = -1

    for sue in sues:
        matches = 0

        for k, v in real_sue.props.items():
            if k not in sue.props:
                continue

            if sue.props[k] == v:
                matches += 1

        if matches > max_matches:
            max_matches = matches
            result = sue.id

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
    print(f"Solution for Day 16, Part One: {result}")


if __name__ == "__main__":
    main()
