from ex0.CreatureFactory import CreatureFactory
from ex0.Creature import Creature
from ex1.Sproutling import Sproutling
from ex1.Bloomelle import Bloomelle


class HealingCreatureFactory(CreatureFactory):
    """Create the family base of the creature"""

    def create_base(self) -> Creature:
        """Creates a first level creature"""
        return Sproutling()

    def create_evolved(self) -> Creature:
        """Creates an evolved creature"""
        return Bloomelle()
