#!/bin/bash

virtualenv --python=/usr/bin/python3 .
. bin/activate
pip install -r requirements.txt
python weatherbot/bot.py
deactivate