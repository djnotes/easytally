from pyrogram import (
    Client,
    filters
)

from bot.logger import BotLogger

@Client.on_message(filters = filters.channel)
def signal_channel(client, message):
    logger = BotLogger(__name__)
    logger.info(f'Inside channel: {message.text}')