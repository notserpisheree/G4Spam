import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *

from src.util import ui
from src.util import logger

logger = logger(name='Main')

ui.banner()
ui.bar()
ui.menu()
logger.log(text='Welcome to G4Spam made by r3ci <3 github.com/R3CI/G4Spam', ts=False)
ui.input(text='Option')