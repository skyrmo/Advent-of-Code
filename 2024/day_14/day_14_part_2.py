import os
import time

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
    h, w = 103, 101

    robots = []
    for line in input_data:
        robot = []
        p, v = line.split(" ")
        robot.append([int(x) for x in p.split("=")[1].split(",")])
        robot.append([int(x) for x in v.split("=")[1].split(",")])
        robots.append(robot)

    for i in range(6000,10000):

        grid = [[0] * w for _ in range(h)]

        for robot in robots:
            p_x, p_y = robot[0]
            v_x, v_y = robot[1]

            p_x += v_x * i
            p_y += v_y * i

            p_x = p_x % w
            p_y = p_y % h

            grid[p_y][p_x] += 1

        # print(f"__iter:{i}__________________________\n")
        for row in grid:
            print("".join([str(x) if x > 0 else '.' for x in row]))
        # print(f"____________________________________\n")
        time.sleep(0.06)


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 14, Part One: {result}")

if __name__ == '__main__':
    main()
