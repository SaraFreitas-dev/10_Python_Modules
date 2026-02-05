def handle_errors(file_name: str) -> None:
    """Attempts to access files and handles every type of possible error"""
    try:
        with open(file_name, "r") as file:
            file.read()
            print(
                f"ROUTINE ACCESS: attempting access to '{file_name}'...\n"
                f"SUCCESS: Archive recovered - '{file_name}'\n"
                "STATUS: Normal operations resumed\n"
            )
    except FileNotFoundError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...\n"
            "RESPONSE: Archive not found in the matrix\n"
            "STATUS: Crisis handled, system stable\n"
        )
    except PermissionError:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...\n"
            "RESPONSE: Security protocols deny access\n"
            "STATUS: Crisis handled, security maintained\n"
        )
    except Exception:
        print(
            f"CRISIS ALERT: Attempting access to '{file_name}'...\n"
            "RESPONSE: There was an unexpected anomaly.\n"
            "STATUS: Crisis handled, security maintained\n"
        )


def ft_crisis_response() -> None:
    """Main function - Test several error types"""
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    handle_errors('lost_archive.txt')
    handle_errors('classified_vault.txt')
    handle_errors('standard_archive.txt')
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
