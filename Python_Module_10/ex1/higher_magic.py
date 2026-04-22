from collections.abc import Callable


def heal(target: str, power: int) -> str:
    """
    Heal a target spell
    """
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    """
    Fire damage spell
    """
    return f"Fireball hits {target} for {power} damage"


def lightning(target: str, power: int) -> str:
    """
    Lightning damage spell
    """
    return f"Lightning strikes {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Combine the strings from both spells
    """
    def combined(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Returns a new spell where the power is multiplied before casting
    """
    def new_spell_amp(target: str, power: int) -> str:
        base_spell(target, (power * multiplier))
        return f'Original: {power}, Amplified: {power * multiplier}'
    return new_spell_amp


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Returns a new spell that only casts if a condition is True.
    If condition fails, return "Spell fizzled
    """
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def is_strong(target: str, power: int) -> bool:
    """
    Helper / condition function to test the above function:
    conditional_caster
    """
    return power >= 15 and target != "elf"


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Return a function that casts all spells in order
    Each spell receives the same arguments
    Returns a list of all spell results
    """
    def spells_seq(target: str, power: int) -> list[str]:
        results: list[str] = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return spells_seq


if __name__ == "__main__":
    # Higher Realm Test Data
    power = [10, 15, 9]
    targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # Example for spell_combiner
    combined = spell_combiner(fireball, heal)
    res_combined = combined("Dragon", 10)
    print("\nTesting spell combiner...\n"
          "Combined spell result: "
          f"{res_combined[0]}, {res_combined[1]}\n")

    # Example for power_amplifier
    power_amp = power_amplifier(lightning, 3)
    res_amp = power_amp('Goblin', 10)
    print("Testing power amplifier...\n"
          "Power amplifier result: "
          f"{res_amp}\n")

    # Example for conditional_caster
    spell_cond = conditional_caster(is_strong, fireball)
    res_cond1 = spell_cond('Wizard', 10)
    res_cond2 = spell_cond('Goblin', 20)
    print("Testing conditional caster...\n"
          "Conditional caster result:\n"
          "  -> Example 1 (False Condition):\n"
          f"    {res_cond1}\n"
          "  -> Example 2 (True Condition):\n"
          f"    {res_cond2}\n")

    # Example for spell_sequence
    spell_seq = spell_sequence([fireball, heal, lightning])
    res_seq = spell_seq('Knight', 12)
    print("Testing spell sequence...\n"
          "Spell sequence result (list): "
          f"{res_seq}\n")
