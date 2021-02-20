from colorama import Back, Fore


class __PowerUp:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def update_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def decrease_life(self):
        self.lives -= 1

class Expamd:
    def __init__(self, x, y):
        super(Expamd, self).__init__(x, y)

    def __str__(self):
        return Back.LIGHTWHITE_EX + "  " + Back.LIGHTBLUE_EX + Fore.LIGHTBLUE_EX + " " + Back.LIGHTWHITE_EX + Fore.RESET + "  "
