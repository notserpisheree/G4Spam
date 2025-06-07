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
    def cls():
        os.system('cls')

    def center(text: str, size: int) -> str:
        lines = text.split('\n')
        centeredlines = []
        for line in lines:
            centeredlines.append(line.center(size))
        return '\n'.join(centeredlines)
    
    def bar():
        tokens = len(files.read('data\\tokens.txt'))
        proxies = len(files.read('data\\proxies.txt'))
        bar = f'                                         {co.reset}{tokens}{co.main} Tokens                                                 {co.reset}{proxies}{co.main} Proxies'
        bar = ui.center(text=bar, size=os.get_terminal_size().columns)
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
╭─────────────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                             │
│   «01» Server                                                                               │
│   «02» Token                                                                                │
│   «03» Spamming                                                                             │
│                                                                                             │
│                                                                                             │
│                                                                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
'''     
        menu: str = ui.center(text=menu, size=os.get_terminal_size().columns)
        
        for char in ['╭', '╯', '╮', '╰', '─', '│', '»', '«']:
            menu = menu.replace(char, f'{co.main}{char}{co.reset}')

        print(menu)

    def input(text: str) -> str:
        return input(f'{co.main}[{co.reset}{text}{co.main}] {co.main}»{co.grey} {co.reset}')