# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    CallbackContext,
)
import logEnabler;

PHOTO = range(1)

# Stores the selected gender and asks for a photo.
def gender(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logEnabler.logger.info("Gender of %s: %s", user.first_name, update.message.text)
    update.message.reply_text(
        'Alright! Now, in order to get to know you better, please send me a photograph of yourself. '
        '(If you don\'t want to or would like to postpone this step, '
        'just send /skip and we will continue to the next step.) ',
        reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO