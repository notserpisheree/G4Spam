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

class joiner:
    def __init__(self):
        self.logger = logger(module='Joiner')
        self.invite = None

        self.serverid = None
        self.servername = None
        self.channelid = None
        self.channeltype = None
        self.verifications = []


    def discover(self, token, cl: client=None):
        try:
            ctoken = ui.cut(text=token, length=20, end='...')
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
                self.logger.succeded(text=f'{ctoken} Discovered server {servername} [{", ".join(self.verifications)}]')
                return True

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                time.sleep(float(limit))
                return self.discover(token, client)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                time.sleep(5)
                return self.discover(token, client)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(text=f'{ctoken} Cloudflare rate limited', fortime=10)
                time.sleep(10)
                return self.discover(token, client)
            
            elif 'You need to verify' in r.text:
                self.logger.locked(text=f'{ctoken} Locked/Flagged')
                return False

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(text=f'{ctoken} Failed to discover invite', error=error)
                return False

        except Exception as e:
            self.logger.error(text=f'{ctoken} Failed to discover invite', error=e)
            return False

    def join(self, token, cl: client=None):
        try:
            ctoken = ui.cut(text=token, length=20, end='...')
            if not cl:
                cl = client(token=token, reffer='https://discord.com/discovery/servers')
            
            client.headers['x-context-properties'] = apibypassing.encode({
                'location': 'Join Guild',
                'location_guild_id': self.serverid,
                'location_channel_id': self.channelid,
                'location_channel_type': self.channeltype
            })

            dojoin = self.discover(token, cl)
            if dojoin:
                r = cl.sess.post(
                    f'https://discord.com/api/v9/invites/{self.invite}',
                    headers=cl.headers,
                    json={
                        'session_id': cl.wssessid
                    }
                )

                if r.status_code == 200:
                    servername = ui.cut(text=self.servername, length=20, end='...')
                    self.logger.succeded(text=f'Joined {servername}')

                elif 'retry_after' in r.text:
                    limit = r.json().get('retry_after', 1.5)
                    self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                    time.sleep(float(limit))
                    return self.discover(token, client)

                elif 'Try again later' in r.text:
                    self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                    time.sleep(5)
                    return self.discover(token, client)

                elif 'Cloudflare' in r.text:
                    self.logger.cloudflared(text=f'{ctoken} Cloudflare rate limited', fortime=10)
                    time.sleep(10)
                    return self.discover(token, client)
                
                elif 'captcha_key' in r.text:
                    self.logger.hcaptcha(text=f'{ctoken} Hcaptcha required')

                elif 'You need to verify' in r.text:
                    self.logger.locked(text=f'{ctoken} Locked/Flagged')

                else:
                    error = self.logger.errordatabase(r.text)
                    self.logger.error(text=f'{ctoken} Failed to discover invite', error=error)

            else:
                self.logger.error(text=f'{token} Skipping join as discovery failed')

        except Exception as e:
            self.logger.error(text=f'{token} Failed to join', error=e)