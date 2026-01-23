
import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):
    lookup = {"^": 0, ">": 1,"v": 2,"<": 3}
    # word_dirs = ['up', 'right', 'down', 'left']

    grid = [list(line) for line in input_data[0].split("\n")]
    moves = [lookup[x] for x in input_data[1] if x != "\n"]

    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    h, w = len(grid), len(grid[0])

    start_pos = [-1, -1]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '@':
                start_pos = [r, c]

    r, c = start_pos
    for move_no, move in enumerate(moves):

        dr, dc = dirs[move]
        nr, nc = r + dr, c + dc
        # print(f"Move:{move_no + 1}-{word_dirs[move]}---------")
        # print(r, c, nr, nc)
        # for row in grid:
        #     print("".join(row))

        if grid[nr][nc] == '.':
            grid[nr][nc] = '@'
            grid[r][c] = '.'
            r, c = nr, nc

        elif grid[nr][nc] == 'O':
            while grid[nr][nc] == 'O':
                nr = nr + dr
                nc = nc + dc

            if grid[nr][nc] == '.':
                grid[nr][nc] = 'O'
                grid[r][c] = '.'
                grid[r + dr][c + dc] = '@'

                r = r + dr
                c = c + dc


    result = 0
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'O':
                result += 100 * r + c

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
    print(f"Solution for Day 15, Part One: {result}")

if __name__ == '__main__':
    main()
