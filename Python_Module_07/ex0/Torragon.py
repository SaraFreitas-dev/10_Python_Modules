from ex0.Creature import Creature


class Torragon(Creature):
    """Creates a Torragon creature (evolved)"""
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Hydro Pump!')
