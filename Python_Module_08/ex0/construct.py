import sys
import os
import site


def construct() -> None:
    """
    • Detects whether it is running inside a virtual environment
    • Displays information about the current Python environment
    • Provides instructions for creating and activating a
    virtual environment if none is detected
    • Shows the difference between global and virtual
    environment package locations
    -> works both inside and outside virtual environments,
    providing different outputs for each scenario
    -> Creating and testing virtual environment
            $> python3 -m venv matrix_env
            $> source matrix_env/bin/activate
            (matrix_env) $> python3 construct.py
            Should detect virtual environment and show details
            Leave the matrix with the deactivate command
    """
    v_path = os.environ.get('VIRTUAL_ENV')

    if v_path:
        # Inside the Construct
        print("\nMATRIX STATUS: Welcome to the construct\n\n"
              f"Current Python: {sys.executable}\n"
              f"Virtual Environment: {os.path.basename(v_path)}\n"
              f"Environment Path: {v_path}\n\n"
              "SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.\n\n"
              "Package installation path: \n")
        if site.getsitepackages():
            print(f"{site.getsitepackages()[0]}")
        else:
            print('N/A')
    else:
        # Outside the Matrix / venv
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}.{sys.version_info.minor}")
        print("Virtual Environment: None detected\n\n"
              "WARNING: You're in the global environment!\n"
              "The machines can see everything you install.\n\n"
              "To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\\Scripts\\activate # On Windows\n\n"
              "Then run this program again.")


if __name__ == "__main__":
    construct()
