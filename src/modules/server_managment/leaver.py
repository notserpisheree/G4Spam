'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *
from src.util.logger import logger
from src.util.client import client
from src.util.ui import ui
from src.util.threading import threading
from src.util.files import files

class leaver:
    def __init__(self):
        self.module = 'Leaver'
        self.logger = logger(module=self.module)
        self.serverid = None

    def leave(self, token, cl: client=None):
        ctoken = ui.cut(text=token, length=20, end='...')
        try:
            if not cl:
                cl = client(token=token, reffer='https://discord.com/discovery/servers')

            r = cl.sess.delete(
                f'https://discord.com/api/v9/users/@me/guilds/{self.serverid}',
                headers=cl.headers,
                json={
                    'lurking': False
                }
            )

            if r.status_code == 204:
                self.logger.succeded(text=f'{ctoken} Left')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                time.sleep(float(limit))
                self.leave(token, client)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=5)
                time.sleep(5)
                self.leave(token, client)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(text=f'{ctoken} Cloudflare rate limited', fortime=10)
                time.sleep(10)
                self.leave(token, client)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(text=f'{ctoken} Hcaptcha required')

            elif 'You need to verify' in r.text:
                self.logger.locked(text=f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(text=f'{ctoken} Failed to leave', error=error)

        except Exception as e:
            self.logger.error(text=f'{ctoken} Failed to leave', error=e)

    def menu(self):
        ui.prep(text=self.module)

        self.serverid = ui.input(text='Server ID', module=self.module)
        self.delay = ui.delayinput(module=self.module)

        threading(
            func=self.leave,
            tokens=files.gettokens(),
            delay=self.delay,
        )