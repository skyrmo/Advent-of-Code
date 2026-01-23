import os
from collections import defaultdict, deque


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


class DSU:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.ranks = [0] * (n + 1)
        self.number_of_components = n

    def find(self, n):
        # get parent of node
        p = self.parents[n]

        # path compression
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]

        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.ranks[p1] > self.ranks[p2]:
            self.parents[p2] = p1
        elif self.ranks[p2] > self.ranks[p1]:
            self.parents[p1] = p2
        else:
            self.parents[p1] = p2
            self.ranks[p2] += 1

        self.number_of_components -= 1

        return True


def solve(input_data):
    dsu = DSU(len(input_data))

    for line in input_data:
        node, neighbours = int(line.split(" <-> ")[0]), line.split(" <-> ")[1]

        for nbr in [int(n) for n in neighbours.strip().split(", ")]:
            dsu.union(node, nbr)

    return dsu.number_of_components


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
    print(f"Solution for Day 12, Part One: {result}")


if __name__ == "__main__":
    main()
