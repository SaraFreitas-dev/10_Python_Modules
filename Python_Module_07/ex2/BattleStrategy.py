from abc import ABC, abstractmethod
from ex0.Creature import Creature


class BattleStrategy(ABC):
    """abstract class that defines the act and is_valid abstract methods."""
    @abstractmethod
    def act(self, creature: Creature) -> str:
        """act method will be called by the tournament script to either
        attack / heal or return an error if none is applied"""
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """The is_valid method returns a bool indicating that a Creature
        is suitable for the strategy"""
        pass
