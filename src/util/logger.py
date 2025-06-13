from src import *

class logger:
    def __init__(self, module: str='Logger'):
        self.module = module

    def gettimestamp(self):
        timestamp = dt.now().strftime('%H:%M:%S')
        return timestamp

    def log(self, text: str, ts: bool=False):
        if ts:
            ts = f'{co.main}[{co.reset}{self.gettimestamp()}{co.main}] '
        else:
            ts = ''
        print(f'{ts}{co.main}[{co.reset}{self.module}{co.main}] {co.main}[{co.reset}{text}{co.main}]{co.reset}')

    def error(self, text: str, error: str='', ts: bool=False):
        if error == '':
            endstr = ''
        else:
            endstr = f'{co.main}[{co.red}{error}{co.main}]{co.reset}'

        if ts:
            ts = f'{co.main}[{co.reset}{self.gettimestamp()}{co.main}] '
        else:
            ts = ''

        print(f'{ts}{co.main}[{co.reset}{self.module}{co.main}] {co.main}[{co.red}{text}{co.main}] {endstr}{co.reset}')

    def errordatabase(self, text: str) -> str:
        db = {
            '10014': 'Unknown emoji',
            '30010': 'Max reactions on message',
            '40007': 'Banned token',
            '40002': 'Locked token',
            '50109': 'Invalid JSON',
            '200000': 'Automod flagged',
            '50007': 'Action not allowed',
            '50008': 'Unable to send',
            '50001': 'No access/Not inside',
            '50013': 'Missing permissions',
            '50024': 'Cant do that on this channel',
            '80003': 'Cant self friend',
            '50168': 'Not in a VC',
            '20028': 'Limited',
            '340013': 'Muted/Acces to send messages limited by server',
            '401: Unauthorized': 'Invalid token/Lock invalided token',
            'Cloudflare': 'Cloudflare',
            'captcha_key': 'Hcaptcha',
            'Unauthorized': 'Invalid token/Lock invalided token',
            'retry_after': 'Limited',
            'You need to verify': 'Locked token',
            'Cannot send messages to this user': 'Disabled DMS',
            'You are being blocked from accessing our API': 'API BAN',
            'Unknown Invite': 'Unknown Invite',
            '150009': 'Alerdy a member (no need to verify)',
            '50055': 'Invalid server',
            '50009': 'Verification too high (server requires PV, EV or being in server for 10 mins)',
            '50035': 'Invalid JSON'
        }

        for key in db.keys():
            if key in text:
                return db[key]

        return text