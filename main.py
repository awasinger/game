import curses, os, json, ast, time, items
from sys import argv
from user import user

def main(win):

    if len(argv) < 2:
        exit('Please specify a world file.')
    elif len(argv) > 2:
        exit('Too many arguments.')
    elif os.path.isfile('./' + argv[1]):
        with open(argv[1], "r") as file:
            obj = json.load(file)
            items.mapItems = {ast.literal_eval(k):v for k, v in obj[0].items()}
            user.pos = tuple(obj[1])
    else:
        print('Creating new world...')
        time.sleep(.5)

    win.clear()
    printMap(win)

    while True:
        key = win.getkey()
        processInput(key, win)
        win.clear()
        printMap(win)

def processInput(key, win):

    if key in ['KEY_UP', "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT", '<', '>']:
        user.move(key)

    elif key == 'p':
        items.placeItem(win)
    elif key == 'd':
        items.delItem(win)
    elif key == 'q':
        with open(argv[1], "w") as file:
            file.write(json.dumps([{str(k): v for k, v in items.mapItems.items()}, user.pos]))
        exit()

def printMap(win):

    for x in range(user.pos[1] - 25, user.pos[1] + 26):
        win.addstr('| ')
        for y in range(user.pos[0] - 25, user.pos[0] + 26):
            if (y, x, user.pos[2]) in items.mapItems:
                win.addstr(items.mapItems[(y, x, user.pos[2])] + ' ')
            elif (y, x, user.pos[2]) == user.pos:
                win.addstr('P ')
            else:
                win.addstr('- ')
        win.addstr('|\n')

    win.addstr(str(user.pos))

if __name__ == "__main__":
    # user.pos = user.pos

    curses.wrapper(main)
