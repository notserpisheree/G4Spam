# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.files import files
from src.util.rpc import RPC

class ui:
    def __init__(self, module=None):
        self.module = module

    def title(self, title):
        os.system(f'title {title}')

    def cls(self):
        os.system('cls')

    def center(self, text, size):
        text = str(text)
        lines = text.split('\n')
        centeredlines = []
        for line in lines:
            visibleline = re.sub(r'\033\[[0-9;]*m', '', line)
            visiblelength = len(visibleline)
            
            if visiblelength >= size:
                centeredlines.append(line)
            else:
                padding = (size - visiblelength) // 2
                centeredlines.append(' ' * padding + line)
        
        return '\n'.join(centeredlines)
    
    def bar(self):
        bar = fr'{co.main}«{len(files.gettokens())}» Tokens                   «{len(files.getproxies())}» Proxies'

        bar = self.center(text=bar, size=os.get_terminal_size().columns)
        bar = str(bar)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def banner(self):
        banner = fr'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = self.center(banner, os.get_terminal_size().columns)

        print(banner)
        
    def menu(self):
        menu = fr'''{co.main}
THIS IS WORK IN PROGRESS NOT EVERYTHING IS MADE JOIN DISCORD FOR INFO
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                │
│   «01» Server managment   «06» Webhook menu       «11» Annoying menu      «18» Unk             │
│   «02» Token managment    «07» Nuking menu        «12» Unk                «17» Unk             │
│   «03» Spamming menu      «08» Proxy menu         «13» Unk                «18» Unk             │
│   «04» Bypass menu        «09» Mass DM menu       «14» Unk                «19» Sources         │
│   «05» VC menu            «10» Mass report menu   «15» Unk                «20» Exit            │
│                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
'''     
        menu: str = self.center(text=menu, size=os.get_terminal_size().columns)
        
        for char in ['╭', '╯', '╮', '╰', '─', '│', '»', '«']:
            menu = menu.replace(char, f'{co.main}{char}{co.reset}')

        print(menu)

    def input(self, text, yesno=False):
        if self.module == None:
            module = ''
        else:
            module = f'{co.main}[{co.reset}{self.module}{co.main}] '

        if yesno:
            result = input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}({co.reset}y/n{co.main}) {co.main}» {co.reset}')
            if result in ['y', 'Y', 'yes', 'Yes', 'YES']:
                return True
            else:
                return False
            
        return input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}» {co.reset}')
    
    def delayinput(self):
        if self.module == None:
            module = ''
        else:
            module = f'{co.main}[{co.reset}{self.module}{co.main}] '

        x = input(f'{module}{co.main}[{co.reset}Delay{co.main}] {co.main}» {co.reset}')
        try:
            float(x)
        except:
            return 0
        
        return x

    def createmenu(self, options):
        toprint = []
        for i, option in enumerate(options, 1):
            number = str(i).zfill(2)
            toprint.append(f'{co.main}[{co.reset}{number}{co.main}] » {co.main}[{co.reset}{option}{co.main}]')
        
        print('\n'.join(toprint))

    def prep(self):
        RPC.update(f'Using {self.module}')
        self.cls()
        self.banner()
        if self.module != None:
            self.title(f'G4Spam - {self.module} - github.com/R3CI/G4Spam - discord.gg/spamming - Made by r3ci')

    def cut(self, text, length, end=''):
        if len(text) <= length:
            return text
        return text[:length] + end
