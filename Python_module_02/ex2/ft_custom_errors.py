class GardenError(Exception):
    """Base exception for garden-related errors"""
    pass

class PlantError(GardenError):
    """Raised when a plant-related error occurs"""
    pass

class WaterError(GardenError):
    """Raised when a watering-related error occurs"""
    pass


def plant_error(plant_name: str, health: int) -> None:
    """Raises plant error exception message"""
    if health < 3:
        raise PlantError(f"The {plant_name} plant is wilting!")


def water_error(water_amount: int) -> None:
    """Raises water error exception message"""
    if water_amount < 5:
        raise WaterError(f"Not enough water in the tank!")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        plant_error("Tomato", 1)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        water_error(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        plant_error("Tomato", 1)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        water_error(2)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    test_errors()
