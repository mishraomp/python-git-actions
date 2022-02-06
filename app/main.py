import logging
import os

LOGGER = logging.getLogger()
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
API_KEY = os.getenv('API_KEY', 'SUPER_SECRET_KEY')
LOGGER.setLevel(LOG_LEVEL)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s"
)
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER = logging.getLogger(__name__)

LOGGER.info(f"This is Log Level '{LOG_LEVEL}'")
LOGGER.info(f"This is API KEY '{API_KEY}'")
