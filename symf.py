import os
import curses
import sys

def save_file(src, buffer):
    """Save the contents of the buffer to the specified file."""
    cont = ''.join([''.join(map(chr, line)) + '\n' for line in buffer])
    with open(src, 'w') as f:
        f.write(cont)

def confirm_exit(stdscr):
    """Display a confirmation message for exiting without saving."""
    stdscr.clear()
    stdscr.addstr(0, 0, "Are you sure you want to exit? (y/n): ")
    stdscr.refresh()
    while True:
        ch = stdscr.getch()
        if ch == ord('y'):
            return False  # Return False to indicate exit
        elif ch == ord('n'):
            return True  # Return True to continue editing

def symf(stdscr, filename):
    """Open a file in a basic text editor for editing."""
    buffer = []
    src = filename  # Use the specified filename

    # Load the file if it exists
    if os.path.exists(src):
        with open(src) as f:
            cont = f.read().split('\n')
            cont = cont[:-1] if len(cont) > 1 else cont
            for rw in cont:
                buffer.append([ord(c) for c in rw])
    else:
        buffer.append([])  # Start with an empty buffer if file does not exist

    R, C = stdscr.getmaxyx()
    x, y, r, c = [0] * 4

    while True:
        stdscr.move(0, 0)
        if r < y: y = r
        if r >= y + R: y = r - R + 1
        if c < x: x = c
        if c >= x + C: c = c - C + 1
        
        for rw in range(R):
            brw = rw + y
            for cl in range(C):
                bcl = cl + x
                try:
                    stdscr.addch(rw, cl, buffer[brw][bcl])
                except:
                    pass
            stdscr.clrtoeol()
        
        curses.curs_set(0)
        stdscr.move(r - y, c - x)
        curses.curs_set(1)
        stdscr.refresh()
        
        ch = -1
        while (ch == -1): 
            ch = stdscr.getch()

        if ch != ((ch) & 0x1f) and ch < 128:
            buffer[r].insert(c, ch)
            c += 1
        elif chr(ch) in '\n\r':
            l = buffer[r][c:]
            buffer[r] = buffer[r][:c]
            r += 1
            c = 0
            buffer.insert(r, [] + l)
        elif ch in [8, 263]:
            if c:
                c -= 1
                del buffer[r][c]
            elif r:
                l = buffer[r][c:]
                del buffer[r]
                r -= 1
                c = len(buffer[r])
                buffer[r] += l
        elif ch == curses.KEY_LEFT:
            if c != 0:
                c -= 1
            elif r > 0:
                r -= 1
                c = len(buffer[r])
        elif ch == curses.KEY_RIGHT:
            if c < len(buffer[r]):
                c += 1
            elif r < len(buffer) - 1:
                r += 1
                c = 0
        elif ch == curses.KEY_UP and r != 0:
            r -= 1
        elif ch == curses.KEY_DOWN and r < len(buffer) - 1:
            r += 1
        
        rw = buffer[r] if r < len(buffer) else None
        rwlen = len(rw) if rw is not None else 0
        if c > rwlen: c = rwlen 
        
        if ch == (ord('q') & 0x1f):  # Ctrl + Q to exit
            if not confirm_exit(stdscr):  # Confirm exit
                break  # Exit the editor
        elif ch == (ord('s') & 0x1f):  # Ctrl + S to save
            save_file(src, buffer)