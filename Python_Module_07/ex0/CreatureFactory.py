from abc import ABC, abstractmethod
from ex0.Creature import Creature


class CreatureFactory(ABC):
    """abstract class that will allow you to create the base Creature
    and the evolved Creature for the same family"""

    @abstractmethod
    def create_base(self) -> Creature:
        """Creates a first level creature (Flameling or Aquabub)"""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Creates an evolved creature (Phyrodon or Torragon)"""
        pass
