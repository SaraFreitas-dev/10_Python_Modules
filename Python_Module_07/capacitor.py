from ex1 import HealingCreatureFactory, TransformCreatureFactory


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
        print(sproutling.heal())
        # EVOLVED
        print(" evolved:")
        bloomelle = heal_factory.create_evolved()
        print(bloomelle.describe())
        print(bloomelle.attack())
        print(bloomelle.heal())
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
        print(shiftling.transform())
        print(shiftling.attack())
        print(shiftling.revert())
        # EVOLVED
        print(" evolved:")
        morphagon = transform_factory.create_evolved()
        print(morphagon.describe())
        print(morphagon.attack())
        print(morphagon.transform())
        print(morphagon.attack())
        print(morphagon.revert())
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    ex1_test()
