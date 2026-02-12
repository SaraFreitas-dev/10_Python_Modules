#!/usr/bin/env python3
"""
DataDeck Card Generator

A utility to generate sample cards for testing your DataDeck implementation.
This module provides predefined card data and helper functions to create
test cards for your abstract classes and interfaces.

Usage:
    from tools.card_generator import CardGenerator
    
    generator = CardGenerator()
    creature = generator.get_creature("Fire Dragon")
    spell = generator.get_spell("Lightning Bolt")
"""

from typing import Dict, List, Any, Optional
import random


class CardGenerator:
    """
    Generates sample card data for DataDeck testing.
    
    This class provides methods to retrieve predefined card data
    that can be used to test your abstract card implementations.
    """
    
    def __init__(self) -> None:
        """Initialize the card generator with predefined card data."""
        self._creatures = [
            {"name": "Fire Dragon", "cost": 5, "rarity": "Legendary", "attack": 7, "health": 5},
            {"name": "Goblin Warrior", "cost": 2, "rarity": "Common", "attack": 2, "health": 1},
            {"name": "Ice Wizard", "cost": 4, "rarity": "Rare", "attack": 3, "health": 4},
            {"name": "Lightning Elemental", "cost": 3, "rarity": "Uncommon", "attack": 4, "health": 2},
            {"name": "Stone Golem", "cost": 6, "rarity": "Rare", "attack": 5, "health": 8},
            {"name": "Shadow Assassin", "cost": 3, "rarity": "Uncommon", "attack": 5, "health": 2},
            {"name": "Healing Angel", "cost": 4, "rarity": "Rare", "attack": 2, "health": 6},
            {"name": "Forest Sprite", "cost": 1, "rarity": "Common", "attack": 1, "health": 1},
        ]
        
        self._spells = [
            {"name": "Lightning Bolt", "cost": 3, "rarity": "Common", "effect_type": "damage"},
            {"name": "Healing Potion", "cost": 2, "rarity": "Common", "effect_type": "heal"},
            {"name": "Fireball", "cost": 4, "rarity": "Uncommon", "effect_type": "damage"},
            {"name": "Shield Spell", "cost": 1, "rarity": "Common", "effect_type": "buff"},
            {"name": "Meteor", "cost": 8, "rarity": "Legendary", "effect_type": "damage"},
            {"name": "Ice Shard", "cost": 2, "rarity": "Common", "effect_type": "damage"},
            {"name": "Divine Light", "cost": 5, "rarity": "Rare", "effect_type": "heal"},
            {"name": "Magic Missile", "cost": 1, "rarity": "Common", "effect_type": "damage"},
        ]
        
        self._artifacts = [
            {"name": "Mana Crystal", "cost": 2, "rarity": "Common", "durability": 5, "effect": "Permanent: +1 mana per turn"},
            {"name": "Sword of Power", "cost": 3, "rarity": "Uncommon", "durability": 3, "effect": "Permanent: +2 attack to equipped creature"},
            {"name": "Ring of Wisdom", "cost": 4, "rarity": "Rare", "durability": 4, "effect": "Permanent: Draw an extra card each turn"},
            {"name": "Shield of Defense", "cost": 5, "rarity": "Rare", "durability": 6, "effect": "Permanent: +3 health to all friendly creatures"},
            {"name": "Crown of Kings", "cost": 7, "rarity": "Legendary", "durability": 8, "effect": "Permanent: +1 cost reduction to all cards"},
            {"name": "Boots of Speed", "cost": 2, "rarity": "Uncommon", "durability": 2, "effect": "Permanent: Cards cost 1 less mana"},
            {"name": "Cloak of Shadows", "cost": 3, "rarity": "Uncommon", "durability": 3, "effect": "Permanent: Creatures have stealth"},
            {"name": "Staff of Elements", "cost": 6, "rarity": "Legendary", "durability": 7, "effect": "Permanent: +1 spell damage"},
        ]
    
    def get_creature(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get creature card data by name.
        
        Args:
            name: The name of the creature card
            
        Returns:
            Dictionary containing creature data, or None if not found
        """
        for creature in self._creatures:
            if creature["name"] == name:
                return creature.copy()
        return None
    
    def get_spell(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get spell card data by name.
        
        Args:
            name: The name of the spell card
            
        Returns:
            Dictionary containing spell data, or None if not found
        """
        for spell in self._spells:
            if spell["name"] == name:
                return spell.copy()
        return None
    
    def get_artifact(self, name: str) -> Optional[Dict[str, Any]]:
        """
        Get artifact card data by name.
        
        Args:
            name: The name of the artifact card
            
        Returns:
            Dictionary containing artifact data, or None if not found
        """
        for artifact in self._artifacts:
            if artifact["name"] == name:
                return artifact.copy()
        return None
    
    def get_random_creature(self) -> Dict[str, Any]:
        """
        Get a random creature card.
        
        Returns:
            Dictionary containing random creature data
        """
        return random.choice(self._creatures).copy()
    
    def get_random_spell(self) -> Dict[str, Any]:
        """
        Get a random spell card.
        
        Returns:
            Dictionary containing random spell data
        """
        return random.choice(self._spells).copy()
    
    def get_random_artifact(self) -> Dict[str, Any]:
        """
        Get a random artifact card.
        
        Returns:
            Dictionary containing random artifact data
        """
        return random.choice(self._artifacts).copy()
    
    def get_all_creatures(self) -> List[Dict[str, Any]]:
        """
        Get all available creature cards.
        
        Returns:
            List of dictionaries containing all creature data
        """
        return [creature.copy() for creature in self._creatures]
    
    def get_all_spells(self) -> List[Dict[str, Any]]:
        """
        Get all available spell cards.
        
        Returns:
            List of dictionaries containing all spell data
        """
        return [spell.copy() for spell in self._spells]
    
    def get_all_artifacts(self) -> List[Dict[str, Any]]:
        """
        Get all available artifact cards.
        
        Returns:
            List of dictionaries containing all artifact data
        """
        return [artifact.copy() for artifact in self._artifacts]
    
    def get_cards_by_rarity(self, rarity: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all cards of a specific rarity.
        
        Args:
            rarity: The rarity to filter by ("Common", "Uncommon", "Rare", "Legendary")
            
        Returns:
            Dictionary with card types as keys and lists of matching cards as values
        """
        result = {"creatures": [], "spells": [], "artifacts": []}
        
        for creature in self._creatures:
            if creature["rarity"] == rarity:
                result["creatures"].append(creature.copy())
        
        for spell in self._spells:
            if spell["rarity"] == rarity:
                result["spells"].append(spell.copy())
        
        for artifact in self._artifacts:
            if artifact["rarity"] == rarity:
                result["artifacts"].append(artifact.copy())
        
        return result
    
    def get_cards_by_cost(self, max_cost: int) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get all cards with cost less than or equal to max_cost.
        
        Args:
            max_cost: Maximum mana cost to filter by
            
        Returns:
            Dictionary with card types as keys and lists of matching cards as values
        """
        result = {"creatures": [], "spells": [], "artifacts": []}
        
        for creature in self._creatures:
            if creature["cost"] <= max_cost:
                result["creatures"].append(creature.copy())
        
        for spell in self._spells:
            if spell["cost"] <= max_cost:
                result["spells"].append(spell.copy())
        
        for artifact in self._artifacts:
            if artifact["cost"] <= max_cost:
                result["artifacts"].append(artifact.copy())
        
        return result
    
    def generate_random_deck(self, deck_size: int = 10) -> List[Dict[str, Any]]:
        """
        Generate a random deck of cards.
        
        Args:
            deck_size: Number of cards in the deck
            
        Returns:
            List of random card data dictionaries
        """
        all_cards = self._creatures + self._spells + self._artifacts
        deck = []
        
        for _ in range(deck_size):
            card = random.choice(all_cards).copy()
            deck.append(card)
        
        return deck
    
    def list_available_cards(self) -> None:
        """Print all available cards organized by type."""
        print("=== Available Cards ===\n")
        
        print("Creatures:")
        for creature in self._creatures:
            print(f"  - {creature['name']} ({creature['cost']} mana, {creature['rarity']})")
        
        print("\nSpells:")
        for spell in self._spells:
            print(f"  - {spell['name']} ({spell['cost']} mana, {spell['rarity']})")
        
        print("\nArtifacts:")
        for artifact in self._artifacts:
            print(f"  - {artifact['name']} ({artifact['cost']} mana, {artifact['rarity']})")


def main() -> None:
    """Demonstrate the card generator functionality."""
    generator = CardGenerator()
    
    print("=== DataDeck Card Generator Demo ===\n")
    
    # Show specific cards
    fire_dragon = generator.get_creature("Fire Dragon")
    lightning_bolt = generator.get_spell("Lightning Bolt")
    mana_crystal = generator.get_artifact("Mana Crystal")
    
    print("Sample Cards:")
    print(f"Creature: {fire_dragon}")
    print(f"Spell: {lightning_bolt}")
    print(f"Artifact: {mana_crystal}")
    
    print("\nRandom Cards:")
    print(f"Random Creature: {generator.get_random_creature()}")
    print(f"Random Spell: {generator.get_random_spell()}")
    
    print("\nLegendary Cards:")
    legendary_cards = generator.get_cards_by_rarity("Legendary")
    for card_type, cards in legendary_cards.items():
        if cards:
            print(f"{card_type.capitalize()}: {[card['name'] for card in cards]}")
    
    print("\nLow Cost Cards (3 mana or less):")
    low_cost_cards = generator.get_cards_by_cost(3)
    for card_type, cards in low_cost_cards.items():
        if cards:
            print(f"{card_type.capitalize()}: {len(cards)} cards")
    
    print(f"\nRandom Deck (5 cards): {[card['name'] for card in generator.generate_random_deck(5)]}")


if __name__ == "__main__":
    main()
