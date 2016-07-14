import os

DEFAULT_REPLY = "Say what fool???"
API_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
ERRORS_TO = 'chbatey'
PLUGINS = [
        'slackbot.plugins',
        'plugin',
        'kubernetes',
]
