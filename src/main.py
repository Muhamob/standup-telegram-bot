from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from src.callbacks import sheldons_spot_cmd
from src.commands import start_cmd, timeit_cmd
from src.filters import StandUpFilter
from src.ops import load_secrets

if __name__ == "__main__":
    import logging

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG)

    secret = load_secrets()
    updater = Updater(secret['token'])

    updater.dispatcher.add_handler(
        CommandHandler('start', start_cmd, pass_args=True)
    )
    updater.dispatcher.add_handler(
        CommandHandler('timeit', timeit_cmd)
    )
    updater.dispatcher.add_handler(
        MessageHandler(
            Filters.text & ~Filters.command & StandUpFilter(),
            sheldons_spot_cmd
        )
    )

    updater.start_polling()
    updater.idle()
