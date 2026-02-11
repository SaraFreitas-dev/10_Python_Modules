import alchemy.elements
from alchemy.elements import create_fire, create_earth, create_water
from alchemy.potions import healing_potion as heal
from alchemy.potions import strength_potion
heal.__name__ = "heal"


def safe_print_m1(func) -> None:
    """Method 1: print with full module path"""
    try:
        print(f"{func.__module__}.{func.__qualname__}(): {func()}")
    except AttributeError:
        print(f"{func.__module__}.{func.__qualname__}(): "
              "AttributeError - not exposed\n")


def safe_print_m2(func) -> None:
    """Methods 2-4: print only function name"""
    try:
        print(f"{func.__name__}(): {func()}")
    except AttributeError:
        print(f"{func.__name__}(): AttributeError - not exposed\n")


def ft_import_transmutation() -> None:
    """Print the output from Part II"""
    print("\n=== Import Transmutation Mastery ===\n")

    print("Method 1 - Full module import:")
    safe_print_m1(alchemy.elements.create_fire)

    print("\nMethod 2 - Specific function import:")
    safe_print_m2(create_water)

    print("\nMethod 3 - Aliased import:")
    safe_print_m2(heal)

    print("\nMethod 4 - Multiple imports:")
    safe_print_m2(create_earth)
    safe_print_m2(create_fire)
    safe_print_m2(strength_potion)

    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    ft_import_transmutation()
