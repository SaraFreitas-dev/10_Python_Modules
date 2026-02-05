def ft_ancient_text() -> None:
    """Open, read and close a file"""
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        file_name = "ancient_fragment.txt"
        print(f"Accessing Storage Vault: {file_name}\n"
              "Connection established...\n")
        with open(file_name) as file:
            print(file.read())
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("Error: That file was not found.")
    except Exception:
        print("Error: There was an unexpected anomaly.")


if __name__ == "__main__":
    ft_ancient_text()
