import sys
import math


def calc_distance(coordinates: tuple) -> None:
    """Calculate distance between coordinates and (0,0,0); unpacking"""
    coordinates2 = (0, 0, 0)
    x, y, z = coordinates
    x2, y2, z2 = coordinates2
    distance = math.sqrt((x2-x)**2 + (y2-y)**2 + (z2-z)**2)
    print(f"Distance between {coordinates2} and "
          f"{coordinates}: {distance:.2f}\n")
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def ft_coordinate_system() -> None:
    """Convert input into tuple, show result and prevent errors"""
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) == 1:
        print("No values provided. Please add X, Y and Z values.")
        return
    if (len(sys.argv) != 2) and (len(sys.argv) != 4):
        print("Please add only three values: X, Y and Z.")
        return
    raw_input = ",".join(sys.argv[1:])
    try:
        values = []
        i = 1
        if (len(sys.argv) == 2):
            for i in range(1, len(sys.argv)):
                parts = sys.argv[i].split(",")
            for p in parts:
                values.append(int(p))
            if len(values) != 3:
                raise ValueError("Please add only three values: X, Y and Z.")
            print(f"Parsing coordinates: \"{raw_input}\"")
            coordinates = tuple(values)
            print(f"Parsed position: {coordinates}")
        else:
            for i in range(1, len(sys.argv)):
                values.append(int(sys.argv[i]))
            coordinates = tuple(values)
            print(f"Position created: {coordinates}")
        calc_distance(coordinates)
    except ValueError as e:
        print(f'\nParsing invalid coordinates: "{raw_input}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return


if __name__ == "__main__":
    ft_coordinate_system()
