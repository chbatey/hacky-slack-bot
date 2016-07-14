import os
import time
from slackbot.bot import Bot
import logging

logging.basicConfig(level=logging.INFO)

BOT_NAME = 'corebot'

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()

