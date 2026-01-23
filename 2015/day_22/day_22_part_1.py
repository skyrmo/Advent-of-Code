import collections
import heapq
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


State = collections.namedtuple(
    "State",
    [
        "boss_hp",
        "player_hp",
        "player_mana",
        "shield_effect",
        "poison_effect",
        "recharge_effect",
    ],
)

spells = [
    ("Magic Missile", 53, lambda s: s._replace(boss_hp=s.boss_hp - 4)),
    (
        "Drain",
        73,
        lambda s: s._replace(boss_hp=s.boss_hp - 2, player_hp=s.player_hp + 2),
    ),
    (
        "Shield",
        113,
        lambda s: s._replace(shield_effect=6) if s.shield_effect == 0 else None,
    ),
    (
        "Poison",
        173,
        lambda s: s._replace(poison_effect=6) if s.poison_effect == 0 else None,
    ),
    (
        "Recharge",
        229,
        lambda s: s._replace(recharge_effect=5) if s.recharge_effect == 0 else None,
    ),
]


def apply_spell_effects(state: State):
    boss_hp = state.boss_hp
    player_mana = state.player_mana
    shield_timer = state.shield_effect
    poison_timer = state.poison_effect
    recharge_timer = state.recharge_effect

    if shield_timer > 0:
        shield_timer -= 1

    if poison_timer > 0:
        boss_hp -= 3
        poison_timer -= 1

    if recharge_timer > 0:
        player_mana += 101
        recharge_timer -= 1

    new_state = State(
        boss_hp=boss_hp,
        player_hp=state.player_hp,
        player_mana=player_mana,
        shield_effect=shield_timer,
        poison_effect=poison_timer,
        recharge_effect=recharge_timer,
    )

    return new_state, boss_hp <= 0


def boss_turn(state: State, boss_damage: int):
    damage = boss_damage
    if state.shield_effect > 0:
        damage = max(1, damage - 7)

    new_hp = state.player_hp - damage

    return state._replace(player_hp=new_hp), new_hp > 0 and state.player_mana >= 53


def solve(input_data):
    start_state = State(
        boss_hp=55,
        player_hp=50,
        player_mana=500,
        shield_effect=0,
        poison_effect=0,
        recharge_effect=0,
    )

    cache = set()
    cache.add(start_state)
    q = [(0, start_state)]

    while q:
        spent, state = heapq.heappop(q)

        # -- Player Turn Starts -----
        state, won = apply_spell_effects(state)

        if won:
            return spent

        for _, cost, state_modifer in spells:
            if state.player_mana >= cost:
                new_mana_state = state._replace(player_mana=state.player_mana - cost)

                next_state = state_modifer(new_mana_state)

                if next_state is None:
                    continue

                # -- Boss Turn Starts -----
                next_state, won = apply_spell_effects(next_state)
                if won:
                    return spent + cost

                next_state, survived = boss_turn(next_state, 8)

                if survived and next_state not in cache:
                    cache.add(next_state)
                    heapq.heappush(q, (spent + cost, next_state))


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
    print(f"Solution for Day 22, Part One: {result}")


if __name__ == "__main__":
    main()
