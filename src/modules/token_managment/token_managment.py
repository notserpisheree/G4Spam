'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *
from src.util.logger import logger
from src.util.ui import ui

from src.modules.token_managment.checker import checker

class tokenmanagment:
    def __init__(self):
        self.module = 'Token Managment'
        self.logger = logger(module=self.module)

    def menu(self):
        ui.prep(text=self.module)

        ui.createmenu([
            'Checker',
            'Back'
        ])

        chosen = ui.input(text='Option')

        if chosen == '1':
            checker().menu()

        elif chosen == '3':
            return
        
        else:
            self.menu()