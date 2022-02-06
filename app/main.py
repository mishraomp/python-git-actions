import logging
import os
from pythonjsonlogger import jsonlogger

LOGGER = logging.getLogger()
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
API_SECRET_KEY = os.getenv('API_KEY', 'SUPER_SECRET_KEY')
LOGGER.setLevel(LOG_LEVEL)
handler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
handler.setFormatter(formatter)
LOGGER.addHandler(handler)
LOGGER = logging.getLogger(__name__)

LOGGER.info(f"This is Log Level '{LOG_LEVEL}'")
LOGGER.info(f"This is API KEY '{API_SECRET_KEY}'")
