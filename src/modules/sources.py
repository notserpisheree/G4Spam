from src import *
from src.util.ui import ui

class sources:
    def menu():
        module = 'Sources'
        ui.prep(module)
        ui.createmenu([
            'Private raiders',
            'Proxies',
            'Tokens',
            'Solvers',
            'Back'
        ])

        chosen = ui.input('Option')

        if chosen == '1': 
            webbrowser.open('https://r3ci.sellhub.cx')

        elif chosen == '2':
            ui.createmenu([
                'IPRoyal',
                'Mars proxies',
                'Tokenu proxies',
                'Back'
            ])

            chosen = ui.input('Option', module)

            if chosen == '1':   webbrowser.open('https://iproyal.com/?r=429481')
            elif chosen == '2': webbrowser.open('https://marsproxies.com/r/97040')
            elif chosen == '3': webbrowser.open('https://proxy.tokenu.to/pricing?ref=r3ci')
            else:               sources.menu()

        elif chosen == '3':
            ui.createmenu([
                'My shop (UHQ + AGE GARAUNTEED)',
                'Tokenu',
                'Back'
            ])

            chosen = ui.input('Option', module)

            if chosen == '1':   webbrowser.open('https://r3ci.sellhub.cx/product/Discord-tokens/')
            elif chosen == '2': webbrowser.open('https://www.tokenu.net?ref=r3ci')
            else:               sources.menu()

        elif chosen == '4':
            ui.createmenu([
                'Soon'
            ])

        elif chosen == '5':
            return

        else:
            sources.menu()