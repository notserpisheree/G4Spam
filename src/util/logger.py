from src import *

class logger:
    def __init__(self, name: str='Logger'):
        self.name = name

    def gettimestamp(self):
        timestamp = dt.now().strftime('%H:%M:%S')
        return timestamp

    def log(self, text: str, ts: bool=False):
        if ts:
            ts = f'{co.main}[{co.reset}{self.gettimestamp()}{co.main}] '
        else:
            ts = ''
        print(f'{ts}{co.main}[{co.reset}{self.name}{co.main}] {co.main}[{co.reset}{text}{co.main}]{co.reset}')

    def error(self, text: str, error: str='', ts: bool=False):
        if error == '':
            endstr = ''
        else:
            endstr = f'{co.grey}({co.grey}{error}{co.grey}){co.reset}'

        if ts:
            ts = f'{co.main}[{co.reset}{self.gettimestamp()}{co.main}] '
        else:
            ts = ''

        print(f'{ts}{co.main}[{co.reset}{self.name}{co.main}] {co.main}[{co.red}{text}{co.main}] {endstr}{co.reset}')