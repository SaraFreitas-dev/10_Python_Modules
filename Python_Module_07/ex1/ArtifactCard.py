from ex0.Card import Card
from .SpellCard import EffectType


class ArtifactCard(Card):
    """Permanent game modifiers"""
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """Play the spell if enough mana is available
        and return result dict."""
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"card_played": self.name, "mana_used": 0,
                    "effect": "Not enough mana"}

        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect
                }

    def activate_ability(self) -> dict:
        pass
