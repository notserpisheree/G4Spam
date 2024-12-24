import os
import subprocess
import sys
import time

def print_section(title):
    print('\n' + '=' * 40)
    print(f'{title}'.center(40))
    print('=' * 40)

os.system('cls')
print_section('INITALIZED')

try:
    # region DEBUG
    print_section('DEBUG')
    print(f'Python Executable >> {sys.executable}')
    print(f'Python Version >> {sys.version}')

    print('System PATH >>')
    system_paths = os.environ['PATH'].split(os.pathsep)
    for path in system_paths:
        print(f'  {path}')
    print('=' * 40)


    # region CHECKING PIP
    print_section('PIP INSTALL CHECK')

    try:
        print('Checking if pip is installed correctly...')

        result = subprocess.run(
            [sys.executable, '-m', 'pip', '--version'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(f'Pip version detected (SAFE TO IGNORE) >> {result.stdout.strip()}')
        print('Pip is installed correctly')

    except subprocess.CalledProcessError as e:
        print('Pip is NOT installed correctly, attempting to install it now...')
        print(f'Pip check details (SAFE TO IGNORE)\nSTDOUT >> {e.stdout}\nSTDERR >> {e.stderr}')

        try:
            print_section('RUNNING ENSUREPIP')
            result = subprocess.run(
                [sys.executable, '-m', 'ensurepip'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(f'Ensurepip Output\nSTDOUT >> {result.stdout.strip()}\nSTDERR >> {result.stderr.strip()}')

            print_section('UPDATING PIP')
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(f'Pip Upgrade Output (SAFE TO IGNORE)\nSTDOUT: {result.stdout.strip()}\nSTDERR: {result.stderr.strip()}')

            print_section('ADDING PIP TO PATH')
            pip_path = os.path.join(os.path.dirname(sys.executable), 'Scripts')
            if pip_path not in os.environ['PATH']:
                os.environ['PATH'] += os.pathsep + pip_path
            print(f'Pip Path >> {pip_path}')
            print('Added pip to PATH')
            print(f'\nPip installed successfully and added to PATH\nCurrent PATH >> {os.environ["PATH"]}')

        except subprocess.CalledProcessError as e:
            print(f'\nFailed to install pip during ensurepip or upgrade\nSTDOUT >> {e.stdout}\nSTDERR >> {e.stderr}')
            input('Enter to quit...')
            exit()

        except Exception as e:
            print_section('ENSUREPIP OR UPGRADE ERROR')
            print(f'\nError while during ensurepip or upgrade >> {e}')
            input('Enter to quit...')
            exit()

    except Exception as e:
        print_section('PIP INSTALL CHECK ERROR')
        print(f'\nError while checking pip installation >> {e}')
        input('Enter to quit...')
        exit()

    # region INSTALLING LIBS
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
        print_section('MODULES NOT FOUND! INSTALLING LIBS NOW!')
        time.sleep(3)

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

        print_section('INSTALLED ALL LIBS OPENING LIME!')
        print_section('INSTALLED ALL LIBS OPENING LIME!')
        print_section('INSTALLED ALL LIBS OPENING LIME!')
        print_section('INSTALLED ALL LIBS OPENING LIME!')
        print_section('INSTALLED ALL LIBS OPENING LIME!')

        os.system('py main.py limev2')
        exit()

    except Exception as e:
        print('Failed to import modules')
        print(e)
        input('Enter to quit...')
        exit()

    print_section('EVERYTHING IS FINE OPENING LIME!')
    print_section('EVERYTHING IS FINE OPENING LIME!')
    print_section('EVERYTHING IS FINE OPENING LIME!')
    print_section('EVERYTHING IS FINE OPENING LIME!')
    print_section('EVERYTHING IS FINE OPENING LIME!')

    os.system('py main.py limev2')

except Exception as e:
    print_section('CORE ERROR')
    print(f'Error >> {e}')
    input('Enter to quit...')
    exit()