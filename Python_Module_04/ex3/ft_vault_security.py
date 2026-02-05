def ft_vault_security() -> None:
    """"""
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    try:
        print("Initiating secure vault access...\n"
              "Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION:")
        file_name = 'classified_data.txt'
        with open(file_name) as file:
            print(file.read())

        print("\nSECURE PRESERVATION:")
        new_text = "\n[CLASSIFIED] New security protocols archived"
        with open(file_name, "a") as file:
            file.write(new_text)
        last_line = ""
        with open(file_name, "r") as file:
            for line in file:
                last_line = line
        print(last_line)

        print("Vault automatically sealed upon completion\n"
              "\nAll vault operations completed with maximum security.")

    except Exception:
        print("Error: There was an unexpected anomaly.")


if __name__ == "__main__":
    ft_vault_security()
