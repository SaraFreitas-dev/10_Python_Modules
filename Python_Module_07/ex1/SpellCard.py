from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    """Enum class for effect_type (used in spell cards)"""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """Instant magic effects"""
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = EffectType(effect_type.lower())

    def play(self, game_state: dict) -> dict:
        """Play the spell if enough mana is available
        and return result dict."""
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {"card_played": self.name, "mana_used": 0,
                    "effect": "Not enough mana"}
        # From de card generator
        targets = game_state.get("targets", [])
        effect_desc = self.resolve_effect(targets)["effect"]
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": effect_desc
                }

    def resolve_effect(self, targets: list) -> dict:
        """Apply spell effect to given targets and return a result dict."""
        target = "target"
        if targets:
            t = targets[0]
            target = t if isinstance(t, str) else getattr(t, "name", "target")

        if self.effect_type == EffectType.DAMAGE:
            effect = f"Deal 3 damage to {target}"
        elif self.effect_type == EffectType.HEAL:
            effect = f"Restore 3 health to {target}"
        elif self.effect_type == EffectType.BUFF:
            effect = f"Increase {target}'s attack by 2"
        else:
            effect = f"Reduce {target}'s attack by 2"

        return {"effect": effect}
