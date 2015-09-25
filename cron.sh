#!/bin/bash

virtualenv --python=/usr/bin/python3 .
. bin/activate
pip install -r requirements.txt
python buddybot/bot.py
deactivate