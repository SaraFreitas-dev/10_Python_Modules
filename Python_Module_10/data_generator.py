"""
FuncMage Chronicles - Data Generator Helper
Generates test data for all exercises to help learners test their
implementations
"""

import random
from typing import List, Dict, Any


class FuncMageDataGenerator:
    """Generate test data for FuncMage Chronicles exercises."""

    # Fantasy-themed data pools
    MAGE_NAMES = [
        "Alex",
        "Jordan",
        "Riley",
        "Casey",
        "Morgan",
        "Sage",
        "River",
        "Phoenix",
        "Ember",
        "Storm",
        "Luna",
        "Nova",
        "Zara",
        "Kai",
        "Rowan",
        "Ash"]

    ELEMENTS = [
        "fire",
        "ice",
        "lightning",
        "earth",
        "wind",
        "water",
        "light",
        "shadow"]

    SPELL_NAMES = [
        "fireball", "heal", "shield", "lightning", "freeze", "earthquake",
        "tornado", "tsunami", "flash", "darkness", "meteor", "blizzard"
    ]

    ARTIFACT_NAMES = [
        "Crystal Orb",
        "Fire Staff",
        "Ice Wand",
        "Lightning Rod",
        "Earth Shield",
        "Wind Cloak",
        "Water Chalice",
        "Shadow Blade",
        "Light Prism",
        "Storm Crown"]

    ARTIFACT_TYPES = ["weapon", "focus", "armor", "accessory", "relic"]

    ENCHANTMENT_TYPES = [
        "Flaming",
        "Frozen",
        "Shocking",
        "Earthen",
        "Windy",
        "Flowing",
        "Radiant",
        "Dark"]

    @classmethod
    def generate_mages(cls, count: int = 5) -> List[Dict[str, Any]]:
        """Generate a list of mages with random attributes."""
        mages = []
        for _ in range(count):
            mage = {
                'name': random.choice(cls.MAGE_NAMES),
                'power': random.randint(50, 100),
                'element': random.choice(cls.ELEMENTS)
            }
            mages.append(mage)
        return mages

    @classmethod
    def generate_artifacts(cls, count: int = 5) -> List[Dict[str, Any]]:
        """Generate a list of magical artifacts."""
        artifacts = []
        for _ in range(count):
            artifact = {
                'name': random.choice(cls.ARTIFACT_NAMES),
                'power': random.randint(60, 120),
                'type': random.choice(cls.ARTIFACT_TYPES)
            }
            artifacts.append(artifact)
        return artifacts

    @classmethod
    def generate_spells(cls, count: int = 6) -> List[str]:
        """Generate a list of spell names."""
        return random.sample(cls.SPELL_NAMES, min(count, len(cls.SPELL_NAMES)))

    @classmethod
    def generate_spell_powers(cls, count: int = 5) -> List[int]:
        """Generate a list of spell power values."""
        return [random.randint(10, 50) for _ in range(count)]

    @classmethod
    def generate_enchantment_items(cls, count: int = 5) -> List[str]:
        """Generate a list of items to be enchanted."""
        items = [
            "Sword",
            "Shield",
            "Staff",
            "Wand",
            "Armor",
            "Ring",
            "Amulet",
            "Cloak"]
        return random.sample(items, min(count, len(items)))

    @classmethod
    def print_exercise_data(cls, exercise_num: int):
        """Print formatted test data for a specific exercise."""
        print(f"=== Exercise {exercise_num} Test Data ===")

        if exercise_num == 0:
            print("# Lambda Sanctum Test Data")
            print("artifacts =", cls.generate_artifacts(4))
            print("mages =", cls.generate_mages(5))
            print("spells =", cls.generate_spells(4))

        elif exercise_num == 1:
            print("# Higher Realm Test Data")
            print("# Use these in your test functions:")
            print("test_values =", [random.randint(5, 25) for _ in range(3)])
            print("test_targets =", ["Dragon", "Goblin", "Wizard", "Knight"])

        elif exercise_num == 2:
            print("# Memory Depths Test Data")
            print(
                "initial_powers =", [
                    random.randint(
                        20, 80) for _ in range(3)])
            print(
                "power_additions =", [
                    random.randint(
                        5, 20) for _ in range(5)])
            print(
                "enchantment_types =",
                random.sample(
                    cls.ENCHANTMENT_TYPES,
                    3))
            print("items_to_enchant =", cls.generate_enchantment_items(4))

        elif exercise_num == 3:
            print("# Ancient Library Test Data")
            print("spell_powers =", cls.generate_spell_powers(6))
            print("operations = ['add', 'multiply', 'max', 'min']")
            print(
                "fibonacci_tests =", [
                    random.randint(
                        8, 20) for _ in range(3)])

        elif exercise_num == 4:
            print("# Master's Tower Test Data")
            print("test_powers =", [random.randint(5, 30) for _ in range(4)])
            print("spell_names =", random.sample(cls.SPELL_NAMES, 4))
            print("mage_names =", random.sample(cls.MAGE_NAMES, 6))
            print("invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']")

        print()


def main():
    """Interactive data generator for FuncMage Chronicles."""
    print("🧙‍♀️ FuncMage Chronicles - Data Generator Helper 🧙‍♂️")
    print("=" * 50)
    print()

    while True:
        print("Choose an option:")
        print("0. Generate data for Exercise 0 (Lambda Sanctum)")
        print("1. Generate data for Exercise 1 (Higher Realm)")
        print("2. Generate data for Exercise 2 (Memory Depths)")
        print("3. Generate data for Exercise 3 (Ancient Library)")
        print("4. Generate data for Exercise 4 (Master's Tower)")
        print("5. Generate data for ALL exercises")
        print("6. Generate custom mage data")
        print("7. Generate custom artifact data")
        print("q. Quit")
        print()

        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("May your functions be pure and your closures be strong! 🌟")
            break
        elif choice in ['0', '1', '2', '3', '4']:
            FuncMageDataGenerator.print_exercise_data(int(choice))
        elif choice == '5':
            for i in range(5):
                FuncMageDataGenerator.print_exercise_data(i)
        elif choice == '6':
            count = int(
                input("How many mages to generate? (default 5): ") or 5)
            print("mages =", FuncMageDataGenerator.generate_mages(count))
            print()
        elif choice == '7':
            count = int(
                input("How many artifacts to generate? (default 5): ") or 5)
            print(
                "artifacts =",
                FuncMageDataGenerator.generate_artifacts(count))
            print()
        else:
            print("Invalid choice. Please try again.")
            print()


if __name__ == "__main__":
    main()
