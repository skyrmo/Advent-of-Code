import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    nums = [int(x) for x in input_data.split(" ")]
    memo = {}

    def dp(num, itr):
        if (num, itr) in memo:
            return memo[(num, itr)]

        if num == 0:
            products = [1]

        elif len(str(num)) % 2 == 0:
            products = [int(str(num)[:len(str(num))//2]), int(str(num)[len(str(num))//2:])]


        else:
            products = [num * 2024]

        if itr == 0:
            return len(products)

        result = sum([dp(n, itr - 1) for n in products])

        memo[(num, itr)] = result
        return result

    return sum([dp(num, 24) for num in nums])


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 11, Part One: {result}")


if __name__ == '__main__':
    main()
