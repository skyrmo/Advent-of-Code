from collections import defaultdict
import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):
    adj = defaultdict(list)
    for line in input_data:
        a, b = line.split("-")
        adj[a].append(b)
        adj[b].append(a)

    triangles = []
    nodes = list(adj.keys())
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            for k in range(j + 1, len(nodes)):
                a, b, c = nodes[i], nodes[j], nodes[k]
                if a in adj[b] and a in adj[c] and b in adj[c]:
                    if a[0] == 't' or b[0] == 't' or c[0] == 't':
                        triangles.append((a, b, c))

    return len(triangles)

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 23, Part One: {result}")

if __name__ == '__main__':
    main()
