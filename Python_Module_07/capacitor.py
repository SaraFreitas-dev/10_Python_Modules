from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.TransformCapability import TransformCapability
from ex1.HealCapability import HealCapability
from typing import cast


def ex1_test() -> None:
    """ex1 main"""
    try:
        """HEAL CREATURES"""
        print("Testing Creature with healing capability")
        heal_factory = HealingCreatureFactory()
        # BASE
        print(" base:")
        sproutling = heal_factory.create_base()
        print(sproutling.describe())
        print(sproutling.attack())
        # cast to prevent mypy warnings
        healer = cast(HealCapability, sproutling)
        print(healer.heal())
        # EVOLVED
        print(" evolved:")
        bloomelle = heal_factory.create_evolved()
        print(bloomelle.describe())
        print(bloomelle.attack())
        healer = cast(HealCapability, bloomelle)
        print(healer.heal())
    except Exception as e:
        print(f"Error {e}")

    try:
        """TRANSFORM CREATURES"""
        print("\nTesting Creature with transform capability")
        transform_factory = TransformCreatureFactory()
        # BASE
        print(" base:")
        shiftling = transform_factory.create_base()
        print(shiftling.describe())
        print(shiftling.attack())
        transformer = cast(TransformCapability, shiftling)
        print(transformer.transform())
        print(shiftling.attack())
        print(transformer.revert())
        # EVOLVED
        print(" evolved:")
        morphagon = transform_factory.create_evolved()
        print(morphagon.describe())
        print(morphagon.attack())
        transformer = cast(TransformCapability, morphagon)
        print(transformer.transform())
        print(morphagon.attack())
        print(transformer.revert())
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    ex1_test()
