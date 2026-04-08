from ex0.Creature import Creature
from ex0.CreatureFactory import CreatureFactory
from ex0.Aquabub import Aquabub
from ex0.Torragon import Torragon


class AquaFactory(CreatureFactory):
    """Creates Aqua type creatures"""

    def create_base(self) -> Creature:
        """Creates a first level creature (Aquabub)"""
        return Aquabub()

    def create_evolved(self) -> Creature:
        """Creates an evolved creature (Torragon)"""
        return Torragon()
