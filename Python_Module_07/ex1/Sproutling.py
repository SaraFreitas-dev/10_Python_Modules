from ex0.Creature import Creature
from ex1.HealCapability import HealCapability


class Sproutling(Creature, HealCapability):
    """Level one healing creature"""
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Vine Whip!')

    def heal(self) -> str:
        """Apply the heal method. The target is optional"""
        return (f'{self.name} heals itself for a small amount')
