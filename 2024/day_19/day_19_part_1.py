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


# class TrieNode():
#     def __init__(self, char=''):
#         self.char = char
#         self.children = {}
#         self.is_word = False

#     def __repr__(self):
#         children_str = ", ".join(f"'{char}'" for char, node in self.children.items())
#         return f"TrieNode(is_end={self.is_word}, children={{{children_str}}})"


# class Trie():
#     def __init__(self):
#         self.root = TrieNode()

#     def add_word(self, word):
#         cur = self.root
#         for i, char in enumerate(word):
#             if char not in cur.children:
#                 cur.children[char] = TrieNode(char)
#             cur = cur.children[char]
#         cur.is_word = True

#     def check_word(self, word):
#         cur = self.root
#         for char in word:
#             if char not in cur.children:
#                 return False
#             cur = cur.children[char]
#         return cur.is_word


def solve(input_data):
    chunks = set(input_data[0].split(", "))
    patterns = input_data[1].split("\n")
    print(chunks)

    def check(idx, word):
        if idx >= len(word):
            return True

        ss = ''
        for i in range(idx, len(word)):
            ss += word[i]
            if ss in chunks:
                if check(i + 1, word):
                    return True

    result = 0
    for pattern in patterns:
        if check(0, pattern):
            result += 1

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
    print(f"Solution for Day 19, Part One: {result}")


if __name__ == '__main__':
    main()
