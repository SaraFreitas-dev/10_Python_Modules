def check_temperature(temp_str: str) -> int:
    """Validate inputs"""
    print(f'Testing temperature: {temp_str}')
    try:
        temp = int(temp_str)
    except ValueError as exc:
        raise ValueError(f"Error: '{temp_str}' "
                         "is not a valid number\n") from exc
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp


def test_temperature_input() -> None:
    """Test the previous function with different values"""
    tests = ["25", "abc", "100", "-50"]
    try:
        print("=== Garden Temperature Checker ===\n")
        for t in tests:
            try:
                check_temperature(t)
            except ValueError as exc:
                print(exc)
    finally:
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
