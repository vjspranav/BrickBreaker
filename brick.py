from colorama import init, Fore, Back

init(autoreset=True)
bg_color = {
    "red": Back.RED,
    "green": Back.GREEN,
    "blue": Back.BLUE,
    "gray": Back.LIGHTBLACK_EX,
    "orange": Back.LIGHTRED_EX
}

fg_color = {
    "red": Back.RED,
    "green": Back.GREEN,
    "blue": Back.BLUE,
    "gray": Back.LIGHTBLACK_EX,
    "orange": Back.LIGHTRED_EX
}


class _Brick:
    def __init__(self, color, num_lives):
        self.color = color
        self.num_lives = num_lives
        self.is_hit = False

    def collide(self):
        self.is_hit = True
        if self.num_lives != -1:
            self.num_lives -= 1
        if self.num_lives == 2:
            self.color = "blue"
        if self.num_lives == 1:
            self.color = "green"
        if self.num_lives == 0:
            return None

    def change_color(self):
        return

    def __str__(self):
        return bg_color[self.color] + "|___|"


class RedBrick(_Brick):
    def __init__(self):
        super().__init__("red", 3)


class BlueBrick(_Brick):
    def __init__(self):
        super().__init__("blue", 2)


class GreenBrick(_Brick):
    def __init__(self):
        super().__init__("green", 1)


class InvicibleBrick(_Brick):
    def __init__(self):
        super().__init__("gray", -1)


class BombBrick(_Brick):
    def __init__(self):
        super().__init__("orange", -2)


class RainbowBrick(_Brick):
    def __init__(self):
        super().__init__("blue", -2)

    def change_color(self):
        if not self.is_hit:
            color_map = {"red" : ["blue", 2], "blue" : ["green", 1], "green": ["gray", -1], "gray": ["red", 3]}
            self.color, self.num_lives = color_map[self.color]