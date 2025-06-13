'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *
from src.util.files import files
# «
# » 
# ➤
# ◜ ◝
# ◞ ◟
# ❘
# ╭ ╮
# ╰ ╯
# │
# ─
class ui:
    def title(title: str):
        os.system(f'title {title}')

    def cls():
        os.system('cls')

    def center(text: str, size: int) -> str:
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
    
    def bar():
        bar = f'{co.main}«{len(files.readsplitlines('data\\tokens.txt'))}» Tokens                   «{len(files.readsplitlines('data\\proxies.txt'))}» Proxies'

        bar: str = ui.center(text=bar, size=os.get_terminal_size().columns)

        for char in ['»', '«']:
            bar = bar.replace(char, f'{co.main}{char}{co.reset}')

        print(bar)

    def banner():
        banner = fr'''{co.main}
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      ''' 
        banner = ui.center(banner, os.get_terminal_size().columns)

        print(banner)
        
    def menu():
        menu = fr'''{co.main}
THIS IS WORK IN PROGRESS NOT EVERYTHING IS MADE JOIN DISCORD FOR INFO
╭────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                                │
│   «01» Server managment   «06» Webhook menu       «11» Annoying menu      «18» Unk             │
│   «02» Token managment    «07» Nuking menu        «12» Unk                «17» Unk             │
│   «03» Spamming menu      «08» Proxy menu         «13» Unk                «18» Unk             │
│   «04» Bypass menu        «09» Mass DM menu       «14» Unk                «19» Unk             │
│   «05» VC menu            «10» Mass report menu   «15» Unk                «20» Exit            │
│                                                                                                │
╰────────────────────────────────────────────────────────────────────────────────────────────────╯
'''     
        menu: str = ui.center(text=menu, size=os.get_terminal_size().columns)
        
        for char in ['╭', '╯', '╮', '╰', '─', '│', '»', '«']:
            menu = menu.replace(char, f'{co.main}{char}{co.reset}')

        print(menu)

    def input(text: str, module: str=None, yesno: bool=False) -> str:
        if module == None:
            module = ''
        else:
            module = f'{co.main}[{co.reset}{module}{co.main}] '

        if yesno:
            result = input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}({co.reset}y/n{co.main}) {co.reset}')
            if result in ['y', 'Y', 'yes', 'Yes', 'YES']:
                return True
            else:
                return False
            
        return input(f'{module}{co.main}[{co.reset}{text}{co.main}] {co.main}» {co.reset}')
    
    def delayinput(module: str=None) -> str:
        if module == None:
            module = ''
        else:
            module = f'{co.main}[{co.reset}{module}{co.main}] '

        x = input(f'{module}{co.main}[{co.reset}Delay{co.main}] {co.main}» {co.reset}')
        try:
            float(x)
        except:
            return 0
        
        return x

    def createmenu(options: list):
        toprint = []
        for i, option in enumerate(options, 1):
            number = str(i).zfill(2)
            toprint.append(f'{co.main}[{co.reset}{number}{co.main}] » {co.main}[{co.reset}{option}{co.main}]')
        
        print('\n'.join(toprint))

    def prep(text: str=None):
        ui.cls()
        ui.banner()
        if text != None:
            ui.title(f'G4Spam - {text} - github.com/R3CI/G4Spam - discord.gg/spamming - Made by r3ci')

    def cut(text: str, length: int, end: str = '') -> str:
        if len(text) <= length:
            return text
        return text[:length] + end
