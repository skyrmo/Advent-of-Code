from collections import defaultdict
from collections import deque
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

def find_maximum_clique(graph):
    def bron_kerbosch_recursive(current_clique, potential_nodes, excluded_nodes, largest_found):
        # found a maximal clique
        if not potential_nodes and not excluded_nodes:
            if len(current_clique) > len(largest_found[0]):
                largest_found[0] = current_clique.copy()
            return

        # Pivot optimization: choose a vertex that's connected to many potential nodes
        if potential_nodes:
            # Find the node (from potential + excluded) that has the most connections
            # to nodes in our potential set
            pivot_node = max(potential_nodes | excluded_nodes,
                           key=lambda node: len(set(graph[node]) & potential_nodes),
                           default=None)
            pivot_neighbors = set(graph[pivot_node]) if pivot_node else set()
        else:
            pivot_neighbors = set()

        # Try adding each potential node that isn't connected to our pivot
        # (This optimization reduces the number of branches we need to explore)
        for node in list(potential_nodes - pivot_neighbors):
            node_neighbors = set(graph[node])

            # Add this node to our current clique
            current_clique.add(node)

            # Recursive call:
            # - Only consider nodes that are neighbors of our current node
            # - This ensures we maintain the clique property
            new_potential = potential_nodes & node_neighbors
            new_excluded = excluded_nodes & node_neighbors
            bron_kerbosch_recursive(current_clique, new_potential, new_excluded, largest_found)

            # Backtrack: remove node from current clique and move it to excluded
            current_clique.remove(node)
            potential_nodes.remove(node)
            excluded_nodes.add(node)

    # Initialize with empty clique
    largest_clique = [set()]  # Using list for mutable reference
    all_nodes = set(graph.keys())

    # Start the recursive process:
    # - Empty current clique
    # - All nodes are potential
    # - No nodes excluded yet
    bron_kerbosch_recursive(set(), all_nodes, set(), largest_clique)

    return largest_clique[0]


def solve(input_data):
    adj = defaultdict(set)
    for line in input_data:
        a, b = line.split("-")
        adj[a].add(b)
        adj[b].add(a)

    max_clique = find_maximum_clique(adj)

    return ",".join(sorted(max_clique))



def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 23, Part Two: {result}")

if __name__ == '__main__':
    main()
