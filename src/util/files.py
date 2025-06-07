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

    def createdir(path: str):
        if not os.path.exists(path):
            os.makedirs(path)

    def createfile(path: str):
        if not os.path.exists(path):
            open(path, 'w').close()
    
    def removefile(path: str):
        if os.path.exists(path):
            os.remove(path)

    def joinpath(*args):
        return os.path.join(*args)
    
    def getsize(path: str):
        return os.path.getsize(path)
    
    def isfile(path: str):
        return os.path.isfile(path)
    
    def isdir(path: str):
        return os.path.isdir(path)
    
    def exists(path: str):
        return os.path.exists(path)
    
    def walk(path: str):
        return os.walk(path)
    
    def listdir(path: str):
        return os.listdir(path)
    
    def getcwd():
        return os.getcwd()
    
    def runtasks():
        for d in _dirs:
            if not files.exists(d):
                files.createdir(d)
        
        for f in _files:
            if not files.exists(f):
                files.createfile(f)

files.runtasks()