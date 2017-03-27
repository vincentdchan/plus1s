from .start import start
from .errormsg import show_error_message
from time import gmtime, strftime


def plus1s():
    print('You have devoted 1 second for him successfully!')
    print()
    print('Time: ' + strftime('%Y-%m-%d %H:%M:%S', gmtime()))
    print()
    print('Please value time.')
