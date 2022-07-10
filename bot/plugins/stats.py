from bot.util import Cmd
from pyrogram import Client, filters
from pyrogram.types import Message
from bot import startTime
import time

@Client.on_message(
    filters.private & filters.command(Cmd.STATS)
    )
async def start_bot(client: Client, message: Message):
    await message.reply(f"Up time: {int(time.time() - startTime)} seconds")