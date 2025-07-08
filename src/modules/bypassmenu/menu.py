# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
from src.util.ui import ui

from src.modules.bypassmenu.reactionbypass import reactionbypass
from src.modules.bypassmenu.buttonbypass import buttonbypass
from src.modules.bypassmenu.onboarding import onboarding
from src.modules.bypassmenu.rules import rules

class bypassmenu:
    def __init__(self):
        self.module = 'Bypass Menu'
        self.logger = logger(self.module)
        self.ui = ui(self.module)

    def menu(self):
        self.ui.prep()
        self.ui.createmenu([
            'Reaction bypass',
            'Button bypass',
            'Onboarding',
            'Rules',
            'Back'
        ])
        chosen = self.ui.input('Option')

        if chosen == '1':
            reactionbypass().menu()

        elif chosen == '2':
            buttonbypass().menu()

        elif chosen == '3':
            onboarding().menu()
        
        elif chosen == '4':
            rules().menu()

        elif chosen == '5':
            return
        
        else:
            self.menu()