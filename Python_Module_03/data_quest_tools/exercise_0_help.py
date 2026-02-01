"""
Exercise 0 Helper - Discovering Command Line Arguments
This file helps you understand how to receive data from external sources.
"""


def explore_command_line():
    """
    Explore how Python programs can receive information from outside.
    Run this file with different arguments to see what happens!
    """
    print("=== Exploring Command Line Arguments ===")
    print()

    # Let's discover what sys.argv contains
    import sys

    print("What is sys.argv?")
    print(f"sys.argv = {sys.argv}")
    print(f"Type of sys.argv: {type(sys.argv)}")
    print(f"Length of sys.argv: {len(sys.argv)}")
    print()

    print("Let's examine each element:")
    for i, arg in enumerate(sys.argv):
        print(f"  sys.argv[{i}] = '{arg}' (type: {type(arg)})")
    print()

    # Show how to process arguments
    if len(sys.argv) > 1:
        print("Arguments passed to the program:")
        for i, arg in enumerate(sys.argv[1:], 1):
            print(f"  Argument {i}: {arg}")
        print()

        # Try to convert to numbers
        print("Trying to convert arguments to numbers:")
        numbers = []
        for arg in sys.argv[1:]:
            try:
                number = int(arg)
                numbers.append(number)
                print(f"  '{arg}' -> {number} ✓")
            except ValueError:
                print(f"  '{arg}' -> Not a valid number ✗")

        if numbers:
            print(f"\nValid numbers found: {numbers}")
            print(f"Sum: {sum(numbers)}")
            print(f"Average: {sum(numbers) / len(numbers)}")
            print(f"Max: {max(numbers)}")
            print(f"Min: {min(numbers)}")
    else:
        print("No arguments provided!")
        print("Try running: python3 exercise_0_help.py 100 200 300")

    print("\n" + "=" * 50)
    print("DISCOVERY HINTS for Exercise 0:")
    print("1. sys.argv[0] is always the script name")
    print("2. sys.argv[1:] contains the arguments you passed")
    print("3. All arguments come as strings - you need to convert them")
    print("4. Use try/except to handle invalid conversions")
    print("5. Lists are perfect for storing collections of scores!")


def demonstrate_list_operations():
    """
    Show why lists are perfect for score analytics.
    """
    print("\n=== Why Lists Are Perfect for Scores ===")

    # Sample scores
    scores = [1500, 2300, 1800, 2100, 1950]
    print(f"Sample scores: {scores}")
    print()

    # List operations useful for analytics
    print("Useful list operations for analytics:")
    print(f"  len(scores) = {len(scores)} (count of players)")
    print(f"  sum(scores) = {sum(scores)} (total score)")
    print(f"  max(scores) = {max(scores)} (highest score)")
    print(f"  min(scores) = {min(scores)} (lowest score)")
    print(f"  sorted(scores) = {sorted(scores)} (ordered scores)")
    print()

    # Adding new scores
    print("Lists are mutable - you can add new scores:")
    scores.append(2500)
    print(f"  After append(2500): {scores}")

    scores.extend([1700, 1900])
    print(f"  After extend([1700, 1900]): {scores}")
    print()

    # List comprehensions preview
    print("Preview of list power (you'll learn more about this later):")
    high_scores = [score for score in scores if score > 2000]
    print(f"  High scores (>2000): {high_scores}")


if __name__ == "__main__":
    explore_command_line()
    demonstrate_list_operations()

    print("\n🎯 YOUR MISSION:")
    print("Create ft_score_analytics.py that:")
    print("1. Gets scores from command line arguments (like this program does)")
    print("2. Converts them to integers with error handling")
    print("3. Stores them in a list")
    print("4. Calculates and displays analytics")
    print("5. Handles edge cases (no args, invalid args)")
    print("\nGood luck, data engineer! 🚀")
