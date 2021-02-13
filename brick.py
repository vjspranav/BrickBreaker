from colorama import init, Fore, Back

init(autoreset=True)
bg_color = {
    "red": Back.RED,
    "green": Back.GREEN,
    "blue": Back.BLUE
}

fg_color = {
    "red": Back.RED,
    "green": Back.GREEN,
    "blue": Back.BLUE
}


class _Brick:
    def __init__(self, color, num_lives):
        self.color = color
        self.num_lives = num_lives

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
