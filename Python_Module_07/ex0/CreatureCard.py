from ex0.Card import Card


class CreatureCard(Card):
    """Create a concrete implementation that Inherits from Card"""
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """use the abstact function from Card"""
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        else:
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }

    def get_card_info(self) -> dict:
        """return the dictionary with the info from the card"""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        }

    def attack_target(self, target: str) -> dict:
        """for creature combat | Validates that attack
        and health are positive integers"""
        if self.health <= 0:
            combat_resolved = False
            damage_dealt = 0
        else:
            combat_resolved = True
            damage_dealt = self.attack
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": damage_dealt,
            "combat_resolved": combat_resolved
        }
