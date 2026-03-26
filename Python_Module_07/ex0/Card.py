from abc import ABC, abstractmethod


class Card(ABC):
    """Abstract card used for all card types"""
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """abstract method to use in the creature class"""
        ...

    def get_card_info(self) -> dict:
        return {"name": self.name,
                "cost": self.cost,
                "rarity": self.rarity
                }

    def is_playable(self, available_mana: int) -> bool:
        """Simple return boolean value, check if the play is possible"""
        if (available_mana >= self.cost):
            return True
        return False
