from src import *
from src.plugins.files import *

class RPC:
    def __init__(self):
        try:
            self.client_id = '1321847572096352286'
            self.rpc = Presence(self.client_id)
            self.rpc.connect()
            self.rpc.update(
                state='Lime V2 Free',
                details='discord.gg/spamming',
                start=time.time(),
                large_image='limev2',
                large_text='Lime V2 Free',
                small_image='folder',
                small_text=f'Tokens - {len(files.gettokens())} | Proxies - {len(files.getproxies())}',
                buttons=[
                    {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                    {'label': 'Get Lime V2 Free', 'url': 'https://github.com/R3CI/LimeV2-free'}
                ]
            )
        except:
            pass

    def update(self, state, details):
        try:
            self.rpc.update(
                state=state,
                details=details,
                start=time.time(),
                large_image='limev2',
                large_text='Lime V2 Free',
                small_image='folder',
                small_text=f'Tokens - {len(files.gettokens())} | Proxies - {len(files.getproxies())}',
                buttons=[
                    {'label': 'Join Discord', 'url': 'https://discord.gg/spamming'},
                    {'label': 'Get Lime V2 Free', 'url': 'https://github.com/R3CI/LimeV2-free'}
                ]
            )
        except:
            pass

RPC = RPC()