import os
from collections import defaultdict


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


# class Node:
#     def __init__(self, name, weight, children=[]):
#         self.name = name
#         self.weight = int(weight)
#         self.children = children

#     def __repr__(self):
#         return f"Node({self.name}, {self.weight}, {self.children})"


def solve(input_data):
    in_degrees = defaultdict(int)
    for line in input_data:
        node, children = None, None
        if "->" in line:
            node, children = line.split("->")
            children = children.strip().split(", ")
        else:
            node = line.strip()
            # print(node, children)

        name, weight = node.strip().split(" ")
        weight = int(weight[1:-1].strip())
        # print(line, "---------------")
        # print(name, weight, children)

        if children:
            if name not in in_degrees:
                in_degrees[name] = 0

            for child in children:
                in_degrees[child] += 1

    # for k, v in in_degrees.items():
    # print(k, v)

    # print([k for k, v in in_degrees.items() if v == 0])
    return [k for k, v in in_degrees.items() if v == 0][0]


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
    print(f"Solution for Day 07, Part One: {result}")


if __name__ == "__main__":
    main()
