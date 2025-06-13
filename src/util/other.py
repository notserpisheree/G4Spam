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