from ex0 import AquaFactory, FlameFactory
from ex0.CreatureFactory import CreatureFactory


def testing_factory(factory: CreatureFactory) -> None:
    """receives a factory object and verifies that it can create
    the base and evolved Creature, and then each Creature
    can be described and can attack.
    This function will create a battle with creatures from the same factory"""
    try:
        print("Testing factory")
        base = factory.create_base()
        evolved = factory.create_evolved()
        print(base.describe())
        print(base.attack())
        print(evolved.describe())
        print(evolved.attack() + "\n")
    except Exception as e:
        print(f"Error {e}")


def testing_battle(factory1: CreatureFactory,
                   factory2: CreatureFactory) -> None:
    """This function will create a battle with base creatures
    from different factories"""
    try:
        print("Testing battle")
        base1 = factory1.create_base()
        base2 = factory2.create_base()
        print(base1.describe())
        print(" vs.")
        print(base2.describe())
        print(" fight!")
        print(base1.attack())
        print(base2.attack() + "\n")
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    testing_factory(FlameFactory())
    testing_factory(AquaFactory())
    testing_battle(FlameFactory(), AquaFactory())
