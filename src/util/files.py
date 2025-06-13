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
    def gettokens():
        with open('data\\tokens.txt', 'r') as f:
            return f.read().splitlines()

    def getproxies():
        with open('data\\proxies.txt', 'r') as f:
            return f.read().splitlines()

    def runtasks():
        for d in _dirs:
            if not os.path.exists(d):
                os.mkdir(d)
        
        for f in _files:
            if not os.path.exists(f):
                with open(f, 'w') as f:
                    f.write('')