from colorama import Back, Fore


class Ball:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.x_vel = 0
        self.y_vel = 0

    def update_position(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def update_velo(self, x, y):
        self.x_vel = x
        self.y_vel = y

    def __str__(self):
        return Back.LIGHTWHITE_EX + "  " + Fore.RED + "O" + Back.LIGHTWHITE_EX + Fore.RESET + "  "

