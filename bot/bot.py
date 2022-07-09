from pyrogram import Client,__version__
from bot.logger import BotLogger

from util import Keys
from bot import *

class TgBot(Client):
    async def __init__(self):
        super().__init__(
            name = Keys.USER_SESSION,
            api_id = apiId,
            api_hash = apiHash,
            bot_token=botToken,
            session_string = sessionString,
            in_memory=True
        )
        self.logger = BotLogger(__name__, logging.INFO)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.logger.info(f'@{me.username} based on Pyrogram v{__version__}')

    
    async def stop(self):
        await super().stop()
        self.logger.info('Bot stopped')
    