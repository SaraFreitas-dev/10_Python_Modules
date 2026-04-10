from ex0.Creature import Creature
from ex0.CreatureFactory import CreatureFactory
from ex0.Flameling import Flameling
from ex0.Pyrodon import Pyrodon


class FlameFactory(CreatureFactory):
    """Creates flame type creatures"""

    def create_base(self) -> Creature:
        """Creates a first level creature (flameling)"""
        return Flameling()

    def create_evolved(self) -> Creature:
        """Creates an evolved creature (Phyrodon)"""
        return Pyrodon()
