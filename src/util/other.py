from src import *

class other:
    def getrepostars() -> str:
        r = requests.get(f'https://api.github.com/repos/R3CI/G4Spam')
        return r.json().get('stargazers_count', 'Unk')