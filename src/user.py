from pyrogram import Client,__version__
from src.logger import BotLogger

from src.util import MY_PROXY, Keys
from src import *

class TgUser(Client):
    def __init__(self):
        super().__init__(
            name = Keys.USER_SESSION,
            api_id = apiId,
            api_hash = apiHash,
            session_string = sessionString,
            in_memory = True,
            proxy = MY_PROXY
        )
        self.logger = BotLogger(__name__, logging.INFO)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.logger.info(f'@{me.username} started')

    
    async def stop(self):
        await super().stop()
        self.logger.info('Bot stopped')
    