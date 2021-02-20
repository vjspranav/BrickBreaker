from colorama import init, Fore, Back

init(autoreset=True)


class Placeholder:
    def __init__(self):
        self.object = None
        self.power_up = None
        self.ball = None
        self.paddle = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False
        self.has_ball = False
        self.has_paddle = False

    def add_brick(self, obj):
        self.object = obj
        self.has_object = True
        self.has_brick = True

    def add_power_up(self, obj):
        self.power_up = obj
        self.has_power_up = True

    def add_ball(self, obj):
        self.ball = obj
        self.has_ball = True

    def add_paddle(self, obj):
        self.paddle = obj
        self.has_paddle = True

    def get_object(self):
        return self.object

    def get_paddle(self):
        return self.paddle

    def remove_object(self):
        self.object = None
        self.has_object = False
        self.has_brick = False
        self.has_power_up = False

    def remove_ball(self):
        self.has_ball = False
        self.ball = None

    def remove_paddle(self):
        if self.has_paddle:
            self.paddle = None
            self.has_paddle = False

    def remove_power_up(self):
        self.power_up = None
        self.has_power_up = False

    def collide(self):
        if self.has_brick:
            self.object.collide()
            if self.object.num_lives == 0:
                self.remove_object()
                return 1
            if self.object.num_lives == -1:
                return 0
            return 1
        return 0
    
    def __str__(self):
        if self.has_ball:
            return str(self.ball)
        if self.has_object:
            return str(self.object)
        if self.has_paddle:
            return str(self.paddle)
        return Back.LIGHTWHITE_EX + "  *  "
