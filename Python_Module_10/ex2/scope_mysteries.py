from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    """
    Return a function that counts how many times its been called
    Each call should return the current count (starting from 1)
    The counter should persist between calls
    Creating two separate counters must yield independent state.
    Use closure to maintain state without global variables
    """
    count = 0

    def inner_counter() -> int:
        nonlocal count
        count += 1
        return count
    return inner_counter


def spell_accumulator(initial_power: int) -> Callable:
    """
    Return a function that accumulates power over time
    Each call adds the given amount to the total power
    Return the new total power after each addition
    Start with initial_power as the base
    """
    amount = initial_power

    def increment(nbr: int) -> int:
        nonlocal amount
        amount += nbr
        return amount
    return increment


def enchantment_factory(enchantment_type: str) -> Callable:
    """
    Return a function that applies the specified enchantment
    The returned function takes an item name and returns enchanted description
    Format: "enchantment_type item_name" (e.g., "Flaming Sword")
    Each factory creates functions with different enchantment types
    """
    def enchantment(item_to_enchant: str) -> str:
        return f"{enchantment_type} {item_to_enchant}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    """
    Return a dict with store and recall functions
    Store function: takes (key, value) and stores the memory
    Recall function: takes (key) and returns stored value or "Memory not found"
    Use closure to maintain private memory storage
    """
    vault_info: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault_info[key] = value

    def recall(key: str) -> Any:
        return vault_info.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


if __name__ == "__main__":
    # Memory Depths Test Data
    initial_powers = [43, 44, 62]
    power_additions = [9, 8, 11, 9, 13]
    enchantment_types = ['Frozen', 'Radiant', 'Windy']
    items_to_enchant = ['Cloak', 'Amulet', 'Wand', 'Staff']

    # mage_counter
    c_a = mage_counter()
    c_b = mage_counter()
    print("Testing mage counter...\n"
          f"counter_a call 1: {c_a()}\n"
          f"counter_a call 2: {c_a()}\n"
          f"counter_b call 1: {c_b()}\n")

    # spell_accumulator
    initial_power = 100
    spell_acc = spell_accumulator(initial_power)
    print("Testing spell accumulator..\n"
          f"Base: {initial_power}, add 20: {spell_acc(20)}\n"
          f"Base: {initial_power}, add 30: {spell_acc(30)}\n")

    # enchantment_factory
    ench_1 = enchantment_factory('Flaming')
    ench_2 = enchantment_factory('Frozen')
    print("Testing enchantment factory...\n"
          f"{ench_1('Sword')}\n"
          f"{ench_2('Shield')}\n")

    # memory_vault
    vault = memory_vault()
    key = "secret"
    value = 42
    vault['store'](key, value)
    print("Testing memory vault...\n"
          f"Store '{key}' = {value}")
    print(f"Recall '{key}': {vault['recall'](key)}\n"
          f"Recall 'unknown': {vault['recall']('unknown')}")
