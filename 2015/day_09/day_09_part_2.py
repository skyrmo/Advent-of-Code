import os
from itertools import permutations


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


# def tsp(dists):
#     n = len(dists)

#     dp = [[0] * n for _ in range(1 << n)]

#     # Base case: visiting just node 'i' (cost 0)
#     for i in range(n):
#         dp[1 << i][i] = 0

#     # for i, row in enumerate(dp):
#     #     print(bin(i)[2:].zfill(n), row)

#     for mask in range(1 << n):
#         # print(bin(mask)[2:].zfill(n))
#         for i in range(n):
#             # If city i is not in the mask, skip
#             if not (mask & (1 << i)):
#                 continue

#             # If this is just a single city, we already set it to 0
#             if mask == (1 << i):
#                 continue

#             # print("->", i)

#             # Try all possible previous cities j
#             for j in range(n):
#                 # j must be in the mask and different from i
#                 if i == j or not (mask & (1 << j)):
#                     continue

#                 # print("-->", j)

#                 # The previous mask is the current mask without city i
#                 prev_mask = mask ^ (1 << i)

#                 # Update: cost to reach (mask, i) via j
#                 if dp[prev_mask][j] != float("inf") and dists[j][i] != float("inf"):
#                     dp[mask][i] = max(dp[mask][i], dp[prev_mask][j] + dists[j][i])


#     full_mask = (1 << n) - 1
#     return max(dp[full_mask][i] for i in range(n))


def perms(dists):
    n = len(dists)
    result = float("inf")

    perms = permutations(range(n))

    # print(list(perms))
    for path in list(perms):
        path_len = 0
        for i in range(1, n):
            a, b = path[i - 1], path[i]
            path_len += dists[a][b]

        result = min(result, path_len)

    return result


def solve(input_data):
    cities = set()
    routes = []

    for line in input_data:
        to_from, cost = line.split(" = ")
        cost = int(cost.strip())
        a, b = [x.strip() for x in to_from.split(" to ")]
        cities.add(a)
        cities.add(b)
        routes.append((a, b, cost))

    n = len(cities)
    dists = [[0] * n for _ in range(n)]

    cities_nodes = {city: i for i, city in enumerate(cities)}

    for a, b, c in routes:
        dists[cities_nodes[a]][cities_nodes[b]] = c
        dists[cities_nodes[b]][cities_nodes[a]] = c

    return perms(dists)


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
    print(f"Solution for Day 09, Part Two: {result}")


if __name__ == "__main__":
    main()
