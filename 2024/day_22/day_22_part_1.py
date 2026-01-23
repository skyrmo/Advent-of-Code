
import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):

    def process(secret_num):
        secret_num_by_64 = secret_num * 64
        secret_num = secret_num ^ secret_num_by_64
        secret_num = secret_num % 16777216

        secret_num_d_32 = secret_num // 32
        secret_num = secret_num ^ secret_num_d_32
        secret_num = secret_num % 16777216

        secret_num_by_2024 = secret_num * 2048
        secret_num = secret_num ^ secret_num_by_2024
        secret_num = secret_num % 16777216

        return secret_num

    result = 0
    for num in input_data:
        # print(num)
        secret_num = num
        for _ in range(2000):
            secret_num = process(secret_num)
        result += secret_num
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
    print(f"Solution for Day 22, Part One: {result}")

if __name__ == '__main__':
    main()
