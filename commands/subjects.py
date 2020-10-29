from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from services import get_question


def chemistry_subject(update, context):
    q = get_question(0)
    question = q["question"]
    buttons = []
    for option in question["options"]:
        buttons.append(
            [
                InlineKeyboardButton(text="{}".format(option["name"]), callback_data="answer_{}_{}_{}_{}".
                                     format(0, question["answer"], option["answer"], int(q["has_next"])))
            ]
        )

    update.message.reply_text(text="{}".format(question["question"]), reply_markup=InlineKeyboardMarkup(buttons))


def math_subject(update, context):
    update.message.reply_text(text="Math")


def literature_subject(update, context):
    update.message.reply_text(text="Literature")


def biology_subject(update, context):
    update.message.reply_text(text="Biology")
