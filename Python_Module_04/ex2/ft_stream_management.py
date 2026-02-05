import sys


def ft_stream_management():
    """Streams"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {arch_id}: {status}")
    sys.stderr.write("\n[ALERT] System diagnostic: "
                     "Communication channels verified")
    sys.stdout.write("\n[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
