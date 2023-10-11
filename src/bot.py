from pyrogram import Client
from src.logger import BotLogger
from src.user import TgUser

from src.util import MY_PROXY, Keys
from src import *


class TgBot(Client):
    def __init__(self):
        super().__init__(
            name = Keys.BOT_SESSION,
            api_id = apiId,
            api_hash = apiHash,
            bot_token=botToken,
            # session_string = sessionString,
            in_memory=True,
            plugins = dict(
                root = "bot/plugins"
            ),
             proxy = MY_PROXY
        )
        self.logger = BotLogger(__name__, logging.INFO)

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.logger.info(f'@{me.username} started')
        if os.getenv(Keys.USER_LOGIN) is not None:
            user = TgUser()
            await user.start()
            user_info = await user.get_me()
            await self.send_message(user_info.id, f" {me.first_name} started")

    
    async def stop(self):
        await super().stop()
        self.logger.info('Bot stopped')
    

bot = TgBot()
bot.run()