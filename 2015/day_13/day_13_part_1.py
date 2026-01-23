import collections
import os
from itertools import permutations


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


def create_dists(input_data):
    people = set()

    for line in input_data:
        split = line.split(" ")
        person = split[0]
        neighbor = split[-1][:-1]

        people.add(person)
        people.add(neighbor)

    people_ids = {name: i for i, name in enumerate(list(people))}
    n = len(people)
    dists = [[0] * n for _ in range(n)]

    for line in input_data:
        split = line.split(" ")
        person = split[0]
        nbr = split[-1][:-1]
        dist = int(split[3])
        if not dist:
            return

        if dist and split[2] == "lose":
            dist = -dist

        person_id = people_ids[person]
        nbr_id = people_ids[nbr]

        dists[person_id][nbr_id] = dist

    return dists


def solve(input_data):
    dists = create_dists(input_data)
    n = len(dists)

    perms = list(permutations(range(n)))

    max_happiness = float("-inf")
    for perm in perms:
        happiness = 0
        for i in range(n):
            happiness += dists[perm[i]][perm[(i + 1) % n]]
            happiness += dists[perm[i]][perm[(i - 1) % n]]
        max_happiness = max(max_happiness, happiness)

    return max_happiness


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
    print(f"Solution for Day 13, Part One: {result}")


if __name__ == "__main__":
    main()
