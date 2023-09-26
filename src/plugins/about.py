from src.util import Cmd
from pyrogram import Client, filters
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message

@Client.on_message(
    filters.private & filters.command(Cmd.ABOUT)
    )
async def start_bot(client: Client, message: Message):
    await message.reply((
        "Easy Tally v0.1.0\n\n"
        "[Author](https://github.com/djnotes)\n\n"
    ),
    parse_mode=ParseMode.MARKDOWN)