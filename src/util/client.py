from src import *
from src.util.logger import logger
from src.util.apibypassing import apibypassing
from src.util.curlwrapper import curlwrapper
logger = logger(module='Client')

apibypassing = apibypassing()
logger.log(text=f'Latest info fingerprint={apibypassing.fingerprint} client_build={apibypassing.clientbuild}', ts=True)

tempsess = curlwrapper.Session(impersonate=apibypassing.fingerprint)
cookie: requests.cookies.RequestsCookieJar = apibypassing.getcookie(headers=apibypassing.headers, session=tempsess)

logger.log(text=f'Got discord info', ts=True)

class client:
    def __init__(self, token=None, reffer='https://discord.com/channels/@me'):
        self.sess = curlwrapper.Session(impersonate=apibypassing.fingerprint)
        self.launchid = str(uuid.uuid4())
        self.wssessid = str(uuid.uuid4())
        self.sess.cookies.update(cookie)

        self.headers = apibypassing.headers
        self.headers['reffer'] = reffer
        self.headers['authorization'] = token

        xsuper = apibypassing.xsuper  
        xsuper['referrer'] = reffer
        xsuper['client_launch_id'] = self.launchid
        xsuper['client_heartbeat_session_id'] = self.wssessid
        xsuper = apibypassing.encode(xsuper)
        self.headers['X-Super-Properties'] = xsuper

        