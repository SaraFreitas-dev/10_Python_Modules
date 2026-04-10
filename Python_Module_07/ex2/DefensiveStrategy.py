from ex2.BattleStrategy import BattleStrategy
from ex1.HealCapability import HealCapability
from ex0.Creature import Creature


class DefensiveStrategy(BattleStrategy):
    """Suitable for Creature with healing capabilities,
    that will attack and then heal during the tournament."""
    def act(self, creature: Creature) -> str:
        """act method will be called by the tournament script to
        heal or return an error if its not a heal creature"""
        if self.is_valid(creature):
            return creature.attack() + "\n" + creature.heal()
        else:
            raise ValueError(f"Invalid Creature '{creature.name}'"
                             " for this defensive strategy")

    def is_valid(self, creature: Creature) -> bool:
        """The is_valid method returns a bool indicating that a Creature
        is suitable for the strategy"""
        return isinstance(creature, HealCapability)
