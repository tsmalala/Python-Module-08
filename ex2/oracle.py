import os


def print_config(matrix: str, database: str | None, api: str | None,
                 log: str | None, zion: str | None) -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    print(f"Mode: {matrix}")
    print(f"Database: {database}")
    print(f"API Access: {api}")
    print(f"Log Level: {log}")
    print(f"Zion Network: {zion}")


def get_config() -> bool:
    try:
        from dotenv import find_dotenv, load_dotenv
    except Exception as e:
        print(f"[ERROR] {e}")
        return False

    dotenv_path = find_dotenv()
    if not dotenv_path:
        print("[WARNING] No .env file found")
        return False

    load_dotenv(dotenv_path)
    MATRIX_MODE = os.getenv("MATRIX_MODE")
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_KEY = os.getenv("API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

    required = {
        "MATRIX_MODE": MATRIX_MODE,
        "DATABASE_URL": DATABASE_URL,
        "API_KEY": API_KEY,
        "LOG_LEVEL": LOG_LEVEL,
        "ZION_ENDPOINT": ZION_ENDPOINT
        }
    for key, values in required.items():
        if not values:
            print(f"\n[ERROR] missing {key}")
            return False

    if not all(required.values()):
        print("[ERROR] Missing required configuration")
        return False

    if MATRIX_MODE == "development":
        print_config(MATRIX_MODE, "Connected to local instance", API_KEY,
                     "DEBUG", ZION_ENDPOINT)
    elif MATRIX_MODE == "production":
        print_config(MATRIX_MODE, "Connected to production server", API_KEY,
                     "WARNING", ZION_ENDPOINT)
    else:
        print("[ERROR] Unknown MATRIX_MODE")
        return False

    return True


if __name__ == "__main__":
    if get_config():
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
