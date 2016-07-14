from slackbot.bot import respond_to
from slackbot.bot import listen_to

import re
import subprocess
import logging

friends = ['batey', 'U04L7FQ1E', 'U0C6FD6SJ', 'mals']

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('Hello there')
    message.react('+1')

@listen_to('Can someone help me?')
def help(message):
    message.reply('There is no help for you!')

@respond_to('say hello to (.*)')
def say_hello(message, name):
    logging.info("the name is %s", name)
    # This is my userid which comes through if sonmeone
    # @s me
    friendly = False
    for friend in friends:
        if friend in name:
            friendly = True;

    if friendly: 
        msg = "Hello my hero %s!!!" % name
    else:
        msg = "but I don't like %s" % name

    message.reply(msg)


