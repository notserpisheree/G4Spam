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
from src.util.discordutils import discordutils
from src.util.files import files

class checker:
    def __init__(self):
        self.module = 'Checker'
        self.logger = logger(module=self.module)

        self.valids = []
        self.failed = []
        self.locked = []
        self.nitro = []
        self.nonitro = []
        self.ev = []
        self.noev = []
        self.pv = []
        self.nopv = []
        self.hasemail = []
        self.hasnoemail = []
        self.hasmfa = []
        self.hasnomfa = []

    def check(self, token, cl: client=None):
        ctoken = ui.cut(text=token, length=20, end='...')
        try:
            if not cl:
                cl = client(token=token, reffer='https://discord.com/channels/@me')

            r = cl.sess.get(
                f'https://discord.com/api/v9/users/@me/library',
                headers=cl.headers,
            )

            if r.status_code == 200:
                self.valids.append(token)

                def info():
                    domain, mfa, ev, email, phone, nitro, age = None, None, None, None, None, None, None
                    r = cl.sess.get(
                        'https://discord.com/api/v9/users/@me',
                        headers=cl.headers
                    )

                    if r.status_code == 200:
                        mfa = r.json().get('mfa_enabled', 'Unknown')
                        ev = r.json().get('verified', 'Unknown')
                        email: str = r.json().get('email', 'Unknown')
                        phone = r.json().get('phone', 'Unknown')
                        nitro = int(r.json().get('premium_type', '0'))

                        if mfa:
                            mfa = f'{co.green}[MFA]{co.green}'
                            self.hasmfa.append(token)
                        else:
                            mfa = f'{co.red}[MFA]{co.green}'
                            self.hasnomfa.append(token)

                        if ev:
                            ev = f'{co.green}[EV]{co.green}'
                            self.ev.append(token)
                        else:
                            ev = f'{co.red}[EV]{co.green}'
                            self.noev.append(token)

                        if phone:
                            phone = f'{co.green}[PHONE]{co.green}'
                            self.pv.append(token)
                        else:
                            phone = f'{co.red}[PHONE]{co.green}'
                            self.nopv.append(token)

                        if nitro != 0:
                            nitro = f'{co.green}[NITRO]{co.green}'
                            self.nitro.append(token)
                        else:
                            nitro = f'{co.red}[NITRO]{co.green}'
                            self.nonitro.append(token)

                        if email:
                            domain = email.split('@')[1]
                            email = f'{co.green}[EMAIL]{co.green}'
                            self.hasemail.append(token)
                        else:
                            email = f'{co.red}[EMAIL]{co.green}'
                            self.hasnoemail.append(token)
                    
                        timestamp = ((int(discordutils.getid(token)) >> 22) + 1420070400000) / 1000
                        creation_date = dt.fromtimestamp(timestamp, tz=timezone.utc)
                        current_date = dt.now(timezone.utc)
                        age = (current_date - creation_date).days

                    elif 'retry_after' in r.text:
                        limit = r.json().get('retry_after', 1.5)
                        self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                        time.sleep(float(limit))
                        info(token, client)

                    elif 'Try again later' in r.text:
                        self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=5)
                        time.sleep(5)
                        info(token, client)

                    elif 'Cloudflare' in r.text:
                        self.logger.cloudflared(text=f'{ctoken} Cloudflare rate limited', fortime=10)
                        time.sleep(10)
                        info(token, client)
                    
                    elif 'captcha_key' in r.text:
                        self.logger.hcaptcha(text=f'{ctoken} Hcaptcha required')

                    elif 'You need to verify' in r.text:
                        self.logger.locked(text=f'{ctoken} Locked/Flagged')

                    else:
                        error = self.logger.errordatabase(r.text)
                        self.logger.error(text=f'{ctoken} Failed to check', error=error)
                    
                    return domain, mfa, ev, email, phone, nitro, age

                domain, mfa, ev, email, phone, nitro, age = info()

                self.logger.succeded(text=f'{ctoken} Valid {domain} {mfa} {ev} {email} {phone} {nitro} {age} days')

            elif 'retry_after' in r.text:
                limit = r.json().get('retry_after', 1.5)
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=limit)
                time.sleep(float(limit))
                self.check(token, client)

            elif 'Try again later' in r.text:
                self.logger.ratelimited(text=f'{ctoken} Rate limited', fortime=5)
                time.sleep(5)
                self.check(token, client)

            elif 'Cloudflare' in r.text:
                self.logger.cloudflared(text=f'{ctoken} Cloudflare rate limited', fortime=10)
                time.sleep(10)
                self.check(token, client)
            
            elif 'captcha_key' in r.text:
                self.logger.hcaptcha(text=f'{ctoken} Hcaptcha required')

            elif 'You need to verify' in r.text:
                self.logger.locked(text=f'{ctoken} Locked/Flagged')

            else:
                error = self.logger.errordatabase(r.text)
                self.logger.error(text=f'{ctoken} Failed to check', error=error)

        except Exception as e:
            self.logger.error(text=f'{ctoken} Failed to check', error=e)

    def menu(self):
        ui.prep(text=self.module)

        self.delay = ui.delayinput(module=self.module)

        threading(
            func=self.check,
            tokens=files.gettokens(),
            delay=self.delay,
        )

        if self.valids:
            save = ui.input(text='Replace tokens.txt with only valid tokens', module=self.module, yesno=True)
            if save:
                with open('data\\tokens.txt', 'w') as f:
                    f.write('\n'.join(self.valids))
        
        else:
            self.logger.log(text='Blud has no valid tokens 😭😭😭')

        timestamp = dt.now().strftime('%Y-%m-%d--%H-%M-%S')
        timestamp = f'{timestamp}--{len(files.gettokens())}-TOKENS'
        fullpath = f'data\\checker\\{timestamp}'
        os.makedirs(fullpath, exist_ok=True)

        with open(f'{fullpath}\\valids.txt', 'w') as f:
            f.write('\n'.join(self.valids))

        with open(f'{fullpath}\\failed-invalid.txt', 'w') as f:
            f.write('\n'.join(self.failed))

        with open(f'{fullpath}\\locked.txt', 'w') as f:
            f.write('\n'.join(self.locked))

        with open(f'{fullpath}\\nitro.txt', 'w') as f:
            f.write('\n'.join(self.nitro))

        with open(f'{fullpath}\\nonitro.txt', 'w') as f:
            f.write('\n'.join(self.nonitro))

        with open(f'{fullpath}\\ev.txt', 'w') as f:
            f.write('\n'.join(self.ev))

        with open(f'{fullpath}\\noev.txt', 'w') as f:
            f.write('\n'.join(self.noev))

        with open(f'{fullpath}\\pv.txt', 'w') as f:
            f.write('\n'.join(self.pv))

        with open(f'{fullpath}\\nopv.txt', 'w') as f:
            f.write('\n'.join(self.nopv))

        with open(f'{fullpath}\\hasemail.txt', 'w') as f:
            f.write('\n'.join(self.hasemail))

        with open(f'{fullpath}\\hasnoemail.txt', 'w') as f:
            f.write('\n'.join(self.hasnoemail))

        with open(f'{fullpath}\\hasmfa.txt', 'w') as f:
            f.write('\n'.join(self.hasmfa))

        with open(f'{fullpath}\\hasnomfa.txt', 'w') as f:
            f.write('\n'.join(self.hasnomfa))

        os.system(f'start {fullpath}')

        self.logger.log(f'Made full report on {fullpath}')