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


weights = defaultdict(int)
adj = defaultdict(list)
seen_result = False
result = None


def dfs(node):
    weight = weights[node]

    child_weights = [(child, dfs(child)) for child in adj[node]]
    child_weights_equal = all([w == child_weights[0][1] for c, w in child_weights])

    if child_weights_equal:
        weight += sum(w for c, w in child_weights)
    else:
        for i, (c, w) in enumerate(child_weights):
            print(c, w, weights[c])
        print("Result ^^^^^^^")

    return weight


def solve(input_data):
    for line in input_data:
        node = line.split(")")
        name, weight = node[0].strip().split("(")
        weights[name.strip()] = int(weight)

    for line in input_data:
        if "->" in line:
            node, children = line.split("->")
            children = children.strip().split(", ")
            name, _ = node.split(" (")
            name = name.strip()

            if children:
                for child in children:
                    adj[name].append(child.strip())

    dfs("ahnofa")
    return result


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
    print(f"Solution for Day 07, Part Two: {result}")


if __name__ == "__main__":
    main()
