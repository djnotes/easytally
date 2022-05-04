"""
A bot to calculate money spent in different periods by the user.
Calculation is done based on special messages containing expenditure summary
sent to a channel.

"""

from datetime import datetime
from warnings import filters
from pyrogram.types import Message
import os
from pyrogram import Client,filters
import logging
from classes import Report, ReportType
import debugpy

from util import Commands, Keys
from language import Farsi as lang

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("application.log")
formatter = logging.Formatter("%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)



api_id = os.getenv(Keys.API_ID)
api_hash = os.getenv(Keys.API_HASH)

if not api_id or not api_hash:
    logger.error(f"{Keys.API_ID} or {Keys.API_HASH} environment variables not specified. Exiting...")
    exit(1)


app = Client("accounting_bot", api_id, api_hash)



@app.on_message(filters.channel | filters.group)
async def handleBot(client: Client, message: Message):
    # Return if not a member
    me = await client.get_chat_member(message.chat.id, 'me')
    logger.debug(f"Me: {me}")
    if not me:
        return
    logger.info(f"New message: {message}")
    chatId = message.chat.id
    if message.command:
        cmdParts = message.command
        if len(cmdParts) == 1:
            if cmdParts[0] == Commands.COST:
                await message.reply(lang.please_wait_until_your_cost_is_calculated)
                # Get the reports for the last 30 days and calculate expenditure and income
                now = datetime.now()
                msgs = await client.get_chat_history(chat_id = chatId, offset_date = datetime(month=now.month - 1))
                sum = 0.0
                for msg in msgs:
                    report = Report(msg.text)
                    logger.debug(f"Processing {report.text}")
                    if report.type == ReportType.EXPENSE:
                        sum += report.value
                await message.reply(f"{lang.your_expenditure_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum} {lang.TOMANS}")
            elif cmdParts[0] == Commands.INCOME:
                await message.reply(lang.please_wait_until_your_income_is_calculated)
                now = datetime.now()
                msgs = await client.get_chat_history(chat_id = chatId, offset_date = datetime(month=now.month - 1))
                sum = 0.0
                for msg in msgs:
                    report = Report(msg.text)
                    logger.debug(f"Processing {report.text}")
                    if report.type == ReportType.INCOME:
                        sum += report.value
                await message.reply(f"{lang.your_income_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum}")

            


debugpy.listen(('localhost', 5678))
logger.info(f"Starting {app.name}")
app.run()

