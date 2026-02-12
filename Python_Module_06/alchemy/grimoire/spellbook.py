def record_spell(spell_name: str, ingredients: str) -> str:
    """Validate if the ingredient is valid and spell it / Late import"""
    from .validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if result.endswith("INVALID"):
        return f"Spell rejected: {spell_name} ({result})"
    return f"Spell recorded: {spell_name} ({result})"
