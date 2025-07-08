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

class messagereport:
    def __init__(self):
        self.module = 'Message Report'
        self.logger = logger(self.module)
        self.ui = ui(self.module)
        
        self.channelid = None
        self.messageid = None
        self.reason = None
        self.delay = 0

    def report(self, token, cl: client=None):
        ctoken = self.ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token)

            r = cl.sess.post(
                'https://discord.com/api/v9/report',
                headers=cl.headers,
                json={
                    'version': '1.0',
                    'variant': '3',
                    'language': 'en',
                    'breadcrumbs': [10, 41],
                    'elements': {},
                    'name': 'report',
                    'report_type': 1,
                    'object_type': 1,
                    'object_id': self.messageid,
                    'channel_id': self.channelid,
                    'reason': self.reason
                }
            )

            if r.status_code == 201:
                self.logger.succeded(f'{ctoken} Reported message')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(float(limit))
                self.report(token, cl)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                time.sleep(5)
                self.report(token, cl)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                time.sleep(10)
                self.report(token, cl)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(f'{ctoken} Hcaptcha required')

            elif 'You need to verify' in r.text:
                self.logger.locked(f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(f'{ctoken}', error)

        except Exception as e:
            self.logger.error(f'{ctoken}', e)

    def menu(self):
        self.ui.prep()
        message_link = self.ui.input('Message Link to report')
        ids = discordutils.extractids(message_link)
        self.channelid = ids['channel']
        self.messageid = ids['message']
        
        self.ui.createmenu([
            'Harassment',
            'Spam',
            'Self-harm',
            'NSFW content',
            'Hate speech',
            'Doxxing/Personal info',
            'Threats of violence',
            'Other'
        ])
        
        reason_choice = self.ui.input('Report reason')
        reasons = {
            '1': 1,  # Harassment
            '2': 2,  # Spam
            '3': 3,  # Self-harm
            '4': 4,  # NSFW
            '5': 5,  # Hate speech
            '6': 6,  # Doxxing
            '7': 7,  # Threats
            '8': 8   # Other
        }
        
        self.reason = reasons.get(reason_choice, 8)
        self.delay = self.ui.delayinput()

        threading(
            func=self.report,
            tokens=files.gettokens(),
            delay=self.delay,
        )