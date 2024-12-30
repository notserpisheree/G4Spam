from src import *
from src.plugins.log import *
from src.plugins.files import *

class prep:
    def __init__(self):
        log.info('Client', 'Getting client info...')
        self.sess = tls_client.Session(
            random_tls_extension_order=True, 
            client_identifier='chrome_120'
        )

        self.headers = None
        self.xsup = None
        self.ua = None
        log.info('Client', 'Inited header values')

        self.os = platform.system()
        self.client_version = '1.0.9175'
        self.os_version = platform.version()
        self.os_arch = platform.architecture()[0]
        self.app_arch = platform.architecture()[0] 
        self.browser_version = '32.2.7'
        self.os_sdk_version = platform.version().split('.')[0]
        self.client_build_number = 355624
        self.native_build_number = 56716
        log.info('Client', 'Inited xsup values')

        r = requests.get(
            'https://raw.githubusercontent.com/R3CI/discord-api/refs/heads/main/latest-headers.json'
        )
        if r.status_code == 200:
            self.ua = r.json().get('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9175 Chrome/128.0.6613.186 Electron/32.2.7 Safari/537.36')
        else:
            self.ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9175 Chrome/128.0.6613.186 Electron/32.2.7 Safari/537.36'
        log.info('Client', 'Got the User-Agent for the discord app')

        self.cookies = {}
        self.cookies_renew()
        log.info('Client', 'Updated discord info')

        self.xsup_form()
        log.info('Client', 'Formed xsup base')
        self.xsup_client()
        log.info('Client', 'Got xsup client info')
        self.xsup_native()
        log.info('Client', 'Got xsup native info')

        self.headers_form()
        log.info('Client', 'Formed headers')

    def cookies_renew(self):
        r = self.sess.get(
            'https://discord.com',
            headers=self.headers
        )

        cookies_ = r.cookies.get_dict()
        self.cookies['__dcfduid'] = cookies_.get('__dcfduid')
        self.cookies['__sdcfduid'] = cookies_.get('__sdcfduid')
        self.cookies['_cfuvid'] = cookies_.get('_cfuvid')
        self.cookies['locale'] = 'en-US'
        self.cookies['__cfruid'] = cookies_.get('__cfruid')

    def headers_form(self):
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-GB,pl;q=0.9',
            'Content-Type': 'application/json',
            'Origin': 'https://discord.com',
            'Referer': 'https://discord.com/@me',
            'Priority': 'u=1, i',
            'Sec-Ch-Ua': '"Not;A=Brand";v="24", "Chromium";v="128"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': self.ua,
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Europe/Warsaw',
            'X-Super-Properties': self.xsup
        }

        self.headers = headers

    def xsup_form(self):
        xsup = {
            'os': self.os,
            'browser': 'Discord Client',
            'release_channel': 'stable',
            'client_version': self.client_version,
            'os_version': self.os_version,
            'os_arch': self.os_arch,
            'app_arch': self.app_arch,
            'system_locale': self.cookies['locale'],
            'has_client_mods': False,
            'browser_user_agent': self.ua,
            'browser_version': self.browser_version,
            'os_sdk_version': self.os_sdk_version,
            'client_build_number': self.client_build_number,
            'native_build_number': self.native_build_number,
            'client_event_source': None
        }

        self.xsup = base64.b64encode(json.dumps(xsup).encode()).decode()

    def xsup_native(self):
        r = self.sess.get(
            'https://updates.discord.com/distributions/app/manifests/latest?channel=stable&platform=win&arch=x86',
            headers=self.headers
        )

        self.native_build_number = r.json().get('client_version', self.native_build_number)

    def xsup_client(self):
        r = self.sess.get(
            'https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86',
            headers=self.headers,
            allow_redirects=False
        )

        match = re.search(r'/(\d+\.\d+\.\d+)/DiscordSetup.exe', r.text)
        if match:
            self.client_build_number = match.group(1)
prep = prep()

class client:
    def __init__(self, token=None):
        self.token = token
        self.proxy = None

        self.sess = tls_client.Session(
            client_identifier='chrome_120',
            random_tls_extension_order=True,
            ja3_string='771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0',
            h2_settings={
                'HEADER_TABLE_SIZE': 65536,
                'MAX_CONCURRENT_STREAMS': 1000,
                'INITIAL_WINDOW_SIZE': 6291456,
                'MAX_HEADER_LIST_SIZE': 262144
            },
            h2_settings_order=[
                'HEADER_TABLE_SIZE',
                'MAX_CONCURRENT_STREAMS',
                'INITIAL_WINDOW_SIZE',
                'MAX_HEADER_LIST_SIZE'
            ],
            supported_signature_algorithms=[
                'ECDSAWithP256AndSHA256',
                'PSSWithSHA256',
                'PKCS1WithSHA256',
                'ECDSAWithP384AndSHA384',
                'PSSWithSHA384',
                'PKCS1WithSHA384',
                'PSSWithSHA512',
                'PKCS1WithSHA512'
            ],
            supported_versions=['GREASE', '1.3', '1.2'],
            key_share_curves=['GREASE', 'X25519'],
            cert_compression_algo='brotli',
            connection_flow=15663105,
            force_http1=False,
        )
        self.headers = prep.headers
        self.cookies = prep.cookies
        self.xsup = prep.xsup
        self.ua = prep.ua
