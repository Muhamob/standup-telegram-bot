import datetime

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет всем, кто есть в этом чате!')


def callback_alarm(context: CallbackContext, chat_id):
    context.bot.send_message(chat_id=chat_id, text='Саня, иди на хй. Не стал писать полное сообщение, а то вдруг сбер всё это читает')


def callback_timer(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Setting a timer for Every Day')

    context.job_queue.run_daily(lambda x: callback_alarm(x, update.message.chat_id), datetime.time(hour=15, minute=48), (0, 1, 2, 3, 4))


if __name__ == "__main__":
    updater = Updater("1616350146:AAFF8enpWcAXT4Czgyoo_tzs767sIWhKl2o")

    updater.dispatcher.add_handler(CommandHandler('start', start, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('timeit', callback_timer))

    updater.start_polling()
    updater.idle()
