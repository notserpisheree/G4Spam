from src import *

class ui:
    def center(text: str, size: int) -> str:
        lines = text.split('\n')
        centeredlines = []
        for line in lines:
            centeredlines.append(line.center(size))
        return '\n'.join(centeredlines)

    def banner():
        banner = r'''
   ________ __ _____                     
  / ____/ // // ___/____  ____ _____ ___ 
 / / __/ // /_\__ \/ __ \/ __ `/ __ `__ \
/ /_/ /__  __/__/ / /_/ / /_/ / / / / / /
\____/  /_/ /____/ .___/\__,_/_/ /_/ /_/ 
                /_/                      
''' 
        banner = ui.center(banner, os.get_terminal_size().columns)
        print(ab5.vgratient(banner, co.gmain, co.gmain_))
        