from telegram import ReplyKeyboardMarkup, KeyboardButton


def start_receiver(update, context):
    try:
        user_id = update.message.from_user.id
        if user_id:
            buttons = [[KeyboardButton(text="Telefon raqamni yuborish", request_contact=True)]]
            update.effective_message.reply_text("This is a bot.", quote=False,
                                                reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True,
                                                                                 resize_keyboard=True))
            return 1
        else:
            return 0
    except Exception as e:
        print('start error: %s' % str(e))