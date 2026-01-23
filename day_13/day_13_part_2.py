import os
from math import gcd


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


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def solve(input_data):
    scanners = []
    for line in input_data:
        time, range_val = map(int, line.split(": "))
        period = 2 * (range_val - 1)
        scanners.append((time, range_val, period))

    scanners.sort(key=lambda x: x[2])

    candidates = [1]
    current_lcm = 1

    for time, _, period in scanners:
        new_lcm = lcm(current_lcm, period)
        stretch_factor = new_lcm // current_lcm
        # print(period, new_lcm, stretch_factor)

        # Stretch candidates to cover the new LCM range
        # For each existing candidate, add multiples of current_lcm
        new_candidates = []
        for candidate in candidates:
            for i in range(stretch_factor):
                new_candidates.append(candidate + i * current_lcm)

        # Filter out candidates that would collide with this scanner
        # A collision occurs when (delay + time) % period == 0
        filtered_candidates = []
        for candidate in new_candidates:
            if (candidate + time) % period != 0:
                filtered_candidates.append(candidate)

        # Update for next iteration
        candidates = filtered_candidates
        current_lcm = new_lcm

    return min(candidates) if candidates else None


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
    print(f"Solution for Day 13, Part Two: {result}")


if __name__ == "__main__":
    main()
