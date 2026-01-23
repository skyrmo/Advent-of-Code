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
    # for line in grid:
    #     print("".join(line))
    h, w = len(grid), len(grid[0])

    # region_id = 0
    visited = set()
    result = 0

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

        edges = 0
        diffs = 0
        for r, c in area:
            # print(r, c)
            for nr, nc in [[r - 1, c], [r, c + 1], [r + 1, c], [r, c - 1]]:
                if nr < 0 or nr >= h or nc < 0 or nc >= w:
                    edges += 1

                elif grid[r][c] != grid[nr][nc]:
                    diffs += 1

                else:
                    continue



        print(len(area), edges + diffs)
        return len(area) * (edges + diffs)

    # print(flood((0, 0)))

    for r in range(h):
        for c in range(w):
            if (r, c) not in visited:
                result += flood((r, c))

    return result


    # for line in grid:
    #     print("".join(line))


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 12, Part One: {result}")

if __name__ == '__main__':
    main()
