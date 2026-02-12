def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Check if values are incorrect - error handling"""
    if not plant_name:
        raise ValueError("Plant name cannot be empty!\n")
    elif (water_level < 1):
        raise ValueError(f"Water level {water_level} "
                         "is too low (min 1)\n")
    elif (water_level > 10):
        raise ValueError(f"Water level {water_level} "
                         "is too high (max 10)\n")
    elif (sunlight_hours < 2):
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too low (min 2)\n")
    elif (sunlight_hours > 12):
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too high (max 12)\n")
    else:
        return (f"Plant \'{plant_name}\' is healthy!\n")


def test_plant_checks() -> None:
    """Test the previous functions with different error types"""
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 3))
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 3, 4))
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing bad water level...")
    try:
        print(check_plant_health("lettuce", 15, 2))
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("carrots", 10, 0))
    except ValueError as e:
        print(f"Error: {e}")
    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
