import sys, os; sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
from src import *
from src.plugins.error_chandler import *
from src.plugins.log import *
from src.plugins.ui import *
from src.plugins.files import *
from src.plugins.rpc import RPC
from src.plugins.auto_update import *

RPC.update('Starting up', 'discord.gg/spamming')
ui().cls()
ui().title('Lime V2 FREE - discord.gg/spamming')
ui().banner()
log.info('Main', 'Startring up!')
auto_update().auto_update()

pause = False

if files.getsolverapikey() or files.getsolverstatus():
    log.warn('Files', f'Solver support is PAID ONLY')
    pause = True

if files.getproxystatus():       
    log.warn('Files', 'Proxy support is PAID ONLY')
    pause = True

if not files.gettokens():
    log.warn('Files', 'You did not input any tokens into input\\tokens.txt please input them in! (NOT DISCORD BOT TOKENS ACTUAL ACCOUNT TOKENS) run /tokens command on my server to get more info')
    pause = True

if pause: 
    log.info('Main', 'Press enter to continue', True)

from src.modules.joiner import *
from src.modules.leaver import *
from src.modules.isinserver import *
from src.modules.message_spammer import *
from src.modules.checker import *
from src.modules.display_changer import *
from src.modules.pron_changer import *
from src.modules.reaction import *

while True:
    RPC.update('In the main menu', 'discord.gg/spamming')
    ui().cls()
    ui().title('Lime V2 FREE - discord.gg/spamming')
    ui().banner()
    ui().stats()
    ui().menu()

    choice = ui().ask('Choice')

    if choice.startswith('0') and len(choice) == 2:
        choice = str(int(choice))

    options = {
        '>>': lambda: (ui().menu2(), ui().ask('Choice')),
        '1': joiner().main,
        '2': leaver().main,
        '3': isinserver().main,
        '4': log.premium_only,
        '5': log.premium_only,
        '6': message_spammer().main,
        '7': log.premium_only,
        '8': log.premium_only,
        '9': log.premium_only,
        '10': log.premium_only,
        '11': checker().main,
        '12': log.premium_only,
        '13': log.premium_only,
        '14': display_changer().main,
        '15': pron_changer().main,
        '16': log.premium_only,
        '17': reaction().main,
        '18': log.premium_only,
        '19': log.premium_only,
        '20': log.premium_only
    }

    if choice in options:
        options[choice]()
    else:
        log.info('Main', 'That option does not exist yet', True)

    log.info('Main', 'Finished! Enter to continue | If you enjoyed the tool make sure to leave a vouch on the discord!', True)