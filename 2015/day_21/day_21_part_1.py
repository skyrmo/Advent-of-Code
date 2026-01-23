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


class Player:
    def __init__(self, health, damage, armour):
        self.health = health
        self.damage = damage
        self.armour = armour


SHOP = {
    "weapons": [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)],
    "armor": [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)],
    "rings": [
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ],
}


def simulate(loadout):
    cost, weapon, armor, ring1_d, ring1_a, ring2_d, ring2_a = loadout

    hero = Player(100, weapon + ring1_d + ring2_d, armor + ring1_a + ring2_a)
    villain = Player(100, 8, 2)

    while villain.health > 0 and hero.health > 0:
        villain.health -= max(1, hero.damage - villain.armour)

        if villain.health <= 0:
            return True

        hero.health -= max(1, villain.damage - hero.armour)

        if hero.health <= 0:
            return False

    return False


def solve(input_data):
    loadouts = []
    for w_cost, w_damage in SHOP["weapons"]:
        for a_cost, armor in SHOP["armor"]:
            for r1_cost, r1_damage, r1_armour in SHOP["rings"]:
                loadouts.append(
                    (
                        w_cost + a_cost + r1_cost,
                        w_damage,
                        armor,
                        r1_damage,
                        r1_armour,
                        0,
                        0,
                    )
                )
                for ring2_cost, ring2_damage, ring2_armour in SHOP["rings"]:
                    if r1_cost == ring2_cost:
                        continue

                    loadouts.append(
                        (
                            w_cost + a_cost + r1_cost + ring2_cost,
                            w_damage,
                            armor,
                            ring1_damage,
                            ring1_armour,
                            ring2_damage,
                            ring2_armour,
                        )
                    )

    # sorting the list dident effect the speed in any meaningful way.
    for loadout in loadouts:
        if simulate(loadout):
            return loadout[0]


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    # input_path = os.path.join(script_dir, 'input.txt')
    input_path = os.path.join(script_dir, "sample_input.txt")

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 21, Part One: {result}")


if __name__ == "__main__":
    main()
