from bot.util import Cmd
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(
    filters.private & filters.command(Cmd.START)
    )
async def start_bot(client: Client, message: Message):
    await message.reply("Welcome to the bot")