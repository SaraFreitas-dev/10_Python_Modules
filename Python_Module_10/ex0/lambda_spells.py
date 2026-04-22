from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Sort magical artifacts by power level (descending)
    And return the sorted list
    """
    sorted_art = sorted(artifacts, key=lambda x: x['power'], reverse=True)
    return sorted_art


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    """
    Filter mages by power
    Find mages with power >= min_power and return that filtered list
    """
    filtered_art = list(filter(lambda x: (x['power'] >= min_power), mages))
    return filtered_art


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform spell names: add "* " prefix and " *" suffix
    Return a list of transformed spell names
    """
    prefix = "* "
    suffix = " *"
    spell_names = list(map(lambda s: prefix + s + suffix, spells))
    return spell_names


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    """
    Find:
        -> Most powerful mages power level
        -> Least powerful mages power level
        -> Average power level (rounded to 2 decimals)
    return dict: {max_power: int, min_power: int, avg_power: float}
    """
    min_power = min(mages, key=lambda x: x['power'])['power']
    max_power = max(mages, key=lambda x: x['power'])['power']
    avg_power = round(sum(map(lambda x: x['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    # Data generated from data_generator.py
    artifacts = [{'name': 'Earth Shield', 'power': 108, 'type': 'focus'},
                 {'name': 'Wind Cloak', 'power': 71, 'type': 'accessory'},
                 {'name': 'Fire Staff', 'power': 106, 'type': 'relic'},
                 {'name': 'Wind Cloak', 'power': 101, 'type': 'armor'}]
    mages = [{'name': 'Sage', 'power': 93, 'element': 'earth'},
             {'name': 'Alex', 'power': 96, 'element': 'shadow'},
             {'name': 'River', 'power': 53, 'element': 'light'},
             {'name': 'Jordan', 'power': 97, 'element': 'fire'},
             {'name': 'Zara', 'power': 62, 'element': 'water'},
             {'name': 'Nova', 'power': 59, 'element': 'wind'},
             {'name': 'Kai', 'power': 71, 'element': 'ice'}]
    spells = ['tsunami', 'blizzard', 'lightning', 'flash']
    print("\n======artifact_sorter======")
    print(artifact_sorter(artifacts))
    print("\n========power_filter========")
    print(power_filter(mages, 70))
    print("\n=====spell_transformer=====")
    print(spell_transformer(spells))
    print("\n========mage_stats========")
    print(mage_stats(mages))
