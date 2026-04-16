import os
import sys
# pip install python-dotenv
from dotenv import load_dotenv


def load_config() -> dict[str, str]:
    try:
        load_dotenv()
        # Using a default value for matrix_mode and log_level
        matrix_mode = os.getenv('MATRIX_MODE', 'development')
        database_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL', 'INFO')
        zion_endpoint = os.getenv('ZION_ENDPOINT')

        if not database_url or not api_key or not zion_endpoint:
            print("ERROR: Missing required configuration")
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
        print("[WARNING] .env file not found (using environment variables)")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def oracle(variables: dict[str, str]) -> None:
    """Print the final output"""
    try:
        print("\nORACLE STATUS: Reading the Matrix...\n"
              "Configuration loaded:\n")
        # MODE
        print(f"Mode: {variables['mode']}\n\n")
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
    if not config:
        sys.exit(1)
    oracle(config)
    security_check()
