from os import environ as env
from dotenv import load_dotenv

load_dotenv()


class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 21204722))
    API_HASH = env.get("TELEGRAM_API_HASH", "4f5b4bbc15e7f9df9961ac92e8fd219b")
    OWNER_ID = int(env.get("OWNER_ID", 5310455183))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "film_studiox2_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6043054287:AAGXPR4Ktv1SX3ViDSQmX10QmAzvjTo_L00")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001944482996))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))


class Server:
    BASE_URL = env.get("BASE_URL", "http://127.0.0.1:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))


class DB:
    DB_URL = env.get("DB_URL", "postgres://avnadmin:AVNS_hoyHB3aI_Uqco7x__2q@oshada-fx-4273.h.aivencloud.com:27745/defaultdb?sslmode=require")


class Util:
    PING_INTERVAL = int(env.get("PING_INTERVAL ", 1200))  # 20 minutes
    SUB_CHANNEL = int(env.get("SUB_CHANNEL", 0))
    SUB_CHANNEL_LINK = env.get("SUB_CHANNEL_LINK", "t.me/elupdates")


# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s",
            "datefmt": "%d/%m/%Y %H:%M:%S",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "event-log.txt",
            "formatter": "default",
        },
        "stream_handler": {"class": "logging.StreamHandler", "formatter": "default"},
    },
    "loggers": {
        "uvicorn": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
        "uvicorn.error": {
            "level": "WARNING",
            "handlers": ["file_handler", "stream_handler"],
        },
        "bot": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
        "ping": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
    },
}
