from src import *

class logger:
    def __init__(self, name: str = 'Logger'):
        self.name = name

    def gettimestamp(self):
        timestamp = dt.now().strftime('%H:%M:%S')
        return timestamp

    def log(self, text: str):
        print(f'{co.grey}[{self.gettimestamp()}{co.grey}] {co.grey}[{co.main}{self.name}{co.grey}] {co.grey}[{co.main}{text}{co.grey}]')

    def error(self, text: str, error: str):
        print(f'{co.grey}[{self.gettimestamp()}{co.grey}] {co.grey}[{co.main}{self.name}{co.grey}] {co.grey}[{co.red}{text}{co.grey}] {co.grey}({co.red}{error}{co.grey})')