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
from src.util.apibypassing import apibypassing
from src.util.discordutils import discordutils
from src.util.threading import threading
from src.util.files import files

apibypassing = apibypassing()

class joiner:
    def __init__(self):
        self.module = 'Joiner'
        self.logger = logger(self.module)
        self.invite = None

        self.serverid = None
        self.servername = None
        self.channelid = None
        self.channeltype = None
        self.verifications = []


    def discover(self, token, cl: client=None):
        ctoken = ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token=token, reffer='https://discord.com/discovery/servers')

            r = cl.sess.get(
                f'https://discord.com/api/v9/invites/{self.invite}?inputValue={self.invite}&with_counts=true&with_expiration=true&with_permissions=true',
                headers=cl.headers
            )

            if r.status_code == 200:
                data = r.json()
                guild: dict = data.get('guild', {})
                features = guild.get('features', [])
                channel: dict = data.get('channel', {})

                self.serverid = guild.get('id')
                self.servername = guild.get('name')
                self.channelid = channel.get('id')
                self.channeltype = channel.get('type')
                
                if 'GUILD_ONBOARDING' in features:
                    self.verifications.append('Onboarding')

                if 'MEMBER_VERIFICATION_GATE_ENABLED' in features:
                    self.verifications.append('Rules')
                
                servername = ui.cut(text=self.servername, length=20, end='...')

                if self.verifications:
                    endstr = f' [{", ".join(self.verifications)}]'
                else:
                    endstr = ''

                self.logger.succeded(f'{ctoken} Discovered server {servername}{endstr}')
                return True

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(float(limit))
                return self.discover(token, client)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                time.sleep(5)
                return self.discover(token, client)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                time.sleep(10)
                return self.discover(token, client)
            
            elif 'You need to verify' in r.text:
                self.logger.locked(f'{ctoken} Locked/Flagged')
                return False

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(f'{ctoken} Failed to discover invite', error)
                return False

        except Exception as e:
            self.logger.error(f'{ctoken} Failed to discover invite', e)
            return False

    def join(self, token, cl: client=None):
        ctoken = ui.cut(token, 20, '...')
        try:
            if not cl:
                cl = client(token=token, reffer='https://discord.com/discovery/servers')
            
            cl.headers['x-context-properties'] = apibypassing.encode(data={
                'location': 'Join Guild',
                'location_guild_id': self.serverid,
                'location_channel_id': self.channelid,
                'location_channel_type': self.channeltype
            })

            if self.discover(token, cl):
                r = cl.sess.post(
                    f'https://discord.com/api/v9/invites/{self.invite}',
                    headers=cl.headers,
                    json={
                        'session_id': cl.wssessid
                    }
                )

                if r.status_code == 200:
                    servername = ui.cut(self.servername, 20, '...')
                    self.logger.succeded(f'{ctoken} Joined {servername}')

                elif 'retry_after' in r.text:
                    limit = r.json().get('retry_after', 1.5)
                    self.logger.ratelimited(f'{ctoken} Rate limited', limit)
                    time.sleep(float(limit))
                    self.join(token, client)

                elif 'Try again later' in r.text:
                    self.logger.ratelimited(f'{ctoken} Rate limited', 5)
                    time.sleep(5)
                    self.join(token, client)

                elif 'Cloudflare' in r.text:
                    self.logger.cloudflared(f'{ctoken} Cloudflare rate limited', 10)
                    time.sleep(10)
                    self.join(token, client)
                
                elif 'captcha_key' in r.text:
                    self.logger.hcaptcha(f'{ctoken} Hcaptcha required')

                elif 'You need to verify' in r.text:
                    self.logger.locked(f'{ctoken} Locked/Flagged')

                else:
                    error = self.logger.errordatabase(r.text)
                    self.logger.error(f'{ctoken} Failed to join', error)

            else:
                self.logger.error(f'{ctoken} Skipping join as discovery failed')

        except Exception as e:
            self.logger.error(f'{ctoken} Failed to join', e)

    def menu(self):
        ui.prep(self.module)

        self.invite = discordutils.extractinv(ui.input('Invite link', self.module))
        self.delay = ui.delayinput(self.module)

        threading(
            func=self.join,
            tokens=files.gettokens(),
            delay=self.delay,
        )