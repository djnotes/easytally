import os
import logging
from src.logger import BotLogger


from src.util import Cmd, Keys
from src.language import Farsi as lang
import time



apiId = os.getenv(Keys.API_ID)
apiHash = os.getenv(Keys.API_HASH)
botToken = os.getenv(Keys.BOT_TOKEN)

sessionString = os.getenv(Keys.SESSION_STRING)
startTime = time.time()

logger = BotLogger(__name__)

if not apiId or not apiHash or not botToken:
    logger.error(f"{Keys.API_ID} or {Keys.API_HASH} or {Keys.BOT_TOKEN} environment variables not specified. Exiting...")
    exit(1)