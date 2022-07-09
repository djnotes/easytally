import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.logger import BotLogger
from bot.report import Report, ReportType
from bot.user import TgUser
from bot.util import Cmd
from bot.language import Farsi as lang
from bot import *


@Client.on_message(filters = filters.private & filters.command(Cmd.INCOME))
async def calculate_cost(client: Client, message: Message):
    userClient = TgUser()
    logger = BotLogger(__name__, logging.DEBUG)
    await message.reply("Calculating income: Coming soon")
    await message.reply(lang.please_wait_until_your_income_is_calculated)
    now = datetime.now()
    sum = 0.0
    async for msg in userClient.get_chat_history(chat_id = message.chat.id, offset_date = datetime(now.year, now.month - 1, now.day)):
        report = Report(msg.text)
        logger.debug(f"Processing {report.text}")
        if report.type == ReportType.INCOME:
            sum += report.value
    await message.reply(f"{lang.your_income_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum}")    