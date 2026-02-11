from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients


def ft_circular_curse() -> None:
    """Print the output from Part II"""
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print("validate_ingredients(\"fire air\"): "
          f"{validate_ingredients("fire air")}")
    print("validate_ingredients(\"dragon scales\"): "
          f"{validate_ingredients("dragon scales")}")
    

if __name__ == "__main__":
    ft_circular_curse()
