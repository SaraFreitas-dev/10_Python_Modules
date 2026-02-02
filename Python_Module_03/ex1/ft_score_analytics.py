import sys


def ft_score_analytics() -> None:
    """Accept player scores and perform the necessary calculations"""
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return
    try:
        numbers = []
        i = 1
        for i in range(1, len(sys.argv)):
            numbers.append(int(sys.argv[i]))
    except ValueError:
        print("Error: all scores must be numeric values.")
        return
    print(f"Scores processed: {numbers}")
    print(f"Total players: {len(numbers)}")
    print(f"Total score: {sum(numbers)}")
    print(f"Average score: {sum(numbers) / len(numbers)}")
    print(f"High score: {max(numbers)}")
    print(f"Low score: {min(numbers)}")
    print(f"Score range: {max(numbers) - min(numbers)}\n")


if __name__ == "__main__":
    ft_score_analytics()
