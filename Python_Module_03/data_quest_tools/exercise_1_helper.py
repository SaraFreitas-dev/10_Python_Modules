#!/usr/bin/env python3
"""
Exercise 1 Helper - Score Analytics with Elegant Data Generation
===============================================================

This helper provides elegant utilities for generating and analyzing player scores
in the Data Quest gaming environment. It demonstrates clean Python patterns
that learners can study and emulate.

Features:
    - Realistic score distributions
    - Edge case generation
    - Statistical analysis tools
    - Command line integration examples
"""

import random
import sys
import statistics
from typing import List, Dict, Optional


class ScoreAnalyticsGenerator:
    """Elegant score data generator with realistic gaming patterns."""

    def __init__(self, seed: Optional[int] = None):
        """Initialize generator with optional seed for reproducible results."""
        if seed is not None:
            random.seed(seed)

        self.player_archetypes = {
            'casual': {'min': 200, 'max': 800, 'weight': 0.4},
            'regular': {'min': 600, 'max': 1500, 'weight': 0.35},
            'competitive': {'min': 1200, 'max': 2500, 'weight': 0.20},
            'expert': {'min': 2000, 'max': 3500, 'weight': 0.05}
        }

        self.game_modes = {
            'tutorial': {'multiplier': 0.3, 'variance': 0.1},
            'casual': {'multiplier': 1.0, 'variance': 0.2},
            'ranked': {'multiplier': 1.5, 'variance': 0.15},
            'tournament': {'multiplier': 2.0, 'variance': 0.25}
        }

    def generate_realistic_scores(self, count: int = 20) -> List[int]:
        """
        Generate realistic score distribution based on gaming psychology.

        Args:
            count: Number of scores to generate

        Returns:
            List of integer scores following realistic patterns
        """
        scores = []

        for _ in range(count):
            # Select player archetype based on weights
            archetype = self._weighted_choice(self.player_archetypes)
            archetype_data = self.player_archetypes[archetype]

            # Generate base score within archetype range
            base_score = random.randint(
                archetype_data['min'], archetype_data['max'])

            # Apply game mode modifier
            mode = random.choice(list(self.game_modes.keys()))
            mode_data = self.game_modes[mode]

            # Calculate final score with variance
            multiplier = mode_data['multiplier']
            variance = mode_data['variance']

            # Add some randomness within variance
            final_multiplier = multiplier * \
                (1 + random.uniform(-variance, variance))
            final_score = int(base_score * final_multiplier)

            # Ensure minimum score of 0
            scores.append(max(0, final_score))

        return scores

    def _weighted_choice(self, choices: Dict[str, Dict]) -> str:
        """Select item based on weights using elegant algorithm."""
        total_weight = sum(data['weight'] for data in choices.values())
        random_value = random.uniform(0, total_weight)

        cumulative_weight = 0
        for choice, data in choices.items():
            cumulative_weight += data['weight']
            if random_value <= cumulative_weight:
                return choice

        # Fallback (should never reach here with proper weights)
        return list(choices.keys())[0]

    def generate_edge_cases(self) -> List[int]:
        """Generate edge cases for robust testing."""
        return [
            0,          # Minimum possible score
            1,          # Just above minimum
            999,        # Edge of 3-digit numbers
            1000,       # Start of 4-digit numbers
            9999,       # Edge of 4-digit numbers
            10000,      # Start of 5-digit numbers
            99999       # Large score
        ]

    def analyze_scores(self, scores: List[int]) -> Dict[str, float]:
        """
        Perform comprehensive statistical analysis on scores.

        Args:
            scores: List of integer scores

        Returns:
            Dictionary containing various statistical measures
        """
        if not scores:
            return {'error': 'No scores provided'}

        analysis = {
            'count': len(scores),
            'total': sum(scores),
            'mean': statistics.mean(scores),
            'median': statistics.median(scores),
            'mode': statistics.mode(scores) if len(
                set(scores)) < len(scores) else None,
            'min': min(scores),
            'max': max(scores),
            'range': max(scores) - min(scores),
            'std_dev': statistics.stdev(scores) if len(scores) > 1 else 0}

        # Add percentiles
        sorted_scores = sorted(scores)
        analysis['q1'] = self._percentile(sorted_scores, 25)
        analysis['q3'] = self._percentile(sorted_scores, 75)
        analysis['iqr'] = analysis['q3'] - analysis['q1']

        return analysis

    def _percentile(self, sorted_data: List[int], percentile: float) -> float:
        """Calculate percentile using elegant interpolation."""
        if not sorted_data:
            return 0

        index = (percentile / 100) * (len(sorted_data) - 1)
        lower_index = int(index)
        upper_index = min(lower_index + 1, len(sorted_data) - 1)

        if lower_index == upper_index:
            return sorted_data[lower_index]

        # Linear interpolation
        weight = index - lower_index
        return sorted_data[lower_index] * \
            (1 - weight) + sorted_data[upper_index] * weight

    def format_for_command_line(self, scores: List[int]) -> str:
        """Format scores for command line testing."""
        return ' '.join(map(str, scores))

    def generate_test_scenarios(self) -> Dict[str, List[int]]:
        """Generate various test scenarios for comprehensive testing."""
        return {
            'small_dataset': self.generate_realistic_scores(5),
            'medium_dataset': self.generate_realistic_scores(20),
            'large_dataset': self.generate_realistic_scores(100),
            'edge_cases': self.generate_edge_cases(),
            'uniform_scores': [1500] * 10,  # All same score
            # Perfectly ascending
            'ascending_scores': list(range(100, 1100, 100)),
            # High variance
            'high_variance': [100, 3000, 200, 2800, 150, 2900],
            'single_score': [1337],  # Single element
            'empty_list': []  # Edge case: no scores
        }

    def demonstrate_list_operations(self, scores: List[int]) -> None:
        """Demonstrate elegant list operations for educational purposes."""
        print("=== List Operations Demonstration ===")
        print(f"Original scores: {scores}")
        print()

        if not scores:
            print("Empty list - no operations possible")
            return

        # Basic operations
        print("Basic List Operations:")
        print(f"  Length: len(scores) = {len(scores)}")
        print(f"  Sum: sum(scores) = {sum(scores)}")
        print(f"  Maximum: max(scores) = {max(scores)}")
        print(f"  Minimum: min(scores) = {min(scores)}")
        print()

        # Sorting operations
        print("Sorting Operations:")
        print(f"  Sorted (ascending): {sorted(scores)}")
        print(f"  Sorted (descending): {sorted(scores, reverse=True)}")
        print()

        # List comprehensions preview
        print("List Comprehensions (Advanced Preview):")
        high_scores = [score for score in scores if score > 1000]
        print(f"  High scores (>1000): {high_scores}")

        doubled_scores = [score * 2 for score in scores[:3]]  # First 3 only
        print(f"  First 3 scores doubled: {doubled_scores}")
        print()

        # Slicing operations
        print("List Slicing:")
        print(f"  First 3 scores: {scores[:3]}")
        print(f"  Last 3 scores: {scores[-3:]}")
        print(f"  Every 2nd score: {scores[::2]}")


def main():
    """Elegant command line interface for the score generator."""
    generator = ScoreAnalyticsGenerator(seed=42)  # Reproducible results

    if len(sys.argv) == 1:
        # Interactive mode
        print("=== Score Analytics Generator ===")
        print("Elegant data generation for Exercise 1\n")

        print("Available commands:")
        print("  python3 exercise_1_helper.py generate [count]")
        print("  python3 exercise_1_helper.py analyze <score1> <score2> ...")
        print("  python3 exercise_1_helper.py scenarios")
        print("  python3 exercise_1_helper.py demo")
        print()

        # Generate sample data
        scores = generator.generate_realistic_scores(10)
        print("Sample realistic scores:")
        print(generator.format_for_command_line(scores))
        print()

        print("Test your ft_score_analytics.py with:")
        cmd = generator.format_for_command_line(scores)
        print(f"python3 ft_score_analytics.py {cmd}")

    elif sys.argv[1] == "generate":
        # Generate scores
        count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        scores = generator.generate_realistic_scores(count)
        print(generator.format_for_command_line(scores))

    elif sys.argv[1] == "analyze":
        # Analyze provided scores
        try:
            scores = [int(arg) for arg in sys.argv[2:]]
            analysis = generator.analyze_scores(scores)

            print("=== Score Analysis ===")
            for key, value in analysis.items():
                if isinstance(value, float):
                    print(f"{key.replace('_', ' ').title()}: {value:.2f}")
                else:
                    print(f"{key.replace('_', ' ').title()}: {value}")

        except ValueError:
            print("Error: All arguments must be valid integers")

    elif sys.argv[1] == "scenarios":
        # Show test scenarios
        scenarios = generator.generate_test_scenarios()

        print("=== Test Scenarios ===")
        for name, scores in scenarios.items():
            if scores:  # Skip empty list for command line display
                cmd_line = generator.format_for_command_line(scores)
                print(f"{name.replace('_', ' ').title()}:")
                print(f"  python3 ft_score_analytics.py {cmd_line}")
                print()
            else:
                print(f"{name.replace('_', ' ').title()}: (no arguments)")
                print("  python3 ft_score_analytics.py")
                print()

    elif sys.argv[1] == "demo":
        # Demonstrate list operations
        scores = generator.generate_realistic_scores(8)
        generator.demonstrate_list_operations(scores)

    else:
        print(f"Unknown command: {sys.argv[1]}")
        print("Use 'python3 exercise_1_helper.py' for help")


if __name__ == "__main__":
    main()
