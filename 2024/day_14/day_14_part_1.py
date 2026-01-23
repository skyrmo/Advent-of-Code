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
    h, w = 103, 101
    num_iters = 100

    robots = []
    for line in input_data:
        robot = []
        p, v = line.split(" ")
        robot.append([int(x) for x in p.split("=")[1].split(",")])
        robot.append([int(x) for x in v.split("=")[1].split(",")])
        robots.append(robot)

    quads = [0] * 4

    for robot in robots:
        # print(robot)
        p_x, p_y = robot[0]
        v_x, v_y = robot[1]

        p_x += v_x * num_iters
        p_y += v_y * num_iters

        p_x = p_x % w
        p_y = p_y % h

        if p_y < h //2:
            if p_x < w //2:
                quads[0] += 1
            elif p_x > (w //2):
                quads[1] += 1

        elif p_y > (h // 2):
            if p_x < w //2:
                quads[2] += 1
            elif p_x > (w //2):
                quads[3] += 1

    result = 1
    for val in quads:
        result *= val

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
    print(f"Solution for Day 14, Part One: {result}")

if __name__ == '__main__':
    main()
