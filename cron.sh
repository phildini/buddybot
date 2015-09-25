#!/bin/bash

virtualenv .
. /bin/activate
pip install -r requirements.txt
python buddybot/bot.py
deactivate