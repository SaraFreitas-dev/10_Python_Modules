import alchemy.transmutation


def safe_print(func) -> None:
    """print the function name and result"""
    try:
        print(f"{func.__name__}(): {func()}")
    except AttributeError:
        print(f"{func.__name__}(): AttributeError - not exposed\n")


def safe_print_mod(func) -> None:
    """Method 1: print with full module path"""
    try:
        print(f"alchemy.transmutation.{func.__qualname__}(): {func()}")
    except AttributeError:
        print(f"alchemy.transmutation.{func.__qualname__}(): "
              "AttributeError - not exposed\n")


def ft_pathway_debate() -> None:
    """Print the output from Part III"""
    print("\n=== Pathway Debate Mastery ===\n")
    print("Testing Absolute Imports (from basic.py):")
    safe_print(alchemy.transmutation.lead_to_gold)
    safe_print(alchemy.transmutation.stone_to_gem)

    print("\nTesting Relative Imports (from advanced.py):")
    safe_print(alchemy.transmutation.philosophers_stone)
    safe_print(alchemy.transmutation.elixir_of_life)

    print("\nTesting Package Access:")
    safe_print_mod(alchemy.transmutation.lead_to_gold)
    safe_print_mod(alchemy.transmutation.philosophers_stone)

    print("\vBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
