import os
import json

Settings = None


def load_settings():
    global Settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Settings.json')) as f:
        Settings = json.load(f)


load_settings()
