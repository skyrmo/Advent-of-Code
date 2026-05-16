import math
import os
import re
from collections import defaultdict


class Particle:
    def __init__(self, id, vals):
        self.id = id
        self.pos = {"x": vals[0], "y": vals[1], "z": vals[2]}
        self.vel = {"x": vals[3], "y": vals[4], "z": vals[5]}
        self.acc = {"x": vals[6], "y": vals[7], "z": vals[8]}


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")


def solve_q(dp, dv, da):
    a = da
    b = 2 * dv + a
    c = 2 * dp

    if a == 0:
        if b == 0:
            return []
        t = -c / b
        return [t] if t > 0 else []

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return []

    t1 = (-b + math.sqrt(discriminant)) / (2 * a)
    t2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return [t for t in [t1, t2] if t > 0]


def is_integer(t, epsilon=1e-6):
    return abs(t - round(t)) < epsilon


def common_t(A, B):
    results = []
    for axis in ["x", "y", "z"]:
        da = A.acc[axis] - B.acc[axis]
        dv = A.vel[axis] - B.vel[axis]
        dp = A.pos[axis] - B.pos[axis]
        ts = solve_q(dp, dv, da)
        ts = {round(t) for t in ts if is_integer(t)}
        results.append(ts if ts or (da or dv or dp) else None)

    valid = [r for r in results if r is not None]
    if not valid:
        return set()
    return valid[0].intersection(*valid[1:])


def solve(input_data):
    collisions = defaultdict(list)
    dead = set()

    particles = []
    for i, line in enumerate(input_data):
        vals = list(map(int, re.findall(r"-?\d+", line)))
        particles.append(Particle(i, vals))

    n = len(particles)

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            results = common_t(particles[i], particles[j])
            for t in results:
                collisions[t].append((i, j))

    for t in sorted(collisions.keys()):
        this_t_dead = set()
        this_t = collisions[t]
        for i, j in this_t:
            if i in dead or j in dead:
                continue
            this_t_dead.add(i)
            this_t_dead.add(j)

        dead.update(this_t_dead)

    return n - len(dead)


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
