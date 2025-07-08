# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.logger import logger
from src.util.client import client
from src.util.ui import ui
from src.util.threading import threading
from src.util.files import files
from src.util.discordutils import discordutils

class reactionspeller:
    def __init__(self):
        self.module = 'Reaction Speller'
        self.logger = logger(self.module)
        self.ui = ui(self.module)
        
        self.channelid = None
        self.messageid = None
        self.word = None
        self.delay = 0

    def spell(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            for letter in self.word.lower():
                if letter.isalpha():
                    emoji = f'🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿'[ord(letter) - ord('a')]
                    
                    r = cl.sess.put(
                        f'https://discord.com/api/v9/channels/{self.channelid}/messages/{self.messageid}/reactions/{emoji}/@me',
                        headers=cl.headers,
                        params={'location': 'Message Hover Bar'}
                    )

                    if r.status_code == 204:
                        self.logger.succeded(f'{ctoken} Added {emoji} ({letter})')
                    else:
                        self.logger.error(f'{ctoken} Failed to add {emoji}')
                    
                    time.sleep(0.5)  # Small delay between reactions

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def menu(self):
        self.ui.prep()
        message_link = self.ui.input('Message Link to spell on')
        ids = discordutils.extractids(message_link)
        self.channelid = ids['channel']
        self.messageid = ids['message']
        
        self.word = self.ui.input('Word to spell')
        self.delay = self.ui.delayinput()

        # Use only one token for this to avoid conflicts
        tokens = files.gettokens()
        if tokens:
            self.spell(tokens[0])
        else:
            self.logger.error('No tokens available')