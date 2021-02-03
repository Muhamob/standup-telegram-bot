from telegram import Update
from telegram.ext import CallbackContext

from src.ops import ROOT_DIR


def sheldons_spot_cmd(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Did you say стендап?????")

    with open(ROOT_DIR / "static/sheldons_spot.jpg", "rb") as f:
        context.bot.send_photo(update.message.chat_id, f)
