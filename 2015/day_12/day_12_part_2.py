import collections
import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def count_string(string):
    line = string
    n = len(line)
    result = 0

    DIGITS = [
        "-",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    cur_num = collections.deque()
    for i in range(n - 1, -1, -1):
        c = line[i]
        if c in DIGITS:
            cur_num.appendleft(c)
        elif cur_num:
            num = int("".join(list(cur_num)))

            result += num
            cur_num.clear()

    if cur_num:
        num = int("".join(list(cur_num)))
        result += num

    return result


def solve(line):
    n = len(line)
    total_count = count_string(line)

    idx_to_check = [i for i in range(n - 3) if line[i : i + 6] == ':"red"']
    strings_to_check = set()

    for i in idx_to_check:
        found_bracket = False
        li = i
        stack = []

        while li > 0 and not found_bracket:
            if line[li] == "}":
                stack.append("}")
            elif line[li] == "{" and stack:
                stack.pop()
            elif line[li] == "{":
                found_bracket = True
                break
            li -= 1

        found_bracket = False

        ri = i + 6
        stack = []
        while ri < n and not found_bracket:
            if line[ri] == "{":
                stack.append("{")
            elif line[ri] == "}" and stack:
                stack.pop()
            elif line[ri] == "}":
                found_bracket = True
                break
            ri += 1

        string_to_check = line[li : ri + 1]
        strings_to_check.add((string_to_check, li, ri + 1))

    strings_to_check = sorted(list(strings_to_check), key=lambda x: (x[1], -x[2]))

    strings_to_minus = [strings_to_check[0]]

    for i in range(1, len(strings_to_check)):
        s, l, _ = strings_to_check[i]
        if l > strings_to_minus[-1][2]:
            strings_to_minus.append(strings_to_check[i])

    for s, _, _ in strings_to_minus:
        cnt = count_string(s)
        total_count -= cnt

    return total_count


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, "input.txt")
    # input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 12, Part Two: {result}")


if __name__ == "__main__":
    main()
