import os
import collections

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
        #
        # 5. split into two sections
        return data.split('\n\n')

        return data

def solve(input_data):
    rules, updates = [data.split("\n") for data in input_data]
    rules = [[int(rule.split("|")[0]), int(rule.split("|")[1])] for rule in rules]
    updates = [[int(x) for x in update.split(",")] for update in updates]
    result = 0

    requirments = collections.defaultdict(set)
    for a, b in rules:
        requirments[a].add(b)

    for update in updates:
        seen = set()
        should_update = True
        for val in update:
            if any([req in seen for req in requirments[val]]):
                should_update = False
                break
            else:
                seen.add(val)

        if should_update:
            result += update[len(update)//2]


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
    print(f"Solution for Day 05, Part One: {result}")

if __name__ == '__main__':
    main()
