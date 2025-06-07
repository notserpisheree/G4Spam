import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *

from src.util import ui
from src.util import logger

logger = logger('Main')

logger.error('Jaki pechhhh')
logger.log('Jaki pechhhh')

ui.banner()
ui.menu()
ui.input('Option')