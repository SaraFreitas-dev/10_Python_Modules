from .elements import (
    create_fire,
    create_water,
    create_earth,
    create_air,
)


def healing_potion() -> str:
    """Return Healing potion brewed combo"""
    return ("Healing potion brewed with "
            f"{create_fire()} and {create_water()}")


def strength_potion() -> str:
    """Return Strength potion brewed combo"""
    return ("Strength potion brewed with "
            f"{create_earth()} and {create_fire()}")


def invisibility_potion() -> str:
    """Return Invisibility potion brewed combo"""
    return ("Invisibility potion brewed with "
            f"{create_air()} and {create_water()}")


def wisdom_potion() -> str:
    """Return Wisdom potion brewed combo"""
    elem = [create_fire(), create_water(),
            create_earth(), create_air()]
    return ("Wisdom potion brewed with all elements: " + ", ".join(elem))
