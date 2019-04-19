import curses, time
from user import user

mapItems = {}

def checkEmpty(dir):
    if dir in ['n', 'KEY_UP']:
        newItem = (user.pos[0], user.pos[1] - 1, user.pos[2])
        if newItem not in mapItems:
            return newItem
        else:
            return False
    elif dir in ['s', 'KEY_DOWN']:
        newItem = (user.pos[0], user.pos[1] + 1, user.pos[2])
        if newItem not in mapItems:
            return newItem
        else:
            return False
    elif dir in ['e', 'KEY_RIGHT']:
        newItem = (user.pos[0] + 1, user.pos[1], user.pos[2])
        if newItem not in mapItems:
            return newItem
        else:
            return False
    elif dir in ['w', 'KEY_LEFT']:
        newItem = (user.pos[0] - 1, user.pos[1], user.pos[2])
        if newItem not in mapItems:
            return newItem
        else:
            return False

def checkFull(dir):
    if dir == 'n':
        newItem = (user.pos[0], user.pos[1] - 1, user.pos[2])
        if newItem in mapItems:
            return newItem
        else:
            return False
    elif dir == 's':
        newItem = (user.pos[0], user.pos[1] + 1, user.pos[2])
        if newItem in mapItems:
            return newItem
        else:
            return False
    elif dir == 'e':
        newItem = (user.pos[0] + 1, user.pos[1], user.pos[2])
        if newItem in mapItems:
            return newItem
        else:
            return False
    elif dir == 'w':
        newItem = (user.pos[0] - 1, user.pos[1], user.pos[2])
        if newItem in mapItems:
            return newItem
        else:
            return False

def placeItem(win):
    win.addstr("\nEnter location: ")

    curses.echo()
    loc = win.getstr().decode(encoding="utf-8")
    curses.noecho()

    newItem = checkEmpty(loc)

    if not newItem:
        win.addstr("Can't place item: Space occupied\n")
        win.refresh()
        time.sleep(1)
    else:
        mapItems[newItem] = 'x'

def delItem(win):
    win.addstr("\nEnter location: ")

    curses.echo()
    loc = win.getstr().decode(encoding="utf-8")
    curses.noecho()

    newItem = checkFull(loc)

    if not newItem:
        win.addstr("Can't remove item: Space Empty\n")
        win.refresh()
        time.sleep(1)
    else:
        del mapItems[newItem]
