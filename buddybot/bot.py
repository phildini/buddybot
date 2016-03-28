import os
import random
import requests
from dotenv import load_dotenv, set_key
from slacker import Slacker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise EnvironmentError(error_msg)

SLACK_API_KEY = get_env_variable('SLACK_API_KEY')

OPTED_IN_USERS = [
    'phildini',
    'nicholle',
    'arctansusan',
    'erich',
]

MESSAGES = [
    "You look nice today.",
    "There are people in your life who think you're amazing.",
    "Whatever you decide for your body is right. No one else knows better.",
    "You do not owe it to anyone to look a particular way.",
    "Please try not to take yourself for granted. You're important.",
    "Hey, when's the last time you had water? Maybe you should have some now!",
    "Somebody misses you right now.",
    "Don't forget to breathe.",
    "Sometimes when things are falling apart, they may be falling into place.",
    "You are somebody's reason to smile.",
    "You are amazing!",
    "Just keep swimming!",
    "What's going well with your day?",
    "It's ok to take pleasure in your own solitude.",
    "Trust yourself.",
    "You matter and what you have to offer this world also matters.",
    "It's ok to forgive yourself for mistakes.",
]

slack = Slacker(SLACK_API_KEY)

def main():
    user = get_valid_user()
    message = random.choice(MESSAGES)
    print(("{} - {}").format(user, message))
    send_buddybot_message(message=message, user=user)


def send_buddybot_message(message, user=None, channel=None):
    if user:
        message_response = slack.chat.post_message(
            "@{}".format(user),
            message,
            username="BuddyBot",
            icon_emoji=":heart:",
        )
    if channel:
        message_response = slack.chat.post_message(
            "#{}".format(channel),
            message,
            username="BuddyBot",
            icon_emoji=":heart:",
        )


def get_valid_user():
    user = random.choice(OPTED_IN_USERS)
    if user == get_env_variable('LAST_USER'):
        user = get_valid_user()
    set_key(os.path.join(BASE_DIR, '.env'), 'LAST_USER', user)
    return user

def get_users_from_slack():
    response = slack.users.list()
    users = response.body.get('members')
    usernames = [
        user.get('name') for user in users if (
            not user['deleted'] and not user['is_bot']
        )
    ]
    return random.choice(usernames)


if __name__ == '__main__':
    main()
