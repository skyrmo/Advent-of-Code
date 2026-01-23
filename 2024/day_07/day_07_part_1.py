
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
    def test_line(target, nums):

        def recurse(total, idx):
            result = 0
            # print(total, idx)

            if idx == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            result += recurse(total + nums[idx], idx + 1)
            result += recurse(total * nums[idx], idx + 1)

            return result

        return recurse(nums[0], 1)




    count = 0
    for line in input_data:
        target, nums = line.split(":")
        target = int(target)
        nums = [int(num) for num in nums.split(" ") if num.isdigit()]
        if test_line(target, nums) > 0:
            count += target

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
    print(f"Solution for Day 07, Part One: {result}")

if __name__ == '__main__':
    main()
