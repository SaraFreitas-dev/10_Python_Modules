def water_plant(plant_list: list) -> None:
    """Check for errors"""
    print("Opening watering system")
    try:
        for plant in plant_list:
            if not isinstance(plant, str):
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Tests on different error types"""
    ok_list = ["tomato",
               "lettuce",
               "carrots"]
    ko_list = ["tomato",
               None]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plant(ok_list)
    print("Watering completed successfully!\n")
    print("Testing with error...")
    water_plant(ko_list)
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
