from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from services import get_question


def inline_query(update, context):
    try:
        query = update.callback_query
        user_id = query.from_user.id
        data_sp = query.data.split("_")

        if data_sp[0] == "answer":
            print(data_sp)
            context.bot.delete_message(chat_id=query.from_user.id, message_id=query.message.message_id)
            if data_sp[2] == data_sp[3]:
                context.bot.send_message(chat_id=query.from_user.id, text="Javob to'g'ri")
            else:
                context.bot.send_message(chat_id=query.from_user.id, text="Javob noto'g'ri")

            if data_sp[3] == "1":
                q = get_question(int(data_sp[1])+1)
                question = q["question"]
                buttons = []
                for option in question["options"]:
                    buttons.append(
                        [
                            InlineKeyboardButton(text="{}".format(option["name"]),
                                                 callback_data="answer_{}_{}_{}_{}".format(int(data_sp[1]) + 1, question["answer"], option["answer"], int(
                                                     q["has_next"])))
                        ]
                    )

                context.bot.send_message(
                    chat_id=query.from_user.id,
                    text="{}".format(question["question"]),
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
    except Exception as e:
        context.bot.delete_message(update.callback_query.from_user.id, update.callback_query.message.message_id)
        print('inline query error: %s' % str(e))


inline_snippets = CallbackQueryHandler(inline_query)
