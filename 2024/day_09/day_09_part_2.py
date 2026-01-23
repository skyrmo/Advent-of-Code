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

        return data

def solve(input_data):
    data = [int(x) for x in list(input_data)]

    arr = []
    q = collections.deque()

    idx = 0
    for i, num in enumerate(data):
        if num == 0:
            idx += num
            continue

        q.appendleft((i//2, idx, num))
        for _ in range(num):
            if i % 2 == 0:
                arr.append(i// 2)
            else:
                arr.append(-1)
        idx += num

    # uses q queue and two pointers.
    while q:
        num, idx, repeat = q.popleft()

        # using a window to keep trak of the number of spaces
        window_space_count = len([x for x in arr[:repeat] if x == -1])

        for i in range(min(len(arr) - repeat, idx)):
            if window_space_count == repeat:
                for j in range(repeat):
                    arr[i + j], arr[idx + j] = arr[idx + j], arr[i + j]
                break

            if arr[i] == -1:
                window_space_count -= 1
            if arr[i + repeat] == -1:
                window_space_count += 1


    result = 0
    for i, num in enumerate(arr):
        if num >= 0:
            result += i * num

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
    print(f"Solution for Day 09, Part Two: {result}")

if __name__ == '__main__':
    main()
