from dotenv import load_dotenv
from environs import Env

load_dotenv()
env = Env()


class Settings:
    TOR_ADDRESS = env.str("TOR_ADDRESS", "socks5://localhost:9051")
    SERVER_ADDRESS = env.str("SERVER_ADDRESS")
    CHECKER_ADDRESS = env.str("CHECKER_ADDRESS")
    TOTAL_EMAILS = env.int("TOTAL_EMAILS", 500)
    RAISE_TIMEOUT = env.int("RAISE_TIMEOUT", 60)
    TIMEOUT = env.int("TIMEOUT", 1800)
