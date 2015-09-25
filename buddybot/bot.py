import os
import random
import requests
from dotenv import load_dotenv
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
    'clach04',
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
]

slack = Slacker(SLACK_API_KEY)

def main():
    user = random.choice(OPTED_IN_USERS)
    message = random.choice(MESSAGES)
    print(("{} - {}").format(user, message))
    message_response = slack.chat.post_message(
        "@{}".format(user),
        message,
        username="BuddyBot",
        icon_emoji=":heart:",
    )

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