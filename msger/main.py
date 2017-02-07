
from __future__ import print_function
import requests
import os
import json

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

INI_FILEPATH = '~/'
INI_FILENAME    = '.msger.ini'
INI_SECTIONNAME = 'main'

INI_PATH        = os.path.join(os.path.expanduser(INI_FILEPATH), INI_FILENAME)

parser = configparser.ConfigParser()
parser.read(INI_PATH)

API_URI = parser.get(INI_SECTIONNAME, 'API_URI')
ICON_URL = parser.get(INI_SECTIONNAME, 'ICON_URL')
DISPLAY_NAME = parser.get(INI_SECTIONNAME, 'DISPLAY_NAME')
CHANNEL = parser.get(INI_SECTIONNAME, 'CHANNEL')


def send_message(message):
    paramators = {
        'text' : message,
        'username' : DISPLAY_NAME,
        'icon_url' : ICON_URL,
        'channel' : CHANNEL
    }

    r = requests.post(API_URI, data=json.dumps(paramators))
    return r

