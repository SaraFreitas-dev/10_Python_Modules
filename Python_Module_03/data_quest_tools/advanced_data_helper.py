#!/usr/bin/env python3
"""
Advanced Data Helper for Data Quest - The Pixel Dimension
=========================================================

This module provides advanced utilities for generating complex gaming data
scenarios and testing edge cases in your Python Module 03 exercises.

Usage:
    python3 advanced_data_helper.py [options]

Features:
    - Complex nested data structures
    - Edge case generators
    - Performance testing utilities
    - Data validation helpers
"""

import random
import sys
from typing import Dict, List, Tuple, Set, Any, Generator


class AdvancedDataHelper:
    """Advanced utilities for complex data scenarios."""

    def __init__(self):
        self.player_names = [
            "Alice",
            "Bob",
            "Charlie",
            "Diana",
            "Eve",
            "Frank",
            "Grace",
            "Henry",
            "Ivy",
            "Jack",
            "Kate",
            "Liam",
            "Maya",
            "Noah",
            "Olivia",
            "Paul"]

        self.achievements = [
            "first_kill", "level_10", "level_50", "level_100", "speedrun",
            "explorer", "treasure_hunter", "boss_slayer", "collector",
            "perfectionist", "social_butterfly", "lone_wolf", "strategist",
            "berserker", "pacifist", "completionist"
        ]

        self.item_types = [
            "sword", "shield", "potion", "bow", "arrow", "armor", "helmet",
            "boots", "ring", "amulet", "scroll", "gem", "key", "map"
        ]

    def generate_complex_scores(self, count: int = 100) -> List[int]:
        """Generate complex score distributions for testing."""
        scores = []

        # Normal distribution (70%)
        for _ in range(int(count * 0.7)):
            scores.append(random.randint(800, 1200))

        # High scores (20%)
        for _ in range(int(count * 0.2)):
            scores.append(random.randint(1500, 2500))

        # Low scores (10%)
        for _ in range(int(count * 0.1)):
            scores.append(random.randint(100, 500))

        random.shuffle(scores)
        return scores

    def generate_coordinate_clusters(
            self, clusters: int = 3, points_per_cluster: int = 10) -> List[Tuple[float, float]]:
        """Generate clustered coordinate data for advanced testing."""
        coordinates = []

        # Generate cluster centers
        centers = [(random.uniform(-50, 50), random.uniform(-50, 50))
                   for _ in range(clusters)]

        for center_x, center_y in centers:
            for _ in range(points_per_cluster):
                # Add some noise around the center
                x = center_x + random.uniform(-5, 5)
                y = center_y + random.uniform(-5, 5)
                coordinates.append((round(x, 2), round(y, 2)))

        return coordinates

    def generate_achievement_network(
            self, player_count: int = 20) -> Dict[str, Set[str]]:
        """Generate complex achievement networks with dependencies."""
        network = {}

        for i in range(player_count):
            player = f"player_{i:02d}"

            # Simulate achievement progression
            player_achievements = set()

            # Everyone gets basic achievements
            if random.random() > 0.1:  # 90% chance
                player_achievements.add("first_kill")

            if "first_kill" in player_achievements and random.random() > 0.3:
                player_achievements.add("level_10")

            if "level_10" in player_achievements and random.random() > 0.6:
                player_achievements.add("level_50")

            if "level_50" in player_achievements and random.random() > 0.8:
                player_achievements.add("level_100")

            # Add random achievements
            available = [
                a for a in self.achievements if a not in player_achievements]
            num_random = random.randint(0, min(5, len(available)))
            player_achievements.update(random.sample(available, num_random))

            network[player] = player_achievements

        return network

    def generate_nested_inventory(self, complexity: int = 3) -> Dict[str, Any]:
        """Generate deeply nested inventory structures."""
        inventory = {
            "players": {},
            "global_stats": {
                "total_items": 0,
                "total_value": 0,
                "rarest_items": []
            },
            "market_data": {
                "prices": {},
                "trends": {}
            }
        }

        for player in random.sample(
            self.player_names, min(
                8, len(
                self.player_names))):
            player_inv = {
                "items": {},
                "stats": {
                    "total_items": 0,
                    "total_value": 0,
                    "favorite_type": None
                },
                "history": []
            }

            # Generate items
            num_items = random.randint(3, 12)
            for _ in range(num_items):
                item = random.choice(self.item_types)
                quantity = random.randint(1, 10)
                value = random.randint(10, 500)

                if item in player_inv["items"]:
                    player_inv["items"][item]["quantity"] += quantity
                else:
                    player_inv["items"][item] = {
                        "quantity": quantity,
                        "value_per_unit": value,
                        "rarity": random.choice(["common", "uncommon", "rare", "epic", "legendary"])
                    }

                player_inv["stats"]["total_items"] += quantity
                player_inv["stats"]["total_value"] += quantity * value

            # Set favorite type
            if player_inv["items"]:
                player_inv["stats"]["favorite_type"] = max(
                    player_inv["items"].keys(),
                    key=lambda x: player_inv["items"][x]["quantity"]
                )

            inventory["players"][player] = player_inv
            inventory["global_stats"]["total_items"] += player_inv["stats"]["total_items"]
            inventory["global_stats"]["total_value"] += player_inv["stats"]["total_value"]

        return inventory

    def generate_streaming_data(
            self, duration: int = 100) -> Generator[Dict[str, Any], None, None]:
        """Generate streaming game events for generator testing."""
        event_types = [
            "kill",
            "death",
            "level_up",
            "item_found",
            "quest_complete"]

        for i in range(duration):
            yield {
                "timestamp": i,
                "player": random.choice(self.player_names),
                "event_type": random.choice(event_types),
                "data": {
                    "value": random.randint(1, 100),
                    "location": (random.uniform(-100, 100), random.uniform(-100, 100)),
                    "metadata": {
                        "session_id": f"session_{random.randint(1000, 9999)}",
                        "server": f"server_{random.randint(1, 10)}"
                    }
                }
            }

    def validate_data_structure(self, data: Any, expected_type: str) -> bool:
        """Validate data structures for testing."""
        type_map = {
            "list": list,
            "tuple": tuple,
            "set": set,
            "dict": dict
        }

        if expected_type not in type_map:
            return False

        return isinstance(data, type_map[expected_type])

    def performance_test_data(self, size: str = "medium") -> Dict[str, Any]:
        """Generate data for performance testing."""
        sizes = {
            "small": 100,
            "medium": 1000,
            "large": 10000,
            "huge": 100000
        }

        count = sizes.get(size, 1000)

        return {
            "scores": [random.randint(0, 3000) for _ in range(count)],
            "coordinates": [(random.uniform(-1000, 1000), random.uniform(-1000, 1000))
                            for _ in range(count // 10)],
            "achievements": {f"player_{i}": set(random.sample(self.achievements,
                                                              random.randint(1, len(self.achievements))))
                             for i in range(count // 100)},
            "inventory": {f"player_{i}": {item: random.randint(1, 50)
                                          for item in random.sample(self.item_types, random.randint(1, 5))}
                          for i in range(count // 200)}
        }


def main():
    """Main function for command-line usage."""
    helper = AdvancedDataHelper()

    if len(sys.argv) < 2:
        print("Advanced Data Helper - Usage Examples:")
        print("  python3 advanced_data_helper.py scores")
        print("  python3 advanced_data_helper.py coordinates")
        print("  python3 advanced_data_helper.py achievements")
        print("  python3 advanced_data_helper.py inventory")
        print("  python3 advanced_data_helper.py streaming")
        print("  python3 advanced_data_helper.py performance")
        return

    command = sys.argv[1].lower()

    if command == "scores":
        scores = helper.generate_complex_scores(50)
        print("Complex score distribution:")
        print(" ".join(map(str, scores[:20])))  # Show first 20
        print(f"... and {len(scores) - 20} more")

    elif command == "coordinates":
        coords = helper.generate_coordinate_clusters(3, 5)
        print("Clustered coordinates:")
        for x, y in coords[:10]:
            print(f"  ({x}, {y})")
        print(f"... and {len(coords) - 10} more")

    elif command == "achievements":
        network = helper.generate_achievement_network(5)
        print("Achievement network:")
        for player, achievements in network.items():
            print(f"  {player}: {len(achievements)} achievements")

    elif command == "inventory":
        inventory = helper.generate_nested_inventory()
        print("Nested inventory structure:")
        print(f"  Players: {len(inventory['players'])}")
        print(f"  Total items: {inventory['global_stats']['total_items']}")
        print(f"  Total value: {inventory['global_stats']['total_value']}")

    elif command == "streaming":
        print("Streaming data (first 10 events):")
        for i, event in enumerate(helper.generate_streaming_data(10)):
            print(f"  Event {i}: {event['event_type']} by {event['player']}")

    elif command == "performance":
        data = helper.performance_test_data("medium")
        print("Performance test data generated:")
        for key, value in data.items():
            print(f"  {key}: {len(value)} items")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
