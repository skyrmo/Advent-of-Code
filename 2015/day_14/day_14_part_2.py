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


class Deer:
    def __init__(self, name, speed, fly_time, rest_time, id):
        self.id = id
        self.name = name
        self.speed = speed
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.distance = 0
        self.fly = fly_time
        self.rest = rest_time
        self.points = 0

    def __repr__(self):
        return f"Deer({self.name}, {self.distance}, {self.fly}, {self.rest}, {self.points})"


def solve(input_data):
    deer = []

    for i, line in enumerate(input_data):
        match = re.match(
            r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.",
            line,
        )

        if match:
            name, speed, fly_time, rest_time = match.groups()
            deer.append(Deer(name, int(speed), int(fly_time), int(rest_time), i))
        else:
            print("Invalid input format")

    max_distance = 0
    for t in range(2503):
        for d in deer:
            if d.fly > 0:
                d.distance += d.speed
                d.fly -= 1

            elif d.rest > 0:
                d.rest -= 1

            if d.fly == 0 and d.rest == 0:
                d.fly = d.fly_time
                d.rest = d.rest_time

            max_distance = max(max_distance, d.distance)

        for d in deer:
            if d.distance == max_distance:
                d.points += 1

    return max([d.points for d in deer])


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
    print(f"Solution for Day 14, Part Two: {result}")


if __name__ == "__main__":
    main()
