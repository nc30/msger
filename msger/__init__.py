from __future__ import print_function
try:
    from .main import send_message
except ValueError:
    from main import send_message
