import os
from collections import deque


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def generate_hash(input):
    input_data = [ord(str(x)) for x in input] + [17, 31, 73, 47, 23]
    i = 0
    skip = 0
    n = 256
    data = list(range(256))

    for _ in range(64):
        for change in input_data:
            data = data[i:] + data[:i]

            data = data[:change][::-1] + data[change:]
            p = (n - i) % n
            data = data[p:] + data[:p]

            i = (i + change + skip) % n
            skip += 1

    result = ""
    for i in range(16):
        start, end = 16 * i, 16 * (i + 1)

        val = data[start]
        for num in data[start + 1 : end]:
            val ^= num
        result += str(hex(val)[2:].zfill(2))

    return result


def solve(input_data):
    grid = []
    for i in range(128):
        input = f"{input_data}-{i}"
        generated_hash = generate_hash(input)

        row = []
        for h in generated_hash:
            binary = bin(int(h, 16))[2:].zfill(4)
            row += [int(x) for x in binary]

        grid.append(row)

    h = w = 128
    region_id = 0
    seen = set()

    for row in range(h):
        for col in range(w):
            if grid[row][col] == 0:
                continue

            if (row, col) in seen:
                continue

            region_id += 1

            q = deque([(row, col)])
            seen.add((row, col))

            while q:
                r, c = q.popleft()

                grid[r][c] = region_id

                for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                    if not (0 <= nr < h and 0 <= nc < w):
                        continue

                    if grid[nr][nc] == 0:
                        continue

                    if (nr, nc) in seen:
                        continue

                    seen.add((nr, nc))

                    q.append((nr, nc))

    return region_id


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
    print(f"Solution for Day 14, Part Two: {result}")


if __name__ == "__main__":
    main()
