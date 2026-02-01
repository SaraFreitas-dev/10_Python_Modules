import sys


def ft_command_quest() -> None:
    """Receive, show and count the arguments received"""
    print("=== Command Quest ===")
    program_name = sys.argv[0].split("/")[-1].split("\\")[-1]
    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {len(sys.argv) - 1}")
    i = 1
    while i < len(sys.argv):
        print(f"Argument {i}: {sys.argv[i]}")
        i += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()
