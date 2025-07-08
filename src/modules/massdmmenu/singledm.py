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
from src.util.other import other

class singledm:
    def __init__(self):
        self.module = 'Single DM'
        self.logger = logger(self.module)
        self.ui = ui(self.module)
        
        self.userid = None
        self.messages = []
        self.delay = 0

    def dm(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            # Create DM channel
            r = cl.sess.post(
                'https://discord.com/api/v9/users/@me/channels',
                headers=cl.headers,
                json={
                    'recipients': [self.userid]
                }
            )

            if r.status_code != 200:
                self.logger.error(f'{ctoken} Failed to create DM channel')
                return

            channel_id = r.json()['id']
            
            while True:
                other.delay(self.delay)
                message = random.choice(self.messages)

                r = cl.sess.post(
                    f'https://discord.com/api/v9/channels/{channel_id}/messages',
                    headers=cl.headers,
                    json={
                        'content': message,
                        'nonce': discordutils.getsnowflake(),
                        'flags': 0
                    }
                )

                if r.status_code == 200:
                    self.logger.succeded(f'{ctoken} Sent DM')
                    continue

                elif 'retry_after' in r.text:
                    limit = r.json().get('retry_after', 1.5)
                    self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                    time.sleep(float(limit))
                    continue

                elif 'Try again later' in r.text:
                    self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                    time.sleep(5)
                    continue

                elif 'Cloudflare' in r.text:
                    self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                    time.sleep(10)
                    continue
                
                elif 'captcha_key' in r.text:
                    self.logger.hcaptcha(f'{ctoken} Hcaptcha required')
                    break

                elif 'You need to verify' in r.text:
                    self.logger.locked(f'{ctoken} Locked/Flagged')
                    break

                else:
                    error = self.logger.errordatabase(r.text)
                    self.logger.error(f'{ctoken}', error)
                    break

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def menu(self):
        self.ui.prep()
        self.userid = self.ui.input('User ID to DM')
        
        if self.ui.input('Use messages from a file', True):
            path = files.choosefile()
            if not os.path.exists(path):
                self.logger.log('File does not exist')
                self.messages = [self.ui.input('Message')]
            else:
                with open(path, 'r') as f:
                    self.messages = f.read().splitlines()
        else:
            self.messages = [self.ui.input('Message')]

        self.delay = self.ui.delayinput()

        threading(
            func=self.dm,
            tokens=files.gettokens(),
            delay=self.delay,
        )