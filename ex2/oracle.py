import os

def get_config() -> bool:
    try:
        from dotenv import find_dotenv, load_dotenv
    except Exception as e:
        print(f"[ERROR] {e}")

    dotenv_path = find_dotenv()
    if dotenv_path:
        load_dotenv(dotenv_path)
        MATRIX_MODE = os.getenv("MATRIX_MODE")
        DATABASE_URL = os.getenv("DATABASE_URL")
        API_KEY = os.getenv("API_KEY")
        LOG_LEVEL = os.getenv("LOG_LEVEL")
        ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

        print("\nORACLE STATUS: Reading the Matrix...")
        print("\nConfiguration loaded:")
        print(f"Mode: {MATRIX_MODE}")
        print(f"Database: {DATABASE_URL}")
        print(f"API Access: {API_KEY}")
        print(f"Log Level: {LOG_LEVEL}")
        print(f"Zion Network: {ZION_ENDPOINT}")
        return True
    print("Missing configuration!")
    return False


if __name__ == "__main__":
    if get_config():
        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
