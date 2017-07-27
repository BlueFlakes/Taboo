import curses



def main():
    screen = curses.initscr()
    x_max, y_max = screen.getmaxyx()

    screen.addstr(int(x_max/2), int(y_max/2), 'Hello World!')
    screen.refresh()
    screen.getch()
    curses.endwin()





if __name__ == "__main__":
    main()

main()
