import datetime

from telegram import Update
from telegram.ext import CallbackContext

from src.constants import timezone, days_of_week_dict


def start_cmd(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='Привет всем, кто есть в этом чате!')


def _notify_colleagues(context: CallbackContext,
                       chat_id: int,
                       text: str = 'Саня, иди на хй. Не буду править это сообщение'):
    context.bot.send_message(chat_id=chat_id, text=text)


def timeit_cmd(update: Update, context: CallbackContext) -> None:
    """
    Метод, который задаёт время стендапа

    TODO:
    1. Менять время стендапа

    :param update: Update
    :param context: Context
    :return: None
    """
    # dates and times
    meeting_time = datetime.time(17, 0, 0, tzinfo=timezone)
    days_of_week = (0, 1, 2, 3, 4)

    # message info
    chat_id = update.message.chat_id

    # messages
    agreement_message = "Setting up a timer for " + ", ".join(
        [days_of_week_dict[i] for i in days_of_week]
    ) + " days at " + meeting_time.strftime("%H:%M")
    notify_message = "Стендаааааааааап!1!1!!!!!!!1"

    context.bot.send_message(chat_id=chat_id, text=agreement_message)
    context.job_queue.run_daily(lambda x: _notify_colleagues(x, chat_id, notify_message),
                                meeting_time,
                                days_of_week)
