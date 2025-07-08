# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
from src.util.ui import ui

from src.modules.spammingmenu.channelspammer import channelspammer
from src.modules.spammingmenu.multichannelspammer import multichannelspammer
from src.modules.spammingmenu.replyspammer import replyspammer

class spammingmenu:
    def __init__(self):
        self.module = 'Spamming Menu'
        self.logger = logger(self.module)
        self.ui = ui(self.module)

    def menu(self):
        self.ui.prep()
        self.ui.createmenu([
            'Channel spammer',
            'Multi-channel spammer',
            'Reply spammer',
            'Back'
        ])
        chosen = self.ui.input('Option')

        if chosen == '1':
            channelspammer().menu()

        elif chosen == '2':
            multichannelspammer().menu()

        elif chosen == '3':
            replyspammer().menu()

        elif chosen == '4':
            return
        
        else:
            self.menu()