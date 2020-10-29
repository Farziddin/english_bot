from commands.start import start_receiver
from telegram.ext import (CommandHandler, MessageHandler, Filters, ConversationHandler)
from commands.inline_query import inline_snippets
from commands.subjects import chemistry_subject, math_subject, literature_subject, biology_subject
from commands.menu import main_menu


class MainController:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.__process_handlers()

    def start(self, update, context):
        try:
            res = start_receiver(update, context)
            if res == 0:
                main_menu(update, context)
        except Exception as e:
            print('Start: ', e)

    def get_contact(self, update, context):
        try:
            contact = update.message.contact.phone_number
            main_menu(update, context)
            print('Number:', contact)
        except Exception as e:
            print('Start: ', e)

    def text_filterer(self, update, context):
        if not update.message:
            return 0
        try:
            message = update.message.text
            if message == "Kimyo":
                chemistry_subject(update, context)
            elif message == "Matematika":
                math_subject(update, context)
            elif message == "Ona tili":
                literature_subject(update, context)
            elif message == "Biologiya":
                biology_subject(update, context)
            else:
                main_menu(update, context)
        except Exception as e:
            print('Start: ', e)

    def __process_handlers(self):

        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text, self.text_filterer))
        self.dispatcher.add_handler(MessageHandler(Filters.contact, self.get_contact))
        self.dispatcher.add_handler(inline_snippets)

