from ex0.Creature import Creature
from ex1.HealCapability import HealCapability


class Bloomelle(Creature, HealCapability):
    """Level two healing creature"""
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        return (f'{self.name} uses Petal Dance!')

    def heal(self) -> str:
        """Apply the heal method. The target is optional"""
        return (f'{self.name} heals itself and others for a large amount')
