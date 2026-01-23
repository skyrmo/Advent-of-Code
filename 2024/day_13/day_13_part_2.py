
import os
import math

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
    machines_data = [[s.split(":") for s in d.split("\n")] for d in input_data]
    machines = []
    count = 0

    for machine_data in machines_data:
        machine = {}
        for field in machine_data:
            if field[0] == 'Button A':
                [x_part, y_part] = field[1].split(", ")
                machine['A'] = [int(x_part.split("+")[1]), int(y_part.split("+")[1])]

            elif field[0] == 'Button B':
                [x_part, y_part] = field[1].split(", ")
                machine['B'] = [int(x_part.split("+")[1]), int(y_part.split("+")[1])]

            else:
                [x_part, y_part] = field[1].split(", ")
                machine['T'] = [int(x_part.split("=")[1]), int(y_part.split("=")[1])]

        machines.append(machine)


    for machine in machines:
        [a_x, a_y], [b_x, b_y], [t_x, t_y] = machine['A'], machine['B'], machine['T']
        t_x += 10000000000000
        t_y += 10000000000000
        det = (a_x * b_y) - (b_x * a_y)

        i = math.floor(((b_y * t_x) - (b_x * t_y)) / det)
        j = math.floor(((a_y * -1) * t_x + a_x * t_y) / det)
        if a_x * i + b_x * j == t_x and a_y * i + b_y * j == t_y:
            count += i * 3 + j


    return count

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 13, Part Two: {result}")

if __name__ == '__main__':
    main()
