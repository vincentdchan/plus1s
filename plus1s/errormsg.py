import random
from xtermcolor import colorize
from os.path import dirname, join

ERROR_MSGS_PATH = join(dirname(__file__), 'resources/error_msgs.txt')


def show_error_message():
    with open(ERROR_MSGS_PATH) as f:
        lines = f.readlines()
        print(colorize(random.choice(lines), rgb=0xff0000))

