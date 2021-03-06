import logging
import os

from telegram.ext import Updater

import commands.start
import commands.synthesize_inline
import commands.error_handler
from bot_env import bot_env

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG if os.getenv('DEBUG') == "1" else logging.INFO
)

updater = Updater(token=bot_env.config.bot_token)
dispatcher = updater.dispatcher

commands.error_handler.register(dispatcher)
commands.start.register(dispatcher)
commands.synthesize_inline.register(dispatcher)

updater.start_polling()
updater.idle()
