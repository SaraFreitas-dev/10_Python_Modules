from validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    """Validate if the ingredient is valid and spell it"""
    if not validate_ingredients(ingredients):
        return (f"Spell rejected: {spell_name} "
                f"{validate_ingredients(ingredients)}")
    return (f"Spell recorded: {spell_name} "
            f"{validate_ingredients(ingredients)}")
