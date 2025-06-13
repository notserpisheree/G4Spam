'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; os.system('cls')
from src import *

from src.util.client import *
from src.util.ui import ui
from src.util.logger import logger
from src.util.other import other

from src.modules.server_managment.server_managment import servermanagment

logger = logger(module='Main')
logger.log(text='Getting repo stars...', ts=True)
stars = other.getrepostars()

logger.log(text='Finished starting G4Spam', ts=True)
time.sleep(1)
while True:
    ui.title(f'G4Spam - github.com/R3CI/G4Spam ({stars}) - discord.gg/spamming - Made by r3ci')
    ui.cls()
    ui.banner()
    ui.bar()
    ui.menu()

    logger.log(text='Welcome to G4Spam made by r3ci <3 github.com/R3CI/G4Spam', ts=False)
    chosen = ui.input(text='Option')

    options = {
        '1': servermanagment().menu,
        '20': lambda: exit(),
    }
    try:
        options[chosen]()
    except KeyError:
        logger.error(text='Invalid option', ts=False)
    
    logger.log(text='Finished, enter to continue')
    input('')