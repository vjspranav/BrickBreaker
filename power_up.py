from colorama import Back, Fore


class __PowerUp:
    def __init__(self, x, y, number):
        self.x_pos = x
        self.y_pos = y
        self.number = number

    def update_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

class Expand(__PowerUp):
    def __init__(self, x, y):
        super(Expand, self).__init__(x, y, 0)

    def __str__(self):
        return Back.LIGHTWHITE_EX + " " + Back.LIGHTBLUE_EX + Fore.LIGHTBLUE_EX + "   " + Back.LIGHTWHITE_EX + Fore.RESET + " "


class Bomb(__PowerUp):
    def __init__(self, x, y):
        super(Bomb, self).__init__(x, y, 1)

    def __str__(self):
        return Back.LIGHTWHITE_EX + " " + Back.LIGHTRED_EX + Fore.LIGHTRED_EX + "   " + Back.LIGHTWHITE_EX + Fore.RESET + " "
