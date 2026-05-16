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


class Particle:
    def __init__(self, id, vals):
        self.id = id
        self.pos = {"x": vals[0], "y": vals[1], "z": vals[2]}
        self.vel = {"x": vals[3], "y": vals[4], "z": vals[5]}
        self.acc = {"x": vals[6], "y": vals[7], "z": vals[8]}
        self.a_sum = abs(self.acc["x"]) + abs(self.acc["y"]) + abs(self.acc["z"])
        self.v_max = max(abs(self.vel["x"]), abs(self.vel["y"]), abs(self.vel["z"]))
        self.p_min = min(self.pos["x"], self.pos["y"], self.pos["z"])

    def __repr__(self):
        return f"Particle(id={self.id}, p={self.pos}, v={self.vel}, a={self.acc})"


def solve(input_data):
    particles = []
    for i, line in enumerate(input_data):
        vals = list(map(int, re.findall(r"-?\d+", line)))

        p = Particle(i, vals)

        particles.append(p)

    particles.sort(key=lambda p: (p.a_sum, -p.v_max, p.p_min))

    return particles[0].id


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
    print(f"Solution for Day 20, Part One: {result}")


if __name__ == "__main__":
    main()
