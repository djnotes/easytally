import datetime
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.logger import BotLogger
from bot.report import *
from bot.language import Farsi as lang
from bot import *
from bot.util import Cmd
from bot.user import TgUser


@Client.on_message(filters = filters.private & filters.command(Cmd.COST))
async def calculate_cost(client: Client, message: Message):
    logger = BotLogger(__name__, logging.DEBUG)
    await message.reply("Calculating cost: Coming soon")
    await message.reply(lang.please_wait_until_your_cost_is_calculated)
    # Get the reports for the last 30 days and calculate expenditure and income
    now = datetime.now()
    sum = 0.0
    userClient = TgUser()
    async for msg in userClient.get_chat_history(chat_id = message.chat.id, offset_date = datetime(now.year, now.month - 1, now.day)):
        report = Report(msg.text)
        logger.debug(f"{lang.processing_} {report.text}")
        if report.type == ReportType.EXPENSE:
            sum += report.value
    await message.reply(f"{lang.your_expenditure_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum} {lang.TOMANS}")
