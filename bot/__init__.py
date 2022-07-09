import os
import logging
from bot.logger import BotLogger


from bot.util import Cmd, Keys
from bot.language import Farsi as lang




apiId = os.getenv(Keys.API_ID)
apiHash = os.getenv(Keys.API_HASH)
botToken = os.getenv(Keys.BOT_TOKEN)

sessionString = os.getenv(Keys.SESSION_STRING)

logger = BotLogger(__name__)

if not apiId or not apiHash or not botToken:
    logger.error(f"{Keys.API_ID} or {Keys.API_HASH} or {Keys.BOT_TOKEN} environment variables not specified. Exiting...")
    exit(1)