import os
import heapq
import collections


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
    start_pos = (h - 2, 1)
    end_pos = (1, w - 2)

    q = [(0, start_pos[0], start_pos[1], 0, 1)]

    lowest_scores = collections.defaultdict(lambda: float('inf'))
    best_score = float('inf')
    backtrack = collections.defaultdict(set)
    end_states = set()

    while q:
        score, r, c, dr, dc = heapq.heappop(q)

        if score > lowest_scores[(r, c, dr, dc)]:
            continue

        lowest_scores[(r, c, dr, dc)] = score

        if (r, c) == end_pos:
            if score > best_score:
                break
            best_score = score
            end_states.add((r, c, dr, dc))


        for new_score, nr, nc, ndr, ndc in ((score + 1, r + dr, c + dc, dr, dc), (score + 1000, r, c, dc, -dr), (score + 1000, r, c, -dc, dr)):
            if grid[nr][nc] == '#':
                continue

            lowest = lowest_scores[(nr, nc, ndr, ndc)]

            if new_score > lowest:
                continue
            elif new_score < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_scores[(nr, nc, ndr, ndc)] = new_score
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc))
            heapq.heappush(q, (new_score, nr, nc, ndr, ndc))

    states = collections.deque(end_states)
    seen = set(end_states)

    while states:
        key = states.popleft()
        for nbr in backtrack[key]:
            if nbr in seen:
                continue
            seen.add(nbr)
            states.append(nbr)

    print(len({(r, c) for r, c, _, _ in seen }))




def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 16, Part Two: {result}")


if __name__ == '__main__':
    main()
