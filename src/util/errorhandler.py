# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
logger = logger('Error Handler')

# this is just a function that sends errors to my server so i can see errors and fix them quicker
def handle_exception(exc_type, exc_value, exc_traceback):
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    logger.error(text=tb)
    try:
        requests.post('https://r3ci.pythonanywhere.com/error', json={
            'title': 'chomik',
            'message': tb,
            'script': 'G4Spam',
            'level': 'jamnik'
        })

    except Exception as e:
        pass

    logger.log(text='Press enter to quit, if this keeps happening join the discord and report the error', ts=True)
    input('')
    sys.exit()

sys.excepthook = handle_exception