# imports
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from handler_functions.start import start
from handler_functions.bio import bio
from handler_functions.gender import gender
from handler_functions.photo import photo, skip_photo
from handler_functions.location import location, skip_location
from handler_functions.cancel import cancel
from conversation_handlers.stage_constants import *

# Adds conversation handler with the states GENDER, PHOTO, LOCATION and BIO for stage 1 of the sign up
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        GENDER: [MessageHandler(Filters.regex('^(Gentleman|Lady|I am a unicorn.)$'), gender)],
        PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
        LOCATION: [
            MessageHandler(Filters.location, location),
            CommandHandler('skip', skip_location),
        ],
        BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)