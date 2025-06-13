'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *
from src.util.logger import logger
from src.util.ui import ui

from src.modules.server_managment.joiner import joiner
from src.modules.server_managment.leaver import leaver

class servermanagment:
    def __init__(self):
        self.logger = logger(module='Server Managment')

    def menu(self):
        ui.prep(text='Server Managment')

        ui.createmenu([
            'Joiner',
            'Leaver',
            'Back'
        ])

        chosen = ui.input(text='Option')

        if chosen == '1':
            joiner().menu()

        elif chosen == '2':
            leaver().menu()

        elif chosen == '3':
            return
        
        else:
            self.menu()