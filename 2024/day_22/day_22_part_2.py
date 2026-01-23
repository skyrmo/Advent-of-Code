from collections import defaultdict
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

    user_zips = defaultdict(lambda: defaultdict(int))

    for user_id, secret_num in enumerate(input_data):
        secret_nums = [secret_num]
        prices = [secret_num % 10]
        changes = []
        seen_prices = set()


        for i in range(2000):
            secret_num = process(secret_num)
            secret_nums.append(secret_num)

            price = secret_num % 10

            changes.append(price - prices[-1])

            prices.append(price)

        for p in range(4, len(prices)):
            last_4_changes = tuple(changes[p - 4:p])
            if last_4_changes not in user_zips[user_id]:
                user_zips[user_id][last_4_changes] = prices[p]
                seen_prices.add(prices[p])


    all_seqs = set()

    for id, dict in user_zips.items():
        for seq, v in dict.items():
           all_seqs.add(seq)

    max_seq = None
    max_points = 0
    for seq in all_seqs:
        points = 0
        for dict in user_zips.values():
            points += dict.get(seq, 0)
        if points > max_points:
            max_points = points
            max_seq = seq

    print(max_seq, max_points)


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 22, Part Two: {result}")

if __name__ == '__main__':
    main()
