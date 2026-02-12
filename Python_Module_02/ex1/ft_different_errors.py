def garden_operations(test_str: str) -> None:
    """Forcing different type of errors"""
    if (test_str == "ValueError"):
        int("abc")
    elif (test_str == "ZeroDivisionError"):
        10/0
    elif (test_str == "FileNotFoundError"):
        open("missing.txt")
    elif (test_str == "KeyError"):
        my_garden = {}
        my_garden["missing_plant"]


def test_error_types() -> None:
    """Catiching each error"""
    print("=== Garden Error Types Demo ===\n")
    tests = ["ValueError",
             "ZeroDivisionError",
             "FileNotFoundError",
             "KeyError"]
    for error in tests:
        try:
            print(f"Testing {error}...")
            garden_operations(error)
        except ValueError:
            print(f"Caught {error}: invalid literal for int()\n")
        except ZeroDivisionError:
            print(f"Caught {error}: division by zero\n")
        except FileNotFoundError as e:
            print(f"Caught {error}: No such file \'{e.filename}\'\n")
        except KeyError as e:
            print(f"Caught {error}: \'{e.args[0]}\'\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
