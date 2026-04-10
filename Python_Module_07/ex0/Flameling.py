from ex0.Creature import Creature


class Flameling(Creature):
    """Creates a Flameling creature (first level)"""
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Ember!')
