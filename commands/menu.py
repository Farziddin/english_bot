from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_menu(update, context):
    buttons = [
        [
            KeyboardButton(text="Kimyo"),
            KeyboardButton(text="Matematika")
        ],
        [
            KeyboardButton(text="Ona tili"),
            KeyboardButton(text="Biologiya")

        ]
    ]

    update.message.reply_text(
        text="Fanlardan birni tanlang:",
        reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    )