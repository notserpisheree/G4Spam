import os
import time
import subprocess
import sys

try:
    print('Checking if pip is installed correctly...')
    subprocess.run([sys.executable, '-m', 'pip', '--version'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print('Pip is installed correctly')
except subprocess.CalledProcessError:
    print('Pip is NOT installed correctly, installing and fixing it now!')
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pip_path = os.path.join(os.path.dirname(sys.executable), 'Scripts')
        if pip_path not in os.environ['PATH']:
            os.environ['PATH'] += os.pathsep + pip_path
        print('Pip installed and added to path succefssfully!')
    except Exception:
        print('Failed to install pip! PLEASE INSTALL PIP MANUALLY!!! AND DO NOT FORGET TO ADD IT TO PATH!!!')
        input('Enter to quit...')
        exit()

try:
    import requests
    import tls_client
    from colorama import Back as B, Style as S
    from datetime import datetime as dt
    import ab5
    from bs4 import BeautifulSoup
    from io import BytesIO
    import zipfile

except ModuleNotFoundError:
    print('Modules not found! Installing them!')

    libs = [
        'uuid',
        'ab5',
        'datetime',
        'colorama',
        'requests',
        'tls-client',
        'beautifulsoup4',
        'typing-extensions',
        'typing'
    ]

    for lib in libs:
        os.system(f'pip install {lib}')
    
    print('Modules installed! Starting lime V2...')
    os.system('py main.py limev2')
    exit()

except Exception as e:
    print('Failed to import modules')
    print(e)
    input('Enter to quit...')
    exit()

os.system('py main.py limev2')