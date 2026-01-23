
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
    machines_data = [[s.split(":") for s in d.split("\n")] for d in input_data]
    machines = []

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


    count = 0

    for machine in machines:
        [a_x, a_y], [b_x, b_y], [t_x, t_y] = machine['A'], machine['B'], machine['T']
        result = float('inf')

        m_x = m_y = 0
        i = 0
        while m_x <= t_x and m_y <= t_y:
            if (t_x - m_x) % a_x == 0 and (t_y - m_y) % a_y == 0 and (t_x - m_x) // a_x == (t_y - m_y) // a_y:
                result = min(result, i + ((t_x - m_x) // a_x) * 3)

            m_x += b_x
            m_y += b_y
            i += 1

        count += result if result != float('inf') else 0

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
    print(f"Solution for Day 13, Part One: {result}")

if __name__ == '__main__':
    main()
