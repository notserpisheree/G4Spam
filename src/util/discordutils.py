from src import *

class discordutils:
    def extractinv(invite: str) -> str:
        match: re.Match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
        if match: 
            return match.group(1)
        
        return invite
    
    def getid(token: str) -> str:
        period = token.find('.')
        if period != -1: 
            cut = token[:period]
        return base64.b64decode(cut + '==').decode()