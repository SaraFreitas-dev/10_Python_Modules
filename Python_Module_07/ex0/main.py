# from tools.card_generator import CardGenerator
from ex0.CreatureCard import CreatureCard


def main_example() -> None:
    """VERSION 1 — NORMAL | Use python -m ex0.main command to run"""
    print("=== DataDeck Card Foundation ===\n")

    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    game_state = {"available_mana": 6}
    print(f"\nPlaying {fire_dragon.name} with "
          f"{game_state["available_mana"]} mana available:")
    print("Playable:", fire_dragon.is_playable(game_state["available_mana"]))

    result = fire_dragon.play(game_state)
    print("Play result:", result)

    target = "Goblin Warrior"
    print(f"\n{fire_dragon.name} attacks {target}:")
    combat = fire_dragon.attack_target(target)
    print("Attack result:", combat)

    game_state["available_mana"] = 3
    print("\nTesting insufficient mana "
          f"({game_state["available_mana"]} available):")
    print("Playable:", fire_dragon.is_playable(game_state["available_mana"]))

    print("\nAbstract pattern successfully demonstrated!")

    # ================================
    # VERSION 2 — WITH CARD GENERATOR
    # ================================


"""
    generator = CardGenerator()
    creature_data = generator.get_creature("Fire Dragon")
    if creature_data:
        generated_card = CreatureCard(**creature_data)

    print("\n=== Using CardGenerator ===\n")
    print("Generated Card Info:")
    print(generated_card.get_card_info())

    game_state = {"available_mana": 6}
    print("Playable:",
          generated_card.is_playable(game_state["available_mana"]))
    print("Play result:",
          generated_card.play(game_state))
    print("Attack result:",
          generated_card.attack_target("Goblin Warrior"))
"""


if __name__ == "__main__":
    main_example()
