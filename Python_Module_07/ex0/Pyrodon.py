from ex0.Creature import Creature


class Pyrodon(Creature):
    """Creates a aquabub creature (evolved)"""
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Flamethrower!')
