'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *

class other:
    def getrepostars() -> str:
        r = requests.get(f'https://api.github.com/repos/R3CI/G4Spam')
        return r.json().get('stargazers_count', 'Unk')
    
    def addlaunch():
        try:
            requests.post('http://r3ci.pythonanywhere.com/launch', timeout=3)
        except:
            pass

    def getlaunches() -> str:
        try:
            return str(requests.get('http://r3ci.pythonanywhere.com/launches', timeout=3).text).strip()
        except:
            return '0'

    def delay(seconds: float) -> None:
        seconds = float(seconds)
        if seconds != 0:
            time.sleep(seconds)