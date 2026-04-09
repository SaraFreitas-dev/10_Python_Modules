from ex0 import AquaFactory, FlameFactory


def ex0_test() -> None:
    """ex0 main"""
    try:
        """FLAME CREATURES"""
        print("Testing factory")
        flame_factory = FlameFactory()
        flameling = flame_factory.create_base()
        pyrodon = flame_factory.create_evolved()
        print(flameling.describe())
        print(flameling.attack())
        print(pyrodon.describe())
        print(pyrodon.attack())
    except Exception as e:
        print(f"Error {e}")

    try:
        """AQUA CREATURES"""
        print("\nTesting factory")
        aqua_factory = AquaFactory()
        aquabub = aqua_factory.create_base()
        torragon = aqua_factory.create_evolved()
        print(aquabub.describe())
        print(aquabub.attack())
        print(torragon.describe())
        print(torragon.attack())
    except Exception as e:
        print(f"Error {e}")

    try:
        """TESTING BATTLE BETWEEN CREATURES"""
        print("\nTesting battle")
        print(f'{flameling.describe()}\n vs.\n'
              f'{aquabub.describe()}')
        print("fight!")
        print(f'{flameling.attack()} \n{aquabub.describe()}')
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    ex0_test()
