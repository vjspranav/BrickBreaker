from colorama import init, Fore, Back

init(autoreset=True)


class Placeholder:
    def __init__(self):
        self.object = None
        self.ball = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False
        self.has_ball = False

    def add_brick(self, obj):
        self.object = obj
        self.has_object = True
        self.has_brick = True

    def add_power_up(self, obj):
        self.object = obj
        self.has_object = True
        self.has_power_up = True

    def add_ball(self, obj):
        self.ball = obj
        self.has_ball = True

    def remove_object(self):
        self.object = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False

    def remove_ball(self):
        self.has_ball = False
        self.ball = None

    def __str__(self):
        if self.has_ball:
            return str(self.ball)
        if self.has_object:
            return str(self.object)
        return Back.LIGHTWHITE_EX + "  *  "
