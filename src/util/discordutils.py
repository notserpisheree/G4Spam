# This code is the property of R3CI.
# Unauthorized copying, distribution, or use is prohibited.
# Licensed under the GNU General Public License v3.0 (GPL-3.0).
# For more details, visit https://github.com/R3CI/G4Spam

from src import *
from src.util.client import client
from src.util.logger import logger
logger = logger('Discord Utils')

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
    
    def extractids(text):
        m: re.Match = re.search(r'discord\.com/channels(?:/(@me|\d+))?(?:/(\d+))?(?:/(\d+))?', text)
        return {
            'server': m.group(1) if m else None,
            'channel': m.group(2) if m else None,
            'message': m.group(3) if m else None
        }
    
    def getreactions(tokens, channelid, messageid):
        reactions = []
        random.shuffle(tokens[:])
        try:
            for token in tokens:
                cl = client(token)
                for _ in range(5):
                    r = cl.sess.get(
                        f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50',
                        headers=cl.headers
                    )

                    if r.status_code == 200:
                        for message in r.json():
                            if message['id'] == messageid:
                                for reaction in message['reactions']:
                                    if not message['reactions']:
                                        return reactions

                                    emoji_name = reaction['emoji']['name']
                                    emoji_id = reaction['emoji']['id']
                                    count = reaction['count']
                                    reactions.append((emoji_name, emoji_id, count))
                                
                                return reactions


                    elif 'retry_after' in r.text:
                        limit = r.json().get('retry_after', 1.5)
                        time.sleep(limit)

                    elif 'Try again later' in r.text:
                        time.sleep(15)

                    elif 'Cloudflare' in r.text:
                        time.sleep(10)

                    else:
                        break
                
                if reactions:
                    break
            
            logger.error('Failed to fetch reactions')
            return reactions
            
        except Exception as e:
            logger.error('Failed to fetch reactions', e, False)
            return reactions