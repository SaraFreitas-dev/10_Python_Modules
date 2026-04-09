from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex1.Shiftling import Shiftling
from ex1.Morphagon import Morphagon


class TransformCreatureFactory(CreatureFactory):
    """Perform a temporary transformation"""

    def create_base(self) -> Creature:
        """Creates a first level creature"""
        return Shiftling()

    def create_evolved(self) -> Creature:
        """Creates an evolved creature"""
        return Morphagon()
