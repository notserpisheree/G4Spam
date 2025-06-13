# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *

_files = [
    'data\\tokens.txt',
    'data\\proxies.txt'
]
_dirs = [
    'data'
]

class files:
    def write(path: str, text: str, method: str):
        with open(path, method) as f:
            f.write(text)

    def read(path: str) -> str:
        with open(path, 'r') as f:
            return f.read()
        
    def readsplitlines(path: str) -> list:
        with open(path, 'r') as f:
            return f.read().splitlines()

    def createdir(path: str):
        if not os.path.exists(path):
            os.makedirs(path)

    def createfile(path: str):
        if not os.path.exists(path):
            open(path, 'w').close()
    
    def removefile(path: str):
        if os.path.exists(path):
            os.remove(path)

    def joinpath(*args) -> str:
        return os.path.join(*args)
    
    def getsize(path: str) -> int:
        return os.path.getsize(path)
    
    def isfile(path: str) -> bool:
        return os.path.isfile(path)
    
    def isdir(path: str) -> bool:
        return os.path.isdir(path)
    
    def exists(path: str) -> bool:
        return os.path.exists(path)
    
    def walk(path: str) -> tuple:
        return os.walk(path)
    
    def listdir(path: str) -> list:
        return os.listdir(path)
    
    def getcwd() -> str:
        return os.getcwd()
    
    def gettokens() -> list:
        return files.readsplitlines('data\\tokens.txt')

    def getproxies() -> list:
        return files.readsplitlines('data\\proxies.txt')

    def runtasks():
        for d in _dirs:
            if not files.exists(d):
                files.createdir(d)
        
        for f in _files:
            if not files.exists(f):
                files.createfile(f)