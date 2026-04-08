from ex0.Creature import Creature


class Aquabub(Creature):
    """Creates a aquabub creature (first level)"""
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Water Gun!')
