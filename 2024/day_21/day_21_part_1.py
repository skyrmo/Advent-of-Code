from functools import cache
import os
from collections import defaultdict, deque
from itertools import product


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
    num_keypad = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        [None, '0', 'A']
    ]

    dir_keypad = [
        [None, '^', 'A'],
        ['<', 'v', '>']
    ]

    result = 0

    def precompute_keypad(keypad):
        h, w = len(keypad), len(keypad[0])

        positions: dict[str, tuple[int, int]] = {}
        for r in range(h):
            for c in range(w):
                if keypad[r][c]:
                    positions[keypad[r][c]] = (r, c)

        moves = defaultdict(list)

        for s in positions.keys():
            for e in positions.keys():
                if s == e:
                    moves[(s, e)].append('A')
                    continue

                optimal = float('inf')

                q = deque([(positions[s], '')])

                while q:
                    (r, c), path = q.popleft()

                    if len(path) > optimal:
                        continue

                    if (r, c) == positions[e]:
                        moves[(s, e)].append(path + 'A')
                        optimal = min(optimal, len(path))
                        continue

                    for nr, nc, nv in ((r - 1, c, '^'), (r, c + 1, '>'), (r + 1, c, 'v'), (r, c - 1, '<')):
                        if 0 <= nr < h and 0 <= nc < w and keypad[nr][nc]:
                            q.append(((nr, nc), path + nv))

        return moves, positions

    num_moves, num_positions = precompute_keypad(num_keypad)
    dir_moves, dir_positions = precompute_keypad(dir_keypad)
    dir_lengths = {k: len(v[0]) for k, v in dir_moves.items()}

    def solve(string, moves):
        options = [moves[(a, b)] for a, b in zip("A" + string, string)]
        return ["".join(x) for x in product(*options)]

    @cache
    def calculate_length(seq, depth=25):
        if depth == 1:
            return sum(dir_lengths[(a, b)] for a, b in zip('A' + seq, seq))
        length = 0
        for a, b in zip('A' + seq, seq):
            length += min(calculate_length(sub_seq, depth - 1) for sub_seq in dir_moves[(a, b)])

        return length


    for line in input_data:
        inputs = solve(line, num_moves)
        length = min(map(calculate_length, inputs))
        result += length * int(line[:-1])

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
    print(f"Solution for Day 21, Part One: {result}")


if __name__ == '__main__':
    main()
