import os
import sys
# pip install python-dotenv
from dotenv import load_dotenv

def load_config() -> dict[str]:
    try:
        load_dotenv()
        matrix_mode = os.getenv('MATRIX_MODE')
        database_url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL')
        zion_endpoint = os.getenv('ZION_ENDPOINT')

        return {
            "mode": matrix_mode,
            "db": database_url,
            "api": api_key,
            "log": log_level,
            "zion": zion_endpoint
        }
    except Exception as e:
        print(f"[LOAD_CONFIG() ERROR]: {e}")

def security_check() -> None:
    pass


if __name__ == "__main__":
    load_config()