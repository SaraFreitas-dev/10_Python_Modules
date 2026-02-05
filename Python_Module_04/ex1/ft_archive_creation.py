def ft_archive_creation() -> None:
    """Create a new archive file and write preservation entries."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    file_name = 'new_discovery.txt'
    entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
    entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    try:
        print(f"Initializing new storage unit: {file_name}")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        with open(file_name, "w") as file:
            file.write(entry1)
            file.write(entry2)
            file.write(entry3)
        with open(file_name) as file:
            print(file.read())
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive \'{file_name}\' ready for long-term preservation.")
    except Exception:
        print("Error: There was an unexpected anomaly.")


if __name__ == "__main__":
    ft_archive_creation()
