import telegram.bot
from telegram.ext import Updater, messagequeue as mq
from telegram.utils.request import Request
from main_controller import MainController
from config import BotConfig


def main():
    try:
        updater = Updater(token=BotConfig.token, use_context=True)
        dispatcher = updater.dispatcher
        test_controller = MainController(dispatcher=dispatcher)
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print('main error: %s' % str(e))

if __name__ == '__main__':
    main()

