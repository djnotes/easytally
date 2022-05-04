"""
A bot to calculate money spent in different periods by the user.
Calculation is done based on special messages containing expenditure summary
sent to a channel.

"""

from datetime import datetime
from pyrogram.types import Message
import os
from pyrogram import Client
import logging
from classes import Report, ReportType

from util import Commands, Keys
from language import Farsi as fa

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler("application.log"))
logger.addHandler(logging.StreamHandler())


api_id = os.getenv(Keys.API_ID)
api_hash = os.getenv(Keys.API_HASH)

if not api_id or not api_hash:
    logger.error(f"{Keys.API_ID} or {Keys.API_HASH} environment variables not specified. Exiting...")
    exit(1)


app = Client("accounting_bot", api_id, api_hash)

@app.on_message()
async def handleBot(client: Client, message: Message):
    chatId = message.chat.id
    if message.command:
        cmdParts = message.command
        if len(cmdParts) == 1:
            if cmdParts[0] == Commands.COST:
                # Get the reports for the last 30 days and calculate expenditure and income
                now = datetime.now()
                msgs = await client.get_chat_history(offset_date = datetime(month=now.month - 1))
                sum = 0.0
                for msg in msgs:
                    report = Report(msg.text)
                    if report.type == ReportType.EXPENSE:
                        sum += report.value
                await message.reply(f"{fa.your_expenditure_for_the_last_} 30 {fa._days} {fa.is_equal_to_} {sum} {fa.TOMANS}")
            elif cmdParts[0] == Commands.INCOME:
                now = datetime.now()
                msgs = await client.get_chat_history(offset_date = datetime(month=now.month - 1))
                sum = 0.0
                for msg in msgs:
                    report = Report(msg.text)
                    if report.type == ReportType.INCOME:
                        sum += report.value
                await message.reply(f"{fa.your_income_for_the_last_} 30 {fa._days} {fa.is_equal_to_} {sum}")

            

app.run()

