from datetime import datetime as dt

def rgb(r, g, b):
    return f'\033[38;2;{r};{g};{b}m'

class co:
    main = rgb(80, 5, 255)
    gmain = rgb(80, 5, 255)
    gmain_ = rgb(120, 50, 255)

    red = rgb(255, 0, 0)
    gred = rgb(255, 100, 100)
    gred_ = rgb(180, 0, 0)

    green = rgb(0, 255, 0)
    ggreen = rgb(100, 255, 100)
    ggreen_ = rgb(0, 180, 0)

    blue = rgb(0, 0, 255)
    gblue = rgb(100, 100, 255)
    gblue_ = rgb(0, 0, 180)

    yellow = rgb(255, 255, 0)
    gyellow = rgb(255, 255, 150)
    gyellow_ = rgb(200, 200, 0)

    orange = rgb(255, 165, 0)
    gorange = rgb(255, 190, 100)
    gorange_ = rgb(200, 100, 0)

    pink = rgb(255, 105, 180)
    gpink = rgb(255, 155, 200)
    gpink_ = rgb(200, 80, 150)

    cyan = rgb(0, 255, 255)
    gcyan = rgb(100, 255, 255)
    gcyan_ = rgb(0, 180, 180)

    magenta = rgb(255, 0, 255)
    gmagenta = rgb(255, 100, 255)
    gmagenta_ = rgb(180, 0, 180)

    lime = rgb(191, 255, 0)
    glime = rgb(220, 255, 100)
    glime_ = rgb(150, 200, 0)

    teal = rgb(0, 128, 128)
    gteal = rgb(80, 180, 180)
    gteal_ = rgb(0, 100, 100)

    indigo = rgb(75, 0, 130)
    gindigo = rgb(120, 60, 160)
    gindigo_ = rgb(50, 0, 90)

    violet = rgb(238, 130, 238)
    gviolet = rgb(250, 180, 250)
    gviolet_ = rgb(200, 100, 200)

    brown = rgb(139, 69, 19)
    gbrown = rgb(180, 120, 70)
    gbrown_ = rgb(100, 50, 10)

    grey = rgb(128, 128, 128)
    ggrey = rgb(180, 180, 180)
    ggrey_ = rgb(90, 90, 90)

    black = rgb(0, 0, 0)
    gblack = rgb(50, 50, 50)
    gblack_ = rgb(0, 0, 0)

    white = rgb(255, 255, 255)
    gwhite = rgb(240, 240, 240)
    gwhite_ = rgb(200, 200, 200)

    reset = '\033[0m'