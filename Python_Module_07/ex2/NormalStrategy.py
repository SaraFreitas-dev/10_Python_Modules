from ex2.BattleStrategy import BattleStrategy
from ex0.Creature import Creature


class NormalStrategy(BattleStrategy):
    """Suitable for any Creature, that will simply use the
    attack method during the tournament."""
    def act(self, creature: Creature) -> str:
        """act method will be called by the tournament script to either
        attack / heal or return an error if none is applied"""
        if self.is_valid(creature):
            return creature.attack()
        else:
            raise ValueError(f"Invalid Creature '{creature.name}'"
                             " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        """The is_valid method returns a bool indicating that a Creature
        is suitable for the strategy"""
        return isinstance(creature, Creature)
