# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
from src.util.ui import ui
from src.modules.annoyingmenu.auditlogspammer import auditlogspammer

class annoyingmenu:
    def __init__(self):
        self.module = 'Annoying Menu'
        self.logger = logger(self.module)
        self.ui = ui(self.module)

    def menu(self):
        self.ui.prep()
        self.ui.createmenu([
            'Audit log spammer',
            'Back'
        ])
        chosen = self.ui.input('Option')

        if chosen == '1':
            auditlogspammer().menu()

        elif chosen == '2':
            return
        
        else:
            self.menu()