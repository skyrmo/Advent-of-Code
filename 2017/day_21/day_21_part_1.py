import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, "r") as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split("\n")

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def rotate(input):
    return tuple("".join(r) for r in zip(*input[::-1]))


def mirror(input):
    return tuple(r[::-1] for r in input)


def create_variants(input):
    for _ in range(4):
        input = rotate(input)
        yield input
        yield mirror(input)


def solve(input_data):
    rules = {}
    for line in input_data:
        input, output = [tuple(x.split("/")) for x in line.split(" => ")]

        for v in create_variants(input):
            rules[v] = output

    cur = (".#.", "..#", "###")

    for _ in range(5):
        size = len(cur)
        stepsize = 2 if size % 2 == 0 else 3
        blocks = size // stepsize

        next_grid = []
        for r_block in range(blocks):
            row_of_tiles = []
            for c_block in range(blocks):
                tile = tuple(
                    cur[r_block * stepsize + r][
                        c_block * stepsize : c_block * stepsize + stepsize
                    ]
                    for r in range(stepsize)
                )

                row_of_tiles.append(rules[tile])

            # print(row_of_tiles)

            for r in range(stepsize + 1):
                next_grid.append("".join(tile[r] for tile in row_of_tiles))

        cur = next_grid

    return sum(row.count("#") for row in cur)


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
    print(f"Solution for Day 21, Part One: {result}")


if __name__ == "__main__":
    main()
