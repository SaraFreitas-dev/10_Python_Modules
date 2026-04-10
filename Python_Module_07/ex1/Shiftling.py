from ex0.Creature import Creature
from ex1.TransformCapability import TransformCapability


class Shiftling(Creature, TransformCapability):
    """Level one transform creature"""
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self.transformed = 0

    def attack(self) -> str:
        """Str to describe the attack that this creature has"""
        if self.transformed == 0:
            return (f'{self.name} attacks normally.')
        else:
            return (f'{self.name} performs a boosted strike!')

    def transform(self) -> str:
        """Transform the creature for a short period"""
        self.transformed = 1
        return (f'{self.name} shifts into a sharper form!')

    def revert(self) -> str:
        """Reverse the creature back to its original form"""
        self.transformed = 0
        return (f'{self.name} returns to normal.')
