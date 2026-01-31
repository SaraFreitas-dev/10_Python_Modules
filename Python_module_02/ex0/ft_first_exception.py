def check_temperature(temp_str: str) -> None:
    """Validate inputs"""
    print(f'Testing temperature: {temp_str}')
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: \'{temp_str}\' is not a valid number")
        return
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp}°C is perfect for plants!")


def test_temperature_input() -> None:
    """Test the previous function with different values"""
    tests = ["25", "abc", "100", "-50"]
    try:
        print("=== Garden Temperature Checker ===\n")
        for t in tests:
            try:
                check_temperature(t)
                print()
            except ValueError as exc:
                print(exc)
                print()
    finally:
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
