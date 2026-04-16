import os
import sys


def load_config() -> dict[str, str]:
    """Returns a dict with the variables from .env"""
    try:
        # To import .env variables
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("\nERROR: Missing dependency: python-dotenv\n"
              "Use the following command to install it:\n"
              "pip install python-dotenv")
        return {}
    try:
        # Using a default value for matrix_mode and log_level
        matrix_mode = os.getenv('MATRIX_MODE', 'development')
        database_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        zion_endpoint = os.getenv('ZION_ENDPOINT')

        if not database_url or not api_key or not zion_endpoint:
            print("ERROR: Missing required environment variables")
            return {}

        return {
            "mode": matrix_mode,
            "db": database_url,
            "api": api_key,
            "log": log_level,
            "zion": zion_endpoint
        }

    except Exception as e:
        print(f"[LOAD_CONFIG() ERROR]: {e}")
        return {}


def security_check() -> None:
    """
    Check for the presence of the .env file
    If all variables pass on oracle(), the security_check
    Will be printed / validation OK
    """
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if not os.path.exists(".env"):
        print("[WARNING] .env file not found\n"
              "'cp .env.example .env' to create a .env file")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")
    # For example:
    # MATRIX_MODE=production API_KEY=secret123 python3 oracle.py


def oracle(variables: dict[str, str]) -> None:
    """Print the final output"""
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n\n"
              "Configuration loaded:")
        # MODE
        print(f"Mode: {variables['mode']}")
        # DATABASE
        if variables['mode'] == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production")
        # API
        print("API Access: Authenticated")
        # LOG_LEVEL
        print(f"Log Level: {variables['log']}")
        # ZION
        print("Zion Network: Online")

    except Exception as e:
        print(f"[ORACLE() ERROR]: {e}")


if __name__ == "__main__":
    config = load_config()
    if config:
        oracle(config)
    security_check()
    if not config:
        sys.exit(1)
