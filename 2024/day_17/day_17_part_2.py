
from ast import Raise
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
    registers = [int(register.split(':')[1]) for register in input_data[0].split("\n")]
    program = [int(x)for x in input_data[1].split(":")[1].split(",")]
    assert program[-2:] == [3, 0]


    def find(target, ans):
        if target == []:
           return ans
        for t in range(8):
            a = ans << 3 | t
            b = 0
            c = 0
            def get_combo(n):
                if 0<= n <= 3: return n
                elif n == 4: return a
                elif n == 5: return b
                elif n == 6: return c
                else:
                    print("THis should not happen")

            output = None

            for pointer in range(0, len(program) - 2, 2):
                inst = program[pointer]
                oper = program[pointer + 1]
                if inst == 0:
                    assert oper == 3
                elif inst == 1:
                    b = b ^ oper
                elif inst == 2:
                    b = get_combo(oper) % 8
                elif inst == 3:
                    raise AssertionError("Program has error")
                elif inst == 4:
                    b = b ^ c
                elif inst == 5:
                    assert output is None
                    output = get_combo(oper) % 8
                elif inst == 6:
                    b = a >> get_combo(oper)
                elif inst == 7:
                    c = a >> get_combo(oper)

                if output == target[-1]:
                    sub = find(target[:-1], a)
                    if sub is None: continue
                    return sub
    print(find(program, 0))






def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 17, Part Two: {result}")

if __name__ == '__main__':
    main()
