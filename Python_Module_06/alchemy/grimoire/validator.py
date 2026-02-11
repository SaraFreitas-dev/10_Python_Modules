def validate_ingredients(ingredients: str) -> str:
    """VCheck if the ingredients are valid - True / False"""
    valid_elements = ["fire", "water", "earth", "air"]
    ingredients_lst: list[str] = ingredients.split()
    for ing in ingredients_lst:
        if ing not in valid_elements:
            return (f"{ingredients} - INVALID")
    return (f"{ingredients} - VALID")
