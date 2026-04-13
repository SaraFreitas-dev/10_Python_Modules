from ex2.BattleStrategy import BattleStrategy
from ex1.TransformCapability import TransformCapability
from ex0.Creature import Creature
from typing import cast


class AggressiveStrategy(BattleStrategy):
    """Suitable for Creature with transform capabilities,
    that will transform, attack, and revert during the tournament."""
    def act(self, creature: Creature) -> str:
        """act method will be called by the tournament script to
        transform or return an error if its not a transform creature"""
        if self.is_valid(creature):
            transformer = cast(TransformCapability, creature)
            return (transformer.transform() + "\n"
                    + creature.attack() + "\n"
                    + transformer.revert())
        else:
            raise ValueError(f"Invalid Creature '{creature.name}'"
                             " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        """The is_valid method returns a bool indicating that a Creature
        is suitable for the strategy"""
        return isinstance(creature, TransformCapability)
