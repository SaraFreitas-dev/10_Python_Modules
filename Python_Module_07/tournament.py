from ex0 import AquaFactory, FlameFactory
from ex0.CreatureFactory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.BattleStrategy import BattleStrategy
from ex2 import AggressiveStrategy, DefensiveStrategy, NormalStrategy
from typing import Any


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    """
    ◦ takes a list of opponents in the tournament;
    each opponent is defined as a tuple
    consisting of a CreatureFactory and a BattleStrategy.
    ◦ makes each opponent fight once all other opponents.
    ◦ organizes each fight using each Creature's associated strategy.
    ◦ handles correctly invalid Creature-strategy tuples.
    """
    try:
        creatures: list[tuple[Any, BattleStrategy]] = []
        opp_n = 0
        for factory, strategy in opponents:
            opp_n += 1
            creature = factory.create_base()
            creatures.append((creature, strategy))

        """Print the list of creatures / strategies"""
        formatted_list = []

        for i in range(len(creatures)):
            creature, strategy = creatures[i]
            factory = opponents[i][0]
            factory_name = factory.__class__.__name__
            if ("Healing" in factory_name or "Transform" in factory_name):
                """for healing or transform creatures"""
                name = factory_name.replace(
                    "CreatureFactory", "").replace("Factory", "")
            else:
                """for flameling or aquabub"""
                name = creature.name

            strat = strategy.__class__.__name__.replace("Strategy", "")
            formatted_list.append(f"({name}+{strat})")

        formatted = ", ".join(formatted_list)
        print(f"[ {formatted} ]")
        """Tournament"""
        print("*** Tournament ***\n"
              f"{opp_n} opponents involved")

        """Battle 2 opponents at a time"""
        for i in range(len(creatures)):
            for j in range(i + 1, len(creatures)):
                creature1, strategy1 = creatures[i]
                creature2, strategy2 = creatures[j]
                print("\n* Battle *")

                print(f"{creature1.describe()}\n vs .\n{creature2.describe()}")
                print(" now fight!")
                strat1_name = strategy1.__class__.__name__.replace(
                    'Strategy', '').lower()
                strat2_name = strategy2.__class__.__name__.replace(
                    'Strategy', '').lower()
                if not strategy1.is_valid(creature1):
                    raise ValueError("Battle error, aborting tournament: "
                                     f"Invalid Creature '{creature1.name}'"
                                     f" for this {strat1_name} strategy")
                if not strategy2.is_valid(creature2):
                    raise ValueError("Battle error, aborting tournament: "
                                     f"Invalid Creature '{creature2.name}'"
                                     f" for this {strat2_name} strategy")
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
    except Exception as e:
        print(f"{e}")


def ex2_test() -> None:
    """ex2 main
    Create various Creature factories (from ex0 and ex1).
    Create the three strategies.
    """
    try:
        """CREATE CREATURES FACTORIES FROM EX0 AND EX1
        CREATE STRATEGIES"""
        print("Tournament 0 (basic)")
        battle([(FlameFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())])

        print("\nTournament 1 (error)")
        battle([(FlameFactory(), AggressiveStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy())])

        print("\nTournament 2 (multiple)")
        battle([(AquaFactory(), NormalStrategy()),
                (HealingCreatureFactory(), DefensiveStrategy()),
                (TransformCreatureFactory(), AggressiveStrategy())])
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    ex2_test()
