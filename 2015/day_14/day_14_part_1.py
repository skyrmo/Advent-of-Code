import collections
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


def solve(input_data):
    results = {}
    for line in input_data:
        match = re.match(
            r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            line,
        )

        if match:
            name, speed, fly_time, rest_time = match.groups()

            dist = 0
            rest = int(rest_time)
            fly = int(fly_time)

            for _ in range(2503):
                if fly > 0:
                    dist += int(speed)
                    fly -= 1

                elif rest > 0:
                    rest -= 1

                if rest == 0:
                    fly = int(fly_time)
                    rest = int(rest_time)

            results[name] = dist

        else:
            print("Invalid input format")

    return max(results.values())


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
    print(f"Solution for Day 14, Part One: {result}")


if __name__ == "__main__":
    main()
