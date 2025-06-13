# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'; os.system('cls')
from src import *

from src.util.client import *
from src.util.ui import ui
from src.util.rpc import RPC
from src.util.logger import logger
from src.util.other import other
from src.util.files import files; files.runtasks()
from src.util.config import config; config()

from src.modules.server_managment.server_managment import servermanagment
from src.modules.token_managment.token_managment import tokenmanagment
from src.modules.sources import sources

logger = logger('Main')
sui = ui('Main')
RPC.update('Launching...')
logger.log('Adding a launch to stats', True)
other.addlaunch()
logger.log('Getting repo stars...', True)
stars = other.getrepostars()
logger.log('Getting launches...', True)
launches = other.getlaunches()

logger.log('Finished starting G4Spam', True)

while True:
    RPC.update('In main menu')
    sui.title(f'G4Spam ({launches}) - github.com/R3CI/G4Spam ({stars}) - discord.gg/spamming - Made by r3ci')
    sui.cls()
    sui.banner()
    sui.bar()
    sui.menu()

    logger.log('Welcome to G4Spam made by r3ci <3 github.com/R3CI/G4Spam')
    logger.log(f'Current version is {version}')
    chosen = sui.input('Option')

    options = {
        '1': servermanagment().menu,
        '2': tokenmanagment().menu,
        '19': sources.menu,
        '20': lambda: exit(),
    }
    try:
        options[chosen]()
    except KeyError:
        logger.log('Invalid option')
    
    logger.log('Finished, enter to continue')
    input('')