from ex0.Card import Card
import random


class Deck:
    """Deck management system"""
    def __init__(self) -> None:
        self.cards_lst = list[Card] = []

    def add_card(self, card: Card) -> None:
        """add a card on the list"""
        self.cards_lst.append(Card)

    def remove_card(self, card_name: str) -> bool:
        """remove a card from the list"""
        self.cards_lst.remove(Card)

    def shuffle(self) -> None:
        pass

    def draw_card(self) -> Card:
        pass

    def get_deck_stats(self) -> dict:
        pass
