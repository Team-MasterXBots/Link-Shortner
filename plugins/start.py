# Author: Fayas 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
Hello {} ✌️
I am a link shortner telegram bot.

» I can short any type of link «

Made by @Master_X_Updates
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Updates Channel📡', url='https://telegram.me/Master_X_Updates'),
        InlineKeyboardButton('Report Bugs🐞', url="https://t.me/Best_Friends15")
        ]]
    )

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
