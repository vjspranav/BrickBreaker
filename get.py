"""Defining input class."""
import sys
import termios
import tty
import fcntl


class __Get:
    """Class to get input."""

    def __call__(self):
        """Defining __call__."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        old_flags = fcntl.fcntl(fd, fcntl.F_GETFL)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if ch == '\x03':
                exit()
        finally:
            fcntl.fcntl(fd, fcntl.F_SETFL, old_flags)
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = __Get()