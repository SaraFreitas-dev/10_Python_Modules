import alchemy
import alchemy.elements


def ft_sacred_scroll() -> None:
    """Print the output from Part I"""
    print("\n=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    for name in ["create_fire", "create_water", "create_earth", "create_air"]:
        try:
            fe = getattr(alchemy.elements, name)
            print(f"alchemy.elements.{name}():", fe())
        except AttributeError:
            print(f"alchemy.{name}(): AttributeError - not exposed")

    print("\nTesting package-level access (controlled by __init__.py):")
    for name in ["create_fire", "create_water", "create_earth", "create_air"]:
        try:
            f = getattr(alchemy, name)
            print(f"alchemy.{name}():", f())
        except AttributeError:
            print(f"alchemy.{name}(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print("Version:", alchemy.__version__)
    print("Author:", alchemy.__author__)


if __name__ == "__main__":
    ft_sacred_scroll()
