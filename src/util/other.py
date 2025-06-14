'''
This code is the property of R3CI.
Unauthorized copying, distribution, or use is prohibited.
Licensed under the GNU General Public License v3.0 (GPL-3.0).
For more details, visit https://github.com/R3CI/G4Spam
'''

from src import *

class other:
    def getrepostars():
        try:
            r = requests.get('https://api.github.com/repos/R3CI/G4Spam', timeout=5)
            r.raise_for_status()
            return r.json().get('stargazers_count', 'Unk')
        except:
            return 'Unk'
   
    def addlaunch():
        try:
            requests.post(f'http://prem-eu1.bot-hosting.net:22100/launch', timeout=3)
        except:
            pass
    
    def getlaunches():
        try:
            r = requests.get(f'http://prem-eu1.bot-hosting.net:22100/launches', timeout=3)
            r.raise_for_status()
            data = r.json()
            return str(data.get('count', 0))
        except:
            return '0'
    
    def delay(seconds):
        seconds = float(seconds)
        if seconds > 0:
            time.sleep(seconds)