import os
import re


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


class Ingredient:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = int(capacity)
        self.durability = int(durability)
        self.flavor = int(flavor)
        self.texture = int(texture)
        self.calories = int(calories)

    def __repr__(self):
        return f"{self.name}({self.capacity}, {self.durability}, {self.flavor}, {self.texture}, {self.calories})"


def solve(input_data):
    ingredients = []
    result = -float("inf")
    for line in input_data:
        match = re.match(
            r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)",
            line,
        )

        if match:
            name, capacity, durability, flavor, texture, calories = match.groups()
            ingredient = Ingredient(
                name, capacity, durability, flavor, texture, calories
            )
            ingredients.append(ingredient)
        else:
            print("Invalid input format")

    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                if a + b + c + d == 100:
                    i_a, i_b, i_c, i_d = (
                        ingredients[0],
                        ingredients[1],
                        ingredients[2],
                        ingredients[3],
                    )

                    capacity = (
                        a * i_a.capacity
                        + b * i_b.capacity
                        + c * i_c.capacity
                        + d * i_d.capacity
                    )
                    durability = (
                        a * i_a.durability
                        + b * i_b.durability
                        + c * i_c.durability
                        + d * i_d.durability
                    )
                    flavor = (
                        a * i_a.flavor
                        + b * i_b.flavor
                        + c * i_c.flavor
                        + d * i_d.flavor
                    )
                    texture = (
                        a * i_a.texture
                        + b * i_b.texture
                        + c * i_c.texture
                        + d * i_d.texture
                    )
                    calories = (
                        a * i_a.calories
                        + b * i_b.calories
                        + c * i_c.calories
                        + d * i_d.calories
                    )

                    if (
                        capacity > 0
                        and durability > 0
                        and flavor > 0
                        and texture > 0
                        and calories == 500
                    ):
                        result = max(result, capacity * durability * flavor * texture)

    return result


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
    print(f"Solution for Day 15, Part Two: {result}")


if __name__ == "__main__":
    main()
