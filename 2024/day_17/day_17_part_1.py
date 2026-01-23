
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
    outputs = []

    def get_combo_operand(num):
        if 0 <= num <= 3:
            return num
        elif 4 <= num <= 6:
            return registers[num - 4]
        else:
            print("this should never happen")
            return -1

    p = 0
    while p < len(program) - 1:
        opcode = program[p]
        operand = program[p + 1]
        # print(opcode, operand)

        if opcode == 0:
            # The adv instruction (opcode 0) performs division. The numerator is the value in the A register.
            # The denominator is found by raising 2 to the power of the instruction's combo operand.
            # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
            # The result of the division operation is truncated to an integer and then written to the A register.
            numerator = registers[0]
            denominator = 2 ** get_combo_operand(operand)
            result = numerator // denominator
            registers[0] = result

        elif opcode == 1:
            # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's
            # literal operand, then stores the result in register B.
            registers[1] = registers[1] ^ operand

        elif opcode == 2:
            # The bst instruction (opcode 2) calculates the value of its combo operand
            # modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
            registers[1] = get_combo_operand(operand) % 8

        elif opcode == 3:
            # The jnz instruction (opcode 3) does nothing if the A register is 0.
            # However, if the A register is not zero, it jumps by setting the instruction pointer to the
            # value of its literal operand; if this instruction jumps, the instruction pointer is not
            # increased by 2 after this instruction.
            if registers[0] == 0:
                p += 2
                continue
            elif operand != p:
                p = operand
                continue
            else:
                p += 2
                continue

        elif opcode == 4:
            # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C,
            # then stores the result in register B. (For legacy reasons, this instruction reads an
            # operand but ignores it.)
            registers[1] = registers[1] ^ registers[2]

        elif opcode == 5:
            # The out instruction (opcode 5) calculates the value of its combo operand modulo 8,
            # then outputs that value. (If a program outputs multiple values, they are separated by commas.)
            outputs.append(get_combo_operand(operand) % 8)

        elif opcode == 6:
            # The bdv instruction (opcode 6) works exactly like the adv instruction except that
            # the result is stored in the B register. (The numerator is still read from the A register.)
            numerator = registers[0]
            denominator = 2 ** get_combo_operand(operand)
            result = numerator // denominator
            registers[1] = result

        elif opcode == 7:
            # The cdv instruction (opcode 7) works exactly like the adv instruction except that
            # the result is stored in the C register. (The numerator is still read from the A register.)
            numerator = registers[0]
            denominator = 2 ** get_combo_operand(operand)
            result = numerator // denominator
            registers[2] = result

        p += 2

    return outputs

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(*result, sep=",")
    # print(f"Solution for Day 17, Part One: {result}")

if __name__ == '__main__':
    main()
