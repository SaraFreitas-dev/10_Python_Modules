from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients


def ft_circular_curse() -> None:
    """Print the output from Part II"""
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): "
          f"{validate_ingredients("fire air")}")
    print("validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients("dragon scales")}\n")

    print("Testing spell recording with validation:")
    print("record_spell(\"Fireball\", \"fire air\"):" +
          record_spell("Fireball", "fire air"))
    print("record_spell(\"Dark Magic\", \"shadow\"):" +
          record_spell("Dark Magic", "shadow"))

    print("\nTesting late import technique:")
    print("record_spell(\"Lightning\", \"air\"):" +
          record_spell("Lightning", "air"))

    print("Circular dependency curse avoided "
          "using late imports!\n"
          "All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
