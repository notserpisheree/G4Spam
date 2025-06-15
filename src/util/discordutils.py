# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.client import client

class discordutils:
    def extractinv(invite):
        match: re.Match = re.search(r'(?:(?:http:\/\/|https:\/\/)?discord\.gg\/|discordapp\.com\/invite\/|discord\.com\/invite\/)?([a-zA-Z0-9-]+)', invite)
        if match: 
            return match.group(1)
        
        return invite
    
    def getid(token) :
        period = token.find('.')
        if period != -1: 
            cut = token[:period]
        return base64.b64decode(cut + '==').decode()
    
    def getsnowflake():
        return ((int(time.time() * 1000) - 1420070400000) << 22)