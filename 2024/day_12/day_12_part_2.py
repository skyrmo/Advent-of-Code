import collections
import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        return [list(line) for line in data.split('\n')]

        # return data

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = set()
    result = 0

    dirs = {
        1: [-1, 0],
        2: [0, 1],
        3: [1, 0],
        4: [0, -1],
    }

    def flood(start_pos):
        q = collections.deque([start_pos])
        visited.add(start_pos)
        area = set([start_pos])

        while q:
            r, c = q.popleft()
            for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
                if 0 <= nr < h and 0<= nc < w and grid[r][c] == grid[nr][nc] and (nr, nc) not in area:
                    area.add((nr, nc))
                    visited.add((nr, nc))
                    q.append((nr, nc))


        edges = collections.defaultdict(list)

        for r, c in area:
            for dir_id, (dr, dc) in dirs.items() :
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= h or nc < 0 or nc >= w or grid[r][c] != grid[nr][nc] :
                    edges[dir_id].append((r, c))


        count = 0
        for dir_id in [1, 3]:
            sorted_edges = sorted(edges[dir_id], key=lambda x: (x[0], x[1]))
            count += 1
            for i in range(1, len(sorted_edges)):
                edge = sorted_edges[i]
                prev_edge = sorted_edges[i - 1]

                if edge[0] != prev_edge[0]:
                    count += 1
                elif edge[1] - prev_edge[1] > 1:
                    count += 1

        for dir_id in [2, 4]:
            sorted_edges = sorted(edges[dir_id], key=lambda x: (x[1], x[0]))
            count += 1
            for i in range(1, len(sorted_edges)):
                edge = sorted_edges[i]
                prev_edge = sorted_edges[i - 1]

                if edge[1] != prev_edge[1]:
                    count += 1
                elif edge[0] - prev_edge[0] > 1:
                    count += 1

        return len(area) * count


    for r in range(h):
        for c in range(w):
            if (r, c) not in visited:
                result += flood((r, c))

    return result


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 12, Part Two: {result}")

if __name__ == '__main__':
    main()
