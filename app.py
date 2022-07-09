"""
A bot to calculate money spent in different periods by the user.
Calculation is done based on special messages containing expenditure summary
sent to a channel.

"""

from pyrogram.handlers import MessageHandler
from datetime import datetime
from warnings import filters
from pyrogram.types import Message
import os
from pyrogram import Client,filters
import logging
from classes import Report, ReportType
import debugpy
from pyrogram import idle

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



# debugpy.listen(('easytally', 5678))


apiId = os.getenv(Keys.API_ID)
apiHash = os.getenv(Keys.API_HASH)
botToken = os.getenv(Keys.BOT_TOKEN)

sessionString = os.getenv(Keys.SESSION_STRING)


if not apiId or not apiHash or not botToken:
    logger.error(f"{Keys.API_ID} or {Keys.API_HASH} or {Keys.BOT_TOKEN} environment variables not specified. Exiting...")
    exit(1)



# app = Client("session/easytally", apiId, apiHash, bot_token=botToken, session_string = sessionString,
# in_memory=False)
app = Client("ephemeral", apiId, apiHash, bot_token=botToken, session_string = sessionString,
in_memory=False)


# @app.on_message((filters.channel | filters.group) & filters.command(["start", "cost", "income"]))
async def handleBot(client: Client, message: Message):
    await message.reply(message.text)
    # Return if not a member
    me = await client.get_chat_member(message.chat.id, 'me')
    logger.debug(f"Me: {me}")
    if not me:
        return
    logger.info(f"New message: {message}")
    chatId = message.chat.id
    cmdParts = message.command
    if len(cmdParts) == 1:
        if cmdParts[0] == Commands.COST:
            await message.reply(lang.please_wait_until_your_cost_is_calculated)
            # Get the reports for the last 30 days and calculate expenditure and income
            now = datetime.now()
            sum = 0.0
            async for msg in client.get_chat_history(chat_id = chatId, offset_date = datetime(now.year, now.month - 1, now.day)):
                report = Report(msg.text)
                logger.debug(f"{lang.processing_} {report.text}")
                if report.type == ReportType.EXPENSE:
                    sum += report.value
            await message.reply(f"{lang.your_expenditure_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum} {lang.TOMANS}")
        elif cmdParts[0] == Commands.INCOME:
            await message.reply(lang.please_wait_until_your_income_is_calculated)
            now = datetime.now()
            sum = 0.0
            async for msg in client.get_chat_history(chat_id = chatId, offset_date = datetime(now.year, now.month - 1, now.day)):
                report = Report(msg.text)
                logger.debug(f"Processing {report.text}")
                if report.type == ReportType.INCOME:
                    sum += report.value
            await message.reply(f"{lang.your_income_for_the_last_} 30 {lang._days} {lang.is_equal_to_} {sum}")










logger.info(f"Starting {app.name}")
app.start()

me = app.get_me()
app.send_message('djnotes', f'Hello from {me.first_name}')

# app.add_handler(MessageHandler(handleBot, filters.private))

idle()

#TODO: Save session string to database here

app.stop()
