#!/usr/bin/env python3
"""
Data Quest: The Pixel Dimension - Unified Data Generator
Generates coherent test data for all exercises with elegant Python patterns.
"""

import random
import sys
from typing import List, Dict, Tuple, Any


class PixelDataGenerator:
    """Elegant data generator for gaming analytics exercises."""

    def __init__(self, seed: int = 42):
        """Initialize with reproducible seed for consistent testing."""
        random.seed(seed)
        self.players = ['alice', 'bob', 'charlie', 'diana', 'eve', 'frank']
        self.achievements = [
            'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
            'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer'
        ]
        self.items = {
            'pixel_sword': {'type': 'weapon', 'value': 150, 'rarity': 'common'},
            'quantum_ring': {'type': 'accessory', 'value': 500, 'rarity': 'rare'},
            'health_byte': {'type': 'consumable', 'value': 25, 'rarity': 'common'},
            'data_crystal': {'type': 'material', 'value': 1000, 'rarity': 'legendary'},
            'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}
        }

    def generate_exercise_data(self, exercise_num: int, **kwargs) -> Any:
        """Generate data for specific exercise with elegant dispatch."""
        generators = {
            0: self._command_for_quest,
            1: self._scores_for_analytics,
            2: self._coordinates_for_system,
            3: self._achievements_for_tracker,
            4: self._inventory_for_system,
            5: self._events_for_stream,
            6: self._analytics_for_dashboard
        }

        if exercise_num not in generators:
            raise ValueError(f"Exercise {exercise_num} not supported")

        return generators[exercise_num](**kwargs)

    def _command_for_quest(
            self,
            count: int = 8,
            format_type: str = 'list') -> Any:
        """Generate command line arguments for sys.argv discovery."""
        commands = [
            ['status', '--verbose'],
            ['analyze', 'player1', 'player2', '--format=json'],
            ['help', 'commands'],
            ['version'],
            ['config', '--set', 'debug=true'],
            ['list', '--all', '--sort=name'],
            ['export', 'data.json', '--compress'],
            ['import', 'backup.json', '--merge']
        ]

        selected = random.sample(commands, min(count, len(commands)))

        if format_type == 'argv':
            return ' '.join(random.choice(selected))
        elif format_type == 'list':
            return selected
        return selected

    def _scores_for_analytics(
            self,
            count: int = 10,
            format_type: str = 'list') -> Any:
        """Generate player scores for command line analytics."""
        scores = [random.randint(100, 2000) for _ in range(count)]

        if format_type == 'argv':
            return ' '.join(map(str, scores))
        elif format_type == 'list':
            return scores
        return scores

    def _coordinates_for_system(
            self, count: int = 8) -> List[Tuple[int, int, int]]:
        """Generate 3D coordinates for tuple unpacking practice."""
        coordinates = []
        for _ in range(count):
            # 3D coordinate (x, y, z)
            coordinates.append((
                random.randint(-50, 50),
                random.randint(-50, 50),
                random.randint(-25, 25)
            ))
        return coordinates

    def _achievements_for_tracker(self) -> Dict[str, List[str]]:
        """Generate player achievements with duplicates for set operations."""
        player_achievements = {}

        for player in self.players:
            # Create list with intentional duplicates to demonstrate set power
            achievements_list = []
            num_unique = random.randint(3, 6)

            # Add unique achievements
            selected = random.sample(self.achievements, num_unique)
            achievements_list.extend(selected)

            # Add some duplicates to show set deduplication
            for _ in range(random.randint(2, 4)):
                achievements_list.append(random.choice(selected))

            player_achievements[player] = achievements_list

        return player_achievements

    def _inventory_for_system(self) -> Dict[str, Any]:
        """Generate nested inventory data for dictionary operations."""
        player_inventories = {}

        for player in self.players[:4]:  # Limit for clarity
            # Each player gets random items with quantities
            selected_items = random.sample(
                list(
                    self.items.keys()), random.randint(
                    2, 4))
            inventory = {item: random.randint(1, 3) for item in selected_items}

            # Calculate total value using item catalog
            total_value = sum(
                self.items[item]['value'] * quantity
                for item, quantity in inventory.items()
            )

            player_inventories[player] = {
                'items': inventory,
                'total_value': total_value,
                'item_count': sum(inventory.values())
            }

        return {
            'players': player_inventories,
            'catalog': self.items
        }

    def _events_for_stream(self, count: int = 50) -> List[Dict[str, Any]]:
        """Generate game events for generator/streaming practice."""
        event_types = [
            'login',
            'logout',
            'kill',
            'death',
            'level_up',
            'item_found']
        events = []

        for event_id in range(1, count + 1):
            event = {
                'id': event_id,
                'player': random.choice(self.players),
                'event_type': random.choice(event_types),
                'timestamp': f"2024-01-{random.randint(1, 30):02d}T{random.randint(0, 23):02d}:{random.randint(0, 59):02d}",
                'data': {
                    'level': random.randint(1, 50),
                    'score_delta': random.randint(-100, 500),
                    'zone': f"pixel_zone_{random.randint(1, 5)}"
                }
            }
            events.append(event)

        return events

    def _analytics_for_dashboard(self) -> Dict[str, Any]:
        """Generate comprehensive data for comprehension exercises."""
        # Player statistics
        players_data = {
            player: {
                'level': random.randint(1, 50),
                'total_score': random.randint(1000, 10000),
                'sessions_played': random.randint(10, 100),
                'favorite_mode': random.choice(['casual', 'competitive', 'ranked']),
                'achievements_count': random.randint(1, len(self.achievements))
            }
            for player in self.players
        }

        # Session data for comprehensions
        sessions = [
            {
                'player': random.choice(self.players),
                'duration_minutes': random.randint(5, 120),
                'score': random.randint(100, 3000),
                'mode': random.choice(['casual', 'competitive', 'ranked']),
                'completed': random.choice([True, False])
            }
            for _ in range(30)
        ]

        return {
            'players': players_data,
            'sessions': sessions,
            'game_modes': ['casual', 'competitive', 'ranked'],
            'achievements': self.achievements
        }

    def generate_test_commands(self) -> None:
        """Generate ready-to-use command line examples for testing."""
        print("🎮 Generating Data Quest test commands...")
        print("Copy and paste these commands to test your exercises:\n")

        exercises = [
            (0, "Command Quest", {}),
            (1, "Score Cruncher", {'count': 8, 'format_type': 'argv'}),
            (2, "Coordinate System", {'count': 5}),
            (3, "Achievement Tracker", {}),
            (4, "Inventory System", {}),
            (5, "Data Stream Processor", {'count': 10}),
            (6, "Analytics Dashboard", {})
        ]

        for ex_num, ex_name, kwargs in exercises:
            print(f"=== Exercise {ex_num}: {ex_name} ===")

            if ex_num == 0:  # Command Quest
                commands = self.generate_exercise_data(ex_num, **kwargs)
                for i, cmd in enumerate(commands[:3], 1):
                    cmd_str = ' '.join(cmd)
                    print(f"Test {i}: python3 ft_command_quest.py {cmd_str}")

            elif ex_num == 1:  # Score Cruncher
                scores = self.generate_exercise_data(ex_num, **kwargs)
                print(f"Test: python3 ft_score_analytics.py {scores}")

            else:
                print(
                    f"Data available via: python3 data_generator.py {ex_num}")

            print()

        print("🚀 All test commands ready!")

    def show_examples(self) -> None:
        """Display usage examples for each exercise."""
        print("\n=== Data Quest: Exercise Examples ===\n")

        # Exercise 0 - Command Quest
        commands = self.generate_exercise_data(0, count=3, format_type='argv')
        print("Exercise 0 - Command Quest:")
        print(f"  Command line test: python3 ft_command_quest.py {commands}")
        print()

        # Exercise 1 - Score Analytics
        scores = self.generate_exercise_data(1, count=6, format_type='argv')
        print("Exercise 1 - Score Cruncher:")
        print(f"  Command line test: python3 ft_score_analytics.py {scores}")
        print()

        # Exercise 2 - Coordinate examples
        coords = self.generate_exercise_data(2, count=3)
        print("Exercise 2 - 3D Coordinate System:")
        for i, coord in enumerate(coords, 1):
            print(f"  Coordinate {i}: {coord} (3D)")
        print()

        # Exercise 3 - Achievement sets
        achievements = self.generate_exercise_data(3)
        print("Exercise 3 - Achievement Tracker:")
        for player, player_achievements in list(achievements.items())[:2]:
            unique_count = len(set(player_achievements))
            total_count = len(player_achievements)
            print(
                f"  {player}: {total_count} total, {unique_count} unique achievements")
        print()

        # Exercise 4 - Inventory preview
        inventory = self.generate_exercise_data(4)
        print("Exercise 4 - Inventory System:")
        for player, data in list(inventory['players'].items())[:2]:
            print(
                f"  {player}: {len(data['items'])} items, {data['total_value']} gold value")
        print()

        # Exercise 5 - Event stream
        events = self.generate_exercise_data(5, count=3)
        print("Exercise 5 - Data Stream Processor:")
        for event in events:
            print(
                f"  Event {event['id']}: {event['player']} - {event['event_type']}")
        print()

        # Exercise 6 - Analytics overview
        analytics = self.generate_exercise_data(6)
        print("Exercise 6 - Analytics Dashboard:")
        print(f"  Players: {len(analytics['players'])}")
        print(f"  Sessions: {len(analytics['sessions'])}")
        print(f"  Game modes: {analytics['game_modes']}")


def main():
    """Elegant command line interface."""
    generator = PixelDataGenerator()

    if len(sys.argv) > 1:
        # Command line usage: python3 data_generator.py <exercise_num>
        # [options]
        try:
            exercise_num = int(sys.argv[1])

            # Parse options
            kwargs = {}
            if '--count' in sys.argv:
                idx = sys.argv.index('--count') + 1
                if idx < len(sys.argv):
                    kwargs['count'] = int(sys.argv[idx])

            if '--format' in sys.argv:
                idx = sys.argv.index('--format') + 1
                if idx < len(sys.argv):
                    kwargs['format_type'] = sys.argv[idx]

            # Generate and display data
            data = generator.generate_exercise_data(exercise_num, **kwargs)
            print(data)

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
            print(
                "Usage: python3 data_generator.py <exercise_num> [--count N] [--format argv|list]")
    else:
        # Interactive mode
        print("=== Data Quest: The Pixel Dimension - Data Generator ===")
        print("Generate test data for your Python exercises.\n")

        choice = input(
            "Choose option:\n1. Generate test commands\n2. Show examples\n3. Both\nChoice (1/2/3): ")

        if choice in ['1', '3']:
            generator.generate_test_commands()

        if choice in ['2', '3']:
            generator.show_examples()

        print("\nHappy coding, pixel warrior! 🎮")


if __name__ == "__main__":
    main()
